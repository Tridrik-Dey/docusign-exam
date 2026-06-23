from pathlib import Path
import re

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from scrape_docusign_study_material import (
    extract_scorm_markdown,
    ensure_course_registered,
    goto_authenticated,
    meaningful_course_markdown,
    page_title,
)


PROFILE_DIR = r"D:\Docusign exam\.docusign-browser-profile-2"
OUTPUT = Path("study_material.md")

COURSES = [
    (
        "Build a Custom eSignature Integration with CORS",
        "https://dsupartners.docusign.com/path/plan-and-manage-esignature-api-integrations/build-a-custom-esignature-integration-with-cors",
    ),
]


def replacement_section(title: str, url: str, body: str) -> str:
    content = body or "_No readable self-paced lesson text was found on this page._"
    return f"### {title}\n\nSource: {url}\n\n{content}\n\n"


def replace_section(markdown: str, title: str, url: str, body: str) -> str:
    pattern = re.compile(
        r"(?ms)^### "
        + re.escape(title)
        + r"(?: [^\n]*)?\n\nSource: "
        + re.escape(url)
        + r"\n\n.*?(?=^### |^## |\Z)"
    )
    new_section = replacement_section(title, url, body)
    updated, count = pattern.subn(new_section, markdown, count=1)
    if count == 0:
        raise RuntimeError(f"Could not find section for {title}")
    return updated


def main() -> None:
    markdown = OUTPUT.read_text(encoding="utf-8")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            channel="msedge",
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.new_page()

        for fallback_title, url in COURSES:
            print(f"Repairing: {fallback_title}", flush=True)
            goto_authenticated(page, url)
            ensure_course_registered(page)
            title = page_title(page, fallback_title)
            body = extract_scorm_markdown(page)
            if not body:
                try:
                    body = meaningful_course_markdown(BeautifulSoup(page.content(), "html.parser"))
                except Exception:
                    body = ""
            markdown = replace_section(markdown, fallback_title, url, body)
            OUTPUT.write_text(markdown, encoding="utf-8")

        context.close()


if __name__ == "__main__":
    main()

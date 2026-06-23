import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag
from playwright.sync_api import sync_playwright


BASE_URL = "https://dsupartners.docusign.com"


@dataclass(frozen=True)
class LearningPath:
    title: str
    slug: str
    expected_courses: int


LEARNING_PATHS = [
    LearningPath("Get Started with Docusign for Developers", "get-started-with-docusign-for-developers", 4),
    LearningPath(
        "Create and Configure Envelopes with the eSignature API",
        "create-and-configure-envelopes-with-the-esignature-api",
        4,
    ),
    LearningPath("Plan and Manage eSignature API Integrations", "plan-and-manage-esignature-api-integrations", 3),
    LearningPath("Docusign Workflow Builder API", "docusign-workflow-builder-api", 5),
    LearningPath("Docusign Web Forms API", "docusign-web-forms-api", 3),
    LearningPath("Docusign Agreement Manager API", "docusign-agreement-manager-api", 5),
    LearningPath(
        "Docusign Connected Fields API and Docusign ID Evidence API",
        "docusign-connected-fields-api-and-docusign-id-evidence-api",
        5,
    ),
    LearningPath("Docusign Extension Apps", "docusign-extension-apps", 3),
]


BOILERPLATE_PATTERNS = [
    "Centro preferenze sulla privacy",
    "Gestisci preferenze consenso",
    "INFORMAZIONI SU DOCUSIGN UNIVERSITY",
    "START Docusign Clickwrap",
    "Google Tag Manager",
    "START:",
    "END ",
    "CorsiAutodidatta",
    "Torna al catalogo",
    "View Results",
    "Ricerca in corso",
    "Si è verificato un problema",
    "Si prega di riprovare",
    "Disconnettiti",
    "Il mio profilo",
    "Cookie ",
    "OneTrust",
]


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def text_from_node(node) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if isinstance(node, Tag):
        return "".join(text_from_node(child) for child in node.children)
    return ""


def html_to_markdown(soup: BeautifulSoup | Tag) -> str:
    for bad in soup(["script", "style", "noscript", "iframe", "header", "footer", "form", "svg"]):
        bad.decompose()

    def render(node, list_type=None, list_index=1):
        if isinstance(node, NavigableString):
            return re.sub(r"\s+", " ", str(node))
        if not isinstance(node, Tag):
            return ""

        if node.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(node.name[1])
            text = normalize_space(text_from_node(node))
            return f"\n{'#' * level} {text}\n\n" if text else ""

        if node.name in {"p", "div", "section", "article"}:
            pieces = [render(child) for child in node.children]
            text = normalize_space("".join(pieces))
            if not text:
                return ""
            if any(pattern in text for pattern in BOILERPLATE_PATTERNS):
                return ""
            return text + "\n\n"

        if node.name == "br":
            return "\n"

        if node.name in {"strong", "b"}:
            text = normalize_space(text_from_node(node))
            return f"**{text}**" if text else ""

        if node.name in {"em", "i"}:
            text = normalize_space(text_from_node(node))
            return f"*{text}*" if text else ""

        if node.name == "a":
            href = node.get("href", "").strip()
            text = normalize_space(text_from_node(node)) or href
            if not text:
                return ""
            if href and href.startswith(("http://", "https://")):
                return f"[{text}]({href})"
            return text

        if node.name == "code":
            text = text_from_node(node).strip()
            return f"`{text}`" if text else ""

        if node.name == "pre":
            content = node.get_text().rstrip()
            return "```\n" + content + "\n```\n\n" if content else ""

        if node.name in {"ul", "ol"}:
            lines = []
            for index, child in enumerate(node.find_all("li", recursive=False), start=1):
                lines.append(render(child, list_type=node.name, list_index=index))
            return "".join(lines) + "\n"

        if node.name == "li":
            marker = "- " if list_type == "ul" else f"{list_index}. "
            text = normalize_space("".join(render(child) for child in node.children))
            return f"{marker}{text}\n" if text else ""

        if node.name == "table":
            rows = []
            for tr in node.find_all("tr"):
                cells = [normalize_space(cell.get_text(" ")) for cell in tr.find_all(["th", "td"])]
                if cells:
                    rows.append(cells)
            if not rows:
                return ""
            width = max(len(row) for row in rows)
            rows = [row + [""] * (width - len(row)) for row in rows]
            table = [
                "| " + " | ".join(rows[0]) + " |",
                "| " + " | ".join(["---"] * width) + " |",
            ]
            table.extend("| " + " | ".join(row) + " |" for row in rows[1:])
            return "\n".join(table) + "\n\n"

        return "".join(render(child) for child in node.children)

    body = soup.find("main") or soup.find("article") or soup.body or soup
    markdown = render(body)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = "\n".join(line.rstrip() for line in markdown.splitlines())
    return markdown.strip()


def clean_title(raw_title: str, fallback: str) -> str:
    title = normalize_space(raw_title)
    title = re.sub(r"\s*\|\s*Docusign University.*$", "", title)
    title = title.replace("DocuSign", "Docusign")
    return title or fallback


def page_title(page, fallback: str) -> str:
    try:
        soup = BeautifulSoup(page.content(), "html.parser")
        h1 = soup.find("h1")
        if h1:
            return clean_title(h1.get_text(" "), fallback)
        title = page.title()
        return clean_title(title, fallback)
    except Exception:
        return fallback


def goto_authenticated(page, url: str) -> None:
    print(f"Navigating: {url}", flush=True)
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=90000)
    except Exception:
        page.goto(url, wait_until="commit", timeout=90000)
    current_url = page.url.lower()
    if any(marker in current_url for marker in ("login", "idp", "sso")):
        print("Login required. Complete sign-in in the opened Edge window.", flush=True)
        page.wait_for_function(
            "!/login|idp|sso/i.test(window.location.href)",
            timeout=180000,
        )
        page.goto(url, wait_until="domcontentloaded", timeout=90000)
    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        pass


def extract_course_links(soup: BeautifulSoup, path: LearningPath) -> list[tuple[str, str]]:
    prefix = f"/path/{path.slug}/"
    found: list[tuple[str, str]] = []
    seen = set()

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].split("#", 1)[0].strip()
        parsed = urlparse(href)
        rel_path = parsed.path if parsed.netloc else href
        if not rel_path.startswith(prefix):
            continue
        if rel_path.rstrip("/") == f"/path/{path.slug}":
            continue

        absolute = urljoin(BASE_URL, rel_path)
        if absolute in seen:
            continue

        label = normalize_space(anchor.get_text(" "))
        is_self_paced = "Self-paced" in label or "Autodidatta" in label
        is_excluded = any(marker in label for marker in ("Video", "Webinar", "Instructor-Led", "Live Training", "Esame", "Exam"))
        if not is_self_paced or is_excluded:
            continue

        title = clean_course_card_title(label)
        if not title:
            title = rel_path.rstrip("/").rsplit("/", 1)[-1].replace("-", " ").title()
        found.append((title, absolute))
        seen.add(absolute)

        if len(found) >= path.expected_courses:
            break

    return found


def clean_course_card_title(label: str) -> str:
    label = re.sub(r"^(Complete|Completa|Registered|Registrato)\s*", "", label).strip()
    label = re.split(
        r"\b(?:Learn|In this series|In this video|Pass this exam)\b|\d+\s*(?:min|ore\s+\d+\s+min)|Autodidatta|Self-paced",
        label,
        maxsplit=1,
    )[0]
    return normalize_space(label)


def is_self_paced_course(soup: BeautifulSoup) -> bool:
    text = normalize_space(soup.get_text(" "))
    if "VideoFree for all" in text or re.search(r"\bVideo\b", text) and "Self-paced" not in text:
        return False
    if any(marker in text for marker in ("Webinar", "Instructor-Led", "Live Training", "Esame", "Exam")):
        return False
    return "Self-paced" in text or "Autodidatta" in text


def meaningful_course_markdown(soup: BeautifulSoup) -> str:
    markdown = html_to_markdown(soup)
    lines = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            if lines and lines[-1] != "":
                lines.append("")
            continue
        if any(pattern in stripped for pattern in BOILERPLATE_PATTERNS):
            continue
        if stripped in {"Annulla", "Applica", "Attiva", "Consenti tutti", "Rifiuta tutti"}:
            continue
        lines.append(stripped)
    return "\n".join(lines).strip()


def clean_scorm_text(text: str) -> str:
    lines = []
    skip_exact = {
        "SKIP TO LESSON",
        "EXIT COURSE",
        "Home",
        "Course Complete",
        "START COURSE",
    }
    for raw_line in text.splitlines():
        line = normalize_space(raw_line)
        if not line:
            continue
        if line in skip_exact:
            continue
        if re.fullmatch(r"\d+% (?:Completed|COMPLETE)", line):
            continue
        if re.fullmatch(r"(?:Started|Unstarted|Complete|Completed)", line):
            continue
        lines.append(line)

    deduped = []
    previous = None
    for line in lines:
        if line == previous:
            continue
        deduped.append(line)
        previous = line
    return "\n".join(deduped).strip()


def extract_scorm_markdown(page) -> str:
    page.wait_for_timeout(2500)
    scorm_frames = []
    for _ in range(20):
        scorm_frames = [frame for frame in page.frames if "scormcontent" in frame.url]
        if scorm_frames:
            break
        page.wait_for_timeout(1000)
    if not scorm_frames:
        return ""

    frame = scorm_frames[0]

    for label in ("START COURSE", "Start Course", "Start"):
        try:
            start = frame.get_by_text(label, exact=True).first
            if start.count():
                start.click(timeout=5000)
                page.wait_for_timeout(2500)
                break
        except Exception:
            pass

    collected = []

    def collect_current():
        try:
            text = frame.locator("body").inner_text(timeout=5000)
        except Exception:
            return
        text = clean_scorm_text(text)
        if text and text not in collected:
            collected.append(text)

    collect_current()

    try:
        controls = frame.locator("button, a, [role=button]").all()
    except Exception:
        controls = []

    clicked_labels = set()
    skip_labels = {
        "",
        "SKIP TO LESSON",
        "EXIT COURSE",
        "Home",
        "SAMPLE APPS",
        "Docusign App Center\n(opens in a new tab)",
    }

    for control in controls[:80]:
        try:
            label = normalize_space(control.inner_text(timeout=1000))
        except Exception:
            continue
        if label in skip_labels or label in clicked_labels:
            continue
        if len(label) > 120:
            continue
        clicked_labels.add(label)
        try:
            control.click(timeout=3000)
            page.wait_for_timeout(1200)
            collect_current()
        except Exception:
            continue

    return "\n\n".join(collected).strip()


def ensure_course_registered(page) -> None:
    if any("scormcontent" in frame.url for frame in page.frames):
        return
    try:
        register = page.get_by_text("Register", exact=True).first
        if register.count():
            register.click(timeout=5000)
            page.wait_for_timeout(6000)
    except Exception:
        return


def build_study_material(output: Path, browser_channel: str, headless: bool, profile_dir: str | None) -> None:
    profile_dir = profile_dir or str(Path.cwd() / ".docusign-browser-profile")
    print(f"Using browser profile: {profile_dir}", flush=True)
    sections = [
        "# Certified Docusign IAM Integration & Extension Developer",
        "",
        "Cleaned study material from the self-paced courses in the certification learning paths.",
        "",
    ]

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            channel=browser_channel,
            headless=headless,
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.new_page()

        for path in LEARNING_PATHS:
            path_url = f"{BASE_URL}/path/{path.slug}"
            print(f"Reading learning path: {path.title}", flush=True)
            try:
                goto_authenticated(page, path_url)
            except Exception as exc:
                sections.append(f"## {path.title}")
                sections.append("")
                sections.append(f"_Failed to load learning path: {exc}_")
                sections.append("")
                output.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")
                continue

            soup = BeautifulSoup(page.content(), "html.parser")
            course_links = extract_course_links(soup, path)

            sections.append(f"## {path.title}")
            sections.append("")
            if not course_links:
                sections.append(f"- No self-paced course links found at {path_url}.")
                sections.append("")
                continue

            sections.append("Courses:")
            for title, url in course_links:
                sections.append(f"- [{title}]({url})")
            sections.append("")

            for fallback_title, course_url in course_links:
                print(f"  Reading course: {fallback_title}", flush=True)
                try:
                    goto_authenticated(page, course_url)
                except Exception as exc:
                    sections.append(f"### {fallback_title}")
                    sections.append("")
                    sections.append(f"Source: {course_url}")
                    sections.append("")
                    sections.append(f"_Failed to load course page: {exc}_")
                    sections.append("")
                    output.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")
                    continue
                ensure_course_registered(page)
                title = page_title(page, fallback_title)
                body = extract_scorm_markdown(page)
                if not body:
                    try:
                        course_soup = BeautifulSoup(page.content(), "html.parser")
                        body = meaningful_course_markdown(course_soup)
                    except Exception:
                        body = ""
                sections.append(f"### {title}")
                sections.append("")
                sections.append(f"Source: {course_url}")
                sections.append("")
                if body:
                    sections.append(body)
                    sections.append("")
                else:
                    sections.append("_No readable self-paced lesson text was found on this page._")
                    sections.append("")

            output.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")

        context.close()

    output.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")
    print(f"Saved cleaned study material to {output}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build cleaned Docusign self-paced study material.")
    parser.add_argument(
        "url",
        nargs="?",
        default=f"{BASE_URL}/page/certified-docusign-iam-integration-extension-developer",
        help="Kept for compatibility; targeted learning paths are defined in the script.",
    )
    parser.add_argument("output", nargs="?", default="study_material.md", help="Output Markdown file.")
    parser.add_argument("--browser", default="msedge", help="Playwright browser channel.")
    parser.add_argument("--headless", action="store_true", help="Run browser headless.")
    parser.add_argument("--profile-dir", default=None, help="Browser profile directory to use for the scrape.")
    parser.add_argument("--max-pages", type=int, default=None, help="Ignored; kept for compatibility.")
    args = parser.parse_args()

    build_study_material(Path(args.output), args.browser, args.headless, args.profile_dir)


if __name__ == "__main__":
    main()

from pathlib import Path
import re


BASE_URL = "https://dsupartners.docusign.com"


PATHS = [
    (
        "Docusign eSignature API",
        "Get Started with Docusign for Developers",
        "get-started-with-docusign-for-developers",
        "Learn to integrate with the IAM platform using developer tools.",
    ),
    (
        "Docusign eSignature API",
        "Create and Configure Envelopes with the eSignature API",
        "create-and-configure-envelopes-with-the-esignature-api",
        "In this series, learn how to build and customize envelopes with the Docusign eSignature API.",
    ),
    (
        "Docusign eSignature API",
        "Plan and Manage eSignature API Integrations",
        "plan-and-manage-esignature-api-integrations",
        "Learn how to plan eSignature API integrations and work with an integration in production.",
    ),
    (
        "Docusign IAM APIs",
        "Docusign Workflow Builder API",
        "docusign-workflow-builder-api",
        "Learn to build and integrate workflows with Workflow Builder and the Workflow Builder API.",
    ),
    (
        "Docusign IAM APIs",
        "Docusign Web Forms API",
        "docusign-web-forms-api",
        "Learn to integrate Docusign Web Forms into your agreement processes using the Web Forms API.",
    ),
    (
        "Docusign IAM APIs",
        "Docusign Agreement Manager API",
        "docusign-agreement-manager-api",
        "Learn to integrate agreement data with the Agreement Manager API.",
    ),
    (
        "Docusign IAM APIs",
        "Docusign Connected Fields API and Docusign ID Evidence API",
        "docusign-connected-fields-api-and-docusign-id-evidence-api",
        "Learn to integrate data verification and retrieve ID evidence with Docusign APIs.",
    ),
    (
        "Docusign Extension Apps",
        "Docusign Extension Apps",
        "docusign-extension-apps",
        "Learn to build custom Extension Apps for the Docusign IAM platform.",
    ),
]


def clean_label(label: str) -> tuple[str, str, str]:
    label = re.sub(r"^(Completa|Registrato)", "", label).strip()
    duration = ""
    duration_match = re.search(r"(\d+\s*(?:min|ore\s+\d+\s+min))", label)
    if duration_match:
        duration = duration_match.group(1)

    description = ""
    for marker in ("Learn ", "In this series, ", "In this video, ", "Pass this exam "):
        index = label.find(marker)
        if index != -1:
            title = label[:index].strip()
            remainder = label[index:].strip()
            description = re.split(r"\d+\s*(?:min|ore\s+\d+\s+min)|Autodidatta|Video|Webinar|Esame|Free for all", remainder)[0].strip()
            return title, description, duration

    title = re.split(r"\d+\s*(?:min|ore\s+\d+\s+min)|Autodidatta|Video|Webinar|Esame|Free for all", label)[0].strip()
    return title, description, duration


def extract_courses(raw: str, slug: str) -> list[dict[str, str]]:
    pattern = re.compile(r"\[([^\]]{1,400})\]\(/path/" + re.escape(slug) + r"/([^)]+)\)")
    courses = []
    seen = set()

    for match in pattern.finditer(raw):
        label, course_slug = match.groups()
        if course_slug in seen:
            continue
        seen.add(course_slug)

        is_self_paced = "Self-paced" in label or "Autodidatta" in label
        is_excluded = any(marker in label for marker in ("Video", "Webinar", "Instructor-Led", "Live Training", "Esame", "Exam"))
        if not is_self_paced or is_excluded:
            continue

        title, description, duration = clean_label(label)
        courses.append(
            {
                "title": title,
                "description": description,
                "duration": duration,
                "url": f"{BASE_URL}/path/{slug}/{course_slug}",
            }
        )

    return courses


def main() -> None:
    path = Path("study_material.md")
    raw = path.read_text(encoding="utf-8", errors="replace")

    lines = [
        "# Certified Docusign IAM Integration & Extension Developer",
        "",
        "This file keeps only the self-paced course entries from the certification learning paths. Video-only items, webinars, live training, exams, profile pages, catalog pages, cookie text, and footer/navigation content were removed.",
        "",
    ]

    current_group = None
    for group, title, slug, description in PATHS:
        if group != current_group:
            current_group = group
            lines.extend([f"## {group}", ""])

        url = f"{BASE_URL}/path/{slug}"
        lines.extend([f"### {title}", "", description, "", f"Learning path: {url}", ""])

        courses = extract_courses(raw, slug)
        if not courses:
            lines.extend(
                [
                    "_No self-paced course cards for this learning path were captured in the existing local scrape._",
                    "",
                ]
            )
            continue

        lines.append("| Course | Duration | Description | Source |")
        lines.append("| --- | --- | --- | --- |")
        for course in courses:
            duration = course["duration"] or "-"
            description = course["description"] or "-"
            lines.append(f"| {course['title']} | {duration} | {description} | [Open]({course['url']}) |")
        lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

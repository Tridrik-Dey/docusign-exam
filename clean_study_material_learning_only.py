from pathlib import Path
import re


PATH = Path("study_material.md")


DROP_EXACT = {
    "Courses:",
    "COURSE REVIEW",
    "Learning Links",
    "Course Complete",
    "Course Overview",
    "SAMPLE APPS",
    "DOCUSIGN SUPPORT",
    "START COURSE",
    "SKIP TO LESSON",
    "EXIT COURSE",
    "Home",
    "(opens in a new tab)",
    ".",
}


DROP_PREFIXES = (
    "Source: https://",
    "Watch the following video",
    "Watch the video",
    "Watch a video",
    "Watch the Docusign",
    "Click the Sample Apps button",
    "Click the button to view",
    "Click the button to open",
    "Click DOCUSIGN SUPPORT",
    "Click the link for your account type",
    "Click each +",
    "Click the +",
    "Click each plus sign",
    "Click the numbered icons",
    "Click the tabs below",
    "Click each tab",
    "Click each panel",
    "Select each tab",
    "Select each number",
    "Select each +",
    "Select each plus",
    "Review the following two use case examples",
    "The following diagram illustrates",
    "Click EXIT",
)


DROP_PATTERNS = [
    re.compile(r"^\d+% (?:Completed|COMPLETE)(?:\. Click to complete)?$"),
    re.compile(r"^(?:Completed|Unstarted|Started)(?:\. Click to (?:complete|reset))?$"),
    re.compile(r"^Lesson \d+ of \d+$"),
    re.compile(r"^Lesson \d+ - Learning Links$"),
    re.compile(r"^Duration:\s*\d+ ?(?:minutes|min)?$", re.IGNORECASE),
    re.compile(r"^Course \d+ of \d+ in .+$"),
    re.compile(r"^\(opens in new tab\)$"),
]


def is_drop_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped in DROP_EXACT:
        return True
    if any(stripped.startswith(prefix) for prefix in DROP_PREFIXES):
        return True
    return any(pattern.match(stripped) for pattern in DROP_PATTERNS)


def trim_ui_prompts(line: str) -> str:
    stripped = line.strip()
    for pattern in (
        r"\s+Watch the following video.*$",
        r"\s+Watch the video.*$",
        r"\s+Watch a video.*$",
        r"\s+Click each plus sign.*$",
        r"\s+Click each \+.*$",
        r"\s+Click the numbered icons.*$",
        r"\s+Click each tab.*$",
        r"\s+Select each tab.*$",
        r"\s+Select each \+.*$",
        r"\s+Select each plus.*$",
        r"\s+Click DOCUSIGN SUPPORT.*$",
    ):
        stripped = re.sub(pattern, "", stripped)
    return stripped.strip()


def remove_course_lists(lines: list[str]) -> list[str]:
    cleaned = []
    index = 0
    while index < len(lines):
        if lines[index].strip() == "Courses:":
            index += 1
            while index < len(lines) and (not lines[index].strip() or lines[index].lstrip().startswith("- [")):
                index += 1
            continue
        cleaned.append(lines[index])
        index += 1
    return cleaned


def collapse_repeated_blocks(text: str) -> str:
    blocks = [block.strip() for block in re.split(r"\n{2,}", text) if block.strip()]
    result = []
    recent = []
    for block in blocks:
        normalized = re.sub(r"\s+", " ", block)
        if normalized in recent:
            continue
        result.append(block)
        recent.append(normalized)
        if len(recent) > 8:
            recent.pop(0)
    return "\n\n".join(result) + "\n"


def main() -> None:
    text = PATH.read_text(encoding="utf-8", errors="replace")
    lines = remove_course_lists(text.splitlines())

    kept = []
    previous_blank = False
    previous_line = None
    for line in lines:
        stripped = trim_ui_prompts(line)
        if is_drop_line(stripped):
            continue
        if stripped == previous_line:
            continue
        if not stripped:
            if previous_blank:
                continue
            kept.append("")
            previous_blank = True
            previous_line = None
            continue
        kept.append(stripped)
        previous_blank = False
        previous_line = stripped

    cleaned = "\n".join(kept).strip() + "\n"
    cleaned = collapse_repeated_blocks(cleaned)
    PATH.write_text(cleaned, encoding="utf-8")


if __name__ == "__main__":
    main()

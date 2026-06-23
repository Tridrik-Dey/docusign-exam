from __future__ import annotations

import json
import re
from collections import defaultdict, deque
from pathlib import Path

import pdfplumber

from create_quiz_data import parse_questions
from enhance_quiz_questions import enrich_stem, improve_option_explanations


BASE_SOURCE = Path("output/docusign_iam_integration_extension_300_practice_questions.md")
PDF_SOURCE = Path(r"C:\Users\Admin\Downloads\Docusign_Combined_QA_Explained.pdf")
JSON_DEST = Path("quiz-app/src/questions.json")
MARKDOWN_DEST = Path("output/docusign_iam_integration_extension_practice_questions_with_pdf.md")


DOMAIN_ORDER = [
    "API Authentication",
    "Go Live Process",
    "Docusign Connect",
    "eSignature API",
    "eSignature Features and Web Forms",
    "Agreement Manager API",
    "Workflow Builder and Workflow API",
    "App Center and Extension Apps",
]


def clean_text(text: str) -> str:
    text = text.replace("â€”", "-").replace("�", "-")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_pdf_text() -> str:
    with pdfplumber.open(str(PDF_SOURCE)) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    text = re.sub(r"\n\s*4\s+([A-D])\.", r"\n\1.", text)
    text = re.sub(r"(?m)^Docusign Developer.*Page \d+\s*$", "", text)
    return text


def parse_pdf_option_notes(block: str) -> dict[str, str]:
    section_match = re.search(r"(?ms)Why each option.*?:\s*(.*)$", block)
    if not section_match:
        return {}
    section = section_match.group(1).strip()
    notes = {}
    for option, note in re.findall(r"(?ms)([A-D])\s+(.*?)(?=\n[A-D]\s+|\Z)", section):
        notes[option] = clean_text(note)
    return notes


def parse_pdf_questions(text: str) -> list[dict]:
    starts = list(re.finditer(r"(?m)^Q(\d+)\.\s*$", text))
    questions = []
    for seq, match in enumerate(starts, start=1):
        end = starts[seq].start() if seq < len(starts) else len(text)
        block = text[match.end() : end]
        answer_match = re.search(r"Answer:\s*([A-D])", block)
        option_match = re.search(
            r"(?ms)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nAnswer:",
            block,
        )
        if not answer_match or not option_match:
            continue

        stem = clean_text(block[: option_match.start()])
        options = [
            {"id": "A", "text": clean_text(option_match.group(1))},
            {"id": "B", "text": clean_text(option_match.group(2))},
            {"id": "C", "text": clean_text(option_match.group(3))},
            {"id": "D", "text": clean_text(option_match.group(4))},
        ]
        correct = answer_match.group(1)
        answer_text = next(option["text"] for option in options if option["id"] == correct)
        option_notes = parse_pdf_option_notes(block)
        explanation = option_notes.get(correct, f"{answer_text} is the correct answer for this scenario.")
        explanation = re.sub(r"^Correct\.\s*", "", explanation)
        question = {
            "id": seq,
            "domain": infer_domain(stem, answer_text, options),
            "topic": infer_topic(stem, answer_text, options),
            "stem": stem,
            "options": options,
            "correct": correct,
            "answerText": answer_text,
            "explanation": explanation,
            "optionExplanations": {
                option["id"]: option_notes.get(
                    option["id"],
                    (
                        explanation
                        if option["id"] == correct
                        else f"{option['text']} is not the best fit for this scenario."
                    ),
                )
                for option in options
            },
            "source": "Docusign_Combined_QA_Explained.pdf",
            "sourceQuestion": seq,
        }
        questions.append(question)
    return questions


def contains_any(text: str, *needles: str) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def infer_domain(stem: str, answer: str, options: list[dict]) -> str:
    text = " ".join([stem, answer, *(option["text"] for option in options)])
    primary = " ".join([stem, answer])
    if contains_any(
        primary,
        "extension app",
        "app center",
        "api proxy",
        "connectionsreference",
        "connections object",
        "actions object",
        "external platform endpoint",
        "firewall",
        "manifest",
        "connected fields",
        "data verification",
        "public app",
        "private extension",
    ):
        return "App Center and Extension Apps"
    if contains_any(primary, "agreement manager", "agreements:getagreement", "legacy agreement"):
        return "Agreement Manager API"
    if contains_any(primary, "go-live", "go live", "production", "promotes an integration key", "apps and keys"):
        return "Go Live Process"
    if contains_any(primary, "web form", "identity verification", "id evidence", "brand destination"):
        return "eSignature Features and Web Forms"
    if contains_any(primary, "workflow", "maestro", "from a link", "workflow builder"):
        return "Workflow Builder and Workflow API"
    if contains_any(primary, "connect", "json sim", "webhook", "recipient-completed event"):
        return "Docusign Connect"
    if contains_any(primary, "oauth", "jwt", "authorization code", "bearer", "consent", "scope"):
        return "API Authentication"
    return "eSignature API"


def infer_topic(stem: str, answer: str, options: list[dict]) -> str:
    text = " ".join([stem, answer, *(option["text"] for option in options)])
    primary = " ".join([stem, answer])
    topic_rules = [
        ("Docusign JS client SDK", "Web Forms embedding"),
        ("Agreements:getAgreement", "Agreement data"),
        ("Agreement Manager", "Agreement data"),
        ("Workflow Builder API", "Workflow API"),
        ("Public Authorization Code", "OAuth flow selection"),
        ("Confidential Authorization Code", "OAuth flow selection"),
        ("JSON Web Token", "JWT Grant"),
        ("eventNotification", "Envelope-level Connect"),
        ("JSON SIM", "JSON SIM"),
        ("clientUserId", "Embedded signing"),
        ("voided", "Cancel envelope"),
        ("redirect URI", "Go-live setup"),
        ("template ID", "Templates in production"),
        ("anchorString", "Anchor tabs"),
        ("Workflow Builder API", "Workflow API"),
        ("Workflow", "Workflow steps"),
        ("Organization-Level Connect", "Configuration level"),
        ("API proxy", "API proxy"),
        ("connections", "Connections"),
        ("firewall", "Firewall"),
        ("Connected Fields", "Connected Fields"),
        ("Data Verification", "Data Verification"),
        ("Private extension app", "Public vs private"),
        ("App Center", "Public App Center"),
        ("Brand Destination", "Brand destination URLs"),
        ("transactionId", "Idempotency"),
    ]
    for needle, topic in topic_rules:
        if contains_any(primary, needle):
            return topic
    for needle, topic in topic_rules:
        if contains_any(text, needle):
            return topic
    return answer[:55].rstrip(".")


def spread_sources_within_domain(questions: list[dict]) -> list[dict]:
    grouped = defaultdict(lambda: {"generated": [], "pdf": []})
    for question in questions:
        bucket = "pdf" if question.get("source") else "generated"
        grouped[question["domain"]][bucket].append(question)

    spread = {}
    for domain, parts in grouped.items():
        generated = parts["generated"]
        pdf = parts["pdf"]
        if not pdf:
            spread[domain] = generated
            continue
        interval = max(1, len(generated) // (len(pdf) + 1))
        output = []
        pdf_index = 0
        for index, question in enumerate(generated, start=1):
            output.append(question)
            if pdf_index < len(pdf) and index % interval == 0:
                output.append(pdf[pdf_index])
                pdf_index += 1
        output.extend(pdf[pdf_index:])
        spread[domain] = output
    return [question for domain in DOMAIN_ORDER for question in spread.get(domain, [])]


def interleave_by_domain(questions: list[dict]) -> list[dict]:
    buckets = {domain: deque() for domain in DOMAIN_ORDER}
    for question in questions:
        buckets.setdefault(question["domain"], deque()).append(question)

    mixed = []
    while any(buckets.values()):
        for domain in DOMAIN_ORDER:
            if buckets[domain]:
                mixed.append(buckets[domain].popleft())
    return mixed


def build_generated_questions() -> list[dict]:
    base = parse_questions(BASE_SOURCE.read_text(encoding="utf-8"))
    generated = []
    for index, question in enumerate(base):
        next_question = dict(question)
        next_question["sourceId"] = question["id"]
        next_question["stem"] = enrich_stem(question, index)
        next_question["optionExplanations"] = improve_option_explanations(next_question)
        generated.append(next_question)
    return generated


def to_markdown(questions: list[dict]) -> str:
    lines = [
        "# Certified Docusign IAM Integration & Extension Developer - Scenario Practice Questions",
        "",
        f"Total questions: {len(questions)}",
        "",
        "Includes the generated scenario practice bank plus questions imported from `Docusign_Combined_QA_Explained.pdf`.",
        "",
    ]
    for question in questions:
        source = f" - source: {question['source']}" if question.get("source") else ""
        lines.append(f"**Q{question['id']}. ({question['domain']} - {question['topic']}{source})** {question['stem']}")
        lines.append("")
        for option in question["options"]:
            lines.append(f"{option['id']}. {option['text']}")
        lines.append("")
        lines.append(f"**Answer:** {question['correct']}. {question['answerText']}")
        lines.append("")
        lines.append(f"**Explanation:** {question['explanation']}")
        lines.append("")
        lines.append("**Option notes:**")
        for option in question["options"]:
            lines.append(f"- {option['id']}. {question['optionExplanations'][option['id']]}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    generated = build_generated_questions()
    pdf_questions = parse_pdf_questions(extract_pdf_text())
    if len(generated) != 300:
        raise RuntimeError(f"Expected 300 generated questions, found {len(generated)}")
    if len(pdf_questions) != 47:
        raise RuntimeError(f"Expected 47 PDF questions, found {len(pdf_questions)}")

    combined = spread_sources_within_domain(generated + pdf_questions)
    mixed = interleave_by_domain(combined)
    for index, question in enumerate(mixed, start=1):
        question["id"] = index

    JSON_DEST.write_text(json.dumps(mixed, indent=2), encoding="utf-8")
    MARKDOWN_DEST.write_text(to_markdown(mixed), encoding="utf-8")

    pdf_count = sum(1 for question in mixed if question.get("source"))
    print(f"Wrote {len(mixed)} questions to {JSON_DEST}")
    print(f"Imported PDF questions: {pdf_count}")
    print(f"Wrote Markdown copy to {MARKDOWN_DEST}")


if __name__ == "__main__":
    main()

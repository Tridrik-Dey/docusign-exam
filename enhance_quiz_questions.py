from __future__ import annotations

import json
import re
from collections import defaultdict, deque
from pathlib import Path


SOURCE = Path("quiz-app/src/questions.json")
DEST = Path("quiz-app/src/questions.json")
MARKDOWN_DEST = Path("output/docusign_iam_integration_extension_300_practice_questions_exam_style.md")


PEOPLE = [
    ("Maya", "an integration lead"),
    ("Daniel", "a solutions architect"),
    ("Priya", "a platform engineer"),
    ("Luca", "a developer on the IAM team"),
    ("Sofia", "a business systems analyst"),
    ("Noah", "an API developer"),
    ("Elena", "an implementation consultant"),
    ("Amir", "a workflow automation engineer"),
    ("Grace", "a product owner"),
    ("Mateo", "a DevOps engineer"),
]

ORGS = [
    "a public-sector records department",
    "a regional healthcare provider",
    "a multinational HR operations team",
    "a commercial real-estate group",
    "a university financial-aid office",
    "a banking compliance unit",
    "a legal operations team",
    "a procurement shared-services group",
    "a partner-built customer portal",
    "a sales contract automation team",
]

PROJECTS = [
    "replacing a manual agreement process with a Docusign IAM integration",
    "moving a pilot integration from a developer account toward production",
    "standardizing how agreements are prepared, sent, monitored, and stored",
    "building a self-service portal for internal teams and external customers",
    "automating high-volume agreement work while keeping auditability intact",
    "connecting several line-of-business systems to Docusign APIs",
    "reducing support tickets caused by inconsistent envelope handling",
    "adding reusable agreement automation to an existing business application",
]

BUSINESS_CONTEXT = {
    "API Authentication": [
        "Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets.",
        "The team must choose an OAuth pattern before the integration key is approved for wider use.",
        "The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable.",
    ],
    "Go Live Process": [
        "The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users.",
        "The release manager is preparing production readiness evidence and wants to avoid common go-live delays.",
        "The team has to distinguish configuration that belongs in demo from configuration that must exist in production.",
    ],
    "Docusign Connect": [
        "Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks.",
        "The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried.",
        "The integration owner is deciding whether to configure notifications globally or for only one envelope workflow.",
    ],
    "eSignature API": [
        "The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process.",
        "Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration.",
        "The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow.",
    ],
    "eSignature Features and Web Forms": [
        "Business users want structured intake and signer verification without asking developers to rebuild every form from scratch.",
        "The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement.",
        "The team is deciding when to use Docusign platform features instead of custom code around the eSignature API.",
    ],
    "Agreement Manager API": [
        "The records team wants agreement data available to downstream reporting and lifecycle processes after signature.",
        "The organization is modernizing legacy agreement records and needs API access to agreement metadata and documents.",
        "The integration must retrieve agreement information without confusing envelope execution data with agreement repository data.",
    ],
    "Workflow Builder and Workflow API": [
        "Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application.",
        "The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern.",
        "A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected.",
    ],
    "App Center and Extension Apps": [
        "A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked.",
        "The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware.",
        "The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately.",
    ],
}

SHORT_PREFIXES = [
    "During a design review, the team asks a direct knowledge-check question.",
    "A developer is validating a single concept before continuing implementation.",
    "In a quick architecture review, the team wants the best answer without extra workflow context.",
]


def split_stem(stem: str) -> tuple[str, str]:
    cleaned = re.sub(r"\s+", " ", stem).strip()
    cleaned = re.sub(r"^.+?scenario:\s*", "", cleaned, flags=re.IGNORECASE)
    if "?" in cleaned:
        before, after = cleaned.rsplit("?", 1)
        sentences = re.split(r"(?<=[.!])\s+", before.strip())
        ask_start = sentences[-1].strip()
        context = " ".join(sentences[:-1]).strip()
        ask = f"{ask_start}?{after}".strip()
        if not context:
            context = before.strip()
        return context, ask
    return cleaned, "What should the developer do?"


def sentence_case(text: str) -> str:
    text = text.strip()
    text = re.sub(r"[.!?]+$", "", text)
    if not text:
        return text
    return text[0].lower() + text[1:]


def enrich_stem(question: dict, index: int) -> str:
    context, ask = split_stem(question["stem"])
    person, role = PEOPLE[index % len(PEOPLE)]
    org = ORGS[(index * 3) % len(ORGS)]
    project = PROJECTS[(index * 5) % len(PROJECTS)]
    domain_notes = BUSINESS_CONTEXT.get(question["domain"], BUSINESS_CONTEXT["eSignature API"])
    note = domain_notes[index % len(domain_notes)]

    pattern = index % 12
    if pattern in {0, 1, 2, 3, 4, 5, 6, 7, 8}:
        return (
            f"{person}, {role} at {org}, is {project}. {note} "
            f"In the current design, {sentence_case(context)}. "
            f"The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. "
            f"{ask}"
        )
    if pattern in {9, 10}:
        return (
            f"{person}, {role}, is reviewing a Docusign implementation for {org}. "
            f"The relevant requirement is that {sentence_case(context)}. {ask}"
        )
    return f"{SHORT_PREFIXES[index % len(SHORT_PREFIXES)]} {ask}"


def improve_option_explanations(question: dict) -> dict[str, str]:
    answer_text = question["answerText"]
    explanation = question["explanation"]
    topic = question["topic"]
    output = {}
    for option in question["options"]:
        if option["id"] == question["correct"]:
            output[option["id"]] = explanation
            continue
        output[option["id"]] = (
            f"{option['text']} can be valid in a different Docusign scenario, but it does not match the requirement in this question. "
            f"The key clue points to {answer_text}: {explanation}"
        )
        if option["text"].lower() == answer_text.lower():
            output[option["id"]] = explanation
        if "Implicit Grant" in option["text"]:
            output[option["id"]] = (
                "Implicit Grant is not the preferred modern choice for these integrations. "
                f"The scenario is testing {topic}, and the better fit is {answer_text}."
            )
    return output


def interleave_by_domain(questions: list[dict]) -> list[dict]:
    buckets: dict[str, deque[dict]] = defaultdict(deque)
    domain_order = []
    for question in questions:
        domain = question["domain"]
        if domain not in buckets:
            domain_order.append(domain)
        buckets[domain].append(question)

    mixed = []
    while any(buckets.values()):
        for domain in domain_order:
            if buckets[domain]:
                mixed.append(buckets[domain].popleft())
    return mixed


def to_markdown(questions: list[dict]) -> str:
    lines = [
        "# Certified Docusign IAM Integration & Extension Developer - Exam-Style Practice Questions",
        "",
        "This version uses longer scenario-based wording for most questions and mixes domains in the default order.",
        "",
    ]
    for question in questions:
        lines.append(f"**Q{question['id']}. ({question['domain']} - {question['topic']})** {question['stem']}")
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
    questions = json.loads(SOURCE.read_text(encoding="utf-8"))
    enriched = []
    for index, question in enumerate(questions):
        next_question = dict(question)
        next_question["sourceId"] = question["id"]
        next_question["stem"] = enrich_stem(question, index)
        next_question["optionExplanations"] = improve_option_explanations(next_question)
        enriched.append(next_question)

    mixed = interleave_by_domain(enriched)
    for index, question in enumerate(mixed, start=1):
        question["id"] = index

    DEST.write_text(json.dumps(mixed, indent=2), encoding="utf-8")
    MARKDOWN_DEST.write_text(to_markdown(mixed), encoding="utf-8")

    long_count = sum(len(question["stem"].split()) >= 55 for question in mixed)
    medium_count = sum(30 <= len(question["stem"].split()) < 55 for question in mixed)
    short_count = len(mixed) - long_count - medium_count
    print(f"Wrote {len(mixed)} mixed questions to {DEST}")
    print(f"Question size mix: {long_count} long, {medium_count} medium, {short_count} short")
    print(f"Wrote Markdown copy to {MARKDOWN_DEST}")


if __name__ == "__main__":
    main()

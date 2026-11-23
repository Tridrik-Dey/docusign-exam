from __future__ import annotations

import json
import re
from pathlib import Path

from create_quiz_data import parse_questions
from improve_wrong_answer_explanations import to_markdown


QUESTIONS = Path("quiz-app/src/questions.json")
BASE_SOURCE = Path("output/docusign_iam_integration_extension_300_practice_questions.md")
MARKDOWN = Path("output/docusign_iam_integration_extension_practice_questions_with_pdf.md")


PEOPLE = [
    "Maya",
    "Daniel",
    "Priya",
    "Luca",
    "Sofia",
    "Noah",
    "Elena",
    "Amir",
    "Grace",
    "Mateo",
    "Nadia",
    "Robin",
]

ROLES = [
    "integration lead",
    "solutions architect",
    "platform engineer",
    "IAM developer",
    "business systems analyst",
    "API developer",
    "implementation consultant",
    "workflow automation engineer",
    "product owner",
    "release manager",
]

ORGS = [
    "a public-sector records office",
    "a regional healthcare provider",
    "a global HR team",
    "a real-estate operations group",
    "a university financial-aid office",
    "a banking compliance team",
    "a legal operations department",
    "a procurement shared-services team",
    "a partner software vendor",
    "a sales contracting team",
]

DOMAIN_CONTEXTS = {
    "API Authentication": [
        "Security review is focused on user consent, token scope, and whether the application can protect secrets.",
        "The integration must authenticate reliably across demo and production without over-permissioning users.",
        "A developer is deciding how the app should obtain tokens before making Docusign API calls.",
    ],
    "Go Live Process": [
        "The demo integration works, but the release checklist is not complete for production.",
        "The team is preparing evidence for go-live review and wants to avoid a failed production cutover.",
        "A production rollout is blocked until the developer separates demo-only configuration from production setup.",
    ],
    "Docusign Connect": [
        "Downstream systems need timely status changes without users manually refreshing dashboards.",
        "The webhook listener must handle the right event source and payload format.",
        "The architect is deciding whether notifications belong on a single envelope, an account, or a broader configuration.",
    ],
    "eSignature API": [
        "The application must prepare and send envelopes without forcing senders through the manual UI.",
        "The developer is translating a sender's manual envelope process into API configuration.",
        "The requirement involves recipients, templates, tabs, envelope status, or an embedded signing session.",
    ],
    "eSignature Features and Web Forms": [
        "Business users want form intake, identity checks, or post-signing behavior handled by Docusign platform features.",
        "The process needs to connect data capture or verification to an agreement workflow.",
        "The product owner wants to avoid rebuilding a Docusign feature as custom application code.",
    ],
    "Agreement Manager API": [
        "The reporting team needs agreement data after documents are signed and stored.",
        "A legacy repository is being modernized so agreement records can be queried through Docusign APIs.",
        "The developer must distinguish live envelope operations from agreement repository operations.",
    ],
    "Workflow Builder and Workflow API": [
        "Business owners want a repeatable process with steps that can change without rewriting the whole application.",
        "The workflow combines data collection, signatures, identity checks, branching, and external system calls.",
        "The team is deciding how a workflow should start and which step belongs where.",
    ],
    "App Center and Extension Apps": [
        "A partner team is packaging reusable behavior that customers can install into the Docusign IAM platform.",
        "The extension app must expose an external capability without making each customer build custom middleware.",
        "The developer is reviewing manifest, connection, proxy, firewall, and distribution choices.",
    ],
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def sentence_body(text: str) -> str:
    text = normalize(re.sub(r"^.+?scenario:\s*", "", text, flags=re.IGNORECASE))
    text = re.sub(r"[.!?]+$", "", text)
    return text[0].lower() + text[1:] if text else text


def ticket_text(context: str) -> str:
    replacements = [
        (r"^a developer needs to ", "configure the integration to "),
        (r"^a developer wants to ", "allow the developer to "),
        (r"^a developer promotes ", "promote "),
        (r"^a developer ", "handle a case where the developer "),
        (r"^an app needs to ", "make the app "),
        (r"^an app ", "handle an app that "),
        (r"^a system must ", "make the system "),
        (r"^a custom app needs ", "make a custom app retrieve "),
        (r"^a custom website needs ", "render "),
    ]
    output = context
    for pattern, replacement in replacements:
        output = re.sub(pattern, replacement, output, flags=re.IGNORECASE)
    return output


def split_original(stem: str) -> tuple[str, str]:
    stem = normalize(stem)
    if "?" not in stem:
        return sentence_body(stem), "What should the developer choose?"
    before, after = stem.rsplit("?", 1)
    sentences = re.split(r"(?<=[.!])\s+", before)
    ask_start = sentences[-1].strip()
    context = " ".join(sentences[:-1]).strip() or before
    return sentence_body(context), f"{ask_start}?{after}".strip()


def article(role: str) -> str:
    return "an" if role[0].lower() in "aeiou" else "a"


def domain_context(domain: str, index: int) -> str:
    contexts = DOMAIN_CONTEXTS.get(domain, DOMAIN_CONTEXTS["eSignature API"])
    return contexts[index % len(contexts)]


def domain_risk(domain: str, index: int) -> str:
    risks = {
        "API Authentication": [
            "Choosing the wrong flow could either expose a secret in the browser or force users through an unnecessary consent experience.",
            "The security team will reject the design if the token flow does not match the client type.",
            "The app must avoid broad permissions while still getting a token that works for the required API calls.",
        ],
        "Go Live Process": [
            "A bad assumption here would pass in demo and then fail immediately after production cutover.",
            "The release cannot depend on demo-only IDs, endpoints, or settings.",
            "The reviewer wants evidence that the production account has the equivalent configuration, not only working demo tests.",
        ],
        "Docusign Connect": [
            "Polling would increase API traffic and still miss the clean event-driven design the business asked for.",
            "If the wrong notification level is used, the listener may receive either too few events or unrelated events.",
            "The receiving system must be able to trust and process the event payload consistently.",
        ],
        "eSignature API": [
            "If this is configured incorrectly, recipients may never receive the envelope or may be sent through the wrong ceremony.",
            "The sender wants the API request to create the same result they would have configured manually.",
            "The implementation needs the right envelope field, not a post-processing workaround.",
        ],
        "eSignature Features and Web Forms": [
            "Using a custom workaround would add maintenance burden and miss the Docusign feature built for this case.",
            "The wrong choice would separate intake, identity, or redirect behavior from the agreement process.",
            "The business wants the signer or form participant experience to stay inside the supported Docusign pattern.",
        ],
        "Agreement Manager API": [
            "Confusing envelope execution with agreement repository data would send the developer to the wrong API surface.",
            "The reporting requirement depends on agreement metadata and extracted data, not just envelope status.",
            "The system of record needs agreement-level information after the document lifecycle has moved beyond signing.",
        ],
        "Workflow Builder and Workflow API": [
            "Putting the step in the wrong order would prevent later steps from using the data or output they depend on.",
            "The business wants the workflow to remain configurable, so the app should not hard-code every branch externally.",
            "The runtime behavior must match how Workflow Builder starts, embeds, and executes workflow instances.",
        ],
        "App Center and Extension Apps": [
            "A wrong manifest or distribution choice would make the extension hard to install or impossible to publish.",
            "The app must respect how Docusign calls external services through extension app actions and connections.",
            "The partner wants a reusable capability, so a one-off custom integration is not enough.",
        ],
    }
    choices = risks.get(domain, risks["eSignature API"])
    return choices[index % len(choices)]


def business_goal(domain: str, index: int) -> str:
    goals = {
        "API Authentication": [
            "The application team is finalizing its sign-in and consent design before creating production credentials.",
            "A security architect is comparing the app's runtime model with Docusign OAuth options.",
            "Developers need a token strategy that matches whether a user is present and whether a secret can be protected.",
        ],
        "Go Live Process": [
            "The release manager is checking what must change when the app moves from demo to production.",
            "The team has a working demo proof of concept and is preparing for the go-live review.",
            "Operations wants to know which configuration has to be recreated or validated in the production account.",
        ],
        "Docusign Connect": [
            "The operations dashboard needs to update from Docusign events instead of manual status checks.",
            "An integration listener is being designed for envelope, recipient, or workflow activity.",
            "The system must receive the right webhook payload at the right level of configuration.",
        ],
        "eSignature API": [
            "The app is replacing manual envelope preparation with an API-driven send experience.",
            "A developer is mapping recipient, template, tab, and envelope status requirements into the create-envelope request.",
            "The business wants the signing experience to behave correctly the first time the envelope is created.",
        ],
        "eSignature Features and Web Forms": [
            "The product owner is deciding which Docusign feature should handle intake, identity, or recipient routing.",
            "A web app needs to embed or coordinate a Docusign experience without rebuilding that feature from scratch.",
            "The process depends on collecting reliable data before or during the agreement flow.",
        ],
        "Agreement Manager API": [
            "A reporting service needs agreement-level records after documents are completed and stored.",
            "The legal team wants structured agreement data available to downstream systems.",
            "A migration project is trying to bring older agreement records into the Docusign agreement layer.",
        ],
        "Workflow Builder and Workflow API": [
            "Process owners are designing a workflow that combines intake, approvals, signatures, and external actions.",
            "A portal needs to launch or embed a workflow while keeping the workflow logic maintainable in Docusign.",
            "The automation team is deciding which Workflow Builder step or API behavior matches the business process.",
        ],
        "App Center and Extension Apps": [
            "A partner is turning an external service into a reusable Docusign extension app.",
            "The developer is configuring how Docusign will authenticate to and call an external platform.",
            "The product team is choosing between a private extension and a public App Center distribution model.",
        ],
    }
    choices = goals.get(domain, goals["eSignature API"])
    return choices[index % len(choices)]


def rewrite_stem(question: dict, original_stem: str, index: int) -> str:
    context, ask = split_original(original_stem)
    person = PEOPLE[index % len(PEOPLE)]
    role = ROLES[(index * 2) % len(ROLES)]
    org = ORGS[(index * 3) % len(ORGS)]
    domain_note = domain_context(question["domain"], index)
    topic = question["topic"]
    risk = domain_risk(question["domain"], index)
    goal = business_goal(question["domain"], index)
    pattern = index % 20

    if pattern == 0:
        return (
            f"{person}, {article(role)} {role} at {org}, is reviewing a Docusign implementation before it is approved. "
            f"{goal} The key requirement is that {context}. {risk} {ask}"
        )
    if pattern == 1:
        return (
            f"A developer on {org} opens an implementation ticket for a Docusign project: {ticket_text(context)}. "
            f"The team wants to use the platform feature intended for this requirement instead of adding custom glue code. "
            f"{risk} {ask}"
        )
    if pattern == 2:
        return (
            f"During a demo test for {org}, the team notices a gap in the design. "
            f"{domain_note} The specific requirement is that {context}. Which answer closes the gap without changing the rest of the workflow?"
        )
    if pattern == 3:
        return (
            f"{person} is comparing four Docusign options for {org}. "
            f"The business process will only work if the configuration handles this condition correctly: {context}. {risk} {ask}"
        )
    if pattern == 4:
        return (
            f"In a design review, the architect removes several custom-code ideas from consideration and asks for the native Docusign approach. "
            f"{goal} For this part of the design, {context}. {ask}"
        )
    if pattern == 5:
        return (
            f"A support ticket from {org} describes a likely production issue: {context}. "
            f"{domain_note} The fix should address the root platform behavior, not only the visible symptom. "
            f"Which response best matches Docusign platform behavior?"
        )
    if pattern == 6:
        return (
            f"{person} is preparing guidance for developers who will maintain a Docusign integration at {org}. "
            f"The guidance needs to explain how to handle this situation: {context}. "
            f"{domain_note} What should the guidance recommend?"
        )
    if pattern == 7:
        return (
            f"An implementation team is converting a manual agreement process into an API-driven Docusign flow. "
            f"They have already agreed on the business process, but this technical detail remains open: {context}. "
            f"The answer should preserve the intended Docusign responsibility instead of shifting the work into custom code. {ask}"
        )
    if pattern == 8:
        return (
            f"{org.capitalize()} asks for a recommendation after a stakeholder challenges the original design. "
            f"The challenged requirement is simple but important: {context}. "
            f"{risk} Which option should the team keep?"
        )
    if pattern == 9:
        return (
            f"A senior developer is reviewing a pull request for a Docusign integration. "
            f"The code path being reviewed assumes that {context}. {ask}"
        )
    if pattern == 10:
        return (
            f"{person} joins a troubleshooting call for {org}. Users report that the process does not behave as expected, and the root requirement is that {context}. "
            f"{risk} Which option should be used?"
        )
    if pattern == 11:
        return (
            f"Before training the support team, {org} wants a clear rule for a recurring Docusign scenario. "
            f"If {context}, what is the correct recommendation?"
        )
    if pattern == 12:
        return (
            f"A customer success engineer writes an implementation note for {org}: {context}. "
            f"The note must point developers to the correct Docusign capability and avoid a workaround that only works in the demo. {ask}"
        )
    if pattern == 13:
        return (
            f"{person}, working with {org}, has to choose one Docusign setting before the build can continue. "
            f"The setting is needed because {context}. Which choice fits?"
        )
    if pattern == 14:
        return (
            f"The project team rejects a manual workaround and returns to the Docusign documentation. "
            f"The requirement they are trying to satisfy is that {context}. {ask}"
        )
    if pattern == 15:
        return (
            f"Knowledge check: {ask} "
            f"Assume {context}. Choose the answer that follows Docusign's normal product behavior."
        )
    if pattern == 16:
        return (
            f"{person} needs a quick architecture answer for {org}. "
            f"The requirement is that {context}. The team is choosing between platform-native options. Which option is correct?"
        )
    if pattern == 17:
        return (
            f"A Docusign implementation has this requirement: {context}. "
            f"The developer wants the answer that matches the supported API or IAM platform pattern. {ask}"
        )
    if pattern == 18:
        return (
            f"During QA, a tester validates this behavior: {context}. "
            f"If the wrong setting is selected, the test will pass only for the narrow demo case. "
            f"What should the expected Docusign configuration be?"
        )
    return (
        f"{topic}: {ask} "
        f"The relevant requirement is that {context}, and the answer should map to the Docusign feature designed for that job."
    )


def main() -> None:
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    originals = {question["id"]: question for question in parse_questions(BASE_SOURCE.read_text(encoding="utf-8"))}

    changed = 0
    for index, question in enumerate(questions):
        if question.get("source"):
            continue
        source_id = question.get("sourceId")
        original = originals.get(source_id)
        if not original:
            continue
        question["stem"] = rewrite_stem(question, original["stem"], index)
        changed += 1

    QUESTIONS.write_text(json.dumps(questions, indent=2), encoding="utf-8")
    MARKDOWN.write_text(to_markdown(questions), encoding="utf-8")
    print(f"Rewrote {changed} generated stems")


if __name__ == "__main__":
    main()

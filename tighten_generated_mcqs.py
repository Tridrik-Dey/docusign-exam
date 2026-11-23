from __future__ import annotations

import json
from difflib import SequenceMatcher
from pathlib import Path

from improve_wrong_answer_explanations import to_markdown, wrong_explanation


QUESTIONS = Path("quiz-app/src/questions.json")
MARKDOWN = Path("output/docusign_iam_integration_extension_practice_questions_with_pdf.md")


DISTRACTOR_POOLS = {
    "oauth_flows": [
        "Confidential Authorization Code Grant",
        "Public Authorization Code Grant with PKCE",
        "JSON Web Token Grant",
        "Implicit Grant",
        "Refresh token exchange",
    ],
    "oauth_support": [
        "/oauth/token",
        "/oauth/userinfo",
        "Authorization: Bearer access token",
        "admin consent for requested scopes",
        "CORS allowed origin",
    ],
    "connect": [
        "account-level Connect configuration",
        "organization-level Connect configuration",
        "eventNotification on the envelope",
        "JSON SIM event payload",
        "HMAC validation on the listener",
        "polling Envelopes:get from the app",
    ],
    "envelope_status": [
        "created",
        "sent",
        "voided",
        "completed",
        "deleted",
    ],
    "embedded": [
        "clientUserId",
        "recipientId",
        "returnUrl",
        "EnvelopeViews:createRecipient",
        "remote signing email",
        "embedded sending view",
    ],
    "templates_tabs": [
        "templateId",
        "serverTemplates and inlineTemplates",
        "anchorString with offsets",
        "tabLabel",
        "brandId",
        "documentId",
    ],
    "bulk_idempotency": [
        "transactionId",
        "BulkSend:createBulkSendList",
        "batchId",
        "envelopeId",
        "retrying with a new subject line",
    ],
    "webforms_identity": [
        "Docusign JS client SDK",
        "Web Form instance URL",
        "externalReferenceId",
        "Identity Verification workflow",
        "recipient authentication",
        "Brand destination URL",
        "ID Evidence API",
    ],
    "agreement_manager": [
        "Agreements:getAgreement",
        "Agreements:list",
        "agreement document retrieval",
        "legacy agreement import",
        "Connect envelope payload",
        "eSignature envelope status",
    ],
    "workflow": [
        "Collect Data with Web Forms, then Get Signatures",
        "Get Signatures before Collect Data",
        "workflow start method: From a Link",
        "workflow start method: From an API call",
        "Extension step",
        "branching condition",
        "workflow instance URL embedded in an iframe",
    ],
    "extension": [
        "private extension app",
        "public App Center listing",
        "manifest actions object",
        "connections object",
        "connectionsReference",
        "API proxy",
        "Configure network firewall",
        "Data IO extension app",
        "File IO extension app",
        "Data Verification extension app",
        "Connected Fields",
    ],
    "golive": [
        "production redirect URI and secret",
        "production base URI and endpoints",
        "deploy or recreate the production template",
        "go-live review classification",
        "reuse the demo account ID",
        "completed demo envelope IDs",
        "post-go-live production validation",
    ],
}


TOPIC_POOLS = {
    "OAuth flow selection": ["oauth_flows"],
    "JWT Grant": ["oauth_flows", "oauth_support"],
    "Consent": ["oauth_support", "oauth_flows"],
    "Scopes": ["oauth_support", "oauth_flows"],
    "User info": ["oauth_support"],
    "PKCE": ["oauth_flows", "oauth_support"],
    "Bearer tokens": ["oauth_support"],
    "Go-live setup": ["golive", "oauth_support"],
    "Integration classification": ["golive", "extension"],
    "Production endpoints": ["golive", "oauth_support"],
    "Templates in production": ["golive", "templates_tabs"],
    "Post go-live": ["golive", "oauth_support"],
    "API limits": ["golive", "connect"],
    "Troubleshooting": ["golive", "oauth_support", "connect"],
    "Envelope-level Connect": ["connect"],
    "Connect vs polling": ["connect"],
    "Configuration level": ["connect"],
    "JSON SIM": ["connect"],
    "Security": ["connect", "extension"],
    "Retries": ["connect"],
    "Payload selection": ["connect"],
    "Envelope create": ["envelope_status", "templates_tabs"],
    "Draft envelope": ["envelope_status"],
    "Cancel envelope": ["envelope_status"],
    "Idempotency": ["bulk_idempotency", "envelope_status"],
    "Template reference": ["templates_tabs"],
    "Composite templates": ["templates_tabs"],
    "Anchor tabs": ["templates_tabs"],
    "Embedded signing": ["embedded"],
    "Signing URL": ["embedded"],
    "Embedded signing timing": ["embedded", "envelope_status"],
    "Embedded sending": ["embedded"],
    "Bulk send": ["bulk_idempotency", "embedded"],
    "Web Forms embedding": ["webforms_identity", "embedded"],
    "Web Form correlation": ["webforms_identity"],
    "Identity verification": ["webforms_identity", "embedded"],
    "Recipient authentication": ["webforms_identity", "embedded"],
    "Brand destination URLs": ["webforms_identity", "templates_tabs"],
    "Connected Fields": ["extension", "webforms_identity"],
    "ID Evidence": ["webforms_identity", "agreement_manager"],
    "Agreement data": ["agreement_manager"],
    "Agreement list": ["agreement_manager"],
    "Legacy import": ["agreement_manager"],
    "Agreement documents": ["agreement_manager"],
    "Workflow steps": ["workflow", "webforms_identity"],
    "Identity step": ["workflow", "webforms_identity"],
    "Extension step": ["workflow", "extension"],
    "Branching": ["workflow"],
    "Start method": ["workflow"],
    "API trigger": ["workflow"],
    "Runtime errors": ["workflow", "connect"],
    "Embedding workflow": ["workflow", "embedded"],
    "Installed extensions": ["workflow", "extension"],
    "Extension app role": ["extension", "workflow"],
    "Public vs private": ["extension"],
    "Public App Center": ["extension"],
    "Manifest": ["extension"],
    "Connections": ["extension", "oauth_support"],
    "connectionsReference": ["extension"],
    "API proxy": ["extension"],
    "Firewall": ["extension"],
    "Data IO": ["extension"],
    "File IO": ["extension"],
    "Data Verification": ["extension", "webforms_identity"],
}


def pool_for(question: dict) -> list[str]:
    pool_names = TOPIC_POOLS.get(question["topic"])
    if not pool_names:
        if question["domain"] == "API Authentication":
            pool_names = ["oauth_flows", "oauth_support"]
        elif question["domain"] == "Docusign Connect":
            pool_names = ["connect"]
        elif question["domain"] == "eSignature API":
            pool_names = ["envelope_status", "embedded", "templates_tabs"]
        elif question["domain"] == "Workflow Builder and Workflow API":
            pool_names = ["workflow"]
        elif question["domain"] == "App Center and Extension Apps":
            pool_names = ["extension"]
        elif question["domain"] == "Agreement Manager API":
            pool_names = ["agreement_manager"]
        elif question["domain"] == "Go Live Process":
            pool_names = ["golive"]
        else:
            pool_names = ["webforms_identity"]
    values = []
    for name in pool_names:
        values.extend(DISTRACTOR_POOLS[name])
    return values


def normalize(text: str) -> str:
    return " ".join(text.lower().replace(":", " ").replace("-", " ").split())


def too_close_to_correct(candidate: str, correct: str) -> bool:
    left = normalize(candidate)
    right = normalize(correct)
    if left == right:
        return True
    if "authorization code grant" in left and "authorization code grant" in right:
        if ("public" in left and "confidential" in right) or ("confidential" in left and "public" in right):
            return False
    if SequenceMatcher(None, left, right).ratio() >= 0.66:
        return True
    important_terms = [
        "eventnotification",
        "docusign js client sdk",
        "redirect uri",
        "secret",
        "json web token",
        "confidential authorization code",
        "public authorization code",
        "clientuserid",
        "transactionid",
        "agreements getagreement",
    ]
    compact_left = left.replace(" ", "")
    compact_right = right.replace(" ", "")
    for term in important_terms:
        if term in compact_left and term in compact_right:
            return True
    return False


def choose_distractors(question: dict) -> list[str]:
    correct = question["answerText"]
    existing_wrong = [option["text"] for option in question["options"] if option["id"] != question["correct"]]
    candidates = []
    for item in pool_for(question) + existing_wrong:
        if too_close_to_correct(item, correct):
            continue
        if normalize(item) in {normalize(value) for value in candidates}:
            continue
        candidates.append(item)
    return candidates[:3]


def main() -> None:
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    changed = 0
    for question in questions:
        if question.get("source"):
            continue
        distractors = choose_distractors(question)
        if len(distractors) < 3:
            continue
        cursor = 0
        for option in question["options"]:
            if option["id"] == question["correct"]:
                continue
            option["text"] = distractors[cursor]
            cursor += 1
        question["optionExplanations"] = {}
        for option in question["options"]:
            if option["id"] == question["correct"]:
                question["optionExplanations"][option["id"]] = question["explanation"]
            else:
                question["optionExplanations"][option["id"]] = wrong_explanation(question, option)
        changed += 1

    QUESTIONS.write_text(json.dumps(questions, indent=2), encoding="utf-8")
    MARKDOWN.write_text(to_markdown(questions), encoding="utf-8")
    print(f"Tightened distractors for {changed} generated questions")


if __name__ == "__main__":
    main()

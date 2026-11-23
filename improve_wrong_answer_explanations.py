from __future__ import annotations

import json
import re
from pathlib import Path


QUESTIONS = Path("quiz-app/src/questions.json")
MARKDOWN = Path("output/docusign_iam_integration_extension_practice_questions_with_pdf.md")


GENERIC_RE = re.compile(
    r"can be valid in a different Docusign scenario|does not match the requirement|key clue points",
    re.IGNORECASE,
)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def has(text: str, *needles: str) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def describe_option(option: str) -> str:
    text = option.lower()
    exact = {
        "json web token grant": "JWT Grant is used for non-interactive service integrations after consent is granted, usually with a system user and RSA key pair.",
        "confidential authorization code grant": "Confidential Authorization Code Grant is for server-side apps that can protect a client secret while an individual user signs in interactively.",
        "public authorization code grant": "Public Authorization Code Grant with PKCE is for public clients such as browser-only or native apps that cannot safely store a client secret.",
        "public authorization code grant with pkce": "Public Authorization Code Grant with PKCE is for public clients such as browser-only or native apps that cannot safely store a client secret.",
        "implicit grant": "Implicit Grant is an older browser-based OAuth flow and is not the recommended modern choice for Docusign public clients.",
        "created": "The created envelope status saves an envelope as a draft; it does not send the envelope to recipients.",
        "sent": "The sent envelope status sends the envelope to recipients for action.",
        "completed": "The completed status is reached after all required recipient actions finish; it is not normally set to start or cancel a workflow.",
        "voided": "The voided status cancels an in-process envelope so recipients can no longer complete it.",
        "deleted": "Deleted is not the normal API status for canceling an active envelope in the signing process.",
        "purged": "Purging removes completed documents according to retention rules; it is not how you route, send, or cancel an active envelope.",
        "envelope purge": "Envelope purge is a retention/privacy operation for removing document content, not a normal sending, routing, or notification step.",
        "clientuserid": "clientUserId identifies an embedded recipient and links that recipient to an embedded signing URL request.",
        "recipientid": "recipientId identifies a recipient within an envelope, but by itself it does not enable embedded signing or external tracking.",
        "transactionid": "transactionId is an idempotency value used to make envelope creation retries safer.",
        "brandid": "brandId applies an account brand to the signing or email experience; it does not control routing, identity, Connect, or OAuth behavior.",
        "returnurl": "returnUrl tells Docusign where to send the browser after an embedded ceremony ends; it is not an authentication, recipient identity, or envelope configuration value.",
        "basepath": "basePath or base URI tells the app which Docusign API host to call; it is not a recipient, template, or workflow setting.",
        "templateid": "templateId references a Docusign template that defines reusable documents, recipients, tabs, and settings.",
        "envelope ids": "Envelope IDs identify individual envelope instances after creation; they are not reusable production configuration.",
        "completed demo envelopes": "Completed demo envelopes are test transaction records; they are not migrated configuration for production go-live.",
        "connect event logs": "Connect event logs help troubleshoot webhook delivery; they are not production app settings that replace redirect URIs, secrets, or templates.",
        "connect hmac secret only": "A Connect HMAC secret signs webhook payloads so the listener can verify authenticity; it does not configure the event source or business workflow.",
        "a connect retry policy": "A Connect retry policy controls webhook redelivery behavior after failures; it does not choose an OAuth flow or create an envelope workflow.",
        "connect json sim": "JSON SIM is a Connect message format for certain event subscriptions; it is not an envelope API action or workflow step.",
        "json sim format": "JSON SIM is a structured Connect event message format used for supported Connect event payloads.",
        "envelope-level connect only": "Envelope-level Connect configures webhook notifications for a specific envelope, not account-wide or organization-wide event coverage.",
        "recipient connect only": "Recipient-focused event settings only track recipient activity; they do not replace broader envelope, account, or organization notifications.",
        "increase polling frequency": "Polling repeatedly asks the API for status; it is less efficient than using Connect events for near-real-time updates.",
        "poll enveloperecipients:list every second": "Polling EnvelopeRecipients:list every second creates unnecessary API traffic and still does not provide true webhook-driven updates.",
        "envelopeviews:createrecipient": "EnvelopeViews:createRecipient creates an embedded signing URL for an envelope recipient; it does not create Web Form instances or configure Connect.",
        "envelopes:create": "Envelopes:create creates an envelope; depending on the status it can save a draft or send it, but it is not the follow-up call for every embedded or workflow scenario.",
        "bulksend:createbulksendlist": "BulkSend:createBulkSendList prepares bulk sending recipients; it is not used for one-off embedded signing, Web Forms, or Connect configuration.",
        "bulk send": "Bulk Send is for sending similar envelopes to many recipients from a list; it does not solve single-recipient routing, identity, or webhook configuration.",
        "bulk send only": "Bulk Send handles high-volume envelope dispatch, but it does not replace Web Forms, workflow steps, or agreement data APIs.",
        "bulk send list id": "A bulk send list ID identifies a prepared recipient list for bulk sending; it is not a general envelope, workflow, or authentication setting.",
        "create a web form instance": "Creating a Web Form instance starts an intake form experience; it does not configure envelope webhooks or cancel/send envelopes.",
        "a web forms client sdk only": "The Web Forms client SDK renders a Web Form instance in a page; it does not create envelopes, retrieve agreements, or configure OAuth by itself.",
        "a web forms clientuserid": "Web Forms can use correlation values for tracking instances, while clientUserId is specifically an embedded-signing recipient value.",
        "web forms client sdk": "The Web Forms client SDK renders a Web Form instance URL inside a host page.",
        "use workflow builder only": "Workflow Builder orchestrates multi-step business processes, but using it alone does not replace specific API fields such as eventNotification.",
        "workflow start link only": "A workflow start link launches a workflow for a user, but it does not handle API-triggered starts or embedded signing URL creation by itself.",
        "workflow trigger requirements": "Workflow trigger requirements define how a workflow can start; they are not the same as envelope or Connect configuration.",
        "a workflow extension action": "A workflow extension action calls an external capability from a workflow; it does not replace core eSignature fields or OAuth configuration.",
        "get signatures step only": "Get Signatures sends documents for signature, but by itself it does not collect intake data, branch logic, or call external systems before signing.",
        "get signatures, then collect data": "Getting signatures before collecting data means the document is already in the signing flow before the intake data can shape or prefill it.",
        "get signatures before collecting data": "Getting signatures before collecting data reverses the intended workflow; the form data cannot be used to prepare or condition the document first.",
        "collect data with web forms, then get signatures": "Collect Data with Web Forms gathers structured intake information first, then Get Signatures can use that data in the signing step.",
        "archive first, then start": "Archiving is a post-completion records step; doing it first leaves no completed agreement to archive and skips the required intake/signing work.",
        "void envelope, then collect data": "Voiding cancels an envelope; it is not a way to begin an intake process or prepare documents for signature.",
        "file archive only": "A file archive extension stores or exports files after a process step; it does not collect data, verify identity, or start signing on its own.",
        "recipient authentication only": "Recipient authentication verifies a signer before access, but it does not collect structured form data or configure workflow sequencing.",
        "identity verification": "Identity Verification checks a signer identity; it does not replace form collection, envelope routing, or agreement retrieval.",
        "verify identity after archiving only": "Verifying identity after archiving is too late; identity checks must happen before the signer accesses or completes the signing process.",
        "brand destination url": "A brand destination URL redirects a signer after signing events; it does not collect data, authenticate APIs, or place tabs.",
        "brand destination urls": "Brand destination URLs control post-signing redirects; they do not configure OAuth, Connect, tabs, or workflow logic.",
        "brand resource file upload": "Brand resource file uploads support branding assets; they do not define recipient routing or destination behavior by themselves.",
        "template reference id only": "A template reference identifies reusable envelope content, but it does not configure a post-signing redirect or runtime workflow behavior.",
        "use a template reference model": "A template reference model reuses envelope structure; it does not replace direct configuration required for this scenario.",
        "a template name only": "A template name is a human-readable label; integrations normally need the correct production template ID or API configuration.",
        "template-only configuration": "Templates can standardize envelope content, but they do not replace OAuth, Connect, Web Forms, or workflow configuration when those are the requirement.",
        "demo-only template": "A demo-only template cannot be referenced by a production account; production needs its own template or migrated equivalent.",
        "reuse the demo template id": "Demo template IDs belong to the demo environment and cannot be used as production template references.",
        "request every docusign scope to avoid future changes": "Requesting every scope over-permissions the app and creates unnecessary consent/security risk.",
        "omit scopes because docusign infers them": "Docusign OAuth requests must include the scopes the app needs; the platform does not infer broad permissions safely.",
        "use account-level connect settings as scopes": "Connect settings control event delivery, while OAuth scopes control token permissions; they are different concepts.",
        "a production account id only": "A production account ID identifies the account, but it does not grant OAuth consent or configure redirect URIs/secrets.",
        "a connect listener url": "A Connect listener URL receives webhook events; it does not grant OAuth consent or create templates.",
        "a new envelope template id": "A template ID references reusable envelope content; it does not satisfy authentication, consent, or webhook requirements by itself.",
        "enable cors only": "CORS controls browser-origin access; it does not grant OAuth consent, select an OAuth flow, or configure production secrets.",
        "configure cors origins": "CORS origins allow browser requests from approved domains; they do not replace OAuth flow selection or embedded recipient setup.",
        "cors configuration": "CORS configuration is only relevant to browser-origin API calls; it does not solve server-side OAuth, workflow, or Connect requirements.",
        "/oauth/token": "/oauth/token issues access tokens; it does not return the user's account list and base URI context.",
        "/oauth/userinfo": "/oauth/userinfo returns account and base URI context for an authenticated user.",
        "/connect/events": "/connect/events relates to Connect event handling, not OAuth account discovery.",
        "/restapi/v2.1/accounts": "/restapi/v2.1/accounts is a REST API path under a known base URI; it is not the OAuth userinfo discovery endpoint.",
        "in the authorization header as a bearer token": "The Authorization: Bearer header is where REST API access tokens are sent.",
        "in an envelope email subject": "The envelope email subject is visible message content for recipients; it is not where API credentials belong.",
        "in a recipient tab label": "A tab label identifies or maps a signing field; it is not an authentication header.",
        "in the safe exam browser": "Safe Exam Browser is unrelated to Docusign API authentication.",
        "recipient tab labels only": "Recipient tab labels help identify signing fields; they do not determine OAuth, Connect, or workflow behavior.",
        "the user's browser zoom level": "Browser zoom changes display scale only; it does not control Docusign tab placement or API behavior.",
        "template color branding only": "Branding changes visual presentation; it does not solve placement, routing, or authentication requirements.",
        "envelope transactionid": "Envelope transactionId helps with idempotent envelope creation retries; it does not identify recipients or configure workflow steps.",
        "jwt consent url": "A JWT consent URL is used to grant consent for JWT; it is not a general-purpose runtime setting for every API scenario.",
        "manually by someone in your organization only": "Manual starts can be valid for human-driven workflows, but they do not satisfy an API-triggered automation requirement.",
        "from an envelope void event only": "A void event occurs when an envelope is canceled; it is not an appropriate trigger for starting a normal business workflow.",
        "from a bulk send batch only": "A bulk send batch starts high-volume sending, not a custom workflow instance from an application action.",
        "a template password": "A template password is not an OAuth or PKCE control and does not secure an authorization-code exchange.",
        "an hmac secret on each envelope": "HMAC is used to verify webhook payloads such as Connect messages; it is not part of PKCE or envelope creation logic.",
        "legacy xml only": "Legacy XML formats do not provide the modern JSON event or API behavior the scenario is asking for.",
        "csv export format": "CSV export is useful for tabular reporting, but it is not the structured API or event format required here.",
        "pdf attachment only": "A PDF attachment gives document content, but it does not provide structured metadata, event data, or workflow configuration by itself.",
        "agreement manager extraction": "Agreement Manager extraction is for agreement data and repository operations, not for every envelope or workflow configuration task.",
        "app center listing": "An App Center listing distributes an extension app; it does not implement the runtime API behavior on its own.",
        "jwt consent": "JWT consent authorizes a JWT integration, but it does not replace unrelated envelope, Connect, or workflow configuration.",
        "a replacement for oauth consent": "This feature does not replace OAuth consent; API access still needs the appropriate OAuth flow, scopes, and consent.",
        "unlimited esignature api calls": "Docusign APIs are subject to limits and responsible usage patterns; no feature grants unlimited calls.",
        "a mandatory pdf renderer": "A PDF renderer displays documents; it does not configure Docusign APIs, workflows, or authentication.",
        "recipient view urls": "Recipient view URLs launch embedded signing sessions; they are not durable status records or production configuration.",
        "retryid": "retryId or retry metadata helps identify webhook retries; it is not an idempotency value for creating an envelope.",
        "a connect listener with no api calls": "A Connect listener receives events, but it does not create signing URLs, retrieve agreement data, or perform OAuth token exchange by itself.",
        "a bulk send csv": "A bulk send CSV supplies recipient data for bulk sending; it does not configure one-off embedded or workflow logic.",
        "changing the envelope email subject": "Changing the email subject affects recipient messaging only; it does not alter API authentication, workflow order, or webhook delivery.",
        "using clientuserid on every signer": "clientUserId should be used for embedded recipients; adding it indiscriminately does not solve unrelated branding or routing requirements.",
        "adding a brand destination url": "A brand destination URL controls post-signing navigation, not authentication, tab placement, or data collection.",
        "the envelope must be voided first": "Voiding cancels an envelope, so doing it first prevents normal signing or downstream processing.",
        "the app must use implicit grant": "Implicit Grant is not the recommended modern pattern and does not satisfy server-side, JWT, or PKCE-specific requirements.",
        "the web form must be public": "Making a Web Form public changes access expectations; it does not provide correlation, embedding, or workflow sequencing by itself.",
        "public app center listing": "A public App Center listing is for distribution and discovery; it does not implement private account-only behavior or runtime API logic.",
        "private app for one account only": "A private app can be installed for limited use, but it does not provide public marketplace distribution.",
        "internal employee-only integration": "An internal-only integration is limited to one organization and does not address marketplace distribution or reusable customer installation.",
        "one-time manual sending workflow": "A one-time manual workflow may work for an individual envelope, but it does not provide reusable automation.",
        "wait for users to forward emails": "Relying on users to forward emails is manual and fragile; it does not provide API-driven tracking or automation.",
        "replace all templates with web forms": "Web Forms collect structured input, but they do not replace every template or signing workflow requirement.",
        "recipient-only connect in each template": "Recipient-only Connect in templates is too narrow when the requirement is broader envelope, account, or organization event coverage.",
        "remote signing email only": "Remote signing email sends recipients to a Docusign-hosted ceremony; it does not provide an embedded in-app experience.",
        "connect retry before web form": "Connect retries are delivery behavior for webhook failures; they do not collect form data or prepare a signing workflow.",
        "branching rule only": "A branching rule chooses a path based on conditions; by itself it does not perform the required data collection, signing, or integration step.",
        "set the envelope status to created": "Setting status to created saves a draft envelope instead of sending it or configuring a webhook.",
        "create an envelope with status voided": "Creating a voided envelope cancels the transaction rather than starting a valid signing process.",
        "use only brand destination urls": "Brand destination URLs control where users land after signing; they do not handle identity, data capture, or envelope setup.",
        "switch to jwt grant": "Switching to JWT Grant changes the authentication model; it does not fix production configuration, template, or workflow requirements unless the scenario is specifically unattended service auth.",
    }
    if text in exact:
        return exact[text]

    if has(text, "extension"):
        return f"{option} relates to Extension Apps, which package reusable capabilities for Docusign workflows or signing experiences."
    if has(text, "workflow"):
        return f"{option} relates to Workflow Builder orchestration, which coordinates steps but must still be placed in the right part of the process."
    if has(text, "connect", "webhook"):
        return f"{option} relates to Docusign Connect event delivery, which is for notifications after configured events occur."
    if has(text, "web form"):
        return f"{option} relates to Web Forms intake, which collects structured data before later agreement steps."
    if has(text, "template"):
        return f"{option} relates to reusable envelope templates, which standardize documents, recipients, tabs, and settings."
    if has(text, "brand"):
        return f"{option} relates to Docusign branding, which changes the recipient experience but does not replace API or workflow configuration."
    if has(text, "agreement"):
        return f"{option} relates to agreement data or agreement lifecycle management rather than the live envelope action in this scenario."
    if has(text, "oauth", "jwt", "grant", "scope", "consent"):
        return f"{option} relates to OAuth authentication or authorization rather than the non-authentication requirement in this scenario."
    if has(text, "bulk"):
        return f"{option} relates to bulk sending, which is for high-volume envelope creation from recipient lists."
    if has(text, "identity", "authentication"):
        return f"{option} relates to validating recipient access or identity before signing."
    return f"{option} is a different Docusign concept or configuration choice from the one required by this scenario."


def scenario_need(question: dict) -> str:
    correct = question["answerText"]
    explanation = clean(question.get("explanation", ""))
    if explanation:
        return f"The scenario needs {correct}: {explanation}"
    return f"The scenario needs {correct}."


def wrong_explanation(question: dict, option: dict) -> str:
    description = describe_option(option["text"])
    need = scenario_need(question)
    topic = question.get("topic", "")

    if has(option["text"], "get signatures, then collect data", "get signatures before collecting data", "get signatures before collect data"):
        return (
            f"{description} It fails here because the form data must be collected before signature so the workflow can use that data "
            "to populate, route, or condition the document before it is sent."
        )
    if has(option["text"], "archive first", "file archive"):
        return (
            f"{description} It fails here because archiving is normally a downstream records step after data collection and signing, "
            "not the step that prepares the agreement for signature."
        )
    if has(option["text"], "void"):
        return f"{description} It fails here because canceling the envelope would stop the business process instead of completing the requested action. {need}"
    if has(option["text"], "created") and has(topic, "envelope create", "envelope-level connect"):
        return f"{description} It fails here because the requirement is not to leave a draft; the integration needs the envelope action or notification configuration described in the scenario. {need}"
    if has(option["text"], "brand"):
        return f"{description} It fails here because the requirement is functional, not just a post-signing redirect or visual brand behavior. {need}"
    if has(option["text"], "connect", "poll", "webhook"):
        return f"{description} It fails here because the scenario requires {question['answerText']}, not a different event-delivery or status-checking pattern."
    if has(option["text"], "oauth", "jwt", "json web token", "authorization code", "implicit", "scope", "consent"):
        return f"{description} It fails here because the scenario's client type, user presence, and secret-storage constraints point to {question['answerText']}."
    if has(option["text"], "template"):
        return f"{description} It fails here because templates only supply reusable envelope structure; they do not satisfy the scenario's required runtime behavior. {need}"
    if has(option["text"], "web form"):
        return f"{description} It fails here because the scenario is not asking merely to create or render an intake form; it needs {question['answerText']}."
    if has(option["text"], "workflow"):
        return f"{description} It fails here because selecting a workflow concept alone does not perform the specific API, step order, or configuration required. {need}"
    if has(option["text"], "bulk"):
        return f"{description} It fails here because the requirement is not high-volume batch sending from a list. {need}"
    if has(option["text"], "recipient", "clientuserid", "returnurl"):
        return f"{description} It fails here because recipient/session fields only support a signing ceremony; they do not replace the required configuration. {need}"
    if has(option["text"], "agreement manager", "agreement"):
        return f"{description} It fails here because agreement repository/data operations happen after or outside the live envelope/workflow action being tested. {need}"
    return f"{description} It fails here because it would solve a different part of the Docusign platform than the requirement being tested. {need}"


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
        correct_ids = question.get("correctAnswers") or [question["correct"]]
        lines.append(f"**Answer:** {', '.join(correct_ids)}. {question['answerText']}")
        lines.append("")
        lines.append(f"**Explanation:** {question['explanation']}")
        lines.append("")
        lines.append("**Option notes:**")
        for option in question["options"]:
            lines.append(f"- {option['id']}. {question['optionExplanations'][option['id']]}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    replaced = 0
    for question in questions:
        for option in question["options"]:
            if option["id"] == question["correct"]:
                continue
            existing = question.get("optionExplanations", {}).get(option["id"], "")
            if GENERIC_RE.search(existing):
                question["optionExplanations"][option["id"]] = wrong_explanation(question, option)
                replaced += 1

    QUESTIONS.write_text(json.dumps(questions, indent=2), encoding="utf-8")
    MARKDOWN.write_text(to_markdown(questions), encoding="utf-8")
    print(f"Replaced {replaced} generic wrong-answer explanations")


if __name__ == "__main__":
    main()

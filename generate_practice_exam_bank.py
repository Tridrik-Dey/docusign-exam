from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import textwrap

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


OUT = Path("output")
OUT.mkdir(exist_ok=True)
MD_PATH = OUT / "docusign_iam_integration_extension_300_practice_questions.md"
PDF_PATH = OUT / "docusign_iam_integration_extension_300_practice_questions.pdf"


@dataclass(frozen=True)
class Seed:
    topic: str
    scenario: str
    stem: str
    answer: str
    distractors: tuple[str, str, str]
    explanation: str


DOMAIN_COUNTS = {
    "API Authentication": 39,
    "Go Live Process": 33,
    "Docusign Connect": 36,
    "eSignature API": 48,
    "eSignature Features and Web Forms": 33,
    "Agreement Manager API": 18,
    "Workflow Builder and Workflow API": 45,
    "App Center and Extension Apps": 48,
}


SEEDS: dict[str, list[Seed]] = {
    "API Authentication": [
        Seed("OAuth flow selection", "A server-side portal can store a client secret and each employee signs in interactively.", "Which OAuth flow best fits this integration?", "Confidential Authorization Code Grant", ("JSON Web Token Grant", "Public Authorization Code Grant with PKCE", "Implicit Grant"), "Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively."),
        Seed("OAuth flow selection", "A browser-only single-page application cannot protect a client secret but must authenticate each individual user.", "Which flow should the developer choose?", "Public Authorization Code Grant with PKCE", ("Confidential Authorization Code Grant", "JSON Web Token Grant", "Implicit Grant"), "Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps."),
        Seed("JWT Grant", "A scheduled service runs nightly using a dedicated system sender account and no person is present to sign in.", "Which authentication model is appropriate?", "JSON Web Token Grant", ("Public Authorization Code Grant", "Confidential Authorization Code Grant", "Implicit Grant"), "JWT Grant supports non-interactive service integrations after consent has been granted."),
        Seed("Consent", "A JWT integration fails because the user has never granted consent for the requested scopes.", "What must be obtained before token requests succeed?", "Individual or admin consent for the integration key and scopes", ("A production account ID only", "A Connect listener URL", "A new envelope template ID"), "JWT and other OAuth flows require consent for requested scopes before access tokens can be issued."),
        Seed("Scopes", "An app only needs to send envelopes and read user account information.", "What should the developer do when requesting OAuth consent?", "Request only the minimum scopes required for those operations", ("Request every Docusign scope to avoid future changes", "Omit scopes because Docusign infers them", "Use account-level Connect settings as scopes"), "Least-privilege scope selection reduces risk and avoids unnecessary consent prompts."),
        Seed("User info", "After receiving an access token, the app must determine which base URI and account ID to use for API calls.", "Which endpoint is used to retrieve that account context?", "/oauth/userinfo", ("/restapi/v2.1/accounts", "/oauth/token", "/connect/events"), "The userinfo response includes account identifiers and base URI information needed for subsequent API calls."),
        Seed("PKCE", "A native app cannot store a client secret securely.", "What protects the public authorization code exchange?", "A PKCE code verifier and code challenge", ("An HMAC secret on each envelope", "A Connect retry policy", "A template password"), "PKCE mitigates interception risk for public clients that cannot keep a client secret."),
        Seed("Bearer tokens", "A REST API request is returning unauthorized even though the token endpoint returned an access token.", "Where should the access token be supplied?", "In the Authorization header as a Bearer token", ("In the envelope email subject", "In the Connect eventNotification object", "In the templateId field"), "Docusign REST calls use Authorization: Bearer <access_token>."),
    ],
    "Go Live Process": [
        Seed("Go-live setup", "A developer promotes an integration key from demo to production.", "Which configuration commonly must be recreated in production?", "Redirect URIs and secret keys", ("Completed demo envelopes", "Envelope IDs", "Connect event logs"), "Security-sensitive settings such as secrets and redirect URIs are configured in the production environment."),
        Seed("Integration classification", "A partner app will be distributed for many customers to install.", "Which go-live classification best reflects the use case?", "ISV or partner-distributed integration", ("Internal employee-only integration", "One-time manual sending workflow", "Template-only configuration"), "Classification should match how the integration is used and distributed."),
        Seed("Production endpoints", "After go-live, API calls still point to demo endpoints.", "What must be changed?", "Use production base URIs and production API endpoints", ("Keep demo endpoints and change only the email subject", "Use a Connect listener as the base URI", "Replace all templates with web forms"), "Production integrations must call production endpoints and the correct account base URI."),
        Seed("Templates in production", "An app uses a template reference model in demo.", "What is required for production?", "Deploy or recreate the template in production and update the template ID", ("Reuse the demo template ID", "Switch to JWT Grant", "Enable CORS only"), "Template IDs differ between environments; the production template must be referenced."),
        Seed("Post go-live", "A promoted integration key uses Confidential Authorization Code Grant.", "What should be validated immediately after go-live?", "Production redirect URIs, secrets, base URI, and consent", ("Recipient tab labels only", "The user's browser zoom level", "Template color branding only"), "OAuth and endpoint settings often need production-specific validation."),
        Seed("API limits", "An integration repeatedly polls envelopes every few seconds for status.", "Which improvement best aligns with API usage guidelines?", "Use Connect webhooks for event-driven status updates", ("Increase polling frequency", "Create duplicate envelopes for retry", "Move all status into email subject lines"), "Webhooks reduce unnecessary polling and help avoid resource-limit issues."),
        Seed("Troubleshooting", "A production app fails after go-live with authentication errors, but worked in demo.", "What should be checked first?", "Production OAuth settings, redirect URI, consent, and account base URI", ("Whether demo envelopes are legally binding", "Whether recipients use the same browser", "Whether document tabs are locked"), "Common post-go-live issues are environment and OAuth configuration mismatches."),
    ],
    "Docusign Connect": [
        Seed("Envelope-level Connect", "A single high-value envelope needs a callback URL different from account-level settings.", "How should the webhook be configured?", "Include eventNotification in the envelope creation request", ("Create a Web Form instance", "Use Workflow Builder only", "Set the envelope status to created"), "The eventNotification object configures per-envelope Connect callbacks."),
        Seed("Connect vs polling", "A system must learn when recipients complete signing without excessive API calls.", "Which design is preferred?", "Subscribe to Connect events", ("Poll EnvelopeRecipients:list every second", "Wait for users to forward emails", "Use a template reference model"), "Connect pushes events and avoids high-volume polling."),
        Seed("Configuration level", "A company wants one webhook for events across all accounts in its Docusign organization.", "Which Connect level is most appropriate?", "Organization-level Connect", ("Envelope-level Connect only", "Recipient-only Connect in each template", "A Web Forms clientUserId"), "Organization-level Connect centralizes events across accounts in the organization."),
        Seed("JSON SIM", "A workflow event must be delivered to a custom listener.", "Which message format is required for workflow-related events?", "JSON SIM format", ("Legacy XML only", "CSV export format", "PDF attachment only"), "Workflow events rely on the JSON SIM event model."),
        Seed("Security", "A listener must verify that incoming webhook messages really came from Docusign.", "Which control helps validate message authenticity?", "HMAC validation or supported Connect authentication", ("Changing the envelope email subject", "Using clientUserId on every signer", "Adding a brand destination URL"), "HMAC and authentication settings help secure Connect listeners."),
        Seed("Retries", "A listener is temporarily unavailable when Docusign sends an event.", "What Connect behavior should the developer understand?", "Docusign retries failed deliveries according to retry rules", ("The envelope is automatically voided", "The integration key is revoked", "The recipient must sign again"), "Connect has retry behavior for delivery failures; listeners should be idempotent."),
        Seed("Troubleshooting", "A listener receives duplicate webhook messages.", "What design practice should the integration use?", "Idempotent processing based on event identifiers or envelope state", ("Treat every duplicate as a new envelope", "Disable OAuth scopes", "Use a different template ID"), "Webhook systems should tolerate retries and duplicate delivery."),
        Seed("Payload selection", "A team wants smaller event payloads and will query details separately.", "Which Connect design choice is relevant?", "Configure the event payload to include only needed data", ("Switch to implicit grant", "Use recipient authentication instead", "Create a bulk send list"), "Connect payload options should match data minimization and processing needs."),
    ],
    "eSignature API": [
        Seed("Envelope create", "An integration needs to send an envelope for signature immediately.", "Which envelope status should be used in the create request?", "sent", ("created", "voided", "deleted"), "Status sent sends the envelope; created saves it as a draft."),
        Seed("Draft envelope", "A developer wants to create an envelope but not send it yet.", "Which status is appropriate?", "created", ("sent", "voided", "completed"), "The created status keeps an envelope in draft state."),
        Seed("Cancel envelope", "A sent envelope has a fatal error and no one should sign it.", "Which status should be set?", "voided", ("deleted", "purged", "created"), "Voiding cancels an in-process envelope and stops signing."),
        Seed("Idempotency", "A network retry might submit the same create-envelope request twice.", "Which value helps avoid duplicate envelopes?", "transactionId", ("recipientId", "retryId", "brandId"), "Supplying a transactionId supports idempotent envelope creation."),
        Seed("Template reference", "A request uses a server template already stored in Docusign.", "Which value identifies the template?", "templateId", ("clientUserId", "returnUrl", "basePath"), "templateId references an existing template in an envelope request."),
        Seed("Composite templates", "A request must combine server templates, inline recipient data, and documents.", "Which model best supports that structure?", "Composite templates", ("Bulk send list only", "Brand destination URLs", "Connect 2.0 only"), "Composite templates allow combining server templates, inline templates, and documents."),
        Seed("Anchor tabs", "A document can vary in page length, but the signature should appear near a specific text string.", "Which tab placement method is best?", "Anchor tagging with anchorString and offsets", ("Fixed x/y coordinates only", "Branding resource files", "CORS origin settings"), "Anchor tabs place fields relative to document text."),
        Seed("Embedded signing", "A recipient must sign inside the host app rather than through an email link.", "Which recipient property marks embedded signing?", "clientUserId", ("emailNotification", "brandId", "listId"), "clientUserId identifies a captive/embedded recipient."),
        Seed("Signing URL", "An app has created an envelope for an embedded recipient.", "What must the app request before the recipient can sign in the host application?", "A recipient view URL from EnvelopeViews:createRecipient", ("A Connect JSON SIM event", "A bulk send batch ID", "A brand resource file"), "Embedded signing requires requesting a short-lived recipient view URL."),
        Seed("Embedded signing timing", "An app creates embedded signing URLs long before users are ready.", "What is the risk?", "The short-lived URL may expire before use", ("The template ID changes", "The account base URI disappears", "Connect retries stop"), "Embedded signing URLs are short-lived and should be generated when the user is ready."),
        Seed("Embedded sending", "A sender must prepare or edit an envelope from inside a custom app.", "Which endpoint family is relevant?", "EnvelopeViews:createSender", ("BulkSend:createBulkSendList", "Agreements:getAgreement", "Connect retry log"), "Embedded sending uses a sender view URL."),
        Seed("Bulk send", "A developer needs to send personalized copies of an envelope to many recipients.", "Which feature is designed for that scenario?", "Bulk Send", ("Recipient authentication only", "Brand destination URLs", "Organization Connect only"), "Bulk Send supports large batches of personalized envelopes."),
    ],
    "eSignature Features and Web Forms": [
        Seed("Web Forms embedding", "A custom website needs to render a Docusign Web Form instance inline.", "What client-side component is used with the instance URL?", "Docusign JS client SDK", ("EnvelopeViews:createRecipient", "Connect JSON SIM", "Workflow start link only"), "Docusign JS renders Web Form instances in the host page."),
        Seed("Web Form correlation", "An app creates one Web Form instance per customer record.", "Which value should be supplied to correlate back to the app?", "clientUserId", ("templateId", "brandId", "envelopeId before creation"), "clientUserId can map a form instance to an external record."),
        Seed("Identity verification", "An envelope must require recipients to prove identity before signing.", "What must be included in the recipient configuration?", "An identity verification or recipient authentication configuration", ("A Connect retry policy", "A workflow extension action", "A template name only"), "Recipient authentication or ID verification settings enforce identity checks."),
        Seed("Recipient authentication", "A signer should receive a one-time code before accessing the envelope.", "Which feature category applies?", "Recipient authentication", ("Bulk Send only", "Agreement Manager extraction", "App Center listing"), "Recipient authentication controls access to signing."),
        Seed("Brand destination URLs", "Remote signers should be redirected to a custom page after finishing.", "Which branding feature is relevant?", "Brand destination URLs", ("Envelope transactionId", "JWT consent URL", "Bulk send list ID"), "Brand destination URLs control post-signing redirect destinations for remote signing."),
        Seed("Connected Fields", "A signer-provided value must be checked against an external data source during signing.", "Which feature supports this?", "Connected Fields or data verification", ("Agreement import only", "Envelope purge", "Safe Exam Browser"), "Connected Fields and data verification support real-time validation scenarios."),
        Seed("ID Evidence", "A system must retrieve retained data about a completed ID Verification event.", "Which API is relevant?", "ID Evidence API", ("Web Forms API only", "BulkSend API", "WorkflowInstanceManagement only"), "The ID Evidence API retrieves retained evidence from ID verification events."),
    ],
    "Agreement Manager API": [
        Seed("Agreement data", "A custom app needs structured extracted data for a specific agreement.", "Which operation is most relevant?", "Agreements:getAgreement", ("Envelopes:create", "Workflow trigger requirements", "BulkSend:createBulkSendList"), "Agreements:getAgreement retrieves agreement data for a specific agreement."),
        Seed("Agreement list", "An app needs to find agreements matching criteria before retrieving details.", "Which API pattern is relevant?", "List or search agreements, then retrieve the target agreement", ("Create an envelope with status voided", "Use only brand destination URLs", "Configure CORS origins"), "Agreement Manager integrations commonly list/search then retrieve detailed agreement data."),
        Seed("Legacy import", "A company wants to bring existing contracts into Agreement Manager.", "Which capability matters?", "Agreement upload or bulk import using the Agreement Manager API", ("Recipient view URLs", "Implicit Grant", "Envelope-level Connect only"), "Agreement Manager supports bringing legacy agreement content and metadata into the repository."),
        Seed("Agreement documents", "A downstream system needs a copy of an agreement document.", "What should the integration plan include?", "Document download using Agreement Manager capabilities", ("A Web Forms client SDK only", "A Connect listener with no API calls", "A bulk send CSV"), "Agreement Manager API scenarios include retrieving agreement documents and metadata."),
    ],
    "Workflow Builder and Workflow API": [
        Seed("Workflow steps", "A workflow must collect form data before sending a document for signature.", "Which step order best fits?", "Collect Data with Web Forms, then Get Signatures", ("Get Signatures, then collect data", "Archive first, then start", "Void envelope, then collect data"), "Workflow step order should match the business process."),
        Seed("Identity step", "A process must gather participant data and then verify identity.", "Which sequence is best?", "Collect Data with Web Forms, then Verify Someone's Identity", ("Verify identity after archiving only", "Get Signatures before collecting data", "Connect retry before web form"), "Collect required data before the identity verification step if the scenario requires it."),
        Seed("Extension step", "After signing, the completed document must be stored in an external file service.", "Which workflow step type is appropriate?", "Extension step using a file/archive extension app", ("Branching rule only", "Get Signatures step only", "CORS configuration"), "Extension steps call external services through installed extension apps."),
        Seed("Branching", "A workflow should follow different paths based on a form response.", "Which workflow capability is used?", "Branching or conditional rules", ("JWT consent", "Envelope purge", "Brand destination URL"), "Branching rules route workflows based on conditions."),
        Seed("Start method", "A portal link should launch a workflow and pass values in the trigger URL.", "Which start method fits?", "From a Link", ("Manually by someone in your organization only", "From an envelope void event only", "From a bulk send batch only"), "A link start method can launch a workflow and pass URL values."),
        Seed("API trigger", "A backend service must programmatically trigger a workflow.", "Which start method/API pattern is relevant?", "From an API call with Workflow Builder API trigger requirements", ("Remote signing email only", "Brand resource file upload", "Template reference ID only"), "API-triggered workflows use trigger requirements and workflow API calls."),
        Seed("Runtime errors", "A workflow trigger fails because required starting variables are missing.", "What should the developer inspect?", "Workflow trigger requirements and variable mapping", ("Brand destination URLs", "Connect HMAC secret only", "Bulk send list status only"), "Workflow trigger requirements define required input variables."),
        Seed("Embedding workflow", "A custom app needs to display a workflow experience inside the app.", "Which capability should be considered?", "Embedding or launching the workflow according to its configured start method", ("Envelope purge", "JWT admin consent only", "Agreement type extraction only"), "Workflow integration depends on the configured start method and embedding/launch pattern."),
        Seed("Installed extensions", "A workflow should call a third-party service through an extension app.", "What must be true?", "The extension app must be installed and available for the workflow step", ("The envelope must be voided first", "The app must use implicit grant", "The Web Form must be public"), "Workflow Builder can use installed extension applications in extension steps."),
    ],
    "App Center and Extension Apps": [
        Seed("Extension app role", "A customer wants Docusign to call an external service during an agreement process.", "What does an extension app provide?", "A packaged way to connect external functionality into Docusign", ("A replacement for OAuth consent", "Unlimited eSignature API calls", "A mandatory PDF renderer"), "Extension apps extend Docusign with external service actions and data."),
        Seed("Public vs private", "An app is only for one organization's internal Docusign accounts.", "Which distribution is most appropriate?", "Private extension app", ("Public App Center listing", "Implicit Grant application", "Recipient Connect only"), "Private apps are limited to selected accounts or the publisher's organization."),
        Seed("Public App Center", "A partner wants customers broadly to discover and install an app.", "Which distribution goal applies?", "Public extension app published to the Docusign App Center", ("Private app for one account only", "Envelope-level Connect only", "Demo-only template"), "Public App Center distribution is for broad customer availability."),
        Seed("Manifest", "An extension app action must call an external API endpoint.", "Where is that endpoint represented?", "In an action definition in the extension app manifest", ("In an envelope email subject", "In a recipient tab label", "In the Safe Exam Browser"), "Actions in the manifest describe calls to external endpoints."),
        Seed("Connections", "An action must use external OAuth credentials.", "Which manifest object defines reusable auth details?", "connections", ("publisher only", "brandColors", "bulkCopies"), "The connections object defines authentication configuration used by actions."),
        Seed("connectionsReference", "An action needs to use a named connection from the manifest.", "What links the action to that authentication configuration?", "connectionsReference", ("recipientId", "transactionId", "brandId"), "connectionsReference ties an action to a connection definition."),
        Seed("API proxy", "The third-party API format does not match what the extension app action needs.", "What architecture component can transform requests and responses?", "API proxy", ("Brand destination URL", "Envelope void status", "Bulk send CSV"), "An API proxy can mediate between Docusign and the external service."),
        Seed("Firewall", "Docusign must call a customer-hosted endpoint for an extension action.", "What network consideration is important?", "Allow Docusign outbound requests through the endpoint firewall", ("Disable all OAuth scopes", "Use only demo endpoints", "Delete the app manifest"), "The external endpoint must be reachable by Docusign."),
        Seed("Data IO", "A workflow needs to read and write structured records in another system.", "Which extension type fits?", "Data IO extension app", ("File archive only", "Branding extension", "Implicit Grant"), "Data IO extensions read/write structured data."),
        Seed("File IO", "A workflow needs to archive completed documents to an external repository.", "Which extension type fits?", "File IO or file archive extension app", ("Connected Fields only", "Recipient authentication only", "CORS origin only"), "File IO extensions handle document storage and retrieval use cases."),
        Seed("Connected Fields", "An extension needs to validate field data while a sender adds fields or a signer signs.", "Which extension category applies?", "Connected Fields", ("File archive only", "Go-live classification", "Agreement list search"), "Connected Fields extensions integrate data validation into eSignature field/signing experiences."),
        Seed("Data Verification", "A signer enters a bank account value that must be validated at signing.", "Which extension pattern fits?", "Data Verification triggered during eSignature signing", ("Public Auth Code only", "Envelope purge", "Agreement Manager import"), "Data Verification checks signer-entered data during the signing experience."),
    ],
}


VARIANTS = [
    "A healthcare onboarding team",
    "A university financial-aid portal",
    "A banking compliance application",
    "A procurement workflow",
    "A legal operations integration",
    "A sales contract portal",
    "An HR onboarding workflow",
    "A partner-built customer app",
    "A public-sector records process",
    "A real-estate transaction workflow",
]


def rotate_options(correct: str, distractors: tuple[str, str, str], number: int) -> tuple[list[str], str]:
    options = [correct, *distractors]
    shift = number % 4
    rotated = options[shift:] + options[:shift]
    correct_letter = "ABCD"[rotated.index(correct)]
    return rotated, correct_letter


def build_questions() -> list[dict[str, str]]:
    questions = []
    number = 1
    for domain, count in DOMAIN_COUNTS.items():
        seeds = SEEDS[domain]
        for index in range(count):
            seed = seeds[index % len(seeds)]
            actor = VARIANTS[(index + len(domain)) % len(VARIANTS)]
            options, correct_letter = rotate_options(seed.answer, seed.distractors, number)
            stem = f"{actor} is working on this scenario: {seed.scenario} {seed.stem}"
            questions.append(
                {
                    "number": number,
                    "domain": domain,
                    "topic": seed.topic,
                    "stem": stem,
                    "options": options,
                    "answer": correct_letter,
                    "answer_text": seed.answer,
                    "explanation": seed.explanation,
                    "source": "Adapted from the supplied prep guide, uploaded QA style, and course knowledge-check content.",
                }
            )
            number += 1
    return questions


def write_markdown(questions: list[dict[str, str]]) -> None:
    lines = [
        "# Certified Docusign IAM Integration & Extension Developer - 300 Practice Questions",
        "",
        "Original practice bank aligned to the 2026 prep guide, the supplied QA/explanation document style, and the self-paced course knowledge-check material in `study_material.md`.",
        "",
        "Question distribution follows the exam guide weights:",
        "",
    ]
    for domain, count in DOMAIN_COUNTS.items():
        lines.append(f"- {domain}: {count} questions")
    lines.append("")
    lines.append("## Questions")
    lines.append("")

    current_domain = None
    for q in questions:
        if q["domain"] != current_domain:
            current_domain = q["domain"]
            lines.append(f"### {current_domain}")
            lines.append("")
        lines.append(f"**Q{q['number']}. ({q['topic']})** {q['stem']}")
        lines.append("")
        for letter, option in zip("ABCD", q["options"]):
            lines.append(f"{letter}. {option}")
        lines.append("")
        lines.append(f"**Answer:** {q['answer']}. {q['answer_text']}")
        lines.append("")
        lines.append(f"**Explanation:** {q['explanation']}")
        lines.append("")

    MD_PATH.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def para(text: str, style: ParagraphStyle) -> Paragraph:
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return Paragraph(escaped, style)


def write_pdf(questions: list[dict[str, str]]) -> None:
    styles = getSampleStyleSheet()
    title = ParagraphStyle("TitleCustom", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=22, spaceAfter=12)
    h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=colors.HexColor("#1f2937"), spaceBefore=10, spaceAfter=6)
    body = ParagraphStyle("BodyCustom", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.7, leading=11, spaceAfter=5)
    qstyle = ParagraphStyle("Question", parent=body, fontName="Helvetica-Bold", spaceBefore=7, spaceAfter=5)
    answer = ParagraphStyle("Answer", parent=body, fontName="Helvetica-Bold", textColor=colors.HexColor("#064e3b"), spaceBefore=4)

    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=letter,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
    )
    story = [
        para("Certified Docusign IAM Integration & Extension Developer - 300 Practice Questions", title),
        para("Aligned to the 2026 prep guide, supplied QA style, and course knowledge-check material.", body),
        Spacer(1, 8),
        para("Distribution", h2),
    ]
    for domain, count in DOMAIN_COUNTS.items():
        story.append(para(f"- {domain}: {count} questions", body))
    story.append(PageBreak())

    current_domain = None
    for q in questions:
        if q["domain"] != current_domain:
            current_domain = q["domain"]
            story.append(para(current_domain, h2))
        story.append(para(f"Q{q['number']}. ({q['topic']}) {q['stem']}", qstyle))
        for option_letter, option in zip("ABCD", q["options"]):
            story.append(para(f"{option_letter}. {option}", body))
        story.append(para(f"Answer: {q['answer']}. {q['answer_text']}", answer))
        story.append(para(f"Explanation: {q['explanation']}", body))
        story.append(Spacer(1, 4))

    def footer(canvas, document):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.grey)
        canvas.drawString(0.55 * inch, 0.35 * inch, "Docusign IAM Integration & Extension Developer practice bank")
        canvas.drawRightString(7.95 * inch, 0.35 * inch, f"Page {document.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def main() -> None:
    questions = build_questions()
    assert len(questions) == 300
    write_markdown(questions)
    write_pdf(questions)
    print(f"Wrote {MD_PATH}")
    print(f"Wrote {PDF_PATH}")


if __name__ == "__main__":
    main()

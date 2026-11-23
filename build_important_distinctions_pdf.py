from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUT = Path("output/pdf/important_distinctions.pdf")


def hex_color(value: str):
    return colors.HexColor(value)


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


# ---------------------------------------------------------------------------
# Content, sourced from study_material.md (the scraped Docusign for Developers
# / Build Extension Apps for the Docusign App Center course text) and cross
# checked against the practice-question explanations in
# output/docusign_iam_integration_extension_300_practice_questions_exam_style.md
# ---------------------------------------------------------------------------

OVERVIEW_ROWS = [
    (
        "File IO\n(File Input Output)",
        "Extension type",
        "Move documents/files into or out of Docusign.",
        "Archiving a completed agreement to an external repository (e.g. a cloud storage or DMS system) after signing.",
    ),
    (
        "Data IO\n(Data Input Output)",
        "Extension type",
        "Read or write structured data (records/fields), not whole documents.",
        "Pulling customer or contract data from an external system into a workflow, or pushing collected data back out to a line-of-business system.",
    ),
    (
        "Data Verification",
        "Capability / extension type",
        "Check signer-provided information against a trusted or internal data source in real time.",
        "Confirming a signer's bank account, SSN, license number, or membership ID is valid before the agreement can be completed.",
    ),
    (
        "Connected Fields",
        "Extension type / API",
        "Wire an external service's data model into Docusign eSignature fields so those fields can be added to agreements, populated, and validated.",
        "An extension app exposes a \"policy number\" field with a data model; Connected Fields lets that field appear on the agreement and be checked against the provider during preparation or signing.",
    ),
]


DETAILS = [
    (
        "File IO (File Input Output)",
        [
            "One of the four extension types you choose when registering an extension app in the Docusign Developer Console "
            "(the others are Data IO, Data Verification, and Connected Fields).",
            "Works at the document/file level: it handles storage and retrieval of files, not individual field values.",
            "Typical use case: a workflow step that archives a completed envelope's documents to an external repository "
            "(cloud storage, a content management system, a shared drive, etc.).",
            "Exam clue: the scenario talks about archiving, storing, or retrieving whole documents/files.",
        ],
    ),
    (
        "Data IO (Data Input Output)",
        [
            "Also one of the four extension types available when registering an extension app.",
            "Works at the structured-data level: it reads and writes records/fields to and from another system, rather than moving files.",
            "Typical use case: syncing structured record data between Docusign and an external line-of-business system as part of a workflow step.",
            "Exam clue: the scenario talks about reading/writing structured data or records, with no mention of verifying the data or handling files.",
        ],
    ),
    (
        "Data Verification",
        [
            "A Docusign capability that verifies signer-provided information in real time against trusted databases, reducing the need to correct bad data later.",
            "Comes in three tiers: Basic and Premium data verification use sources already integrated with Docusign; "
            "Custom data verification checks data against your own internal systems or another authoritative source you choose.",
            "Also listed as one of the four extension types when registering an extension app, since a provider can build an "
            "extension that performs this verification.",
            "Exam clue: the scenario is about validating signer-entered data (bank account, SSN, ID number, eligibility) in real time during signing.",
        ],
    ),
    (
        "Connected Fields",
        [
            "The Connected Fields API is what your integration uses to get information on the connected fields that an agreement uses — "
            "it exposes the data model for each extension app that supports data verification or connected fields.",
            "Your integration uses that data model to add the corresponding fields to an agreement and present them for signature.",
            "In other words, Connected Fields is the plumbing that carries a provider's data model (often a Data Verification provider's) "
            "into Docusign as fields you can place on a document — Data Verification is the check being performed; Connected Fields is how "
            "the field and its data get connected to the agreement.",
            "Also one of the four extension types when registering an extension app.",
            "Exam clue: the scenario is about integrating an external data model as signable/preparable fields on the agreement, or getting "
            "information about which fields an agreement uses.",
        ],
    ),
]


EXAMPLES = [
    (
        "File IO (File Input Output)",
        [
            "A real-estate brokerage's extension app copies every completed lease PDF into the brokerage's document management "
            "system (e.g. SharePoint or a DMS) once the envelope reaches completed status.",
            "A healthcare provider's extension pulls a patient intake form template file from an external content library and "
            "attaches it to the envelope before it is sent.",
            "A bank's extension archives signed loan packages to a compliance cold-storage bucket for long-term retention.",
            "A university's extension retrieves a supporting transcript file from the registrar's file store and adds it as an "
            "attachment on a financial-aid agreement.",
        ],
    ),
    (
        "Data IO (Data Input Output)",
        [
            "A CRM extension pushes a completed contract's key terms (deal value, renewal date, customer ID) back into "
            "Salesforce as structured record fields once the envelope completes.",
            "An HR extension pulls an employee's structured record (name, department, start date) from Workday to pre-populate "
            "a new-hire packet workflow.",
            "A procurement extension writes structured line-item data from an approved purchase agreement into an ERP system's "
            "purchase-order table.",
            "A logistics extension reads shipment and inventory records from a warehouse management system to populate a "
            "workflow's starting variables.",
        ],
    ),
    (
        "Data Verification",
        [
            "During signing, a lending agreement checks the signer-entered bank routing and account number against a "
            "Premium data verification source before allowing the signer to continue.",
            "A government benefits form validates a signer-entered national ID number against an internal eligibility database "
            "using Custom data verification.",
            "An insurance application verifies a signer-entered policy or member ID against the insurer's own system before the "
            "field is accepted as final.",
            "An HR onboarding agreement validates a signer-entered Social Security number format and existence using Basic "
            "data verification.",
        ],
    ),
    (
        "Connected Fields",
        [
            "A payroll provider's extension exposes an employee's salary and benefits-election data model as fields that can be "
            "dropped directly onto an offer-letter agreement and presented for signature.",
            "A title company's extension surfaces a property's parcel number, address, and lien data model as connected fields on "
            "a closing agreement, so the sender can add them without retyping.",
            "An insurance partner's extension exposes a policy data model (policy number, coverage limits, premium) as fields "
            "that populate and can be checked live on a renewal agreement.",
            "A background-check vendor's extension exposes candidate verification fields (status, completion date) that a "
            "recruiter can add to an employment agreement for the signer to see and confirm.",
        ],
    ),
]


KEY_DISTINCTIONS = [
    (
        "File IO vs. Data IO",
        "Both move information between Docusign and an external system, but at different granularity. File IO moves whole "
        "documents/files (e.g. archiving a signed PDF). Data IO moves structured records/fields, with no file handling implied. "
        "If the question says \"archive the completed document,\" think File IO. If it says \"read/write structured data,\" think Data IO.",
    ),
    (
        "Data Verification vs. Connected Fields",
        "Data Verification is the *what*: confirming a signer-entered value is correct or real, in real time, using Basic, Premium, "
        "or Custom sources. Connected Fields is the *how*: the API/extension mechanism that exposes an external provider's data model "
        "so those fields can be added to an agreement and presented for signature. A Connected Fields extension is frequently what "
        "delivers a Data Verification capability into the signing experience, but Connected Fields itself is about the field/data model "
        "plumbing, not the verification logic.",
    ),
    (
        "Connected Fields vs. Data IO",
        "Both deal with structured data rather than files, which makes them easy to confuse. Data IO is a general-purpose structured "
        "data exchange with an external system as part of a workflow step. Connected Fields is specifically about surfacing an external "
        "data model as eSignature fields on an agreement (so the field can be placed on the document and validated during preparation "
        "or signing) — it is tied to the signing/agreement field experience, not a generic workflow data sync.",
    ),
    (
        "File IO vs. Connected Fields / Data Verification",
        "File IO never touches individual field values — it only moves documents. Connected Fields and Data Verification never move "
        "whole documents — they work with individual signer-entered or agreement field values. If the scenario mentions a whole "
        "document/file being stored or fetched, it is File IO; if it mentions a specific value being checked or presented as a field, "
        "it is Data Verification or Connected Fields.",
    ),
    (
        "All four as extension types",
        "When registering an extension app in the Docusign Developer Console, you choose at least one extension type from exactly "
        "these four: File IO, Data IO, Data Verification, and Connected Fields. They are not tiers of one feature — each represents a "
        "distinct kind of integration an extension app can provide.",
    ),
    (
        "externalReferenceId vs. clientUserId",
        "externalReferenceId is a Web Forms API value: it is your app's tracking value passed to Instances:createInstance so a "
        "form instance can be mapped/correlated back to an internal record (e.g. a user or application ID) in your own database. "
        "clientUserId is an eSignature envelope recipient value: it marks that recipient as an embedded/captive signer instead of "
        "a remote email signer. They belong to different API surfaces (Web Forms vs. eSignature recipients) and are not "
        "interchangeable. Exam shortcut: \"map/correlate/track a Web Form instance back to your own record\" -> "
        "externalReferenceId. \"Mark a recipient as embedded/in-app signer\" -> clientUserId.",
    ),
    (
        "JSON SIM vs. XML SIM vs. XML Aggregated (Maestro/workflow events)",
        "The exact required option for Maestro workflow lifecycle events (like workflow-completed) is \"JSON SIM event "
        "message format.\" The real combinations are only three, not a full format-by-mode grid: JSON SIM (per-event, "
        "modern, recommended, supported at all three Connect levels), XML SIM (legacy, per-event, same object model as the "
        "eSignature SOAP API), and XML Aggregated (legacy, combines related events like recipient-complete + "
        "envelope-complete into one message). \"JSON Aggregated format\" is NOT a real option — per the source material, "
        "aggregation is explicitly tied to the XML data type only, with no JSON+Aggregate combination documented. "
        "Organization-level Connect configurations use the JSON SIM model exclusively; the legacy XML formats (SIM or "
        "Aggregated) are only available for account-level and envelope-level configurations. "
        "Exam shortcut: Maestro/workflow events, or \"track more granular/newer event types\" -> JSON SIM. Legacy "
        "XML/SOAP-style integration, or \"payload must never change\" -> XML SIM or XML Aggregated (account/envelope-level "
        "only, not available for org-level or Maestro events). \"JSON Aggregated\" appearing as an option -> distractor, "
        "not a real format.",
    ),
    (
        "Focused View vs. Classic View (embedded signing with Docusign JS)",
        "Docusign JS is the JavaScript client SDK Docusign provides to embed a Web Form or signing session directly inline "
        "in your web page's HTML, loaded via a script tag pointing to https://js-d.docusign.com/bundle.js (developer) or "
        "https://js.docusign.com/bundle.js (production). Focused View: pass the signing URL into the Docusign JS library "
        "script; renders a minimal wrapper around just the agreement plus a navigation button, directly embedded in an HTML "
        "element on your page via the loadDocuSign function. Benefits: modals open over the entire page instead of being "
        "trapped inside an iframe, and easier event handling to trigger next steps after the UI loads or signing completes. "
        "Recommended for most basic embedded-signing use cases. Classic View: redirect the user to the signing URL, or "
        "embed the signing URL inside an iframe on your website. Required instead of Focused View when the integration "
        "needs AI-Assisted Review, payment tabs, ID verification, or certain standards-based signature (SBS) pen "
        "providers — Focused View does not support these yet (the identityVerification parameter cannot be used with "
        "Focused View at this time). Exam shortcut: \"embed inline with modals/events, minimal wrapper, basic signing\" -> "
        "Focused View. \"Needs AI-Assisted Review, payment tabs, ID verification, or SBS pen providers\" -> Classic View "
        "(redirect or iframe).",
    ),
    (
        "What \"directly inline\" means: redirect vs. iframe vs. Docusign JS",
        "\"Directly inline\" means the Docusign content (signing experience or Web Form) is rendered as part of your own "
        "page's HTML, sharing the same page context as the rest of your site, rather than being sent elsewhere or boxed "
        "off in a separate embedded frame. There are three levels: (1) Redirect - not inline at all; the browser navigates "
        "away entirely to a Docusign-hosted page, then returns via returnUrl when finished. (2) Iframe / Classic View - "
        "partially inline; the signing URL is embedded inside an <iframe> element, so it visually sits on your page but is "
        "technically a separate document/browser context - your page's JavaScript cannot freely reach into it, styling "
        "does not automatically match, and modals popping up inside it get clipped to the iframe's boundaries instead of "
        "covering the whole page. (3) Docusign JS / Focused View - truly inline; the library renders the signing UI "
        "directly as elements within an HTML element you specify on your own page via loadDocuSign, with no iframe "
        "boundary, so modals can cover the entire page and your JavaScript can directly listen for events like signing "
        "complete. Analogy: redirect = leaving the building; iframe = a TV playing inside your room showing a different "
        "room; truly inline = the other room's furniture is now just part of your room.",
    ),
]


ID_PARAM_SHORTCUT_ROWS = [
    ("clientUserId", "\"Signal a recipient will sign inside your app (embedded/captive), not remote email\" -> clientUserId, set on the recipient at envelope creation. One-liner: \"this signer is embedded.\""),
    ("returnUrl", "\"Where should the browser go after the embedded signing session ends\" -> returnUrl, set later in the EnvelopeViews:createRecipient request. One-liner: \"where to send them back after.\""),
    ("recipientId", "\"Identify which recipient record inside the envelope\" (no embedded/remote distinction implied) -> recipientId. One-liner: \"which recipient is this.\""),
    ("accountId", "\"Which Docusign account should the API call run against\" -> accountId, retrieved from /oauth/userinfo. One-liner: \"which Docusign account.\""),
    ("externalReferenceId", "\"Map/correlate a Web Form instance (or similar) back to your own internal record\" -> externalReferenceId, passed to Instances:createInstance. One-liner: \"which of MY records does this belong to.\""),
]


WORKFLOW_START_METHOD_ROWS = [
    ("From within Workflow Builder", "Manual", "Someone manually starts the workflow directly in Workflow Builder (click the three dots -> Run Workflow). Anyone with Workflows: Prepare permission can see all published workflows and start them this way - similar to using a template where you populate recipient info and trigger the process.", "Workflows initiated by someone in your organization, e.g. a rental application process"),
    ("From a Link", "Manual", "Someone opens a URL and that action starts the workflow. You copy the workflow's link and embed it in a website or an automated email reply.", "Self-service, participant-initiated workflows - account change requests, client intake forms"),
    ("From an Event", "Automatic", "The workflow starts automatically in response to a triggering event (e.g. an envelope or account event) rather than a person taking a direct action.", "Event-driven automation where a workflow should kick off as a side effect of something else happening"),
    ("From an API call", "Automatic", "An external application programmatically starts the workflow by making a direct API call, using the workflow's trigger requirements and starting variables.", "Custom/API-driven integrations - the developer's own code decides when to start the workflow"),
]


OAUTH_SEQUENCE_ROWS = [
    (
        "1. Authorization request",
        "Redirect the user's browser to the Docusign authorization URI with client_id, redirect_uri, scope, and "
        "response_type=code. The user logs in and grants consent; Docusign redirects back to redirect_uri with an "
        "authorization code.",
    ),
    (
        "2. Token request (/oauth/token)",
        "The server-side app exchanges the authorization code for an access token (and refresh token) via a POST request, "
        "including client_id, client_secret, and grant_type=authorization_code.",
    ),
    (
        "3. User info request (/oauth/userinfo)",
        "Call this endpoint with the access token to retrieve the accountId and baseUri/basePath needed for subsequent "
        "Docusign API calls.",
    ),
]


EVENT_NOTIFICATION_POINTS = [
    "eventNotification is the object you attach to an envelope (in an Envelopes:create request) to configure an "
    "envelope-level Docusign Connect webhook - Docusign's push-notification/webhook mechanism.",
    "It must be set through the API - you cannot create an envelope-level webhook using the eSignature Send page.",
    "It is scoped to one specific envelope: Docusign sends real-time event messages (envelope/recipient status changes) "
    "for just that envelope to your listening application.",
    "It can only be configured at the time the envelope is created/sent, so it is not available for envelopes your "
    "account receives from external senders.",
    "Why use Connect at all: instead of polling the REST API (rate-limited to one GET per envelope every 15 minutes), "
    "Connect pushes a message to your listener the moment a subscribed event happens - no wasted API calls.",
    "Recommended message format: JSON SIM, supported across all three Connect levels (organization, account, and "
    "envelope).",
]


CONNECT_LEVELS_ROWS = [
    ("Organization-level Connect", "All/selected accounts in your Docusign organization", "Docusign Organization Admin page or API"),
    ("Account-level Connect", "All/selected users in your Docusign account", "Docusign eSignature Admin page or API"),
    ("Envelope-level Connect", "One specific envelope", "API only, via the eventNotification object on Envelopes:create"),
]


CONNECT_SECURITY_ROWS = [
    ("HMAC", "Adds signature headers (X-DocuSign-Signature-1, -2, etc.) computed from a shared secret (\"Connect Key\") known only to Docusign and your app. Verifies authenticity (really from Docusign) and integrity (message not altered in transit).", "All three levels - org, account, envelope. For envelope-level, the Connect feature must be enabled on the account first."),
    ("Basic Authentication", "A username/password configured on the Connect config, matching your listener's config. Encrypted in transit via HTTPS/TLS.", "Only Account-level and Envelope/Recipient-level. NOT available for Organization-level, and cannot be combined with OAuth for Connect."),
    ("Mutual TLS (mTLS)", "Two-way certificate-based authentication - both Docusign and your listener prove their identity to each other. Enabled via signMessageWithX509Certificate (API) / signMessageWithX509Cert (eventNotification) or the Admin UI toggle.", "Available across levels; can be combined with OAuth for Connect for stronger protection."),
    ("OAuth for Connect", "Uses the Client Credentials Grant (server-to-server) so your app verifies incoming Connect messages the same way your own OAuth setup already trusts.", "Available at account-level and envelope-level (confirmed by Docusign docs). Especially important at Organization-level since Basic Auth isn't available there, but it is NOT org-level-exclusive - usable and recommended at account-level too."),
    ("HTTPS/port 443 + POST-only listener", "Baseline requirement: your webhook listener must be public-internet-reachable, HTTPS-only, standard port 443, and only accept POST requests.", "All levels."),
]


CONNECT_SECURITY_COMBO_ROWS = [
    ("HMAC and OAuth for Connect", "Valid - Docusign's stated best practice for production", "Default for production apps. HMAC verifies message authenticity/integrity; OAuth for Connect adds server-to-server authentication using your existing OAuth trust setup. Covers both \"is this message genuine\" and \"is this caller authorized.\""),
    ("Basic authentication and OAuth for Connect", "NOT SUPPORTED - Docusign explicitly disallows this combination", "Never. If a question asks which two can't be combined, this is the pair."),
    ("Basic authentication and mutual TLS", "Valid - independent mechanisms", "Use when you want a simple credential check (username/password) plus a stronger transport-layer, certificate-based mutual identity check. Good middle ground when full OAuth infrastructure isn't in place yet."),
    ("HMAC and basic authentication", "Valid - explicitly recommended pairing", "Docusign specifically recommends this pairing: Basic Authentication is easy to set up, and HMAC adds message integrity/authenticity - a good lightweight option when OAuth infrastructure isn't available."),
]


CONNECT_SECURITY_DECISION_ROWS = [
    ("Production app, want Docusign's recommended baseline security", "HMAC + OAuth for Connect - the stated best practice."),
    ("You already have OAuth infrastructure / server-to-server auth set up", "HMAC + OAuth for Connect - leverage what you already have; OAuth authenticates the caller, HMAC authenticates the message content."),
    ("Simple setup, no OAuth infrastructure yet, still want message-integrity protection", "HMAC + Basic Authentication - Docusign's own recommended lightweight pairing."),
    ("Need strong network/transport-layer identity verification but can't do full OAuth yet", "Basic Authentication + Mutual TLS - mTLS proves both sides' identity via certificates; Basic Auth adds a simple credential check on top."),
    ("High-security environment, certificate infrastructure already in place, want it layered with modern auth", "OAuth for Connect + Mutual TLS - complementary because they operate at different network layers (application-layer token trust vs. transport-layer certificate trust)."),
    ("Tempted to use Basic Auth with OAuth \"for extra safety\"", "Don't - this combination is explicitly unsupported. Pick one as your primary auth method, then layer HMAC and/or mTLS on top instead."),
]


OAUTH_FLOW_COMPARISON_ROWS = [
    (
        "1. Authorization redirect",
        "client_id, redirect_uri, scope, response_type=code",
        "Same, plus code_challenge + code_challenge_method=S256",
        "client_id, redirect_uri, scope, response_type=code (no challenge)",
        "N/A - no browser redirect",
    ),
    (
        "2. User login & consent",
        "Yes, interactive",
        "Yes, interactive",
        "Yes, interactive",
        "One-time only (consent granted in advance)",
    ),
    (
        "3. Authorization code returned",
        "Yes, to redirect_uri",
        "Yes, to redirect_uri",
        "Yes, to redirect_uri",
        "N/A",
    ),
    (
        "4. Build & sign JWT assertion",
        "N/A",
        "N/A",
        "N/A",
        "Yes - iss, sub, aud, iat, exp, scope; signed with RSA private key",
    ),
    (
        "5. Token exchange (/oauth/token)",
        "code + client_id + client_secret + grant_type=authorization_code",
        "code + client_id + code_verifier (no secret) + grant_type=authorization_code",
        "code + client_id only (no secret, no verifier)",
        "Signed JWT assertion + JWT bearer grant_type",
    ),
    (
        "6. What protects the exchange",
        "client_secret",
        "code_verifier",
        "Nothing - vulnerable to code interception",
        "RSA signature on the JWT",
    ),
    (
        "7. Tokens returned",
        "Access token + refresh token",
        "Access token + refresh token",
        "Access token + refresh token",
        "Access token only (no refresh token needed)",
    ),
    (
        "8. /oauth/userinfo call",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
    ),
    (
        "9. API calls",
        "Authorization: Bearer access_token",
        "Same",
        "Same",
        "Same",
    ),
    (
        "Who uses it",
        "Server-side apps that can protect a secret",
        "SPAs, native/mobile apps - can't store a secret",
        "Not recommended - insecure for public clients, superseded by PKCE",
        "Background/scheduled services, no user present at runtime",
    ),
]


SOURCES = [
    "study_material.md — Docusign for Developers Overview / Build Extension Apps for the Docusign App Center course text "
    "(Connected Fields API description; \"Extension: Choose at least one type of extension (File Input Output, Data Input Output, "
    "Data Verification, or Connected Fields)\").",
    "output/docusign_iam_integration_extension_300_practice_questions_exam_style.md — practice-question explanations confirming "
    "File IO = document storage/retrieval, Data IO = read/write structured data, Connected Fields = data validation integrated into "
    "eSignature field/signing experiences.",
    "study_material.md — Build Extension Apps for the Docusign App Center, \"Register your App: Edit a Manifest File\" lesson "
    "(connections, extensions, and actions object field definitions).",
    "study_material.md — OAuth Confidential Authorization Code Grant required query string parameters and embedded-signing "
    "walkthrough (client_id, redirect_uri, scope, response_type; /oauth/token; /oauth/userinfo).",
    "study_material.md — Docusign Connect overview and \"Custom Connect Configuration Levels and Options\" lesson "
    "(organization/account/envelope-level Connect; eventNotification property on Envelopes:create).",
    "Web Forms API / eSignature recipient concepts: externalReferenceId as the Instances:createInstance correlation value "
    "vs. clientUserId as the eSignature embedded/captive signing recipient flag.",
    "study_material.md — Embedded Signing Overview, \"Embed the Signing URL with Focused View and Docusign JS\" lesson "
    "(Docusign JS bundle.js, loadDocuSign, Focused View vs. Classic View, style/displayFormat config).",
    "study_material.md — Workflow Components / Start Methods lesson (Manually Triggered tab: From within Workflow "
    "Builder, From a Link) plus practice-question context for From an Event / From an API call.",
    "developers.docusign.com/platform/webhooks/connect/validation-and-security/, /connect/hmac/, "
    "/connect/validation-and-security/oauth-connect/, and developers.docusign.com/platform/webhooks/mutual-tls/ "
    "(Docusign Connect security mechanisms: HMAC, Basic Authentication, mutual TLS, OAuth for Connect).",
    "Docusign developer blog: \"From the Trenches: Updates to mTLS with OAuth for Docusign Connect\" and \"Docusign "
    "Connect Now Includes Basic Authentication Support\" (valid/invalid security-mechanism combinations: Basic "
    "Authentication + OAuth for Connect is unsupported; all other pairings among HMAC, Basic Auth, OAuth, and mTLS "
    "are supported).",
    "study_material.md — \"Integrate More Features with Additional Agreement APIs\" lesson, Web Forms API section "
    "(Web Forms builder creates configurations; Web Forms API creates/integrates instances; Financial Aid Application "
    "use case).",
    "transactionId vs. envelopeId idempotency concept: transactionId supplied by the client before envelope creation to "
    "make retries safe; envelopeId assigned by Docusign only after the envelope exists.",
]


PRACTICE_QUESTIONS = [
    {
        "prompt": "A developer is configuring the connections object for OAuth 2.0 in their extension app manifest. Which four "
        "essential parameters must they obtain from the external API service or identity provider to configure the authorization "
        "flow successfully?",
        "options": [
            ("A", "Client ID, Client Secret, Token URL, and Authorization URL", True),
            ("B", "Publisher name, App name, Short description, and Long description", False),
            ("C", "Integration Key, API Account ID, Redirect URI, and Docusign scopes", False),
            ("D", "Client ID, Public key, JWT, and Authorization URL", False),
        ],
        "answer": "A. Client ID, Client Secret, Token URL, and Authorization URL",
        "explanation": "These map directly to the connections object's params: clientId and clientSecret are the external "
        "platform's OAuth credentials, and customConfig.tokenUrl / authorizationUrl are the provider's OAuth endpoints for "
        "token exchange and authorization.",
        "option_notes": [
            ("A", "Correct. clientId and clientSecret come from the external provider; tokenUrl and authorizationUrl are set "
             "in params.customConfig to point at that provider's OAuth endpoints."),
            ("B", "These are APP DETAILS fields describing the app's App Center listing, not connections/OAuth configuration."),
            ("C", "These are the app's own Docusign OAuth credentials (used when the app authenticates to Docusign), not what "
             "is configured in the manifest's connections object for the external service."),
            ("D", "Mixes in JWT/public key concepts used for JWT Grant authentication to Docusign itself; not part of the "
             "documented connections object fields (clientId, clientSecret, provider, scopes, customConfig)."),
        ],
    },
    {
        "prompt": "A developer wants to integrate a custom validation model that checks if a customer's internal loyalty number "
        "exists in the company's database before permitting signing. Which extension type should they use for this custom check "
        "during the eSignature process?",
        "options": [
            ("A", "Data Verification", True),
            ("B", "File IO", False),
            ("C", "Data IO", False),
            ("D", "Connected Fields", False),
        ],
        "answer": "A. Data Verification",
        "explanation": "Checking a signer-entered value (the loyalty number) against the company's own internal database in "
        "real time, before the signer can continue, is the definition of Data Verification — specifically Custom Data "
        "Verification, since the source is the company's own internal system rather than a Docusign-integrated trusted source.",
        "option_notes": [
            ("A", "Correct. Real-time validation of a signer-entered value against an internal database before signing is "
             "Data Verification (Custom tier)."),
            ("B", "File IO moves whole documents/files; there is no file being archived or retrieved here."),
            ("C", "Data IO reads/writes structured data with an external system but has no built-in pass/fail validation step "
             "against a database before signing."),
            ("D", "Connected Fields is the mechanism that exposes an external data model as fields on the agreement; it can "
             "carry a Data Verification check into the signing UI, but the actual verification logic described here is "
             "Data Verification's job."),
        ],
        "shortcut": "Signer-entered value + \"check against a database in real time before signing\" → Data Verification. "
        "If the question instead emphasized exposing the field itself or adding the field to the agreement from an external "
        "data model, that would point to Connected Fields.",
    },
    {
        "prompt": "A developer needs to create 100 unique web form instances for participants in an internal compliance process "
        "using the Web Forms API. They also need to ensure that the internal system can uniquely map and track the status of "
        "each form instance back to the individual user record in the backend database. Which parameter must be supplied in "
        "the Instances:createInstance request?",
        "options": [
            ("A", "The web form configuration ID, which allows one-to-one mapping for tracking purposes", False),
            ("B", "The API Account ID, which distinguishes instances created under different developer sandboxes", False),
            ("C", "A unique clientUserId value generated by the developer's internal systems", True),
            ("D", "The participant's email address, which serves as the unique key for all Docusign objects", False),
        ],
        "answer": "C. A unique clientUserId value generated by the developer's internal systems",
        "explanation": "By elimination: the web form configuration ID identifies the form template/definition, shared by all "
        "100 instances, so it cannot provide one-to-one mapping. The API Account ID identifies the Docusign account, the same "
        "for every instance. The participant's email is not a unique key for all Docusign objects. Only option C describes a "
        "unique, developer-generated value supplied per instance to correlate it back to an internal record.",
        "option_notes": [
            ("A", "The web form configuration ID identifies the form template itself. All 100 instances of the same "
             "compliance form share the same configuration ID, so it cannot uniquely track one participant."),
            ("B", "The API Account ID identifies the Docusign account the request runs under — the same for every instance, "
             "not a per-instance tracking value."),
            ("C", "Correct by elimination. Describes a unique, app-generated tracking value supplied per instance so it can "
             "be correlated back to the right backend user record."),
            ("D", "Email is not a unique/universal key across all Docusign objects — people can share or change emails, and "
             "many Docusign objects have nothing to do with an email address."),
        ],
        "flag": "Terminology flag: the standard Docusign term for this Web Forms correlation value is externalReferenceId, "
        "not clientUserId. clientUserId is actually an eSignature envelope recipient field that marks a signer as "
        "embedded/captive, unrelated to Web Forms instance tracking. This question's option C mislabels the field, but "
        "functionally describes exactly what externalReferenceId does. None of the four options offer externalReferenceId as "
        "a correctly-labeled choice, so C is correct here only by elimination and by matching this same mislabeled "
        "convention seen elsewhere in this practice bank. If externalReferenceId ever appears as its own option, prefer it.",
    },
    {
        "prompt": "A developer wishes to integrate Docusign Web Forms into their custom application. Which statement "
        "accurately describes the necessary roles of the Web Forms builder UI and the Web Forms API in a custom "
        "integration?",
        "options": [
            ("A", "Web form configurations must be created via the UI, but instances must be created via the API", True),
            ("B", "Both web form configurations and instances must be created via the API, and the UI is not used", False),
            ("C", "Both web form configurations and instances must be created using the UI, and the API is not used", False),
            ("D", "Web form configurations must be created via API, but instances must be created via the UI", False),
        ],
        "answer": "A. Web form configurations must be created via the UI, but instances must be created via the API",
        "explanation": "The Web Forms builder (a no-code UI) is where a form's structure - pages, fields, validation "
        "rules, conditional logic - is designed. Once that configuration exists, a developer uses the Web Forms API to "
        "create and integrate individual instances of that form for end users to fill out, typically embedded via "
        "Docusign JS.",
        "option_notes": [
            ("A", "Correct. Design the form once in the Web Forms builder UI; generate one instance per user "
             "programmatically via the API."),
            ("B", "Wrong - the configuration step explicitly happens in the builder UI, not the API."),
            ("C", "Wrong - instances specifically require the API (Instances:createInstance plus Docusign JS embedding); "
             "the UI alone cannot generate per-user instances for a custom integration."),
            ("D", "Backwards - it is the opposite of the real division of labor."),
        ],
        "shortcut": "Design the form once -> UI (Web Forms builder). Generate one instance per user, programmatically -> "
        "API.",
    },
    {
        "prompt": "The API call to create an envelope failed. Which parameter should you use to retry without creating a "
        "duplicate envelope?",
        "options": [
            ("A", "envelopeId", False),
            ("B", "recipientId", False),
            ("C", "retryId", False),
            ("D", "transactionId", True),
        ],
        "answer": "D. transactionId",
        "explanation": "transactionId is a value you (the client) supply yourself in the original create request, "
        "specifically to make retries safe. If the request fails or times out and you resend the exact same request with "
        "the same transactionId, Docusign can recognize it as the same transaction and avoid creating a duplicate envelope.",
        "option_notes": [
            ("A", "envelopeId doesn't exist yet at the point of failure - it is assigned by Docusign only AFTER the "
             "envelope is successfully created. If the create call failed, there is no envelope, so there is no envelopeId "
             "to reference for a retry."),
            ("B", "recipientId identifies a recipient record inside an already-existing envelope; irrelevant to envelope "
             "creation retries."),
            ("C", "retryId is not a real Docusign parameter."),
            ("D", "Correct. Supplied by the client before sending, which is what makes retry-safety (idempotency) "
             "possible in the first place."),
        ],
        "shortcut": "Retry a failed create request without duplicating -> transactionId (idempotency key, supplied by "
        "you upfront). Reference an envelope that already exists -> envelopeId (assigned by Docusign after the fact).",
    },
]


MANIFEST_SECTIONS_ROWS = [
    ("APP DETAILS", "name, publicationRegions, distribution, description, publisher, termsOfServiceUrl, icon/screenshots", "App Center listing metadata: what customers see and how the app can be installed."),
    ("CONNECTIONS", "One or more named connection objects with auth params", "Reusable authentication/connection details for reaching an external API, API proxy, or identity provider."),
    ("EXTENSIONS", "template, actionReferences", "Groups a set of actions into one extension and declares which extension-type contract (File IO / Data IO / Data Verification / Connected Fields) it fulfills."),
    ("ACTIONS", "name, description, template, connectionsReference, params", "Defines each individual callable task: what it does, which contract it follows, which connection it authenticates with, and which endpoint it calls."),
]


APP_DETAILS_FIELD_ROWS = [
    ("icon.data", "Base64-encoded image data for the app's icon."),
    ("icon.mediaType", "The MIME/media type of the icon image (e.g. image/png)."),
    ("screenshots[].data", "Base64-encoded image data for one screenshot. Up to four screenshots are allowed."),
    ("screenshots[].mediaType", "The MIME/media type of that screenshot image (e.g. image/png)."),
]


CONNECTIONS_FIELD_ROWS = [
    ("name", "Unique identifier for this connection object. This is the value that an action's connectionsReference must match to use this connection."),
    ("params.clientId / params.clientSecret", "Credentials issued by the external platform or identity provider for authenticating to it."),
    ("params.provider", "Set to CUSTOM for a custom/external identity provider connection."),
    ("params.scopes", "List of authorization scopes to request from the external provider during the OAuth exchange."),
    ("params.customConfig.tokenUrl / authorizationUrl", "The external provider's endpoints used to obtain an access token and to perform authorization."),
    ("params.customConfig.authorizationParams", "Extra query parameters required by the external provider's authorization endpoint."),
    ("params.customConfig.authorizationMethod", "Where credentials are sent on the token request: header or body."),
    ("params.customConfig.scopeSeparator", "The delimiter character used to join multiple scopes into one string."),
]


EXTENSIONS_FIELD_ROWS = [
    ("template", "Unique string ID referencing the predefined extension contract that Docusign provides for this extension type (File IO, Data IO, Data Verification, or Connected Fields)."),
    ("actionReferences", "List of action name values (defined in the actions object) that make up this extension. Docusign runs these actions to fulfill the extension's job."),
]


ACTIONS_FIELD_ROWS = [
    ("name", "Unique identifier for this action. Referenced by actionReferences in the extensions object to include the action in an extension."),
    ("description", "Human-readable explanation of what the action does. Documentation only, not functional."),
    ("template", "Action contract reference — a unique string ID for the predefined Docusign action contract/schema this action follows, defining the expected request/response shape."),
    ("connectionsReference", "Must match the name value of a connection object in the connections section. Tells this action which authentication/connection details to use when it calls out."),
    ("params", "Specifies the external API endpoint (or API proxy endpoint) that this action calls, plus any parameters needed for that call."),
]


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(hex_color("#58657a"))
    canvas.drawString(0.55 * inch, 0.42 * inch, "Docusign Extension Types - Important Distinctions")
    canvas.drawRightString(7.95 * inch, 0.42 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_overview_table(style: ParagraphStyle) -> Table:
    data = [[p(f"<b>{h}</b>", style) for h in ["Term", "Kind", "Core job", "Typical example"]]]
    for name, kind, job, example in OVERVIEW_ROWS:
        data.append(
            [
                p(f"<b>{name}</b>".replace("\n", "<br/>"), style),
                p(kind, style),
                p(job, style),
                p(example, style),
            ]
        )
    table = Table(data, colWidths=[1.3 * inch, 1.05 * inch, 2.15 * inch, 2.9 * inch], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), hex_color("#0b5cff")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, hex_color("#d7dfec")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, hex_color("#f6f8fc")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def build_field_table(headers: list, rows: list, col_widths: list, style: ParagraphStyle) -> Table:
    data = [[p(f"<b>{h}</b>", style) for h in headers]]
    for row in rows:
        data.append([p(f"<font face='Courier-Bold'>{row[0]}</font>", style), *[p(str(cell), style) for cell in row[1:]]])
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), hex_color("#0b5cff")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, hex_color("#d7dfec")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, hex_color("#f6f8fc")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def build_wide_table(headers: list, rows: list, col_widths: list, style: ParagraphStyle) -> Table:
    data = [[p(f"<b>{h}</b>", style) for h in headers]]
    for row in rows:
        data.append([p(f"<b>{row[0]}</b>", style), *[p(str(cell), style) for cell in row[1:]]])
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), hex_color("#0b5cff")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, hex_color("#d7dfec")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, hex_color("#f6f8fc")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    title = ParagraphStyle("Title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=hex_color("#0b2545"), spaceAfter=8)
    h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=hex_color("#0b2545"), spaceBefore=12, spaceAfter=7)
    h3 = ParagraphStyle("H3", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=hex_color("#0b2545"), spaceBefore=6, spaceAfter=4)
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=12, textColor=hex_color("#172033"))
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=12, bulletIndent=0, spaceAfter=3)
    intro = ParagraphStyle("Intro", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.6, leading=13, textColor=hex_color("#334155"), spaceAfter=10)
    small = ParagraphStyle("Small", parent=body, fontSize=8, textColor=hex_color("#58657a"))
    tiny = ParagraphStyle("Tiny", parent=body, fontSize=7, leading=9)

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.68 * inch,
    )

    story = [
        Paragraph("Important Distinctions: File IO vs. Data IO vs. Data Verification vs. Connected Fields", title),
        Paragraph(
            "These four terms are the extension types you choose from when registering a Docusign extension app in the "
            "Developer Console. They are easy to confuse because all four move information into or out of Docusign, but each "
            "operates at a different level: whole files, structured data, verification logic, or agreement fields.",
            intro,
        ),
        Paragraph("At a Glance", h2),
        build_overview_table(body),
        Spacer(1, 0.16 * inch),
        Paragraph("Definitions", h2),
    ]

    for name, points in DETAILS:
        block = [Paragraph(name, h3)]
        for point in points:
            block.append(Paragraph(f"&bull; {point}", bullet))
        block.append(Spacer(1, 0.08 * inch))
        story.append(KeepTogether(block))

    story.append(PageBreak())
    story.append(Paragraph("Examples", h2))
    story.append(
        Paragraph(
            "Illustrative scenarios for each extension type, spanning different industries so the pattern is clear regardless "
            "of the wording a question uses.",
            intro,
        )
    )
    for name, examples in EXAMPLES:
        block = [Paragraph(name, h3)]
        for ex in examples:
            block.append(Paragraph(f"&bull; {ex}", bullet))
        block.append(Spacer(1, 0.08 * inch))
        story.append(KeepTogether(block))

    story.append(PageBreak())
    story.append(Paragraph("Key Distinctions", h2))
    for title_text, explanation in KEY_DISTINCTIONS:
        story.append(
            KeepTogether(
                [
                    Table(
                        [[p(f"<b>{title_text}</b>", body)]],
                        colWidths=[7.3 * inch],
                        style=TableStyle(
                            [
                                ("BACKGROUND", (0, 0), (-1, -1), hex_color("#eaf1ff")),
                                ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#c7d8ff")),
                                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                                ("TOPPADDING", (0, 0), (-1, -1), 5),
                                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                            ]
                        ),
                    ),
                    Paragraph(explanation, body),
                    Spacer(1, 0.14 * inch),
                ]
            )
        )

    story.append(PageBreak())
    story.append(Paragraph("Exam Shortcut: recipientId vs. returnUrl vs. accountId vs. clientUserId vs. externalReferenceId", h2))
    story.append(
        Paragraph(
            "A consolidated cheat sheet for five easily-confused ID/parameter names across the eSignature, OAuth, and Web "
            "Forms APIs.",
            intro,
        )
    )
    story.append(
        build_field_table(
            ["Parameter", "Exam cue -> answer"],
            ID_PARAM_SHORTCUT_ROWS,
            [1.6 * inch, 5.7 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Table(
            [[p(
                "<b>Common trap:</b> clientUserId and externalReferenceId both sound like \"my app's tracking ID,\" but "
                "they belong to different API surfaces — clientUserId is an eSignature recipient field (embedded signing "
                "flag), while externalReferenceId is a Web Forms field (instance correlation). Don't swap them.",
                body,
            )]],
            colWidths=[7.3 * inch],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), hex_color("#fde2e1")),
                    ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#f0a9a5")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]
            ),
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("Workflow Start Methods", h2))
    story.append(
        Paragraph(
            "The four ways a Workflow Builder workflow can be initiated, split into manual vs. automatic triggers. "
            "Note on sourcing: the course material explicitly documents \"From within Workflow Builder\" (as \"Manually "
            "in Docusign\") and \"From a Link\" under its Manually Triggered tab. The Automatically Triggered tab's full "
            "content was not captured in the scraped text, so the \"From an Event\" and \"From an API call\" rows reflect "
            "practice-question context plus general Workflow Builder behavior rather than a directly quoted definition.",
            intro,
        )
    )
    story.append(
        build_wide_table(
            ["Start method", "Trigger type", "How it works", "Best for"],
            WORKFLOW_START_METHOD_ROWS,
            [1.5 * inch, 0.95 * inch, 3.05 * inch, 1.8 * inch],
            tiny,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Paragraph(
            "<b>Exam shortcut:</b> \"someone clicks Run Workflow in the tool itself\" -&gt; From within Workflow Builder. "
            "\"Embed a URL on a website/email\" -&gt; From a Link. \"Kicks off automatically because something else "
            "happened\" -&gt; From an Event. \"Your own code/integration starts it programmatically\" -&gt; From an API call.",
            body,
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("OAuth: Confidential Authorization Code Grant Request Sequence", h2))
    story.append(
        Paragraph(
            "The required three-step sequence of API requests to obtain credentials under the Confidential Authorization "
            "Code Grant flow (server-side app that can protect a client secret, with an interactive user login).",
            intro,
        )
    )
    story.append(
        build_field_table(
            ["Step", "What happens"],
            OAUTH_SEQUENCE_ROWS,
            [2.3 * inch, 5.0 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Paragraph(
            "<b>Key distinguishing point:</b> because this is the Confidential flow, the client_secret is used at step 2 "
            "during the token exchange. This is what separates it from Public Authorization Code Grant with PKCE, which uses "
            "a code_verifier/code_challenge instead of a client secret, for apps that cannot safely store one.",
            body,
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("OAuth Flow Comparison: Confidential vs. PKCE vs. No PKCE vs. JWT", h2))
    story.append(
        Paragraph(
            "Step-by-step comparison of what happens at each stage across the four flows. \"No PKCE\" is the plain "
            "Authorization Code Grant without the PKCE extension (no client secret and no code_verifier) — insecure for "
            "public clients and shown here for contrast, not as a recommended approach.",
            intro,
        )
    )
    story.append(
        build_wide_table(
            ["Step", "Confidential", "PKCE (Public)", "No PKCE", "JWT Grant"],
            OAUTH_FLOW_COMPARISON_ROWS,
            [1.35 * inch, 1.55 * inch, 1.55 * inch, 1.5 * inch, 1.55 * inch],
            tiny,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Paragraph(
            "<b>Exam shortcut:</b> Secret involved -&gt; Confidential. No secret but code_verifier/code_challenge involved "
            "-&gt; Public + PKCE. No secret, no verifier, just the bare code -&gt; without PKCE (insecure/legacy — a good "
            "distractor to reject). No browser at all, signed JWT instead -&gt; JWT Grant.",
            body,
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("Docusign Connect: the eventNotification Object", h2))
    block = []
    for point in EVENT_NOTIFICATION_POINTS:
        block.append(Paragraph(f"&bull; {point}", bullet))
    story.append(KeepTogether(block))
    story.append(Spacer(1, 0.14 * inch))
    story.append(Paragraph("The three Connect configuration levels", h3))
    story.append(
        build_field_table(
            ["Level", "Scope", "How configured"],
            CONNECT_LEVELS_ROWS,
            [1.9 * inch, 2.5 * inch, 2.9 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Paragraph(
            "<b>Exam shortcut:</b> \"configure a webhook for just this one envelope, via the API, at send time\" -&gt; "
            "eventNotification. \"webhook for the whole account or all envelopes\" -&gt; account-level or organization-level "
            "Connect, configured through the Admin pages (or API), not eventNotification.",
            body,
        )
    )
    story.append(Spacer(1, 0.16 * inch))

    story.append(Paragraph("Docusign Connect: Security Mechanisms", h3))
    story.append(
        Paragraph(
            "Not covered in the scraped course text (which only names an external \"Connect security\" article) - sourced "
            "from Docusign's live developer documentation instead.",
            intro,
        )
    )
    story.append(
        build_wide_table(
            ["Mechanism", "What it does", "Level availability"],
            CONNECT_SECURITY_ROWS,
            [1.3 * inch, 3.6 * inch, 2.4 * inch],
            tiny,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Paragraph(
            "<b>Level-specific takeaway:</b> Organization-level has no Basic Auth option - relies on OAuth for Connect "
            "(+ optionally HMAC and mTLS). Account-level and Envelope-level (via eventNotification) support the full menu: "
            "HMAC, Basic Authentication, mTLS, AND OAuth for Connect (OAuth is not org-level-exclusive - it is confirmed "
            "available at account-level and envelope-level too). Docusign's stated best practice for production is to use "
            "both HMAC and OAuth 2.0 together, layering in mTLS if infrastructure supports it - and this recommendation "
            "applies at the account level as much as anywhere else.",
            body,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Table(
            [[p(
                "<b>Exam shortcut:</b> \"Organization-level, can't use username/password\" -&gt; correct, no Basic Auth at "
                "that level, use OAuth for Connect instead. \"Verify the message wasn't tampered with\" -&gt; HMAC. \"Both "
                "sides prove identity with certificates\" -&gt; mTLS.",
                body,
            )]],
            colWidths=[7.3 * inch],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), hex_color("#fff3cd")),
                    ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#f0d68a")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]
            ),
        )
    )
    story.append(Spacer(1, 0.16 * inch))

    story.append(Paragraph("Connect Security: Valid Combinations", h3))
    story.append(
        build_wide_table(
            ["Combination", "Valid?", "When to use it"],
            CONNECT_SECURITY_COMBO_ROWS,
            [1.65 * inch, 1.85 * inch, 3.8 * inch],
            tiny,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Table(
            [[p(
                "<b>Exam shortcut:</b> the only invalid pair among these four is Basic Authentication + OAuth for Connect "
                "- they're mutually exclusive. Every other combination (HMAC+OAuth, HMAC+Basic Auth, Basic Auth+mTLS, and "
                "OAuth+mTLS) is supported, since these mechanisms largely operate on different layers and \"can be used in "
                "any combination\" except that one explicit restriction.",
                body,
            )]],
            colWidths=[7.3 * inch],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), hex_color("#fff3cd")),
                    ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#f0d68a")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]
            ),
        )
    )
    story.append(Spacer(1, 0.16 * inch))

    story.append(Paragraph("Connect Security: Decision Guide", h3))
    story.append(
        build_wide_table(
            ["Your situation", "Use this"],
            CONNECT_SECURITY_DECISION_ROWS,
            [3.4 * inch, 3.9 * inch],
            tiny,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Table(
            [[p(
                "<b>Exam shortcut:</b> Can you do OAuth? Yes -&gt; pair it with HMAC (best practice), optionally add mTLS "
                "too if you have certs. No OAuth infrastructure yet? Use Basic Authentication, paired with HMAC (recommended "
                "fallback) or mTLS (if you have certificate infrastructure) - never both Basic Auth and OAuth together. "
                "Memory hook: OAuth pairs with HMAC or mTLS. Basic Auth pairs with HMAC or mTLS. OAuth and Basic Auth never "
                "pair with each other.",
                body,
            )]],
            colWidths=[7.3 * inch],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), hex_color("#fff3cd")),
                    ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#f0d68a")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]
            ),
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("Extension App Manifest: Field Reference", h2))
    story.append(
        Paragraph(
            "The extension app manifest (JSON) has four sections: APP DETAILS, CONNECTIONS, EXTENSIONS, and ACTIONS. "
            "The tables below detail the fields inside each section.",
            intro,
        )
    )
    story.append(
        build_field_table(
            ["Section", "Key fields", "Purpose"],
            MANIFEST_SECTIONS_ROWS,
            [1.1 * inch, 2.6 * inch, 3.6 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.16 * inch))

    story.append(Paragraph("APP DETAILS: icon and screenshots fields", h3))
    story.append(
        build_field_table(
            ["Field", "What it does"],
            APP_DETAILS_FIELD_ROWS,
            [2.3 * inch, 5.0 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.14 * inch))

    story.append(Paragraph("connections object fields", h3))
    story.append(
        build_field_table(
            ["Field", "What it does"],
            CONNECTIONS_FIELD_ROWS,
            [2.3 * inch, 5.0 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.14 * inch))

    story.append(Paragraph("extensions object fields", h3))
    story.append(
        build_field_table(
            ["Field", "What it does"],
            EXTENSIONS_FIELD_ROWS,
            [2.3 * inch, 5.0 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.14 * inch))

    story.append(Paragraph("actions object fields", h3))
    story.append(
        build_field_table(
            ["Field", "What it does"],
            ACTIONS_FIELD_ROWS,
            [2.3 * inch, 5.0 * inch],
            body,
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Paragraph(
            "<b>How the pieces link together:</b> a connection's <font face='Courier-Bold'>name</font> is referenced by an "
            "action's <font face='Courier-Bold'>connectionsReference</font> (auth wiring); an action's "
            "<font face='Courier-Bold'>name</font> is referenced by an extension's <font face='Courier-Bold'>actionReferences</font> "
            "(grouping into a task set); and the extension's <font face='Courier-Bold'>template</font> declares which extension type "
            "(File IO, Data IO, Data Verification, or Connected Fields) the whole group fulfills.",
            body,
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("Practice Question: connections Object", h2))
    for i, q in enumerate(PRACTICE_QUESTIONS, start=1):
        block = [Paragraph(f"<b>Q{i}.</b> {q['prompt']}", body), Spacer(1, 0.06 * inch)]
        for opt_letter, text, is_correct in q["options"]:
            style = body
            block.append(Paragraph(f"{'<b>' if is_correct else ''}{opt_letter}. {text}{'</b>' if is_correct else ''}", style))
        block.append(Spacer(1, 0.08 * inch))
        story.append(KeepTogether(block))

        story.append(
            Table(
                [[p(f"<b>Answer:</b> {q['answer']}", body)]],
                colWidths=[7.3 * inch],
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), hex_color("#e6f6ea")),
                        ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#9fd8b0")),
                        ("LEFTPADDING", (0, 0), (-1, -1), 6),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                        ("TOPPADDING", (0, 0), (-1, -1), 5),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                    ]
                ),
            )
        )
        story.append(Spacer(1, 0.08 * inch))
        story.append(Paragraph(f"<b>Explanation:</b> {q['explanation']}", body))
        story.append(Spacer(1, 0.08 * inch))
        story.append(Paragraph("<b>Option notes:</b>", body))
        for opt_letter, note in q["option_notes"]:
            story.append(Paragraph(f"&bull; <b>{opt_letter}.</b> {note}", bullet))
        if q.get("shortcut"):
            story.append(Spacer(1, 0.06 * inch))
            story.append(
                Table(
                    [[p(f"<b>Exam shortcut:</b> {q['shortcut']}", body)]],
                    colWidths=[7.3 * inch],
                    style=TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, -1), hex_color("#fff3cd")),
                            ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#f0d68a")),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                        ]
                    ),
                )
            )
        if q.get("flag"):
            story.append(Spacer(1, 0.06 * inch))
            story.append(
                Table(
                    [[p(f"<b>&#9888; Flag:</b> {q['flag']}", body)]],
                    colWidths=[7.3 * inch],
                    style=TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, -1), hex_color("#fde2e1")),
                            ("BOX", (0, 0), (-1, -1), 0.4, hex_color("#f0a9a5")),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                        ]
                    ),
                )
            )
        story.append(Spacer(1, 0.14 * inch))

    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("Sources", h2))
    for src in SOURCES:
        story.append(Paragraph(f"&bull; {src}", small))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(OUT)


if __name__ == "__main__":
    main()

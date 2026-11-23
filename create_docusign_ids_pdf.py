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


OUT = Path("output/pdf/docusign_ids_payloads_exam_quick_guide.pdf")


PRIORITIES = {
    "HIGH": {
        "color": "#c1121f",
        "label": "High probability",
        "meaning": "Very likely to appear directly or through close MCQ distractors.",
    },
    "MED": {
        "color": "#b45309",
        "label": "Medium probability",
        "meaning": "Important supporting knowledge; often appears as distractors or secondary clues.",
    },
    "LOW": {
        "color": "#475569",
        "label": "Lower probability",
        "meaning": "Useful context; less likely to be the main tested answer.",
    },
}


ID_ROWS = [
    ("transactionId", "Idempotency value for create-envelope retries; prevents duplicate envelopes when a request is retried.", "Envelope creation request", "HIGH"),
    ("envelopeId", "Docusign-assigned ID of an envelope after it exists; used to retrieve, update, void, or check status.", "Envelope", "HIGH"),
    ("recipientId", "Identifies a recipient record inside an envelope.", "Recipient within envelope", "HIGH"),
    ("clientUserId", "Marks a recipient as embedded/captive signing instead of remote email signing.", "Recipient / embedded signing", "HIGH"),
    ("templateId", "References a reusable Docusign template; demo and production template IDs differ.", "Template", "HIGH"),
    ("eventNotification", "Envelope-level Connect configuration object included in an envelope request.", "Envelope-level Connect", "HIGH"),
    ("HMAC / webhook signature", "Security value used by a listener to verify that a Connect webhook message came from Docusign and was not tampered with.", "Connect webhook security", "MED"),
    ("recipient authentication", "Envelope recipient setting that requires a signer to pass an access check, such as SMS/phone/access code, before viewing or signing.", "Recipient access control", "HIGH"),
    ("Identity Verification", "Verifies who the signer is using stronger identity proofing, such as government ID, electronic/bank ID, KBA, or another configured IDV method.", "Recipient identity proofing", "HIGH"),
    ("Connected Fields", "Connects eSignature fields to an external data source or validation service so field values can be checked during document preparation or signing.", "eSignature field/data validation", "HIGH"),
    ("Data Verification", "Validates signer-entered data in real time during signing against trusted/internal sources, such as bank account, SSN, customer ID, or eligibility values.", "Signer-entered data validation", "HIGH"),
    ("action definition in app manifest", "Defines an Extension App action that Docusign can call, including the external operation/endpoint behavior and related parameters.", "Extension App manifest action", "HIGH"),
    ("connections", "Extension App manifest object defining reusable external auth/connection details.", "Extension App manifest", "HIGH"),
    ("connectionsReference", "Links an Extension App action to a named connection.", "Extension App action", "HIGH"),
    ("Confidential Authorization Code Grant", "Interactive OAuth flow for server-side apps that can protect a client secret while an individual user signs in.", "OAuth flow", "HIGH"),
    ("Public Authorization Code Grant with PKCE", "Interactive OAuth flow for public clients, such as SPAs or native apps, that cannot safely store a client secret.", "OAuth flow", "HIGH"),
    ("PKCE code verifier and code challenge", "Security mechanism used in Public Authorization Code Grant with PKCE to protect the authorization code exchange.", "OAuth / PKCE", "HIGH"),
    ("JSON Web Token Grant", "Non-interactive OAuth flow for service integrations where no user is present at runtime after consent is granted.", "OAuth flow", "HIGH"),
    ("/oauth/token", "OAuth token endpoint. Used to exchange a JWT, authorization code, refresh token, or other supported grant for an access token.", "OAuth endpoint", "HIGH"),
    ("/oauth/userinfo", "OAuth endpoint used after token acquisition to discover account IDs and base URIs available to the authenticated user.", "OAuth/account discovery", "HIGH"),
    ("Authorization: Bearer access token", "HTTP Authorization header value used on Docusign REST API calls after the app receives an access token.", "REST API request header", "HIGH"),
    ("accountId", "Identifies the Docusign account where API calls happen; usually appears in REST API paths.", "Account", "MED"),
    ("baseUri / basePath", "Host/base URI for API calls for a specific account; retrieved from /oauth/userinfo.", "Account / environment", "MED"),
    ("integrationKey / client_id", "Identifies the app/integration in OAuth requests.", "App / OAuth", "MED"),
    ("redirect_uri", "Where Docusign sends the user after OAuth authorization; must match configured redirect URI.", "App / OAuth", "MED"),
    ("documentId", "Identifies a document inside an envelope; tabs often reference document IDs.", "Document within envelope", "MED"),
    ("tabLabel", "Label/name for a tab/field, useful for identifying or mapping tabs.", "Tab / field", "MED"),
    ("anchorString", "Text anchor used to place tabs relative to document text.", "Tab placement", "MED"),
    ("workflowId", "Identifies a Workflow Builder/Maestro workflow definition.", "Workflow definition", "MED"),
    ("workflowInstanceId", "Identifies one running instance of a workflow.", "Workflow runtime instance", "MED"),
    ("Web Form instance URL", "Unique URL for one generated Web Form instance. This is where the user fills the form, usually rendered inside your site with the Docusign JS SDK.", "Web Forms", "MED"),
    ("externalReferenceId / correlation value", "Your app's tracking value for the Web Form instance. Example: map a submitted job application form back to applicant record APP-10492 in your system.", "Web Forms / external system", "MED"),
    ("agreementId", "Identifies an Agreement Manager agreement record.", "Agreement Manager", "MED"),
    ("Agreements:getAgreementsList / Agreements:list", "Finds/searches/lists agreements that match filter criteria before retrieving one specific agreement's details.", "Agreement Manager API", "HIGH"),
    ("Agreements:getAgreement", "Retrieves details for one specific agreement when you already know which agreement record you need.", "Agreement Manager API", "HIGH"),
    ("Agreements:createAgreementSummary", "Creates a summary for agreement content after the target agreement is known; used for summarization, not for searching or retrieving the base agreement record.", "Agreement Manager API / agreement summary", "MED"),
    ("Workflows:getWorkflowsList", "Lists available workflow definitions in Workflow Builder/Maestro so an app can discover or select a workflow to start or manage.", "Workflow API", "MED"),
    ("secretKey / client secret", "Secret used by confidential apps that can safely protect credentials.", "App / OAuth", "LOW"),
    ("returnUrl", "Where the browser goes after embedded signing or embedded sending ends.", "Embedded ceremony", "LOW"),
    ("brandId", "Applies account branding to the recipient/signing experience.", "Brand / envelope experience", "LOW"),
    ("bulkSendListId", "Identifies a Bulk Send recipient list.", "Bulk Send", "LOW"),
    ("batchId", "Identifies a bulk send batch/process.", "Bulk Send batch", "LOW"),
    ("action ID/name", "Identifies a callable action in an Extension App manifest.", "Extension App action", "LOW"),
    ("organization ID", "Identifies a Docusign organization containing one or more accounts.", "Organization", "LOW"),
]


PAYLOAD_ROWS = [
    ("OAuth / JWT", "JWT claims: iss, sub, aud, iat, exp, scope", "iss = integration key, sub = impersonated user, aud = Docusign auth server. Scope should include only needed API scopes after consent.", "HIGH"),
    ("OAuth grant flow", "Confidential Authorization Code Grant", "Use for server-side web apps where a user signs in interactively and the server can protect a client secret.", "HIGH"),
    ("OAuth grant flow", "Public Authorization Code Grant with PKCE", "Use for browser-only, native, or mobile/public clients where a user signs in interactively but the app cannot protect a secret.", "HIGH"),
    ("OAuth grant flow", "JSON Web Token Grant", "Use for non-interactive/background service integrations after consent has been granted.", "HIGH"),
    ("OAuth / PKCE", "PKCE code verifier and code challenge", "Not a separate business flow; it is the security mechanism inside Public Authorization Code Grant with PKCE.", "HIGH"),
    ("OAuth / Auth Code", "client_id, redirect_uri, scope, grant_type", "Recognize which flow uses interactive login and why redirect URI must match app configuration.", "HIGH"),
    ("OAuth / PKCE", "code_verifier / code_challenge", "Used by public clients that cannot protect a secret, such as SPAs or native apps.", "HIGH"),
    ("OAuth token exchange", "/oauth/token", "Endpoint used to request access tokens. The grant_type and body/header values depend on the OAuth flow.", "HIGH"),
    ("OAuth account discovery", "/oauth/userinfo", "Endpoint used after authentication to retrieve account_id and base_uri/baseUri values for API calls.", "HIGH"),
    ("API calls", "Authorization: Bearer access token", "REST calls require the access token in the Authorization header, not in the envelope body, email subject, or tabs.", "HIGH"),
    ("Envelope create", "status", "Controls envelope lifecycle behavior. created saves draft; sent sends immediately; voided cancels an in-process envelope.", "HIGH"),
    ("Envelope create", "recipients, documents, emailSubject", "Core envelope definition: who signs, what they sign, and what email they see.", "HIGH"),
    ("Envelope create", "transactionId", "Idempotency for retries; not the same as envelopeId.", "HIGH"),
    ("Envelope create", "eventNotification", "Envelope-level webhook configuration for one specific envelope.", "HIGH"),
    ("Recipients", "clientUserId", "Required in recipient definition for embedded signing.", "HIGH"),
    ("Recipients", "recipient authentication", "Controls access to the envelope before signing; used when signer must pass an authentication challenge.", "HIGH"),
    ("Recipients", "Identity Verification configuration", "Used when the signer must prove who they are with a configured Docusign IDV method before or during signing.", "HIGH"),
    ("eSignature fields", "Connected Fields", "Used when Docusign needs to validate or connect field values through an external service during field preparation or signing.", "HIGH"),
    ("eSignature fields", "Data Verification", "Used when signer-entered data must be checked in real time during the signing experience.", "HIGH"),
    ("Embedded signing", "EnvelopeViews:createRecipient request + returnUrl", "After creating the envelope for an embedded recipient, request a short-lived recipient view URL.", "HIGH"),
    ("Templates", "templateId / templateRoles", "Use templateId to reference a saved template; templateRoles maps recipient/data into that template.", "HIGH"),
    ("Composite templates", "serverTemplates / inlineTemplates / compositeTemplates", "serverTemplates reference saved Docusign templates stored in the account. inlineTemplates add runtime recipients, tabs, values, or settings inside the API request. compositeTemplates combine saved templates, inline runtime details, and documents when a simple templateId is not flexible enough.", "HIGH"),
    ("Tabs", "anchorString, anchorUnits, anchorXOffset, anchorYOffset", "Anchor tabs place fields relative to text; useful when document content shifts.", "HIGH"),
    ("Connect", "JSON SIM", "Recommended/event-focused Connect format; important for workflow/Maestro events.", "HIGH"),
    ("Connect", "eventData / include data options", "Controls how much envelope/recipient/document data is included in webhook payloads.", "MED"),
    ("Connect", "HMAC/signature settings", "Lets listener verify webhook authenticity; security concept, not the same as message format.", "MED"),
    ("Web Forms", "Web Form instance URL + Docusign JS SDK", "API creates or retrieves a unique URL for one Web Form instance; Docusign JS renders that form in the host page where the user fills it out.", "HIGH"),
    ("Web Forms", "externalReferenceId / correlation value", "Maps each form instance back to your system record, such as a job application, student application, customer onboarding case, or compliance request.", "MED"),
    ("Agreement Manager", "Agreements:getAgreementsList / Agreements:list", "Use when the app needs to find/search/list agreements matching criteria before selecting one.", "HIGH"),
    ("Agreement Manager", "Agreements:getAgreement", "Use when the app needs details for one known agreement record.", "HIGH"),
    ("Agreement Manager", "Agreements:createAgreementSummary", "Use after selecting a target agreement when the app needs a generated summary of agreement content. Do not use it to list agreements or retrieve the normal agreement details.", "MED"),
    ("Workflow API", "Workflows:getWorkflowsList", "Use when the app needs to discover available workflow definitions. This belongs to workflows, not Agreement Manager agreement records.", "MED"),
    ("Workflow API", "start method and starting variables", "Know when a workflow starts from a link, API call, or manual action, and how data enters the workflow.", "HIGH"),
    ("Workflow runtime", "workflow instance URL", "Used when launching or embedding a workflow instance.", "MED"),
    ("Extension App manifest", "action definition in app manifest", "Defines the external action/call Docusign can invoke from the extension app. This is where the operation is described, while connections handles auth.", "HIGH"),
    ("Extension App manifest", "actions", "Top-level manifest area containing the action definitions exposed by the extension app.", "HIGH"),
    ("Extension App manifest", "connections", "Defines reusable authentication details for external systems.", "HIGH"),
    ("Extension App manifest", "connectionsReference", "Connects an action to one of the connection definitions.", "HIGH"),
    ("Extension App manifest", "input/output schema", "Defines data passed into and returned from extension actions.", "MED"),
    ("Extension architecture", "API proxy", "Can transform requests/responses when external API format does not match what Docusign expects.", "MED"),
    ("Extension deployment", "public/private distribution", "Public App Center for broad availability; private for selected/internal accounts.", "HIGH"),
]


OAUTH_REQUIREMENT_ROWS = [
    (
        "Confidential Authorization Code Grant",
        "Interactive user login; server-side app can protect a secret.",
        "integration key/client_id; redirect_uri; client secret; authorization code; requested scopes; /oauth/token exchange.",
        "HIGH",
    ),
    (
        "Public Authorization Code Grant with PKCE",
        "Interactive user login; public client cannot safely store a secret, such as SPA/native/mobile app.",
        "integration key/client_id; redirect_uri; requested scopes; PKCE code challenge during authorize; PKCE code verifier during token exchange; no client secret.",
        "HIGH",
    ),
    (
        "PKCE code verifier and code challenge",
        "Protection mechanism for the public authorization-code exchange.",
        "code challenge is sent with the authorization request; code verifier is sent to /oauth/token to prove the same app started the flow.",
        "HIGH",
    ),
    (
        "JSON Web Token Grant",
        "Non-interactive service integration after consent; no user present at runtime.",
        "integration key/client_id as iss; user ID as sub; aud; iat; exp; scope; RSA private key to sign the JWT; prior user/admin consent; /oauth/token exchange.",
        "HIGH",
    ),
    (
        "Refresh token exchange",
        "Gets a new access token without sending the user through login again.",
        "refresh_token; grant_type=refresh_token; client authentication appropriate to the app type; /oauth/token exchange.",
        "MED",
    ),
    (
        "All OAuth API calls after token",
        "Calling Docusign APIs after receiving an access token.",
        "Authorization: Bearer access token header; accountId and baseUri/basePath from /oauth/userinfo; correct API environment.",
        "HIGH",
    ),
]


STATUS_ROWS = [
    ("Envelope", "created", "Draft envelope. It exists but has not been sent to recipients.", "HIGH"),
    ("Envelope", "sent", "Envelope has been sent and is awaiting recipient action.", "HIGH"),
    ("Envelope", "delivered", "A recipient has opened/viewed the envelope but has not completed their required action yet.", "MED"),
    ("Envelope", "completed", "All required recipients have completed their actions.", "HIGH"),
    ("Envelope", "declined", "A recipient declined to sign or complete the envelope.", "MED"),
    ("Envelope", "voided", "Envelope was canceled; recipients can no longer complete it. Best answer for canceling an in-progress/sent envelope.", "HIGH"),
    ("Envelope", "deleted", "Removed/deleted from a user view or context; not the normal answer for canceling a sent envelope.", "LOW"),
    ("Envelope", "purged", "Document/content removal due to purge or retention behavior; not normal cancellation.", "MED"),
    ("Recipient", "sent / delivered / completed / declined", "Recipient-level progress: sent to recipient, opened/viewed, completed signing, or declined.", "MED"),
    ("Workflow / Maestro", "running / in progress", "Workflow instance is executing and has not reached an end state.", "MED"),
    ("Workflow / Maestro", "completed", "Workflow instance completed its configured process.", "MED"),
    ("Workflow / Maestro", "failed / error", "Workflow instance or step failed and needs troubleshooting.", "MED"),
    ("Workflow / Maestro", "canceled / terminated", "Workflow instance was stopped before normal completion; exact wording can vary by UI/API context.", "LOW"),
    ("Web Forms", "created / started", "A Web Form instance exists or a participant has begun the form experience.", "LOW"),
    ("Web Forms", "submitted / completed", "Participant submitted the Web Form; data can feed downstream agreement/workflow processes.", "MED"),
    ("Bulk Send", "queued / processing", "Bulk send job is waiting or being processed.", "LOW"),
    ("Bulk Send", "sent / completed", "Bulk send envelopes were sent or the batch finished processing.", "MED"),
    ("Bulk Send", "failed", "Bulk send job or some recipients failed and require review.", "LOW"),
    ("Connect delivery", "delivered", "Webhook event was delivered to the listener.", "MED"),
    ("Connect delivery", "failed / retrying", "Webhook delivery failed and may be retried depending on configuration.", "MED"),
    ("Extension App lifecycle", "draft / submitted", "Extension app is being prepared or has been submitted for review.", "LOW"),
    ("Extension App lifecycle", "approved", "Extension app passed review/approval.", "MED"),
    ("Extension App lifecycle", "installed / enabled", "Extension app is available for use in an account/workflow context.", "MED"),
    ("Extension App lifecycle", "disabled", "Extension app is not active/available for use.", "LOW"),
    ("Agreement Manager", "agreement lifecycle/status metadata", "Agreement records can have lifecycle/status metadata depending on repository and agreement type; usually less tested than envelope status.", "LOW"),
]


DISTINCTIONS = [
    (
        "OAuth overview",
        "OAuth is the permission system an app uses to call Docusign APIs without using the user's password. The app gets an access token, then sends that token on API calls with the Authorization: Bearer access token header. Scopes define what the token is allowed to do, such as send envelopes or read user/account information. Consent is the user or admin approval for those requested scopes. Exam shortcut: OAuth = API permission system; access token = temporary API pass; scopes = allowed permissions; consent = approval for those permissions.",
        "HIGH",
    ),
    (
        "Confidential Auth Code vs Public Auth Code with PKCE vs JWT Grant",
        "Confidential Authorization Code Grant is for interactive user login when a server-side app can protect a client secret. Public Authorization Code Grant with PKCE is also interactive, but for public clients such as SPAs or native apps that cannot safely store a secret. JSON Web Token Grant is for non-interactive service integrations where no user is present at runtime after consent has been granted. The exam clue is usually: server can store secret = Confidential; browser/native cannot store secret = Public + PKCE; scheduled/background service = JWT Grant.",
        "HIGH",
    ),
    (
        "PKCE code verifier and code challenge vs OAuth grant flow",
        "PKCE code verifier and code challenge are not the full OAuth flow. They are the security mechanism inside Public Authorization Code Grant with PKCE. Their job is to protect the authorization-code exchange: the app sends a code_challenge during authorization and later proves it with the code_verifier during /oauth/token exchange. Public Authorization Code Grant with PKCE is the full OAuth flow for public clients such as native apps, mobile apps, or SPAs that authenticate an individual user but cannot safely store a client secret. Exam shortcut: asks 'what protects the exchange?' = PKCE verifier/challenge. Asks 'which OAuth flow should a native/browser app use?' = Public Authorization Code Grant with PKCE.",
        "HIGH",
    ),
    (
        "/oauth/token vs /oauth/userinfo vs Authorization: Bearer",
        "/oauth/token is the endpoint used to get an access token by exchanging an authorization code, JWT assertion, refresh token, or other supported grant. /oauth/userinfo is called after the app has an access token; it returns accountId and baseUri/basePath values so the app knows which Docusign account and API host to use. Authorization: Bearer access token is not an endpoint; it is the HTTP header placed on /oauth/userinfo and later REST API calls. Normal order: call /oauth/token, then call /oauth/userinfo with the Bearer token, then call Docusign REST APIs with Authorization: Bearer access token.",
        "HIGH",
    ),
    (
        "Bearer access token vs other OAuth tokens",
        "An access token is the temporary API credential used to call Docusign APIs. Bearer is how the access token is sent: Authorization: Bearer access_token. It is called Bearer because whoever holds the token can use it, so it must be protected. A refresh token is used to get a new access token later. An authorization code is a temporary login/consent result that is exchanged at /oauth/token for tokens. A JWT assertion is a signed claim used in JWT Grant and exchanged at /oauth/token for an access token. A PKCE code verifier is not an API token; it proves the public app that started login is the same app exchanging the authorization code. Exam shortcut: access token = what calls APIs; Bearer = how it is sent; refresh token = gets a new access token; authorization code/JWT assertion = exchanged to get an access token; PKCE verifier = protects the exchange.",
        "HIGH",
    ),
    (
        "transactionId vs envelopeId",
        "transactionId is supplied by your app before or during envelope creation to make retries safe. If the same create request is submitted again after a network error, Docusign can recognize it as the same transaction instead of creating a duplicate. envelopeId is assigned by Docusign after the envelope exists and is used for later operations such as retrieve, update, void, or status checks.",
        "HIGH",
    ),
    (
        "recipientId vs clientUserId",
        "recipientId identifies the recipient record inside the envelope. clientUserId is the key clue for embedded signing: it tells Docusign this recipient will sign inside the host app rather than through a normal remote email link. A question about embedded/captive signing usually points to clientUserId.",
        "HIGH",
    ),
    (
        "Embedded signing step order and ID jobs",
        "Step 1: get an OAuth access token and send it on API calls as Authorization: Bearer access_token. Step 2: use /oauth/userinfo to get accountId and baseUri/basePath for the account. Step 3: call Envelopes:create to create the envelope with documents and recipients. Step 4: include clientUserId on the recipient to mark that recipient as embedded/captive signing instead of remote email signing. Step 5: save the returned envelopeId because it identifies the created envelope. Step 6: call EnvelopeViews:createRecipient for that envelope to request the recipient view URL. The email, userName, and clientUserId in this request must match the recipient values from envelope creation. Step 7: include returnUrl so Docusign knows where to send the signer after the signing session ends. Step 8: use the returned url as the short-lived embedded signing URL and generate it only when the user is ready to sign. Exam shortcut: clientUserId = embedded signer flag; envelopeId = created envelope ID; EnvelopeViews:createRecipient = creates recipient view URL; recipient view URL = short-lived signing link; returnUrl = post-signing destination.",
        "HIGH",
    ),
    (
        "created vs sent vs voided",
        "In an envelope create payload, status=created saves the envelope as a draft. status=sent sends it immediately to recipients. status=voided cancels an envelope that is in progress or should no longer be completed. If the scenario says 'send now', choose sent. If it says 'prepare but do not send yet', choose created. If it says cancel an already-sent or active envelope, choose voided.",
        "HIGH",
    ),
    (
        "voided vs deleted vs purged",
        "voided is the normal exam answer for canceling an active/sent envelope so recipients can no longer complete it. deleted is not the normal status to cancel a sent envelope. purged is about document/content removal due to retention/privacy behavior, not normal cancellation. If a question asks how to immediately cancel an agreement/envelope before completion, choose voided.",
        "HIGH",
    ),
    (
        "eventNotification vs account/org Connect",
        "eventNotification is placed inside an envelope request and configures webhook behavior for that specific envelope. Account-level Connect is configured centrally for an account. Organization-level Connect is configured across selected or all accounts in an organization. These are scope differences, not message-format differences.",
        "HIGH",
    ),
    (
        "JSON SIM vs Connect level",
        "JSON SIM is a message format/model, not a level. It can be used with organization-level, account-level, and envelope-level Connect. Organization-level configurations use the JSON SIM model, and workflow/Maestro event questions often expect JSON SIM as the required format.",
        "HIGH",
    ),
    (
        "HMAC vs recipient authentication vs Identity Verification",
        "HMAC is for webhook security: your listener uses it to verify that a Connect message really came from Docusign and was not altered. Recipient authentication is for signer access control before a recipient views or signs an envelope, such as SMS, phone, or access code. Identity Verification is stronger identity proofing, such as government ID, electronic/bank ID, or KBA depending on configuration. HMAC protects server-to-server event messages; recipient authentication and Identity Verification protect the signing experience.",
        "HIGH",
    ),
    (
        "Identity Verification vs Connected Fields / Data Verification",
        "Identity Verification validates the person: it answers 'is this signer really the person they claim to be?' using ID proofing methods such as government ID, electronic/bank ID, KBA, or other configured IDV checks. Connected Fields and Data Verification validate field/data values: they answer 'is this entered value correct or allowed?' such as bank account number, SSN, customer ID, license number, or eligibility value. Exam shortcut: person identity = Identity Verification; field or data value = Connected Fields / Data Verification.",
        "HIGH",
    ),
    (
        "templateId vs compositeTemplates",
        "templateId references one saved template directly and is best when the envelope can be created from that template with normal role/data mapping. compositeTemplates are used when the request must combine saved server templates, inline recipient data, runtime tabs, settings, or direct documents in one envelope. If the question mentions combining a saved template with runtime recipients/tabs/documents, think compositeTemplates.",
        "HIGH",
    ),
    (
        "serverTemplates vs inlineTemplates",
        "serverTemplates point to saved templates in Docusign. Their job is to reuse existing template structure such as documents, roles, tabs, and settings. inlineTemplates live inside the API request. Their job is to add or override runtime details such as recipients, tabs, values, or envelope settings at send time. compositeTemplates can combine both, so exam questions often use these as close distractors.",
        "HIGH",
    ),
    (
        "fixed tabs vs anchor tabs",
        "Fixed tabs use pageNumber plus x/y positions. Anchor tabs use anchorString and offsets so fields stay near matching text even if the document shifts. If the scenario mentions variable document length or text shifting, anchor tabs are usually the better answer.",
        "HIGH",
    ),
    (
        "Web Form instance URL vs embedded signing URL",
        "A Web Form instance URL is rendered with the Docusign JS SDK so a user can fill out a Web Form, such as a job application, intake form, or onboarding questionnaire. An embedded signing URL is created with EnvelopeViews:createRecipient after an envelope exists for an embedded recipient. They are different experiences and different API surfaces.",
        "HIGH",
    ),
    (
        "clientUserId vs Docusign JS SDK vs Web Form instance URL vs externalReferenceId",
        "clientUserId is an eSignature recipient value that marks a signer as embedded/captive instead of remote email signing. Docusign JS SDK is the browser/client-side SDK used to render supported Docusign experiences such as a Web Form in your web app. Web Form instance URL is the unique URL where the user fills one generated Web Form instance. externalReferenceId is your app's correlation value that maps the Web Form instance back to an internal record. Example: a student starts financial aid form APP-10492. externalReferenceId=APP-10492 maps the form to the student application, the Web Form instance URL is where the student fills the form, the Docusign JS SDK renders it in the portal, and clientUserId is only relevant later if the student signs inside the app as an embedded signer.",
        "HIGH",
    ),
    (
        "externalReferenceId / correlation value vs Web Form instance URL",
        "The Web Form instance URL is where the user fills the form. The externalReferenceId or correlation value is how your system tracks what that form belongs to. For example, a careers portal may create a Web Form for applicant Jordan and store externalReferenceId=APP-10492, so when the form is submitted the app can update the correct job application record.",
        "HIGH",
    ),
    (
        "Agreement Manager operations: list vs get vs summary",
        "Agreements:getAgreementsList, also described as Agreements:list in the study notes, is for finding or listing agreements that match criteria, such as active agreements for a customer or agreements of a certain type. Agreements:getAgreement retrieves the details of one specific agreement after the app knows which agreement record it wants. Agreements:createAgreementSummary creates a summary for agreement content after the target agreement is known. Exam order: list/search first when you do not know the agreementId, getAgreement when retrieving one known record, createAgreementSummary when the question asks for a summary.",
        "HIGH",
    ),
    (
        "Agreement Manager operations vs Workflow operations",
        "Agreement operations work with agreement records and agreement content. Workflows:getWorkflowsList belongs to Workflow Builder/Maestro and lists workflow definitions an app may start or manage. If the question asks for agreements, use an Agreements operation; if it asks for available workflow definitions, use Workflows:getWorkflowsList.",
        "MED",
    ),
    (
        "connections vs connectionsReference",
        "connections defines reusable authentication/connection details in the Extension App manifest. connectionsReference appears on an action and points that action to the correct connection. If the question asks what links an action to auth credentials, the answer is connectionsReference.",
        "HIGH",
    ),
    (
        "action definition in app manifest vs connections",
        "An action definition in the app manifest describes what external capability Docusign can call, such as an endpoint/action for a third-party service. The connections object defines reusable authentication details. The connectionsReference on the action links the action to that auth configuration. If a question asks where the external API action is defined, choose action definition/actions; if it asks where reusable auth is defined, choose connections.",
        "HIGH",
    ),
    (
        "Extension App manifest shortcut: fields, actions, connections",
        "Validate signer or field data = Connected Fields / Data Verification. Define a callable external operation = actions or action definition in the manifest. Define reusable external authentication = connections. Link one action to the correct auth configuration = connectionsReference. Job wording: actions describe what Docusign can call; connections describe how Docusign authenticates; connectionsReference ties the action to the named connection.",
        "HIGH",
    ),
    (
        "Connected Fields vs Data Verification",
        "Both relate to validating data, but they appear in different extension/use-case language. Connected Fields is commonly tied to field/data validation integrated into eSignature field/signing experiences. Data Verification emphasizes validating signer-entered data in real time during signing against trusted/internal sources.",
        "HIGH",
    ),
    (
        "Workflow start link vs API trigger",
        "A workflow start link is useful when the user initiates or embeds a workflow through a URL-style launch. An API trigger/start is used when an application programmatically starts the workflow. Look for clues like iframe/link variables versus backend button/API call.",
        "MED",
    ),
    (
        "Data IO vs File IO",
        "Data IO extensions read and write structured records in another system. File IO or file archive extensions handle document storage/retrieval use cases, such as archiving completed agreements to an external repository.",
        "MED",
    ),
]


GLOSSARY_ROWS = [
    ("custom glue code", "Extra custom code written just to connect systems or force a process to work, instead of using a built-in Docusign feature."),
    ("downstream system", "A system that receives data or events after something happens earlier. Example: CRM updated after envelope completion."),
    ("narrow demo case", "A limited demo setup that works for one simple test but may fail in real production."),
    ("workaround", "A temporary, manual, or custom solution used instead of the proper supported feature."),
    ("native Docusign approach", "The built-in Docusign feature designed for the problem."),
    ("platform-native", "Using supported Docusign platform behavior instead of custom code."),
    ("production cutover", "The moment an integration moves from demo/testing into production."),
    ("stakeholder", "A person or team affected by the project, such as business owner, security, legal, support, or operations."),
    ("root platform behavior", "The actual Docusign feature or rule causing the result, not just the visible symptom."),
    ("gap in the design", "A missing or incorrect part of the integration design."),
    ("implementation ticket", "A development task or requirement written for engineers."),
    ("pull request", "A proposed code change being reviewed before merge."),
    ("trigger URL", "A URL that starts a workflow and may pass values into it."),
    ("system of record", "The authoritative system for a type of data, such as HR system for employee records."),
    ("hard-code", "Put fixed values directly in code instead of using configuration or dynamic data."),
    ("external capability", "A feature provided by another system that Docusign can call through an extension/app/integration."),
    ("external service", "A third-party or internal system outside Docusign, such as CRM, ERP, Google Drive, or a custom API."),
    ("runtime", "When the integration or workflow is actually executing, not when it is being designed/configured."),
    ("payload", "The JSON/body data sent in an API request or received in a webhook."),
    ("callback URL", "The URL Docusign calls or sends events to, usually for webhook notifications."),
    ("listener", "Your app/server endpoint that receives webhook events from Docusign."),
    ("correlation", "Mapping one Docusign object/process back to your internal record, such as a form instance to a job application ID."),
    ("idempotency", "Safe retry behavior: repeating the same request should not create duplicates. transactionId supports this for envelope creation."),
    ("event-driven", "The system reacts when Docusign sends an event, instead of constantly checking/polling."),
    ("polling", "Repeatedly asking Docusign whether something changed through API calls. Usually worse than Connect webhooks."),
    ("reusable capability", "A feature packaged so multiple workflows, customers, or accounts can use it, not a one-off script."),
    ("one-off integration", "A custom integration built for only one case, customer, or process."),
    ("line-of-business system", "A business application like CRM, HRIS, ERP, procurement, or compliance system."),
    ("source of truth", "The system that owns the correct/current version of a piece of data."),
    ("close-call distractor", "A wrong MCQ option that sounds plausible because it is related, but fails one key requirement."),
]


def hex_color(value: str):
    return colors.HexColor(value)


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


def badge(priority: str, style: ParagraphStyle) -> Paragraph:
    info = PRIORITIES[priority]
    return Paragraph(f"<b><font color='{info['color']}'>{info['label']}</font></b>", style)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(hex_color("#58657a"))
    canvas.drawString(0.55 * inch, 0.42 * inch, "Docusign IAM Integration & Extension Developer - IDs and Payloads Exam Guide")
    canvas.drawRightString(7.95 * inch, 0.42 * inch, f"Page {doc.page}")
    canvas.restoreState()


def priority_legend(style: ParagraphStyle) -> Table:
    rows = [[p("<b>Priority</b>", style), p("<b>Meaning</b>", style)]]
    for key in ["HIGH", "MED", "LOW"]:
        info = PRIORITIES[key]
        rows.append([badge(key, style), p(info["meaning"], style)])
    table = Table(rows, colWidths=[1.65 * inch, 5.75 * inch])
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, hex_color("#d7dfec")),
                ("BACKGROUND", (0, 0), (-1, 0), hex_color("#eaf1ff")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def build_table(headers: list[str], rows: list[tuple], col_widths: list[float], style: ParagraphStyle) -> Table:
    data = [[p(f"<b>{header}</b>", style) for header in headers]]
    for row in rows:
        *cells, priority = row
        data.append([*(p(str(cell), style) for cell in cells), badge(priority, style)])
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), hex_color("#0b5cff")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, hex_color("#d7dfec")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, hex_color("#f6f8fc")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
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
    h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=hex_color("#0b2545"), spaceBefore=10, spaceAfter=7)
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.3, leading=10.5, textColor=hex_color("#172033"))
    intro = ParagraphStyle("Intro", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.4, leading=12.5, textColor=hex_color("#334155"), spaceAfter=10)

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.68 * inch,
    )

    story = [
        Paragraph("Docusign IDs, Payloads, and Exam Distinctions", title),
        Paragraph(
            "Exam-focused guide for the main IDs, references, payload fields, and close-call distinctions in the Docusign IAM Integration & Extension Developer material. This is not an exhaustive API reference; it highlights what is most likely to matter in MCQs and scenario questions.",
            intro,
        ),
        priority_legend(body),
        Spacer(1, 0.14 * inch),
        Paragraph("IDs and References", h2),
        build_table(
            ["ID / reference", "Job", "Level / scope", "Exam priority"],
            ID_ROWS,
            [1.45 * inch, 3.55 * inch, 1.35 * inch, 1.05 * inch],
            body,
        ),
        PageBreak(),
        Paragraph("OAuth Flow Requirements Checklist", h2),
        build_table(
            ["Flow / item", "When it applies", "Required pieces to recognize", "Exam priority"],
            OAUTH_REQUIREMENT_ROWS,
            [1.75 * inch, 1.85 * inch, 2.85 * inch, 0.95 * inch],
            body,
        ),
        PageBreak(),
        Paragraph("Important Payload Parts", h2),
        build_table(
            ["Area", "Payload part", "Why it matters", "Exam priority"],
            PAYLOAD_ROWS,
            [1.35 * inch, 2.0 * inch, 3.05 * inch, 1.0 * inch],
            body,
        ),
        PageBreak(),
        Paragraph("Statuses to Recognize", h2),
        build_table(
            ["Area", "Status / wording", "Job / meaning", "Exam priority"],
            STATUS_ROWS,
            [1.35 * inch, 1.75 * inch, 3.25 * inch, 1.05 * inch],
            body,
        ),
        PageBreak(),
        Paragraph("Most Exam-Important Distinctions", h2),
    ]

    for title_text, explanation, priority in DISTINCTIONS:
        story.append(
            KeepTogether(
                [
                    Table(
                        [[p(f"<b>{title_text}</b>", body), badge(priority, body)]],
                        colWidths=[5.95 * inch, 1.35 * inch],
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
    story.append(Paragraph("Scenario Jargon Glossary", h2))
    story.append(
        Paragraph(
            "Plain-English meanings for recurring wording used in the practice questions. These are not Docusign product names, but they help decode exam scenarios.",
            intro,
        )
    )
    glossary_data = [[p("<b>Term</b>", body), p("<b>Meaning</b>", body)]]
    for term, meaning in GLOSSARY_ROWS:
        glossary_data.append([p(term, body), p(meaning, body)])
    glossary = Table(glossary_data, colWidths=[1.85 * inch, 5.55 * inch], repeatRows=1)
    glossary.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), hex_color("#0b5cff")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, hex_color("#d7dfec")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, hex_color("#f6f8fc")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(glossary)

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

    print(OUT)


if __name__ == "__main__":
    main()

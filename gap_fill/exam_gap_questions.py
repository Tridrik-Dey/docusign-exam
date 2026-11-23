# Gap-filling questions mapped to official Prep Guide (v. 2026) objectives.
# Each entry: (domain, topic, stem, [(id,text,explanation)], correct_ids, explanation)

Q = []
def q(domain, topic, stem, options, correct, explanation):
    Q.append(dict(domain=domain, topic=topic, stem=stem, options=options, correct=correct, explanation=explanation))

AUTH = "API Authentication"
GOLIVE = "Go Live Process"
CONNECT = "Docusign Connect"
ESIG = "eSignature API"
FEAT = "eSignature Features and Web Forms"
AM = "Agreement Manager API"
WF = "Workflow Builder and Workflow API"
APPS = "App Center and Extension Apps"

# ---------------- Section 1: API Authentication (consent, revoke) ----------------
q(AUTH, "Revoke consent",
  "A user revokes consent for a JWT-based integration through Manage Profile > Connected Apps. The integration still holds an access token that was issued 20 minutes ago. What happens?",
  [("A", "The existing access token is invalidated immediately and the next API call returns 401.",
        "Revoking consent does not kill live access tokens. They stay valid until they expire naturally, so the next call does not fail immediately."),
   ("B", "The existing access token keeps working until it expires; the next JWT exchange fails until consent is granted again.",
        "Correct. Revoking consent invalidates refresh tokens and blocks new tokens, but live access tokens (including JWT-issued ones) remain usable until they expire."),
   ("C", "The token keeps working, and the integration can keep minting new JWT tokens because JWT does not use consent.",
        "JWT Grant absolutely requires consent. Without it, the JWT exchange returns consent_required."),
   ("D", "Docusign automatically re-prompts the user for consent on the next API call.",
        "API calls never trigger a consent prompt. The integration must send the user's browser to /oauth/auth to obtain consent again.")],
  ["B"],
  "Per 'Obtain and revoke consent': revoking consent invalidates refresh tokens and requires new consent before new tokens are issued, but live access tokens and JWT tokens remain active until they expire.")

q(AUTH, "Revoke consent",
  "Consent for an internal JWT integration was granted by an organization administrator for all users in the claimed domain. A user in that domain wants to revoke the app's access to their account. What is true?",
  [("A", "The user can revoke it from Manage Profile > Connected Apps like any other app.",
        "Users who belong to the organization's reserved (claimed) domains cannot revoke admin-granted consent individually."),
   ("B", "Admin-granted consent must be revoked by an administrator in Docusign Admin; users in the reserved domain cannot revoke it individually.",
        "Correct. When consent was provided by an organization administrator, it is revoked with the Docusign Admin tool, and reserved-domain users cannot revoke it themselves."),
   ("C", "The integration key must be deleted to remove consent.",
        "Deleting the key is unnecessary and affects every user. Consent is revoked in Docusign Admin."),
   ("D", "The user must open a support case with Docusign.",
        "Revocation is self-service for the organization admin through Docusign Admin.")],
  ["B"],
  "Admin consent (common for JWT) is revoked with Docusign Admin. Users who are members of the organization's reserved domains cannot revoke consent individually.")

q(AUTH, "Consent",
  "An ISV sells a JWT-based integration to many customers. Some customers have Docusign Access Management with claimed domains; others do not. Which TWO design choices follow Docusign best practice? (Select two)",
  [("A", "Offer the admin consent for external applications flow (scope=openid plus admin_consent_scope) for customers with claimed domains.",
        "Correct. ISV-owned apps licensed to other organizations use admin consent for external applications, requested with scope=openid and admin_consent_scope."),
   ("B", "Always build an individual consent fallback for users or customers who cannot use admin consent.",
        "Correct. Admin consent needs Access Management and a claimed domain, which not every customer has, so an individual consent path is required."),
   ("C", "Ask each customer's admin to authorize the app from Docusign Admin > Connected Apps > Authorize Application.",
        "That UI path only works for internal apps (keys owned by the organization). For external apps, consent cannot be granted from the UI."),
   ("D", "Skip consent entirely by requesting the impersonation scope in the JWT assertion.",
        "Impersonation must itself be consented to. Putting the scope in the assertion does not replace consent.")],
  ["A", "B"],
  "JWT best practice: try admin consent (external-app flow for ISV apps), then fall back to individual consent, because admin consent needs Access Management and a claimed domain.")

q(AUTH, "Consent",
  "A developer sends an org admin to /oauth/auth with scope=openid and admin_consent_scope=signature%20impersonation. After the admin consents, how does the app find out WHICH organizations granted consent?",
  [("A", "From the coid claim in the ID token returned with the access token.",
        "Correct. When openid is requested, the response includes an ID token whose coid property lists the consenting organization IDs. That is the only way to get this list."),
   ("B", "By calling the eSignature Accounts:get endpoint.",
        "Accounts:get returns eSignature account settings, not the organizations that granted admin consent."),
   ("C", "From the state parameter echoed back to the redirect URI.",
        "state is a CSRF value the app supplies. It carries no consent information from Docusign."),
   ("D", "From the X-DocuSign-Org header on later API calls.",
        "No such header carries consent organizations.")],
  ["A"],
  "The ID token (requested via openid) has no system function. It only records the consenting admin and the consenting organization IDs in coid.")

q(AUTH, "Scopes",
  "Which TWO statements about scopes for the admin consent for external applications flow are correct? (Select two)",
  [("A", "The scope parameter is set to openid.",
        "Correct. Admin consent for external apps uses scope=openid so the consenting organization IDs are recorded."),
   ("B", "The scopes requested for each org user go in admin_consent_scope (for example signature impersonation).",
        "Correct. admin_consent_scope holds the space-separated scopes granted on behalf of each user in the organization."),
   ("C", "The extended scope can be used with JWT Grant to get a refresh token.",
        "extended issues a refresh token and only applies to the Authorization Code flow. JWT Grant never returns a refresh token."),
   ("D", "The Maestro aow_manage scope is implied by signature.",
        "Maestro scopes must be requested explicitly. signature does not imply aow_manage.")],
  ["A", "B"],
  "External admin consent uses scope=openid plus admin_consent_scope. extended only works with Authorization Code Grant, and API-specific scopes like aow_manage must be requested explicitly.")

# ---------------- Section 2: Go Live / API limits / efficiency ----------------
q(GOLIVE, "API limits",
  "An account's integrations exceed the default hourly API call limit. What happens, and what is the default?",
  [("A", "Default 1,000 calls/hour; extra calls are queued and processed next hour.",
        "The default is 3,000 calls per hour, and excess calls are blocked, not queued."),
   ("B", "Default 3,000 calls/hour per account; further calls are blocked until the start of the next hour.",
        "Correct. The hourly limit is shared by all apps on the account; once exceeded, calls fail until the hour resets."),
   ("C", "Default 3,000 calls/hour per integration key; the key is permanently disabled.",
        "The limit applies per account (shared by all apps), and the key is not permanently disabled."),
   ("D", "There is no hourly limit, only a burst limit.",
        "Both hourly and burst limits exist.")],
  ["B"],
  "Docusign's default hourly limit is 3,000 calls per account. When exceeded, calls are blocked until the next hour and fail with 'The maximum number of hourly API invocations has been exceeded.'")

q(GOLIVE, "API limits",
  "Which TWO practices align with Docusign guidance for staying within API resource limits? (Select two)",
  [("A", "Subscribe to Docusign Connect instead of polling envelope status.",
        "Correct. Connect pushes status changes, removing the need to poll."),
   ("B", "If polling is unavoidable, poll a given envelope no more than once every 15 minutes.",
        "Correct. Status polling per envelope is limited to once per 15 minutes; violations can fail Go-Live review."),
   ("C", "Retry failed calls immediately in a tight loop until they succeed.",
        "Tight retry loops amplify burst-limit violations. Read the rate-limit headers and back off."),
   ("D", "Split traffic across multiple integration keys to multiply the hourly limit.",
        "The hourly limit is per account and shared by all integrations, so extra keys do not add capacity.")],
  ["A", "B"],
  "Use Connect over polling, respect the once-per-15-minutes polling rule, read the X-RateLimit headers, and back off when limits are reached.")

q(GOLIVE, "API limits",
  "An app receives the error code Burst_APIInvocation_Envelope_Limit_Exceeded. What does it indicate?",
  [("A", "The account exceeded its 3,000 calls per hour.",
        "That produces the hourly limit message, not an envelope-specific burst code."),
   ("B", "Too many GET/PUT requests were made against a single envelope (and its documents/objects) within a short 30-second window.",
        "Correct. Per-envelope burst limits cap calls against one envelope's resources in a 30-second window."),
   ("C", "The envelope has too many recipients.",
        "Recipient counts are not related to this error code."),
   ("D", "The bulk send batch is too large.",
        "Bulk send size limits have different error codes.")],
  ["B"],
  "Docusign enforces hourly and 30-second burst limits on GET/PUT per envelope. Exceeding them returns codes like Burst_APIInvocation_Envelope_Limit_Exceeded or Hourly_Envelope_Polling_Limit_Exceeded.")

q(GOLIVE, "Efficiency score",
  "Where can an account admin see efficiency scores for each integration and the factors that lower them?",
  [("A", "API Usage Center (Admin > Integrations > API Usage Center).",
        "Correct. The API Usage Center dashboard shows calls by integration key, limit status and efficiency scores, with recommendations."),
   ("B", "Connect Failures log.",
        "The Connect failure log lists failed webhook deliveries, not API efficiency."),
   ("C", "Apps and Keys > Service Integration.",
        "Apps and Keys manages integration keys, secrets and RSA keys. It does not show efficiency scores."),
   ("D", "The envelope audit history.",
        "Audit history covers single-envelope events, not app-level API efficiency.")],
  ["A"],
  "The API Usage Center lets you monitor call volume, see which apps approached limits, view efficiency scores and update the hourly limit.")

q(GOLIVE, "Efficiency score",
  "Which THREE are factors in the API Usage Center efficiency score? (Select three)",
  [("A", "Excessive envelope status requests", "Correct. Repeatedly requesting envelope status (polling) lowers the efficiency score."),
   ("B", "Excessive document retrieval requests", "Correct. Repeatedly downloading the same documents is a scored inefficiency."),
   ("C", "Excessive requests for nonexistent envelopes", "Correct. Calling for envelope IDs that do not exist wastes calls and is a scored factor."),
   ("D", "Number of templates in the account", "Template count is not an efficiency score factor."),
   ("E", "Use of composite templates", "Composite templates are a request model, not a scored factor.")],
  ["A", "B", "C"],
  "Efficiency factors include blocked calls, exceeded burst/hourly limits, excessive document retrieval, excessive envelope API/status/recipient-status requests, requests for nonexistent envelopes, excessive requests per envelope and low call activity.")

q(GOLIVE, "API limits",
  "An admin wants to raise the account's hourly API limit in the API Usage Center but the Update Hourly Limit option is rejected. Which TWO conditions could explain it? (Select two)",
  [("A", "Some apps on the account have unresolved efficiency issues.",
        "Correct. You must fix flagged efficiency issues before the limit can be changed."),
   ("B", "The account plan does not include the limit management feature.",
        "Correct. Without the feature in the plan, the update option is not available."),
   ("C", "The integration key uses JWT Grant instead of Authorization Code Grant.",
        "The OAuth flow has no effect on limit management."),
   ("D", "The account has Connect configured.",
        "Using Connect is a best practice and does not block limit changes.")],
  ["A", "B"],
  "Prerequisites: the plan includes limit management, you are an account admin, no Support-set temporary/permanent limit is in effect, apps are operating efficiently, and there is enough call history.")

q(GOLIVE, "API limits",
  "An integration must reconcile envelope statuses after its Connect listener was down for two hours. What is the recommended way to catch up?",
  [("A", "Call Envelopes:get for every envelope ever sent.",
        "Polling every envelope wastes calls and can hit per-envelope and hourly limits."),
   ("B", "Call Envelopes:listStatusChanges with a from_date covering the outage, using overlapping time spans.",
        "Correct. listStatusChanges returns changed envelopes in one call; overlapping windows avoid missed changes."),
   ("C", "Delete and recreate the Connect configuration so it replays every event.",
        "Recreating the configuration does not replay history. Use the failure log/republish or listStatusChanges."),
   ("D", "Increase the hourly API limit and poll each envelope every minute.",
        "Per-envelope polling is limited to once per 15 minutes regardless of the hourly limit.")],
  ["B"],
  "Docusign's guidance: when you need status history, use listStatusChanges with overlapping time spans rather than per-envelope polling.")

# ---------------- Section 3: Connect (multi-answer) ----------------
q(CONNECT, "Security",
  "Which TWO mechanisms help a Connect listener verify that a webhook really came from Docusign and was not altered? (Select two)",
  [("A", "HMAC signature validation using the X-DocuSign-Signature-1 header.",
        "Correct. Connect signs the payload with an HMAC key; the listener recomputes and compares it."),
   ("B", "Mutual TLS (client certificate) between Docusign and the listener.",
        "Correct. mTLS lets the listener verify Docusign's client certificate."),
   ("C", "Checking that the envelopeId exists in the payload.",
        "Any attacker can include an envelope ID. This proves nothing about the sender."),
   ("D", "Requiring the listener URL to be HTTP on port 80.",
        "Connect requires HTTPS in production; plain HTTP weakens security.")],
  ["A", "B"],
  "Connect listener security options include HMAC signatures, mutual TLS, Basic authentication and OAuth 2.0 for Connect.")

q(CONNECT, "Retries",
  "Which TWO listener behaviors reduce Connect failures and retries? (Select two)",
  [("A", "Return HTTP 200 quickly, then process the payload asynchronously (for example via a queue).",
        "Correct. Slow processing causes timeouts that Docusign treats as failures and retries."),
   ("B", "Make processing idempotent so a redelivered event does no harm.",
        "Correct. Retries and republishes can deliver the same event twice."),
   ("C", "Return HTTP 500 for events the app does not care about.",
        "Any non-2xx response is a failure that triggers retries. Acknowledge and ignore instead."),
   ("D", "Call Envelopes:get for every event before acknowledging.",
        "Extra synchronous API calls slow the response and waste API quota.")],
  ["A", "B"],
  "Connect retries failed deliveries. Acknowledge fast, queue the work and process idempotently.")

# ---------------- Section 4: eSignature API (multi-answer) ----------------
q(ESIG, "Composite templates",
  "A request uses compositeTemplates with one serverTemplate (sequence 1) and one inlineTemplate (sequence 2) that both define a signer for role 'Client'. Which TWO statements are correct? (Select two)",
  [("A", "The inline template recipient data overlays the server template where they overlap, which lets the app supply runtime values.",
        "Correct. The inline template sets the recipient's name and email at runtime, and that data is merged with the server template's role definition."),
   ("B", "Server and inline templates in a composite template are combined according to their sequence numbers.",
        "Correct. The sequence value controls how templates are layered."),
   ("C", "Composite templates cannot mix server and inline templates in one request.",
        "Mixing them is exactly what composite templates are for."),
   ("D", "Composite templates require envelope status 'created' and cannot be sent directly.",
        "Composite template envelopes can be created with status 'sent'.")],
  ["A", "B"],
  "Composite templates layer server templates and inline templates by sequence. Inline templates typically supply runtime recipient and tab data for template roles.")

q(ESIG, "Embedded signing",
  "Which TWO are required for embedded signing with EnvelopeViews:createRecipient? (Select two)",
  [("A", "The signer has a clientUserId set when the envelope is created.",
        "Correct. clientUserId marks the recipient as embedded, and the same value must be passed to createRecipient."),
   ("B", "The request includes a returnUrl where Docusign redirects after the signing session.",
        "Correct. returnUrl is required, and Docusign appends an event parameter such as signing_complete."),
   ("C", "The signing URL is emailed to the signer.",
        "Embedded signing URLs are opened directly by your app, not emailed."),
   ("D", "The envelope must be in 'created' (draft) status.",
        "The envelope must be sent before a recipient view can be generated.")],
  ["A", "B"],
  "Embedded signing: create the envelope with clientUserId, then call createRecipient with matching recipient details, an authenticationMethod and a returnUrl. The URL is short-lived and single-use.")

# ---------------- Section 5: Features & Web Forms ----------------
q(FEAT, "Recipient authentication",
  "A sender wants signers to enter a code shared out-of-band (for example read out over the phone) before opening documents. No extra cost or third-party check is wanted. Which method fits?",
  [("A", "Access code authentication", "Correct. An access code is set on the envelope before sending, and each recipient must enter it to open the documents."),
   ("B", "Knowledge-based authentication (KBA)", "KBA asks public-record questions through a third-party service. It is heavier and is not an out-of-band shared code."),
   ("C", "ID verification (IDV)", "IDV checks a government ID and is a premium feature, which is more than this requires."),
   ("D", "Recording authenticationMethod on createRecipient", "This only records how your app authenticated the signer. It enforces nothing.")],
  ["A"],
  "Access code is the lightest enforced method: an alphanumeric phrase set on the envelope that the recipient must enter.")

q(FEAT, "Recipient authentication",
  "Which statement about ID verification (IDV) as a recipient authentication method is correct?",
  [("A", "It is enabled by default in every developer (demo) account.",
        "IDV is the one method not enabled by default in the developer environment."),
   ("B", "It requires your account's IDV workflowId, retrieved with IdentityVerifications:list, and is available in eSignature REST API v2.1.",
        "Correct. Add identityVerification with the workflowId from IdentityVerifications:list to the recipient (v2.1 API)."),
   ("C", "It uses questions based on the signer's public records.",
        "That describes KBA, not IDV."),
   ("D", "It only records the authentication your app performed.",
        "That describes the authenticationMethod record for embedded signing.")],
  ["B"],
  "IDV verifies government photo IDs and eIDs. It needs the account's workflow ID (IdentityVerifications:list), uses REST v2.1, and must be enabled by Docusign.")

q(FEAT, "Recipient authentication",
  "Which TWO statements correctly compare recipient authentication methods? (Select two)",
  [("A", "Phone authentication lets the recipient receive a code by call or SMS and uses a workflowId from IdentityVerifications:list.",
        "Correct. Phone authentication is configured through the identity verification workflow mechanism."),
   ("B", "KBA verifies the signer with questions drawn from public records (US only) and can be cumbersome for low-risk documents.",
        "Correct. KBA uses public-record questions and is heavier than needed for low-risk agreements."),
   ("C", "Access code authentication checks a government-issued photo ID.",
        "Access code is a shared phrase. ID checks are IDV."),
   ("D", "Adding more authentication methods always improves the signer experience.",
        "More methods add friction. Docusign advises matching authentication to the document's risk.")],
  ["A", "B"],
  "Choose authentication by risk: access code is light, phone (call/SMS) adds a second factor, KBA uses public-record questions (US), and IDV checks ID documents. All except IDV are enabled in demo.")

q(FEAT, "Recipient authentication",
  "An app authenticates users with its own SSO before embedded signing and wants that fact recorded on the certificate of completion. What should it do?",
  [("A", "Set authenticationMethod (for example SingleSignOn_SAML) in the EnvelopeViews:createRecipient request.",
        "Correct. authenticationMethod (plus optional authenticationInstant, assertionId, securityDomain) records your app's authentication on the certificate."),
   ("B", "Add an access code to the envelope.", "That adds a Docusign-enforced check. It does not record your SSO."),
   ("C", "Enable KBA on the recipient.", "KBA adds another check rather than recording the one your app performed."),
   ("D", "Put the SSO name in the email subject.", "The email subject is not an authentication record.")],
  ["A"],
  "For embedded signing, authenticationMethod records (but does not enforce) the method your app used, which helps with non-repudiation.")

q(FEAT, "Standards-based signatures",
  "A European customer needs signers to apply an EU Qualified Electronic Signature (QES). What must the envelope request include?",
  [("A", "recipientSignatureProviders on the signer, naming a signature provider (QES from a Qualified Trust Service Provider).",
        "Correct. Standards-based signatures are requested per signer with recipientSignatureProviders (signatureProviderName plus optional signatureProviderOptions)."),
   ("B", "An access code only.", "An access code is authentication, not a qualified digital signature."),
   ("C", "A brandId for an EU brand.", "Branding does not change the legal signature type."),
   ("D", "A Connect configuration in the EU data center.", "Connect is notifications only and has nothing to do with signature level.")],
  ["A"],
  "SBS supports AES (certificates from Docusign or your organization) and QES (from government-certified QTSPs). Include recipientSignatureProviders for at least one signer in Envelopes:create.")

q(FEAT, "Standards-based signatures",
  "Which TWO statements about Standards-Based Signatures (SBS) are correct? (Select two)",
  [("A", "Some features, such as Markup, Notary and attachment by fax, are not compatible with SBS.",
        "Correct. Docusign lists features that are not compatible with SBS because they would break digital signatures."),
   ("B", "A downloaded combined PDF is not digitally signed, because concatenating signed PDFs breaks the signatures.",
        "Correct. Download documents individually to keep each digital signature intact."),
   ("C", "SBS envelopes can freely add or delete fields with Advanced Correct after signing starts.",
        "After the first signature, adding or deleting fields is not allowed, because it would invalidate the signature."),
   ("D", "AccountSignatureProviders:list returns the IDV workflow IDs.",
        "It returns the signature providers available to the account. IDV workflow IDs come from IdentityVerifications:list.")],
  ["A", "B"],
  "SBS changes how features behave: no field add/delete after first signature, combined PDFs are unsigned, watermarks become annotations, and some features are incompatible.")

q(FEAT, "Web form configuration type",
  "A team wants a web form that only collects survey data into their database. No signature or envelope is needed. Which configuration type fits?",
  [("A", "Standalone web form", "Correct. Standalone web forms are not linked to an eSignature template, and no envelope is generated. They are for data collection only."),
   ("B", "Template-based web form", "Template-based forms generate an envelope after submission, which is not needed here."),
   ("C", "PowerForm", "PowerForms are a legacy self-service signing feature, not a Web Forms API configuration type."),
   ("D", "Remote web form instance", "Remote is a delivery method that is emailed and envelope-oriented, not a configuration type for data-only collection.")],
  ["A"],
  "Web Forms supports two types: template-based (an envelope is generated after submission) and standalone (no envelope, data collection only).")

q(FEAT, "Web form configuration type",
  "Which TWO statements about web form instances created from a STANDALONE configuration are correct? (Select two)",
  [("A", "No envelope is generated, so the envelopes array in Instances:getInstance is empty.",
        "Correct. Envelopes are generated only for template-based configurations."),
   ("B", "Submitted values are retrieved from the formValues object in the Instances:getInstance response.",
        "Correct. formValues holds the submitted field names and values."),
   ("C", "authenticationMethod/assertionId can be used to record recipient authentication on the certificate of completion.",
        "Those properties are not supported for standalone configurations or remote instances, because there is no envelope and no certificate."),
   ("D", "Envelope status should be tracked with a Connect listener.",
        "There is no envelope to track. Track the instance status instead (for example SUBMITTED).")],
  ["A", "B"],
  "Standalone means no envelope: use instance status (INITIATED, INPROGRESS, SUBMITTED, EXPIRED, FAILED) and formValues from getInstance.")

q(FEAT, "Web form configuration type",
  "For a TEMPLATE-BASED web form delivered as an EMBEDDED instance, when is the envelope generated?",
  [("A", "When Instances:createInstance is called.", "That is when it happens for remote instances, not embedded ones."),
   ("B", "When the first user submits the web form instance.", "Correct. For embedded instances, the envelope is generated on first submission."),
   ("C", "Never. Embedded instances do not create envelopes.", "Template-based configurations always produce an envelope."),
   ("D", "Only after the web form configuration is republished.", "Republishing affects configuration versions, not envelope generation.")],
  ["B"],
  "Remote instance: envelope generated when createInstance is processed. Embedded instance: envelope generated when the first user submits.")

q(FEAT, "Web Forms embedding",
  "Which TWO are required or valid when creating an EMBEDDED web form instance with Instances:createInstance? (Select two)",
  [("A", "clientUserId, which identifies the user in your system (max 100 characters).",
        "Correct. clientUserId is required for embedded instances."),
   ("B", "formValues, to prefill known data from your system of record.",
        "Correct. Prefill uses the formValues object with field names from Configurations:getForm."),
   ("C", "sendOption: 'now' with a recipients array of roleName entries.",
        "That pattern is for remote instances, where users are reached by email."),
   ("D", "An envelopeId from a previously sent envelope.",
        "Instances are created from a web form configuration (formId), not an existing envelope.")],
  ["A", "B"],
  "Embedded instances need clientUserId and can use formValues and tags. Remote instances use sendOption and recipients with roleName.")

q(FEAT, "ID Evidence",
  "A compliance team needs the ID evidence (for example scanned ID images) collected during a signer's IDV. Which approach fits?",
  [("A", "Use the ID Evidence API to retrieve ID evidence events/media for the recipient after verification.",
        "Correct. The ID Evidence API is designed to retrieve IDV evidence for audit and regulatory needs."),
   ("B", "Download the certificate of completion, which contains the ID images.", "The certificate records events, not the raw evidence images."),
   ("C", "Read the Connect envelope-completed payload.", "Connect envelope events do not carry the IDV evidence media."),
   ("D", "Query Agreement Manager for the agreement.", "Agreement Manager holds agreement data, not IDV evidence.")],
  ["A"],
  "Objective: 'Outline how to create an API integration with IDV that retrieves ID data' maps to the ID Evidence API (How to Retrieve ID Evidence Events).")

# ---------------- Section 6: Agreement Manager ----------------
q(AM, "AI / RAG",
  "A team wants an internal AI assistant to answer questions about signed contracts using retrieval-augmented generation (RAG). Which TWO steps fit an Agreement Manager API design? (Select two)",
  [("A", "Retrieve agreements and their AI-extracted fields (parties, dates, provisions) through the Agreement Manager API.",
        "Correct. Structured extracted data is ideal context for retrieval."),
   ("B", "Index that agreement data (and documents) in the AI system's retrieval store, keyed by agreement ID for traceability.",
        "Correct. RAG needs the data in a searchable store, and keeping the agreement ID lets answers cite the source."),
   ("C", "Poll each envelope every minute to rebuild the index.",
        "Aggressive polling breaks API limits and is the wrong source. Agreement data comes from Agreement Manager."),
   ("D", "Give the AI system the Docusign admin password so it can browse the web app.",
        "Never share credentials. Use OAuth with the appropriate scopes.")],
  ["A", "B"],
  "Objective: 'Explain how to incorporate agreement data in an external AI system for RAG'. Pull extracted agreement data with the API and index it for retrieval.")

q(AM, "Legacy import",
  "Which TWO statements about bringing legacy agreements into Agreement Manager are correct? (Select two)",
  [("A", "Legacy (non-Docusign) agreements can be bulk imported so AI extraction runs on them as well.",
        "Correct. Importing legacy agreements lets them benefit from the same AI extraction and search."),
   ("B", "After import, extracted data can be reviewed and corrected before it is relied on downstream.",
        "Correct. Extractions flagged for review should be validated, matching the 'review and update extraction' objective."),
   ("C", "Legacy agreements must first be re-signed through eSignature.",
        "No re-signing is needed. Import brings existing agreements in as they are."),
   ("D", "Import is only possible through Connect.", "Connect sends event notifications. It does not import agreements.")],
  ["A", "B"],
  "Agreement Manager objectives cover bulk import of legacy agreements and a review/update process for extractions.")

# ---------------- Section 7: Workflow Builder & API ----------------
q(WF, "Workflow instance management",
  "A custom portal triggered a Maestro workflow and stored the returned instance ID. How should it show the user the workflow's current status?",
  [("A", "Call getWorkflowInstance (GET /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}).",
        "Correct. getWorkflowInstance returns the instance's status, start/end times and who started it."),
   ("B", "Call getWorkflowTriggerRequirements.", "That describes the inputs needed to trigger, not an instance's status."),
   ("C", "Call Envelopes:get on the workflow ID.", "A workflow ID is not an envelope ID."),
   ("D", "Call pauseNewWorkflowInstances.", "That stops new instances being created. It does not report status.")],
  ["A"],
  "Workflow instance management: getWorkflowInstancesList, getWorkflowInstance and cancelWorkflowInstance; pause/resume apply to creating new instances.")

q(WF, "Workflow instance management",
  "Which scope must an access token include to call Maestro workflow management endpoints such as pause, resume and cancel?",
  [("A", "signature", "signature covers eSignature. Maestro needs its own scope."),
   ("B", "aow_manage", "Correct. Maestro endpoints require the aow_manage scope."),
   ("C", "impersonation only", "impersonation enables JWT on behalf of a user but grants no Maestro permission."),
   ("D", "extended", "extended only issues refresh tokens in the Authorization Code flow.")],
  ["B"],
  "Maestro uses the same OAuth tokens as eSignature but needs Maestro-specific scopes, for example aow_manage.")

q(WF, "Workflow instance management",
  "Which TWO statements about Maestro instance management are correct? (Select two)",
  [("A", "pauseNewWorkflowInstances stops NEW instances from being created; running instances are not canceled.",
        "Correct. Pause applies to creating new instances, and resumePausedWorkflow turns creation back on."),
   ("B", "cancelWorkflowInstance stops a specific running instance so it executes no further steps.",
        "Correct. Cancel terminates one instance immediately."),
   ("C", "Pausing a workflow deletes its in-flight instances.", "Pause never deletes instances."),
   ("D", "Instance management endpoints use the eSignature base path /restapi/v2.1.",
        "Maestro uses https://api-d.docusign.com/v1 (demo) or https://api.docusign.com/v1 (production).")],
  ["A", "B"],
  "Maestro API endpoints: GetWorkflowsList, GetWorkflowTriggerRequirements, TriggerWorkflow, getWorkflowInstancesList, getWorkflowInstance, cancelWorkflowInstance, pauseNewWorkflowInstances, resumePausedWorkflow.")

q(WF, "API trigger",
  "Which TWO steps are needed before an app can trigger a published Maestro workflow by API? (Select two)",
  [("A", "Call getWorkflowTriggerRequirements to learn the trigger URL and required input fields.",
        "Correct. Trigger requirements give the trigger endpoint and the input schema."),
   ("B", "Get an access token that includes the required Maestro scope (for example aow_manage).",
        "Correct. Without the Maestro scope the trigger call is rejected."),
   ("C", "Create an eSignature envelope with status 'sent' first.", "The workflow itself creates envelopes in its steps."),
   ("D", "Configure an envelope-level Connect webhook.", "Connect is optional for notifications. It is not a trigger prerequisite.")],
  ["A", "B"],
  "Flow: get a token with Maestro scopes, call GetWorkflowTriggerRequirements, then TriggerWorkflow with the required inputs, and track it with getWorkflowInstance.")

q(WF, "Publishing",
  "A Maestro workflow publish call fails its pre-publication check because of consent errors. What should the developer do?",
  [("A", "Open the URL in the consentUrl field, have the user grant consent, then repeat the call.",
        "Correct. The pre-run check returns a consentUrl when consent is missing. Grant consent, then publish again (without isPreRunCheck=true)."),
   ("B", "Recreate the workflow from scratch.", "The workflow definition is fine. Only consent is missing."),
   ("C", "Switch the integration to Implicit Grant.", "Changing the OAuth flow does not satisfy workflow consent."),
   ("D", "Ignore it. Production publishes skip the check.", "Every publish must pass the check.")],
  ["A"],
  "Maestro publishing runs an automated review. If it fails for consent, use consentUrl, then publish again.")

# ---------------- Section 8: App Center & Extension Apps ----------------
q(APPS, "Extension selection",
  "A lender must confirm during signing that the signer is the owner (or authorized signatory) of the US bank account they enter. Which extension fits?",
  [("A", "Bank account owner verification (Verify.Version1.BankAccountOwner)",
        "Correct. It verifies both the account and that the person is the owner or authorized signatory (US ABA routing numbers only)."),
   ("B", "Bank account verification (Verify.Version3.BankAccount)", "That only validates the account details, not who owns the account."),
   ("C", "Data IO", "Data IO reads/writes system-of-record data in Maestro workflows. It does not verify fields during signing."),
   ("D", "File output cloud storage", "That writes documents to storage.")],
  ["A"],
  "Bank account owner verification is a Data Verification extension (form-based: verification type 'Bank Account Owner'; manifest: Verify.Version1.BankAccountOwner).")

q(APPS, "Extension selection",
  "Which TWO data verification extensions can also be used in Web Forms, not only in the eSignature Add Fields view and signing? (Select two)",
  [("A", "Email address verification", "Correct. Its extension points include eSignature and Web Forms."),
   ("B", "Phone verification", "Correct. Its extension points include eSignature and Web Forms."),
   ("C", "SSN verification", "Its extension points are the eSignature Add Fields view and signing only."),
   ("D", "Business FEIN verification", "Its extension points are the eSignature Add Fields view and signing only.")],
  ["A", "B"],
  "Per Supported extensions, email and phone verification extend into Web Forms; the other verification types target eSignature Add Fields and signing.")

q(APPS, "Extension selection",
  "A new extension app must save completed documents to a customer's cloud storage from a Maestro workflow. Which extension should it implement?",
  [("A", "File output cloud storage", "Correct. New apps should use file output cloud storage, a File IO extension used in Maestro workflows."),
   ("B", "File archive", "It is still supported for existing apps, but Docusign says new apps should use file output cloud storage instead."),
   ("C", "Connected fields", "Connected fields verify envelope data. They do not write documents."),
   ("D", "Postal address verification", "Postal address verification is a data verification extension.")],
  ["A"],
  "File IO: file output cloud storage (recommended for new apps) and the legacy file archive extension.")

q(APPS, "Connected Fields",
  "Which TWO actions does Docusign call on a connected fields extension app when a connection is created or refreshed? (Select two)",
  [("A", "Get Type Names (DataIO.Version6.GetTypeNames)", "Correct. It runs first to list the types your system of record exposes."),
   ("B", "Get Type Definitions (DataIO.Version6.GetTypeDefinitions)", "Correct. It runs next and returns the type definitions in Concerto format."),
   ("C", "Verify (ConnectedFields.Version1.Verify)", "Verify runs during signing when required connected fields are filled, not on connection."),
   ("D", "Archive document", "That is a file extension action.")],
  ["A", "B"],
  "On connect/refresh, Docusign calls Get Type Names then Get Type Definitions (Concerto data model). Verify runs at signing time.")

q(APPS, "Connected Fields",
  "How can an integration programmatically receive the verification results from connected fields in an envelope?",
  [("A", "A Connect listener subscribed to the extension-executed event (JSON SIM event model only).",
        "Correct. Verification results are delivered with the extension-executed event, which is supported only in JSON SIM."),
   ("B", "Call TabInfo:GetConnectedFieldsTabGroups after signing.",
        "That endpoint lists available connected fields for building envelopes, not verification results."),
   ("C", "Use the legacy XML Connect format.", "The extension-executed event is JSON SIM only."),
   ("D", "Poll Envelopes:get every minute.", "That breaks the polling limits and the results are not exposed that way.")],
  ["A"],
  "Results also appear in envelope history and the certificate of completion, but programmatically they come through Connect extension-executed events (JSON SIM).")

q(APPS, "Connected Fields",
  "Which TWO steps are needed to send an envelope with connected fields through the API? (Select two)",
  [("A", "Call TabInfo:GetConnectedFieldsTabGroups to get the installed apps' connected field definitions.",
        "Correct. This returns the extension data needed for each connected tab."),
   ("B", "Put that data in each tab's extensionData property in the Envelopes:create request.",
        "Correct. extensionData marks the tab as a connected field to verify."),
   ("C", "Add the connected fields as a Maestro workflow step.", "Connected fields are not currently supported in Maestro."),
   ("D", "Create the envelope with the Web Forms API.", "Connected-field envelopes are created with the eSignature Envelopes:create request.")],
  ["A", "B"],
  "Connected Fields API flow: GetConnectedFieldsTabGroups, then build tabs with extensionData, then Envelopes:create; verification happens when the recipient enters data.")

q(APPS, "Public vs private",
  "A bank builds a connected fields extension that verifies values against its own internal customer database. How should it usually be distributed?",
  [("A", "As a private extension app available only to the bank's own accounts.",
        "Correct. Connected fields verify organization-specific data, so private distribution is usually the right choice."),
   ("B", "As a public App Center listing for all Docusign customers.", "Other customers cannot use the bank's internal database."),
   ("C", "Through Connect.", "Connect is a webhook service, not an app distribution channel."),
   ("D", "As a PowerForm.", "PowerForms are unrelated to extension apps.")],
  ["A"],
  "Docusign notes connected fields extensions are useful for private extension apps, which are published only for specific accounts.")

q(APPS, "Register, test, publish",
  "Which THREE belong to the process of building and releasing an extension app? (Select three)",
  [("A", "Register the app in the Developer Console (form-based or by uploading an app manifest).",
        "Correct. Registration defines the extensions, actions and connections."),
   ("B", "Run connection and extension tests in the Developer Console.", "Correct. Console tests show detailed errors before functional testing."),
   ("C", "Submit the app for review and publish it to the App Center (public) or privately.",
        "Correct. Publishing makes it installable."),
   ("D", "Request a Go-Live review for the eSignature integration key.", "Go-Live promotes eSignature API integration keys. Extension apps follow the App Center review/publish path."),
   ("E", "Add the app to a PowerForm.", "This is unrelated.")],
  ["A", "B", "C"],
  "Objective: 'Outline the steps required to register, test, and publish an extension app': register (form or manifest), test (Console tests plus functional tests), then publish.")

q(APPS, "Infrastructure",
  "Which TWO are infrastructure considerations when hosting an extension app's backend service? (Select two)",
  [("A", "The endpoint must be publicly reachable over HTTPS by Docusign (or reached through an API proxy).",
        "Correct. Docusign calls your service, so it must be reachable and secured."),
   ("B", "Authorization for Docusign's calls to your service must be configured (for example OAuth 2.0 client credentials or authorization code).",
        "Correct. Extension apps define how Docusign authenticates to your service."),
   ("C", "The service must run inside the customer's Docusign account.", "Your service runs on your own infrastructure."),
   ("D", "The service must poll Docusign every minute for work.", "Docusign calls your service on demand. There is no polling.")],
  ["A", "B"],
  "Plan for reachability (public HTTPS, firewall allow-listing, or an API proxy) and for the authorization model Docusign uses to call your service.")

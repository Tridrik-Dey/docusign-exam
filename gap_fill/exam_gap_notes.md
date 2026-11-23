## Official Exam Overview (Prep Guide v. 2026)

- 60 multiple-choice items. **Some questions have more than one correct answer.** Answer every question; there is no penalty for guessing.
- 150 minutes, proctored online via Certiverse (Safe Exam Browser, webcam, government photo ID).
- Passing score: 70%. Retake waiting period: 45 days.

| Section | Weight |
|---|---|
| 1. API Authentication | 13% |
| 2. Go Live Process | 11% |
| 3. Docusign Connect | 12% |
| 4. eSignature API | 16% |
| 5. eSignature Features & Web Forms | 11% |
| 6. Agreement Manager API | 6% |
| 7. Workflow Builder & Workflow API | 15% |
| 8. App Center & Extension Apps | 16% |

Out of scope (removed from these notes): Responsive Signing, PowerForms, Workspaces API, and the Agreement Manager UI-only topics (sharing permissions, dashboards/reports/renewals). No official exam objective covers them.

## Exam Gap Topics (official objectives the courses cover lightly)

Sources: Docusign Developer Center pages listed as "Support Resources" in the official Prep Guide.

### Section 1 - Obtain and revoke consent
- Three ways to get consent: **individual consent**, **admin consent for internal apps** (the integration key is owned by your org; granted in Docusign Admin > Connected Apps > Authorize Application), and **admin consent for external apps** (an ISV app; browser goes to `/oauth/auth?response_type=code&scope=openid&client_id=...&redirect_uri=...&admin_consent_scope=signature%20impersonation`).
- Admin consent requires **Access Management** and a **claimed domain**. It applies to users in the reserved domains.
- With `openid`, the response includes an **ID token**. Its `coid` claim lists the consenting organization IDs. This is the only way to get that list. The ID token is not used to call APIs.
- Best practice for JWT/ISV apps: try admin consent, and **always build an individual consent fallback**.
- **Revoking consent**:
  - Individual: Manage Profile > **Connected Apps** > Revoke.
  - Admin-granted consent: revoke in **Docusign Admin**. Users in reserved domains **cannot** revoke individually.
  - Revoking **invalidates refresh tokens** and blocks new tokens. **Live access tokens (including JWT ones) keep working until they expire.**
- `extended` scope = reusable refresh token, **Authorization Code Grant only**. JWT never returns a refresh token (its token lasts 1 hour; mint a new JWT).

### Section 2 - API limits and efficiency score
- Default **3,000 calls/hour per account**, shared by all integrations; resets on the hour. Exceeding it blocks calls until the next hour ("The maximum number of hourly API invocations has been exceeded").
- **Burst limit**: 500 calls per 30 seconds in production, 200 in demo.
- **Polling**: at most **once per 15 minutes per envelope**. Violations can fail Go-Live review. Prefer **Connect**. For catch-up, use `Envelopes:listStatusChanges` with overlapping time spans.
- Per-envelope error codes: `Hourly_Envelope_Polling_Limit_Exceeded`, `Burst_Envelope_Polling_Limit_Exceeded`, `Hourly_APIInvocation_Envelope_Limit_Exceeded`, `Burst_APIInvocation_Envelope_Limit_Exceeded`.
- Read the `X-RateLimit-*` response headers, log usage, alert near the limit, and back off. Aim for 5 or fewer calls to create/update an envelope.
- **API Usage Center** (Admin > Integrations > API Usage Center): calls by integration key, limit status, **efficiency scores**, and an **Update Hourly Limit** option.
- **Efficiency score factors**: blocked API calls; exceeded burst limit; exceeded hourly limit; excessive document retrieval requests; excessive envelope API requests; excessive envelope status requests; excessive recipient status requests; excessive requests for nonexistent envelopes; excessive requests per envelope; low call activity.
- Raising the limit yourself requires all of these: the plan includes limit management, you are an account admin, no Support-set limit is in effect, apps are efficient (fix the flagged issues first), and there is enough call history.

### Section 5 - Recipient authentication: comparison
| Method | How it is configured | Notes |
|---|---|---|
| Access code | `accessCode` on the recipient | Shared out of band. Lightest enforced method. |
| Phone (call or SMS) | `identityVerification.workflowId` (from `IdentityVerifications:list`) | Second factor. SMS can cost extra. |
| KBA | e.g. `idCheckConfigurationName` = "ID Check $" | Public-record questions, **US only**, LexisNexis. Heavy for low-risk documents. |
| ID verification (IDV) | `identityVerification.workflowId` (REST v2.1) | Government photo ID or eID. **Not enabled by default in demo**; ask the account manager. |
| Embedded record | `authenticationMethod` (+ `authenticationInstant`, `assertionId`, `securityDomain`) on `createRecipient` | **Records** your app's authentication on the certificate. It does **not enforce** anything. |
- All methods except IDV are enabled in demo, and production may cost extra. Match the method to the document's risk.
- Retrieve IDV evidence (ID images and events) with the **ID Evidence API**.

### Section 5 - EU Standards-Based Signatures (SBS)
- Signature types: electronic, **AES** (certificates from Docusign or your organization), and **QES** (from government-certified **QTSPs**).
- Add `recipientSignatureProviders` (`signatureProviderName` plus `signatureProviderOptions`, for example `oneTimePassword` or `sms`) to at least one signer in `Envelopes:create`.
- Available providers: `GET /restapi/v2.1/accounts/{accountId}/signatureProviders` (AccountSignatureProviders:list).
- **Not compatible with SBS**: attachment by fax, concatenating signer attachments, legacy digital signatures, Markup, Notary.
- **Works differently with SBS**:
  - Advanced Correct: no adding or deleting fields after the first signature.
  - Combined PDF download is **not** digitally signed.
  - Free-form signing: only signature and initials fields after someone has signed.
  - Watermarks are added as annotations.
  - Wet-signed documents are added as new documents.

### Section 5 - Web forms with vs. without an envelope
- **Template-based** configuration: built from an eSignature template (copied into a *web form template*). An **envelope is generated** after submission.
  - **Remote** instance: the envelope is created when `createInstance` is processed.
  - **Embedded** instance: the envelope is created when the **first user submits**.
- **Standalone** configuration: **no envelope**, data collection only. The `envelopes` array is empty.
- **Embedded** instances need `clientUserId` (max 100 characters) and render with the Docusign JS SDK.
- **Remote** instances use `sendOption` and `recipients[]` with `roleName`; users are reached by email.
- Prefill with `formValues`. Get field names from `Configurations:getForm`.
- Read results with `Instances:getInstance` / `listInstances`: `status` is INITIATED, INPROGRESS, SUBMITTED, EXPIRED or FAILED; also `instanceRecipientStatus`, `formValues` and `envelopes[]`.
- **Record of recipient authentication** (`authenticationMethod`, `authenticationInstant`, `assertionId`, `securityDomain` in `createInstance`): only for **embedded signing** of template-based forms. **Not supported** for remote instances or standalone configurations.

### Section 6 - Agreement Manager API: RAG and review
- Retrieve agreements and their AI-extracted data (parties, dates, provisions) with the Agreement Manager API (for example `getAgreement`).
- Index that data in your AI system's retrieval store, keyed by agreement ID, so answers can cite their source.
- Bulk-import legacy agreements so AI extraction runs on them too. Then review and correct the extractions (an external review step) before relying on them downstream.

### Section 7 - Workflow instance management (Maestro / Workflow Builder API)
- Base path: `https://api-d.docusign.com/v1` (demo) or `https://api.docusign.com/v1` (production). Scope: **`aow_manage`**, in addition to normal OAuth.
| Operation | Method and path |
|---|---|
| GetWorkflowsList | GET `/accounts/{accountId}/workflows` |
| GetWorkflowTriggerRequirements | GET `/workflows/{workflowId}/trigger-requirements` |
| TriggerWorkflow | POST `/workflows/{workflowId}/actions/trigger` |
| getWorkflowInstancesList | GET `/workflows/{workflowId}/instances` |
| **getWorkflowInstance** | GET `/workflows/{workflowId}/instances/{instanceId}` (status, start/end times, `started_by`) |
| cancelWorkflowInstance | POST `/instances/{instanceId}/actions/cancel` (stops one running instance) |
| pauseNewWorkflowInstances / resumePausedWorkflow | POST `/workflows/{workflowId}/actions/pause` or `resume` (affects **new** instances only) |
- Publishing runs an automated pre-publication check. If consent is missing, open the returned `consentUrl`, grant consent, and publish again (without `isPreRunCheck=true`).

### Section 8 - Extensions and extension points
| Extension | Extension point | Manifest value |
|---|---|---|
| Connected fields | eSignature Add Fields and signing | `ConnectedFields.Version1.Verify` (+ `DataIO.Version6.GetTypeNames` and `GetTypeDefinitions`) |
| Data IO | Maestro workflows | read/write system of record |
| Bank account owner verification | eSignature | `Verify.Version1.BankAccountOwner` (owner or authorized signatory; US ABA routing only) |
| Bank account verification | eSignature | `Verify.Version3.BankAccount` |
| Email / Phone verification | eSignature **and Web Forms** | `Verify.Version1.Email` / `Verify.Version1.PhoneNumber` |
| Business FEIN | eSignature | `Verify.Version1.BusinessEntity` |
| SSN, Postal address | eSignature | |
| File output cloud storage | Maestro workflows | use this for **new** apps (file archive is legacy) |
- Connected fields: when a connection is created or refreshed, Docusign calls Get Type Names, then Get Type Definitions (**Concerto** data model). Verify runs when the signer completes the required fields.
- Connected fields are **not supported in Maestro**.
- Sending by API: `TabInfo:GetConnectedFieldsTabGroups`, then put the data in each tab's `extensionData`, then `Envelopes:create`.
- Verification results come through the Connect **extension-executed** event (**JSON SIM only**), and also appear in envelope history and the certificate of completion.
- Org-specific verification usually belongs in a **private** extension app.
- Lifecycle: register (form or manifest) in the **Developer Console**, run connection and extension tests, run functional tests, then publish (public App Center review, or private).

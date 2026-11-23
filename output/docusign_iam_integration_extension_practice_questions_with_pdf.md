# Certified Docusign IAM Integration & Extension Developer - Practice Question Bank

Total questions: 390

Each question has an importance tag (HIGH = must know, MEDIUM = important, LOW = background), a marked trap option, and a 'why this answer and not the others' explanation.

**Q1. (API Authentication - OAuth flow selection) [HIGH]** A records office runs a server-side web portal that keeps its client secret in a server vault. Each employee signs in to Docusign interactively and sends envelopes as themselves. Which OAuth flow best fits?

A. Public Authorization Code Grant with PKCE
B. JSON Web Token Grant
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** A server that can protect a client secret plus an individual user who signs in interactively is the textbook case for Confidential Authorization Code Grant.

**Why this answer and not the others:** D is right because the portal can keep a secret and each employee is present to sign in. The trap is A: PKCE-based Public Auth Code also signs users in, but it is meant for clients that cannot store a secret, which is not the case here. B needs no user at all, and C is the legacy browser flow Docusign no longer recommends.

**Option notes:**
- A (TRAP). Public Auth Code Grant with PKCE is for SPAs and native apps that cannot hold a secret; this portal has a server vault, so the confidential variant applies.
- B. JWT Grant is for unattended service integrations that impersonate a consented user, not for employees signing in interactively.
- C. Implicit Grant is a legacy browser flow that Docusign does not recommend; a server that can hold a secret should never use it.
- D. Correct. Secret stored on a server plus an interactive user sign-in means Confidential Authorization Code Grant.

**Q2. (Go Live Process - Go-live setup) [HIGH]** A developer promotes an integration key from the developer environment to production. Which configuration must be added again on the production version of the key?

A. Redirect URIs and secret keys
B. A new integration key GUID, because the demo GUID is invalid in production
C. The integration type chosen under How will you use this integration?
D. The Account Base URI value shown on the Apps and Keys page

**Answer:** A. Redirect URIs and secret keys

**Explanation:** Go-Live duplicates the integration key into production, but configuration parameters such as secrets and redirect URIs are not copied and must be added in production.

**Why this answer and not the others:** A is right because secrets and redirect URIs are not duplicated with the key. The trap is B: the production key is a separate copy, but it keeps the same key value, so no new GUID is needed. C is chosen before Go-Live, not recreated afterwards, and D is a read-only value Docusign displays for the account, not something you configure.

**Option notes:**
- A. Correct. Secrets and redirect URIs are not copied during Go-Live and must be added to the production key.
- B (TRAP). The production key has the same value as the demo key; it is duplicated, not regenerated.
- C. The integration type is selected when the key is set up, before Go-Live; it is not re-entered in production.
- D. The Account Base URI is displayed by Docusign for the account (and returned by userinfo); you read it, you do not recreate it.

**Q3. (Docusign Connect - Envelope-level Connect) [HIGH]** One high-value envelope sent through the eSignature REST API must post its status events to a different listener URL than the account's Connect configuration. No other envelope should use that URL. What should the developer do?

A. Create a second account-level Connect configuration filtered to the sending user
B. Create an organization-level Connect configuration for the account
C. Set the envelope's notification object (reminders and expiration)
D. Add an eventNotification object to the Envelopes:create request

**Answer:** D. Add an eventNotification object to the Envelopes:create request

**Explanation:** Envelope-level Connect is configured with the eventNotification property on Envelopes:create, so the custom listener URL applies only to that one envelope. The clue is that no other envelope may use the URL.

**Why this answer and not the others:** D is right because eventNotification scopes the webhook to the single envelope being created. The trap is A: an account-level configuration filtered to one user would also fire for every other envelope that user sends. B is broader still (accounts across the org), and C confuses the notification object, which controls reminders and expiration, with eventNotification.

**Option notes:**
- A (TRAP). An account-level configuration filtered by user still covers all envelopes that user sends or receives, not one envelope.
- B. Organization-level Connect covers envelopes for all or selected accounts in the org, far wider than one envelope.
- C. The envelope notification object sets reminders and expiration for signers; it does not define a webhook.
- D. Correct. eventNotification on Envelopes:create defines an envelope-level webhook URL and events for that envelope only.

**Q4. (eSignature API - Envelope create) [HIGH]** An integration calls Envelopes:create and the recipients must receive the envelope as soon as the call succeeds. Which value should the request's status property have?

A. created
B. voided
C. completed
D. sent

**Answer:** D. sent

**Explanation:** Setting status to sent in the Envelopes:create request sends the envelope immediately. The clue is that recipients must receive it as soon as the call succeeds.

**Why this answer and not the others:** D is right because sent is the only status that delivers the envelope on creation. The trap is A: created is a valid value for the same request, but it only saves a draft. B and C are not set on create: voided cancels an in-process envelope and completed is set by Docusign when all recipients finish.

**Option notes:**
- A (TRAP). created saves the envelope as a draft; nothing is delivered until the status is later changed to sent.
- B. voided is used to cancel an envelope that is already in process; it cannot be used to deliver a new one.
- C. completed is reached by Docusign after every recipient finishes; an integration does not set it on create.
- D. Correct. status sent tells Envelopes:create to send the envelope to recipients immediately.

**Q5. (eSignature Features and Web Forms - Web Forms embedding) [HIGH]** A custom website must show a Docusign web form inline on its own page. The app has already called Instances:createInstance with a clientUserId and received the instance URL. Which client-side component renders that URL in the page?

A. An embedded signing URL from EnvelopeViews:createRecipient
B. A remote instance created with sendOption and recipients[]
C. Brand destination URLs on the account brand
D. Docusign JS client SDK

**Answer:** D. Docusign JS client SDK

**Explanation:** The app already holds the instance URL from createInstance with a clientUserId, which is the embedded pattern; Docusign JS is the client-side SDK that renders that URL inline.

**Why this answer and not the others:** D is right because Docusign JS is the documented way to embed a web form instance URL in a host page. The trap is A: embedded signing does use a recipient view URL, but that is for an envelope, and an embedded web form instance has its own URL and no envelope yet. B and C fail because a remote instance sends email links and destination URLs only redirect after signing.

**Option notes:**
- A (TRAP). EnvelopeViews:createRecipient returns a signing view for an existing envelope recipient; an embedded web form instance has no envelope until the first submit, and it already has its own instance URL.
- B. A remote instance emails participants a link; it does not render anything inline on the custom website.
- C. Destination URLs only redirect remote signers after events such as signing complete; they do not render a form.
- D. Correct. Docusign JS is the JavaScript client SDK Docusign provides to embed a web form instance URL inside a host web page.

**Q6. (Agreement Manager API - Agreement data) [HIGH]** An ERP sync job already stores the agreementId of a signed supply contract. It must copy that agreement's AI-extracted parties and provisions into the ERP. Which call should it make?

A. Agreements:getAgreementsList
B. eSignature Envelopes:get on the source envelope
C. Agreements:getAgreement
D. Agreements:createAgreementSummary

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement returns the full structured record (type, category, parties, provisions) for one agreement. The job already has the agreementId, so a direct single-record call is the right fit.

**Why this answer and not the others:** C is right because the ID is known and the job needs one agreement's extracted fields. The trap is B: the contract was signed in an eSignature envelope, but Envelopes:get returns envelope status and recipients, not Iris-extracted parties and provisions. A lists many agreements (a search step that is unnecessary here) and D produces an AI prose summary rather than structured fields.

**Option notes:**
- A. Lists agreements for the account; useful when the ID is unknown, but the job already has the agreementId.
- B (TRAP). Returns envelope metadata (status, recipients, dates), not the AI-extracted parties and provisions stored in Agreement Manager.
- C. Correct. Returns one agreement's structured, AI-extracted data, which is exactly what the ERP sync needs.
- D. Generates an AI-written summary of the agreement document, not structured field values to map into an ERP.

**Q7. (Workflow Builder and Workflow API - Workflow steps) [HIGH]** A loan intake workflow must capture applicant details on a form and use those values to fill the agreement the applicant then signs. Which step order should the workflow use?

A. Collect Data with Web Forms, then Prepare eSignature Template, then Send Documents for Signature
B. Send Documents for Signature, then Collect Data with Web Forms
C. Prepare eSignature Template, then Collect Data with Web Forms, then Send Documents for Signature
D. Collect Data with Web Forms, then a Send an Email step with the form attached

**Answer:** A. Collect Data with Web Forms, then Prepare eSignature Template, then Send Documents for Signature

**Explanation:** The form values must exist before the template step can map them into the document, and the Prepare step is followed by Send Documents for Signature. Step order must match the business process: collect, prepare, sign.

**Why this answer and not the others:** A is right because data is collected first, mapped into the template, then sent for signature. The trap is C: it uses the right steps, but preparing the template before the form runs means there are no applicant values to map yet. B sends for signature before any data exists, and D never requests a signature at all.

**Option notes:**
- A. Correct. Collect the data, prepare the template with the collected values, then send it for signature.
- B. Signing first means the agreement cannot contain the applicant's form values.
- C (TRAP). The Prepare eSignature Template step runs before the form, so the variables it should map are still empty.
- D. An email step only notifies; it does not produce a signed agreement.

**Q8. (App Center and Extension Apps - Extension app role) [HIGH]** A customer wants Docusign to call its external service (for example, to verify entered data or store completed files) during an agreement process, packaged so account admins can simply install it. What does an extension app provide?

A. A way for an external app to call eSignature APIs with an integration key
B. A Connect webhook that pushes envelope events to an external listener
C. A branded signing page hosted on the customer's own website
D. A packaged way to connect third-party service functionality into Docusign

**Answer:** D. A packaged way to connect third-party service functionality into Docusign

**Explanation:** Extension apps connect third-party services into Docusign: Docusign calls the external service through the app's actions, and admins install the app from the App Center. The clue is that Docusign must call out to the service and admins install it.

**Why this answer and not the others:** D is right because an extension app plugs external functionality into Docusign and is installed from the App Center. The trap is A: an integration key lets your app call Docusign, which is the opposite direction. B (Connect) only notifies a listener of events, and C is a signing-UI customization, neither of which is an installable package of external functionality.

**Option notes:**
- A (TRAP). An integration key lets an external app call Docusign APIs; here Docusign must call the external service, which is the reverse direction.
- B. Connect pushes event notifications outward; it does not let Docusign invoke an external service as part of the process.
- C. Branding or embedding the signing page changes the UI, not which external functionality Docusign can invoke.
- D. Correct. An extension app packages external functionality (verify, read/write data, store files) that Docusign invokes and admins install.

**Q9. (API Authentication - OAuth flow selection) [HIGH]** A financial-aid office builds a browser-only single-page application with no backend. It cannot protect a client secret, and each individual user must sign in. Which flow should the team keep?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** A browser-only SPA is a public client that cannot keep a secret, and users sign in, so Public Authorization Code Grant with PKCE is the recommended flow.

**Why this answer and not the others:** C is right because the clues are no backend, no secret, and an interactive user. The trap is D: Implicit Grant was historically used for SPAs, but it is legacy and Docusign recommends Public Auth Code with PKCE instead. A needs a secret the SPA cannot protect, and B has no user sign-in.

**Option notes:**
- A. Confidential Auth Code Grant requires a protected client secret, which a browser-only SPA cannot keep.
- B. JWT Grant is for unattended service integrations and needs a protected RSA private key; it does not sign in individual users.
- C. Correct. SPA, no secret, interactive user: Public Authorization Code Grant with PKCE.
- D (TRAP). Implicit Grant used to be the SPA answer but is legacy and not recommended; Public Auth Code with PKCE replaces it.

**Q10. (Go Live Process - Integration classification) [HIGH]** A software vendor is building an app that many Docusign customers will use with their own Docusign accounts, authorizing the app to connect to their accounts. Which integration type should the vendor choose?

A. Private custom integration
B. Third-party integration key
C. Embedded integration
D. Public integration

**Answer:** D. Public integration

**Explanation:** An app built for multiple Docusign customers who connect it to their own Docusign accounts is a Public integration (it requires joining the Docusign Partner Program).

**Why this answer and not the others:** D is right because the deciding clue is that customers use their own Docusign accounts and authorize the app. The trap is C: Embedded integration is also for vendors, but there the customers do not have their own Docusign accounts and use the vendor's account. A is for apps used by your own employees or your customers' employees, and B is for a customer who must supply its own key to a partner product.

**Option notes:**
- A. Private custom integration is for apps directly used by your own employees or your customers' employees, not a multi-customer partner app.
- B. Third-party integration key is chosen by a customer who must supply its own key to a partner integration, not by the vendor.
- C (TRAP). Embedded integration is for vendors whose customers use Docusign features through the vendor's own account, without their own Docusign accounts.
- D. Correct. A public integration serves many Docusign customers who authorize it against their own accounts.

**Q11. (Docusign Connect - Connect vs polling) [HIGH]** A system must learn as soon as recipients complete signing, without making excessive API calls. Which option should be used?

A. Poll Envelopes:get for every open envelope every minute
B. Poll each envelope once every 15 minutes as the primary status method
C. Subscribe to Connect events
D. Rely on the completion email sent to the envelope sender

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes a message only when something changes, so the system learns of completions immediately and spends no API calls checking.

**Why this answer and not the others:** C is right because a webhook delivers the event when it happens and does not consume API calls. The trap is B: polling every 15 minutes per envelope respects the polling limit, but it still burns calls and can be up to 15 minutes late. A violates the polling limit outright, and D relies on a human-facing email that a system cannot use reliably.

**Option notes:**
- A. Polling every minute violates the once-per-15-minutes-per-envelope limit and can fail Go-Live review.
- B (TRAP). Compliant polling still uses API calls for unchanged envelopes and adds up to 15 minutes of delay.
- C. Correct. Connect pushes events when they occur, with no polling calls.
- D. Completion emails go to people, not systems, and are not an integration mechanism.

**Q12. (eSignature API - Draft envelope) [HIGH]** A developer wants to create an envelope now and send it later, after an internal reviewer approves it. Which status value should the Envelopes:create request use?

A. sent
B. draft
C. created
D. completed

**Answer:** C. created

**Explanation:** status created builds the envelope without sending it, leaving a draft that can be sent later. The clue is 'create now, send later'.

**Why this answer and not the others:** C is right because created is the API value for a draft envelope. The trap is B: the envelope is called a draft, but draft is not a valid status value. A would send immediately and D is set by Docusign after all recipients finish.

**Option notes:**
- A. sent delivers the envelope immediately, before the reviewer can approve it.
- B (TRAP). draft describes the result, but it is not the status value; the API expects created.
- C. Correct. status created saves the envelope as a draft so it can be sent later.
- D. completed is a terminal status set by Docusign after all recipients finish.

**Q13. (eSignature Features and Web Forms - Web Form correlation) [HIGH]** An app creates one embedded web form instance per customer record and must map each instance back to that record. Which createInstance value carries your system's own user identifier?

A. The formId of the web form configuration
B. The envelopeId of the generated envelope
C. clientUserId
D. The instance URL

**Answer:** C. clientUserId

**Explanation:** clientUserId is the value your app supplies to tie the embedded instance to its own user or record.

**Why this answer and not the others:** C is right because clientUserId is your own identifier, supplied on createInstance. The trap is A: it is a real Web Forms ID, but it identifies the shared form configuration, not an individual customer. B and D fail because the envelope does not exist yet when an embedded instance is created and the instance URL is a Docusign-generated rendering URL.

**Option notes:**
- A (TRAP). The formId identifies the configuration that every instance is created from, so it is the same for all customers and cannot identify one record.
- B. For an embedded instance the envelope is only created when the first user submits, so there is no envelopeId at creation time (and standalone forms never have one).
- C. Correct. clientUserId is a value you choose to identify the user in your system (max 100 characters), and it is required for embedded instances.
- D. The instance URL is what Docusign JS renders; it is generated by Docusign, not a value you supply from your records.

**Q14. (Agreement Manager API - Agreement list) [HIGH]** A renewals app must find all NDAs expiring this quarter, then show the full extracted data for the one the user selects. The app does not know any agreementId in advance. Which approach fits?

A. Call Agreements:getAgreement with the expiration criteria as parameters
B. Call Agreements:getAgreementsList to find matches, then Agreements:getAgreement for the selected one
C. Call eSignature Envelopes:listStatusChanges filtered by completed date
D. Call Agreements:createAgreementSummary on every agreement in the account

**Answer:** B. Call Agreements:getAgreementsList to find matches, then Agreements:getAgreement for the selected one

**Explanation:** The app has criteria but no agreementId, so it first lists or searches agreements with getAgreementsList and then calls getAgreement for the chosen record.

**Why this answer and not the others:** B is right because search comes first when the ID is unknown, then the detail call. The trap is A: getAgreement does return the full extracted data, but it needs a specific agreementId in the path and does not search by criteria. C finds completed envelopes, not agreements with extracted expiration dates, and D creates AI summaries rather than filtering agreements.

**Option notes:**
- A (TRAP). getAgreement requires a specific agreementId; it is not a search operation.
- B. Correct. List or search agreements first, then retrieve the detailed record for the selected agreement.
- C. Returns envelope status changes; it does not filter on AI-extracted agreement fields such as expiration date.
- D. Produces AI summaries one agreement at a time; it neither filters nor returns structured fields.

**Q15. (Workflow Builder and Workflow API - Identity step) [MEDIUM]** In a US new-hire workflow, the new hire has already submitted a web form. Next, the new hire must be invited to complete identity verification themselves. Which step sequence matches the Workflow Builder onboarding pattern?

A. Verify Someone's Identity, then Set Up Invite
B. Send an Email step, then Send Documents for Signature
C. Show a Confirmation Screen, then Verify Someone's Identity
D. Set Up Invite, then Verify Someone's Identity

**Answer:** D. Set Up Invite, then Verify Someone's Identity

**Explanation:** In the course onboarding example, a Set Up Invite step invites the new hire, and the Verify Someone's Identity step follows it. The invite must come first so the participant can reach the verification step.

**Why this answer and not the others:** D is right because the participant is invited first and then completes the identity step. The trap is A: it uses the same two steps but in reverse, so the verification would run before the new hire was invited to it. B skips verification entirely, and C only shows a screen; it does not invite the participant.

**Option notes:**
- A (TRAP). Reversed order: the participant cannot complete verification before being invited to it.
- B. An email notification followed by signing skips the required identity verification.
- C. A confirmation screen displays a message; it does not invite a participant to act.
- D. Correct. Set Up Invite routes the new hire to the workflow, then Verify Someone's Identity runs.

**Q16. (App Center and Extension Apps - Public vs private) [HIGH]** An extension app will be used only by one organization's own Docusign production accounts and must not be installable by other customers. Which distribution is appropriate?

A. Public app with publicationRegions limited to the organization's region
B. Leave the approved app in the developer account
C. Private extension app shared with the organization's production accounts
D. Public app installed only by admins who know its App ID

**Answer:** C. Private extension app shared with the organization's production accounts

**Explanation:** Private distribution limits installation to a specific list of production accounts, which matches an app meant for one organization only.

**Why this answer and not the others:** C is right because private distribution restricts installation to listed production accounts. The trap is A: publicationRegions restricts geography for public apps, so any customer in that region could still install it. B keeps the app in the demo developer account only, and D is not a real access control because public apps are available to all App Center users.

**Option notes:**
- A (TRAP). publicationRegions limits regions, not organizations; any customer in the region could install a public app.
- B. Before publishing, an app is usable only in the developer account in demo, not in the organization's production accounts.
- C. Correct. Private distribution lets only the listed production accounts install the app.
- D. Public apps are available to all App Center users; knowing an App ID is not an access restriction.

**Q17. (API Authentication - JWT Grant) [HIGH]** A partner vendor's scheduled service runs nightly on a secure server, sending envelopes from a dedicated system sender account. No person is present to sign in. Which option is correct?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** No user is present, so JWT Grant is the fit: the service signs an assertion with its RSA private key and impersonates the consented system user.

**Why this answer and not the others:** B is right because the deciding clue is that nobody is present to sign in. The trap is A: the secure server could store a secret, but Confidential Auth Code still needs a user to sign in through a browser. C and D are also interactive browser flows.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant fits servers that store a secret, but it still requires an interactive user sign-in.
- B. Correct. Unattended service using a system user after consent is JWT Grant.
- C. Public Auth Code Grant with PKCE is an interactive flow for clients without a secret, not an unattended job.
- D. Implicit Grant is a legacy interactive browser flow and cannot run unattended.

**Q18. (Go Live Process - Production endpoints) [MEDIUM]** After Go-Live, an eSignature app authenticates in production but its API calls still go to https://demo.docusign.net/restapi and fail. What must be changed?

A. Keep the demo host but send the production access token with each call
B. Hardcode https://www.docusign.net/restapi for every production account
C. Call the account's production base URI (from userinfo) instead of the demo host
D. Generate a new integration key so that calls are routed to production

**Answer:** C. Call the account's production base URI (from userinfo) instead of the demo host

**Explanation:** Production API calls must use the account's base URI, which you obtain from the userinfo endpoint (for example https://{server}.docusign.net/restapi), instead of demo.docusign.net.

**Why this answer and not the others:** C is right because production accounts live on a specific server whose base URI comes from userinfo. The trap is B: it does use a production host, but hardcoding one server breaks accounts that live on other data centers (NA2, EU, CA and so on). A mixes a production token with the demo host, and D is unnecessary because the key keeps the same value in production.

**Option notes:**
- A. A production token is not valid against the demo host; the host itself must change.
- B (TRAP). Production accounts sit on different servers, so a single hardcoded host fails for many accounts; use the base_uri from userinfo.
- C. Correct. The production base URI comes from the userinfo response (or the Account Base URI on Apps and Keys).
- D. The production key has the same value as the demo key; the routing problem is the host, not the key.

**Q19. (Docusign Connect - Configuration level) [HIGH]** A company wants one webhook configuration that receives events for envelopes across all accounts in its Docusign organization. What should the Connect configuration be?

A. An account-level Connect configuration in each account
B. Organization-level Connect
C. eventNotification on every envelope
D. An account-level configuration in the primary account only

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect covers envelopes sent or received by all or selected accounts in the organization from a single configuration.

**Why this answer and not the others:** B is right because only an org-level configuration spans multiple accounts at once. The trap is A: one account-level configuration per account would deliver the events, but it is several configurations to maintain, not the single webhook requested. C only covers API-sent envelopes and must be repeated on each one, and D misses every other account.

**Option notes:**
- A (TRAP). Works, but requires a separate configuration in every account instead of one org-wide configuration.
- B. Correct. Organization-level Connect covers all or selected accounts in the organization.
- C. eventNotification covers only API-sent envelopes, one envelope at a time.
- D. An account-level configuration sees only its own account's envelopes.

**Q20. (eSignature API - Cancel envelope) [MEDIUM]** A sent envelope contains a fatal error and no one should sign it. The integration must cancel it permanently. Which status should it set?

A. created
B. voided
C. declined
D. deleted

**Answer:** B. voided

**Explanation:** Voiding (status voided with a voidedReason) permanently cancels an in-process envelope and stops signing. The clue is a sent envelope that must be canceled permanently.

**Why this answer and not the others:** B is right because voided is the documented way to cancel an envelope that is in process. The trap is D: deleting sounds permanent, but it is not how the sender cancels an in-process envelope. A only applies to drafts and C is an action a recipient takes, not one the sender sets.

**Option notes:**
- A. created describes a draft; it does not cancel an envelope that is already sent.
- B. Correct. status voided permanently cancels the in-process envelope so no one can sign it.
- C. declined is recorded when a recipient refuses to sign; the sender does not set it to cancel.
- D (TRAP). deleted is not the documented cancel action for an in-process envelope; voiding is.

**Q21. (eSignature Features and Web Forms - Identity verification) [HIGH]** A public-sector records office requires signers to prove their identity with a government-issued photo ID before they can sign. What must be added to each signer in the Envelopes:create request?

A. authenticationMethod on the EnvelopeViews:createRecipient call
B. An identityVerification object with the account's IDV workflowId
C. An accessCode on the recipient
D. A clientUserId on the recipient

**Answer:** B. An identityVerification object with the account's IDV workflowId

**Explanation:** A government photo ID check before signing is ID verification, configured with identityVerification.workflowId on the recipient.

**Why this answer and not the others:** B is right because IDV is enforced per recipient with identityVerification.workflowId. The trap is A: it is identity-related and appears on the certificate, but it only records your app's own authentication and enforces nothing. C and D fail because an access code checks a shared secret, not an ID, and clientUserId only controls embedded signing.

**Option notes:**
- A (TRAP). authenticationMethod only records on the certificate how your app authenticated the user; it does not enforce any identity check.
- B. Correct. ID verification is enforced by adding identityVerification.workflowId (from IdentityVerifications:list, REST v2.1) to the recipient.
- C. An access code is a shared secret entered by the recipient; it does not check a government photo ID.
- D. clientUserId makes the recipient an embedded signer; it adds no identity verification.

**Q22. (Agreement Manager API - Legacy import) [MEDIUM]** A real-estate company has thousands of signed leases that were never sent through Docusign. It wants them in Agreement Manager with AI-extracted data like any other agreement. Which capability fits?

A. Bulk import the legacy agreements into Agreement Manager
B. Re-send each lease as a new eSignature envelope
C. Agreements:getAgreementsList
D. Store key lease terms as envelope custom fields

**Answer:** A. Bulk import the legacy agreements into Agreement Manager

**Explanation:** Agreement Manager supports bulk import of existing, non-Docusign agreements, and AI extraction runs on imported agreements just as on completed envelopes.

**Why this answer and not the others:** A is right because import brings the existing files into the repository where Iris extracts their data. The trap is B: completed envelopes do flow into Agreement Manager, but re-sending already-signed leases is unnecessary and creates new signing events. C only reads agreements already in the repository, and D stores data on envelopes, not in Agreement Manager.

**Option notes:**
- A. Correct. Bulk import adds legacy agreements to Agreement Manager so AI extraction can run on them.
- B (TRAP). Already-signed leases do not need to be re-signed; import is the intended path for legacy contracts.
- C. Reads agreements already in Agreement Manager; it cannot add the legacy leases.
- D. Envelope custom fields are eSignature metadata and do not create agreement records.

**Q23. (Workflow Builder and Workflow API - Extension step) [HIGH]** After the signing step, a contracts workflow must save the completed agreement to the company's Box account. The Box extension app is already installed. Which step should be added?

A. A Send an Email step that mails the document to a shared inbox
B. A Read step from an extension app
C. A Store Files extension app step placed after Send Documents for Signature
D. A Store Files extension app step placed before Send Documents for Signature

**Answer:** C. A Store Files extension app step placed after Send Documents for Signature

**Explanation:** Store Files app steps automate storage of completed agreements in services such as Box or Google Drive. It must come after the signing step so the stored file is the completed agreement.

**Why this answer and not the others:** C is right because Store Files is the app-step category for saving documents, and it runs after signing. The trap is D: correct step type, wrong position, so it would store the unsigned document. A only emails the file, and B imports data from an external system rather than saving files to it.

**Option notes:**
- A. Emailing a document is not archiving it in Box.
- B. Read steps import data into the workflow; they do not save files externally.
- C. Correct. A Store Files step after signing saves the completed agreement to Box.
- D (TRAP). Placed before signing, it would save a document that has not been signed yet.

**Q24. (App Center and Extension Apps - Connections) [HIGH]** Within the actions object of the manifest, what is the primary purpose of the connectionsReference property?

A. It specifies the OAuth scopes required by the external API
B. It indicates whether the app is PUBLIC or PRIVATE
C. It defines the endpoint URL for the external API call
D. It links the action to authentication defined in the connections object

**Answer:** D. It links the action to authentication defined in the connections object

**Explanation:** connectionsReference points an action to a named connection, so the action uses that connection's authentication.

**Why this answer and not the others:** D is right because connectionsReference ties an action to a connection's auth settings. The trap is A: scopes are configured in the connection itself, not in the reference. B is the distribution property, and C is part of the action's own endpoint definition.

**Option notes:**
- A (TRAP). Scopes are part of the connection's auth configuration, not the reference.
- B. PUBLIC or PRIVATE is set by the distribution property.
- C. The endpoint is defined by the action; connectionsReference only points to auth.
- D. Correct. It links the action to the authentication declared in a named connection.

**Q25. (API Authentication - Consent) [HIGH]** A JWT integration's token request fails with consent_required. The impersonated user has never granted consent for the requested scopes. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and requested scopes
B. A newly generated RSA key pair for the integration key
C. A client secret added to the JWT token request
D. Production approval (Go-Live) for the integration key

**Answer:** A. Individual or admin consent for the integration key and requested scopes

**Explanation:** JWT Grant only issues tokens after the impersonated user, or an admin on their behalf, has consented to the integration key and its scopes; consent_required means that step is missing.

**Why this answer and not the others:** A is right because the error and the stem both point to missing consent. The trap is B: key problems also break JWT requests, but a new RSA key pair does not grant consent. C is not part of JWT Grant, and D is about promoting the key to production, not about consent.

**Option notes:**
- A. Correct. JWT needs individual or admin consent for the integration key and scopes before tokens are issued.
- B (TRAP). A new RSA key pair fixes signing problems, but the user would still not have consented.
- C. JWT Grant authenticates with an RSA-signed assertion; a client secret is not used and does not grant consent.
- D. Go-Live promotes the key to production; it does not record consent from the impersonated user.

**Q26. (Go Live Process - Templates in production) [HIGH]** After Go-Live, an app that creates envelopes from a server template fails in production with a template-not-found error. It still sends the templateId it used in the developer account. What is the fix?

A. Wait for the Go-Live review to finish copying the developer templates
B. Create the template in the production account and use its production templateId
C. Keep the same templateId and only switch the base URI to production
D. Switch the app to composite templates, because server templates are demo-only

**Answer:** B. Create the template in the production account and use its production templateId

**Explanation:** Production account data is separate from the developer account, so templates must be created in production, and they get new production template IDs.

**Why this answer and not the others:** B is right because templates are not migrated by Go-Live and production templates have their own IDs. The trap is C: switching the base URI is also required after Go-Live, but the demo templateId still does not exist in the production account. A is wrong because Go-Live only duplicates the integration key, and D is wrong because server templates work in production.

**Option notes:**
- A. Go-Live duplicates only the integration key; templates are never copied by the review.
- B. Correct. Recreate or migrate the template in production and reference its new production templateId.
- C (TRAP). The base URI change is needed, but the demo templateId does not exist in the production account.
- D. Server templates are fully supported in production; there is no need to change the request model.

**Q27. (Docusign Connect - JSON SIM) [HIGH]** A listener must receive Connected Fields verification results, which Docusign delivers through the extension-executed event. Which Connect message format must the configuration use?

A. JSON SIM (Connect 2.0) format
B. Legacy XML SIM format
C. XML aggregate mode
D. SOAP messages using the eSignature SOAP object model

**Answer:** A. JSON SIM (Connect 2.0) format

**Explanation:** The extension-executed event, which carries Connected Fields verification results, is available only with the JSON SIM format.

**Why this answer and not the others:** A is right because extension-executed is a JSON SIM-only event. The trap is B: XML SIM also sends individual messages, but it is the legacy format and does not offer this event. C and D are other legacy XML options that are envelope-focused and also lack the event.

**Option notes:**
- A. Correct. extension-executed is available only with JSON SIM.
- B (TRAP). Legacy XML SIM sends individual messages but does not provide the extension-executed event.
- C. Aggregate mode is a legacy XML option and does not deliver extension-executed.
- D. SOAP-style XML messages are the legacy format; the event is JSON SIM only.

**Q28. (eSignature API - Idempotency) [LOW]** A network retry might submit the same create-envelope request twice. Which sender-supplied value on the envelope helps the app avoid creating a duplicate?

A. transactionId
B. recipientId
C. batchId
D. envelopeId

**Answer:** A. transactionId

**Explanation:** transactionId is a sender-generated value on the envelope definition that lets the app recognize whether an earlier create request already produced the envelope. The clue is 'sender-supplied'.

**Why this answer and not the others:** A is right because transactionId is the value the sender generates to identify the create attempt. The trap is D: envelopeId identifies the envelope, but Docusign generates it and only returns it after a successful create. B identifies a recipient within an envelope and C identifies a bulk send batch.

**Option notes:**
- A. Correct. A sender-generated transactionId lets the app detect a create request that already succeeded.
- B. recipientId identifies a recipient within one envelope; it says nothing about duplicate envelopes.
- C. batchId is returned when a bulk send is initiated; it tracks a batch, not a single create retry.
- D (TRAP). envelopeId is generated by Docusign and returned only after success, so the client cannot supply it for a retry.

**Q29. (eSignature Features and Web Forms - Recipient authentication) [HIGH]** A university financial-aid office wants Docusign to send each signer a one-time code by text message, which the signer must enter before opening the envelope. Which recipient authentication method fits?

A. Phone authentication (code by SMS or voice call)
B. Access code
C. Knowledge-based authentication (KBA)
D. authenticationMethod recorded on createRecipient

**Answer:** A. Phone authentication (code by SMS or voice call)

**Explanation:** The clue is a one-time code that Docusign sends by text message, which is phone authentication.

**Why this answer and not the others:** A is right because phone authentication delivers a code by SMS or voice before the recipient can access the envelope. The trap is B: it is also a code the signer types, but the sender sets it and shares it out of band. C and D fail because KBA uses public-record questions and authenticationMethod only records authentication.

**Option notes:**
- A. Correct. Phone authentication sends the recipient a code by SMS or call that must be entered before access; it is configured with an identityVerification workflowId.
- B (TRAP). An access code is chosen by the sender and shared out of band; Docusign does not generate and text it as a one-time code.
- C. KBA asks public-record questions (US only); it does not send a code.
- D. This only records your app's own authentication on the certificate and enforces nothing.

**Q30. (Agreement Manager API - Agreement documents) [MEDIUM]** A pull request syncs agreements to a records system that must keep a copy of each agreement file, not only its extracted fields. The code calls only Agreements:getAgreement. What should the plan add?

A. Nothing; Agreements:getAgreement already returns the document file content
B. A call to Agreements:getAgreementsList for the same agreement
C. A call to Agreements:createAgreementSummary to produce the stored copy
D. A separate document download step for the agreement file

**Answer:** D. A separate document download step for the agreement file

**Explanation:** getAgreement returns structured JSON (type, parties, provisions), not the document file. A records system that needs the file itself needs a separate document download step.

**Why this answer and not the others:** D is right because extracted data and the document file are different things. The trap is A: getAgreement does return the full agreement record, but that record is metadata and extracted values, not the PDF. B returns list-level agreement data, and C returns an AI-written summary, which is not a copy of the agreement.

**Option notes:**
- A (TRAP). getAgreement returns structured metadata and extracted values, not the agreement file itself.
- B. The list call returns agreement records for many agreements, not the document file.
- C. An AI summary is generated text, not a copy of the signed agreement.
- D. Correct. The file must be retrieved with a separate document download, in addition to the extracted data.

**Q31. (Workflow Builder and Workflow API - Branching) [HIGH]** On a web form, applicants choose 'Individual' or 'Business'. A separate eSignature template already exists for each type. What should follow the form step?

A. Two Collect Data with Web Forms steps in sequence
B. A Branching Rule step on the applicant-type field, with its own Prepare and Send steps on each path
C. One Prepare eSignature Template step that always uses the Individual template
D. A Show a Confirmation Screen step asking the applicant which agreement to sign

**Answer:** B. A Branching Rule step on the applicant-type field, with its own Prepare and Send steps on each path

**Explanation:** Branching rules route the workflow down different paths based on a condition, here the form field. Each path then prepares and sends its own template.

**Why this answer and not the others:** B is right because the form answer decides which template is used, and that is what a branching rule does. The trap is C: Prepare eSignature Template is meant for one template used by every instance, which does not fit two applicant types. A only collects more data, and D shows a message; neither routes the process.

**Option notes:**
- A. A second form collects more data but does not route to a different agreement.
- B. Correct. The branching rule evaluates the form value and routes each applicant type to its own template.
- C (TRAP). A single fixed template ignores the applicant type, so business applicants get the wrong agreement.
- D. A confirmation screen displays information; it cannot branch the workflow.

**Q32. (App Center and Extension Apps - Public App Center) [MEDIUM]** A partner wants Docusign customers broadly to discover and install its app. Which distribution should it choose?

A. Private extension app
B. Public extension app published to the Docusign App Center
C. Private app shared with every customer's account ID
D. Send customers the manifest file to upload into their own accounts

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public distribution makes the app available to all App Center users, which is what broad discovery and installation require.

**Why this answer and not the others:** B is right because public apps are listed for all customers in the App Center. The trap is C: private sharing works from a predefined list of production accounts and cannot realistically cover every customer. A restricts installation, and D does not work because customers install apps from the App Center, not by uploading a manifest.

**Option notes:**
- A. Private apps are limited to specific accounts, so customers cannot broadly discover them.
- B. Correct. A public app in the App Center can be discovered and installed by all customers.
- C (TRAP). Private sharing uses a limited list of production accounts; it is not a broad distribution model.
- D. Manifests are uploaded by the developer in the Developer Console; customers install from the App Center.

**Q33. (API Authentication - Scopes) [MEDIUM]** A web app uses Confidential Authorization Code Grant (users sign in) and only needs to send eSignature envelopes and read the user's account information. Which scopes should it request at consent?

A. signature impersonation
B. Every available scope, to avoid re-consent later
C. No scopes; Docusign infers permissions from the API calls
D. Only the minimum needed for those calls, such as signature

**Answer:** D. Only the minimum needed for those calls, such as signature

**Explanation:** Least privilege: request only the scopes the API calls need; signature covers most eSignature actions for a signed-in user.

**Why this answer and not the others:** D is right because the app's calls only need eSignature access for a signed-in user. The trap is A: signature impersonation is the standard JWT consent, but impersonation is unnecessary when the user signs in directly. B over-requests, and C fails because scopes must be requested explicitly.

**Option notes:**
- A (TRAP). impersonation is for JWT Grant acting as a user; a signed-in Auth Code user does not need it.
- B. Requesting every scope breaks least privilege and makes the consent screen broader than needed.
- C. Docusign does not infer permissions; scopes must be listed on the consent request.
- D. Correct. Request only the scopes the operations need, here signature.

**Q34. (Go Live Process - Post go-live) [HIGH]** An integration key that uses Confidential Authorization Code Grant has just gone live. Which settings must the developer add to the production version of the key?

A. Secret key and redirect URIs
B. An RSA key pair only
C. A new integration key GUID
D. Nothing, because the developer key's settings apply in production

**Answer:** A. Secret key and redirect URIs

**Explanation:** For Authorization Code Grant apps, the After Go-Live guidance says to add redirect URIs and secrets on the production key, because they are not copied from the developer environment.

**Why this answer and not the others:** A is right because the clue is Confidential Authorization Code Grant, which needs a secret and redirect URIs. The trap is B: an RSA key pair is what JWT Grant apps add in production, not Authorization Code Grant apps. C is wrong because the key keeps its value, and D is wrong because production OAuth settings are separate from developer settings.

**Option notes:**
- A. Correct. Authorization Code Grant needs a secret key and redirect URIs, which must be added in production.
- B (TRAP). RSA key pairs are the JWT Grant credential; a Confidential Authorization Code Grant app needs a secret.
- C. The production key keeps the same value as the demo key.
- D. Production OAuth settings are separate from the developer account's settings; nothing carries over.

**Q35. (Docusign Connect - Security) [HIGH]** A listener must verify that each incoming webhook message really came from Docusign and was not altered in transit. Which control does this?

A. Check that the payload's envelopeId exists in the account
B. Rely on the listener's HTTPS certificate alone
C. Use a long, unguessable listener URL path
D. Validate the HMAC signature in the X-DocuSign-Signature-1 header

**Answer:** D. Validate the HMAC signature in the X-DocuSign-Signature-1 header

**Explanation:** With HMAC security, Docusign hashes the message body with a shared secret key and sends it in X-DocuSign-Signature headers, proving both authenticity and integrity.

**Why this answer and not the others:** D is right because only the HMAC check proves the sender knew the shared key and the body is unchanged. The trap is B: HTTPS is required and encrypts the traffic, but the listener's certificate proves the listener's identity, not that the caller is Docusign. A and C rely on values an attacker could obtain or guess.

**Option notes:**
- A. Anyone who knows an envelope ID can put it in a forged payload.
- B (TRAP). HTTPS encrypts traffic and authenticates the listener, not the sender.
- C. A hidden URL is obscurity, not authentication; it can leak.
- D. Correct. Recomputing the HMAC with the shared key verifies authenticity and integrity.

**Q36. (eSignature API - Template reference) [HIGH]** An envelope request uses a server template already stored in Docusign (template reference model). Which value identifies that template?

A. compositeTemplates with an inlineTemplate
B. anchorString with offsets
C. roleName in templateRoles
D. templateId

**Answer:** D. templateId

**Explanation:** In the template reference model, templateId identifies the saved template and templateRoles map recipients into its roles.

**Why this answer and not the others:** D is right because templateId is the reference to the stored template. The trap is C: roleName is part of the same request, but it maps recipients to roles and does not identify the template. A is a different envelope model and B places tabs relative to document text.

**Option notes:**
- A. compositeTemplates is a different envelope model; an inlineTemplate supplies runtime data, not a stored template ID.
- B. anchorString with offsets positions tabs relative to text; it does not reference a template.
- C (TRAP). roleName in templateRoles matches a recipient to a template role; it does not say which template to use.
- D. Correct. templateId references the template stored in Docusign.

**Q37. (eSignature Features and Web Forms - Brand destination URLs) [MEDIUM]** Maya's partner app sends envelopes for remote signing (signers open them from email). After finishing, signers must land on the vendor's own page. Which feature controls this?

A. returnUrl in EnvelopeViews:createRecipient
B. Docusign JS sessionEnd event handler
C. A Connect webhook
D. Brand destination URLs

**Answer:** D. Brand destination URLs

**Explanation:** The clue is remote signing; post-signing redirects for remote signers are set with brand destination URLs.

**Why this answer and not the others:** D is right because destination URLs on a brand control where remote signers go after signing. The trap is A: it is the redirect setting for embedded signing, which does not apply to remote signers. B and C fail because the sessionEnd handler only exists in an embedded session and Connect is server-to-server.

**Option notes:**
- A (TRAP). returnUrl sets the post-session redirect for embedded signing only; remote signers opening email links never go through createRecipient.
- B. This event handler runs in your page during embedded signing; it does not apply to remote signers.
- C. Connect notifies your server of events; it cannot redirect the signer's browser.
- D. Correct. A brand's destination URLs set where remote signers are redirected after events such as signing complete.

**Q38. (Agreement Manager API - Agreement data) [HIGH]** An app displays the legal provisions in use across the organization's agreements and reads its data from the Agreement Manager API. What is the key advantage over the eSignature REST API for this purpose?

A. The Agreement Manager API is exempt from API rate limits
B. eSignature form data holds the same provisions; Agreement Manager is just faster
C. It returns structured, AI-extracted data such as parties and provisions
D. It uses a separate token type unrelated to eSignature OAuth

**Answer:** C. It returns structured, AI-extracted data such as parties and provisions

**Explanation:** Agreement Manager (Iris) extracts parties, dates and provisions from agreements and the API exposes them as structured data. The eSignature API exposes envelopes and tab values, not extracted provisions.

**Why this answer and not the others:** C is right because AI-extracted provisions are what the app displays. The trap is B: eSignature form data does return values signers typed into tabs, but those are not the clause-level provisions Iris extracts from the document text. A is false because API rate limits still apply, and D is false because Agreement Manager uses the same OAuth tokens as eSignature, with Agreement Manager scopes added.

**Option notes:**
- A. False; Agreement Manager calls are still subject to API limits.
- B (TRAP). Form data contains tab values entered during signing, not provisions extracted from the agreement text.
- C. Correct. The API returns AI-extracted structured data such as parties and provisions.
- D. False; the same OAuth tokens are used, with Agreement Manager scopes such as adm_store_unified_repo_read requested.

**Q39. (Workflow Builder and Workflow API - Start method) [HIGH]** A marketing website has no server-side code. Site visitors, who have no Docusign accounts, must be able to start a client intake workflow themselves by clicking a button. Which start method fits?

A. From a link
B. Manually in Docusign (Run Workflow)
C. From an API call
D. Triggered from a CLM workflow

**Answer:** A. From a link

**Explanation:** From a link gives a URL that starts the workflow when opened. It can be embedded in a website and is recommended for self-service intake initiated by a participant.

**Why this answer and not the others:** A is right because a visitor opening the link starts the workflow, with no backend involved. The trap is C: From an API call also starts workflows from outside Docusign, but it requires server code with an OAuth token, which this site does not have. B needs an internal user with Workflows: Prepare permission, and D is started from inside Docusign CLM.

**Option notes:**
- A. Correct. The workflow link can be embedded in the site so participants start it themselves.
- B. Run Workflow is used by internal users with Workflows: Prepare permission, not by anonymous visitors.
- C (TRAP). An API trigger needs backend code holding an access token; the site has no server side.
- D. A CLM-triggered start runs from within Docusign CLM, not from a public website.

**Q40. (App Center and Extension Apps - Manifest) [HIGH]** An extension app action must call an external API endpoint. Where in the manifest is that endpoint described?

A. In an action definition in the manifest's actions object
B. In the extensions object's actionReferences list
C. In the App Center listing description
D. In the connections object, next to the OAuth settings

**Answer:** A. In an action definition in the manifest's actions object

**Explanation:** Each action in the actions object describes an external operation, including the endpoint Docusign calls.

**Why this answer and not the others:** A is right because actions hold the callable operations and their endpoints. The trap is D: connections hold authentication details (such as token and authorization URLs), not the operation's endpoint. B only lists action names for an extension, and C is listing text for the App Center.

**Option notes:**
- A. Correct. The action definition describes the external endpoint Docusign calls.
- B. actionReferences only points to actions by name; it does not define endpoints.
- C. Listing text is marketing content shown in the App Center, not configuration for calls.
- D (TRAP). Connections define how to authenticate (OAuth URLs, credentials), not the operation endpoint.

**Q41. (API Authentication - User info) [HIGH]** After receiving an access token, the app must find which account ID and base URI to use for API calls. Which endpoint returns that account context?

A. /oauth/token
B. eSignature Accounts:get (/restapi/v2.1/accounts/{accountId})
C. /oauth/userinfo
D. The sub claim of the JWT assertion

**Answer:** C. /oauth/userinfo

**Explanation:** /oauth/userinfo returns the user's accounts; the app uses the account with is_default=true and takes its account_id and base_uri for every API URL.

**Why this answer and not the others:** C is right because userinfo is the discovery step after any OAuth flow. The trap is B: Accounts:get returns account details, but you already need the account ID and base URI to call it. A returns the token itself, and D is the user ID the app supplies in a JWT, not account context.

**Option notes:**
- A. /oauth/token returns the access token and its lifetime, not the account list or base URIs.
- B (TRAP). Accounts:get needs the account ID and base URI in its URL, so it cannot be how you discover them.
- C. Correct. /oauth/userinfo returns accounts with account_id, base_uri, and is_default.
- D. sub is the user ID the app puts in the JWT; it identifies the user, not the account or base URI.

**Q42. (Go Live Process - API limits) [HIGH]** An integration checks envelope status by polling each envelope every few seconds. Which change best follows Docusign API usage guidelines?

A. Poll each envelope every 60 seconds instead
B. Ask Docusign to raise the account's hourly API limit
C. Spread the polling across several integration keys
D. Use Connect webhooks to receive status changes

**Answer:** D. Use Connect webhooks to receive status changes

**Explanation:** Docusign recommends Connect so status changes are pushed to the app instead of polled; polling a single envelope is limited to once every 15 minutes.

**Why this answer and not the others:** D is right because Connect removes the need to poll. The trap is A: it reduces the call rate, but polling every minute still breaks the rule of at most one status request per envelope every 15 minutes. B treats the symptom instead of the inefficient pattern, and C does not help because the hourly limit is shared by all integrations on the account.

**Option notes:**
- A (TRAP). Every 60 seconds still exceeds the limit of one status poll per envelope every 15 minutes.
- B. A higher limit does not fix inefficient polling, and limit increases require efficient apps.
- C. The hourly limit is per account and shared by all keys, so more keys add no capacity.
- D. Correct. Connect pushes envelope events, which avoids excessive status polling.

**Q43. (Docusign Connect - Retries) [MEDIUM]** A Connect listener is down for 20 minutes during maintenance while envelopes are completing. What happens to the events Docusign tried to send?

A. They are lost; the app must poll to recover them
B. Docusign holds the envelopes until the listener is back
C. Docusign treats each delivery as failed and retries it later
D. Docusign switches to emailing the events to the account admin

**Answer:** C. Docusign treats each delivery as failed and retries it later

**Explanation:** Failed Connect deliveries are retried with exponential back-off, so events sent during a short outage are delivered once the listener responds again.

**Why this answer and not the others:** C is right because Connect has a built-in retry process for failed deliveries. The trap is A: polling with listStatusChanges is a valid catch-up tool, but events are not simply lost, because Connect retries them. B and D describe behavior Connect does not have; envelope processing continues regardless of the listener.

**Option notes:**
- A (TRAP). Events are retried, not discarded; polling is only a fallback for catch-up.
- B. Envelope signing is not paused because a listener is down.
- C. Correct. Connect retries failed deliveries using exponential back-off.
- D. Connect does not reroute events to email when the listener fails.

**Q44. (eSignature API - Cancel envelope) [HIGH]** An agreement was sent with the eSignature REST API. Before anyone signs, legal finds a fatal error and the agreement must be canceled permanently. Which status should the integration set in an Envelopes:update request?

A. voided
B. created
C. purged
D. deleted

**Answer:** A. voided

**Explanation:** Setting status to voided (with a voidedReason) in Envelopes:update cancels the in-process envelope, stops signing and notifies recipients.

**Why this answer and not the others:** A is right because voided is the cancel action for an envelope in process. The trap is D: deleted sounds like cancellation, but it is not the documented way to cancel a sent envelope. B is the draft status and C refers to removing documents after completion, not stopping signing.

**Option notes:**
- A. Correct. status voided with a voidedReason permanently cancels the in-process envelope.
- B. created is the draft status; it does not cancel an envelope that has been sent.
- C. Purging removes document content from completed envelopes; it does not stop an in-process envelope.
- D (TRAP). deleted is not the documented cancel action for an in-process envelope; voiding is.

**Q45. (eSignature Features and Web Forms - Web Forms embedding) [HIGH]** Robin is integrating a financial aid web form into a university website and wants the form to appear directly inside the site's UI. Which component must Robin use alongside the Web Forms API call to render the instance URL within the custom page?

A. The eSignature REST API EnvelopeViews:createRecipient endpoint
B. The Docusign JS client SDK
C. The Responsive Signing feature
D. A Workflow Builder 'From a link' start URL

**Answer:** B. The Docusign JS client SDK

**Explanation:** Docusign provides the Docusign JS client SDK alongside the Web Forms API specifically to embed a web form instance in a website.

**Why this answer and not the others:** B is right because Docusign JS takes the instance URL from the Web Forms API and renders it in the page. The trap is A: it is the embedded-signing endpoint for envelopes, so it sounds right for 'embedding', but web form instances are rendered from their own instance URL. C and D fail because responsive signing is a document display feature and a workflow start link launches a Maestro workflow rather than rendering this instance.

**Option notes:**
- A (TRAP). This returns an embedded signing URL for an envelope recipient; it is not used to render a web form instance URL.
- B. Correct. The Web Forms API returns the instance URL and Docusign JS renders it inline in the host page.
- C. Responsive signing adapts document layout for mobile devices; it does not embed a web form instance.
- D. A From a link URL starts a Maestro workflow; it is not the component that renders a web form instance URL from the Web Forms API.

**Q46. (Agreement Manager API - Agreement data) [HIGH]** A reporting service needs the extracted expiration date and total agreement value of one signed and stored agreement whose agreementId it already has. Which call returns these values?

A. The Connect envelope-completed webhook payload
B. eSignature EnvelopeFormData:get on the source envelope
C. Agreements:getAgreement
D. Agreements:createAgreementSummary

**Answer:** C. Agreements:getAgreement

**Explanation:** getAgreement returns the provisions object for one agreement, which includes extracted values such as expiration_date and total_agreement_value.

**Why this answer and not the others:** C is right because the values are AI-extracted provisions of a known agreement. The trap is B: form data returns what signers typed into tabs, which only matches if someone happened to place a tab for each value, and it is not the extracted provision. A notifies about envelope events and does not carry Agreement Manager extractions, and D returns prose rather than discrete field values.

**Option notes:**
- A. Connect reports envelope events; it does not deliver Agreement Manager extracted provisions.
- B (TRAP). Returns signer-entered tab values, not the AI-extracted provisions of the agreement.
- C. Correct. getAgreement returns the agreement's provisions, including expiration date and total value.
- D. Creates an AI-written summary; it does not return discrete fields for reporting.

**Q47. (Workflow Builder and Workflow API - API trigger) [HIGH]** A backend service must start a published Maestro workflow and pass customer values from its database. Which call sequence is correct?

A. Envelopes:create, then TriggerWorkflow with the envelope ID
B. TriggerWorkflow first, then GetWorkflowTriggerRequirements to validate the inputs
C. GetWorkflowsList, then cancelWorkflowInstance
D. Get a token with aow_manage, call GetWorkflowTriggerRequirements, then TriggerWorkflow with trigger_inputs

**Answer:** D. Get a token with aow_manage, call GetWorkflowTriggerRequirements, then TriggerWorkflow with trigger_inputs

**Explanation:** The API trigger flow is: get a token that includes aow_manage, call GetWorkflowTriggerRequirements for the trigger URL and input schema, then call TriggerWorkflow with the required inputs.

**Why this answer and not the others:** D is right because the trigger requirements tell the app where to send the request and which inputs are required. The trap is B: it uses the right two calls in the wrong order, so the app would trigger before it knows the URL and schema. A creates an eSignature envelope the workflow does not need, and C cancels an instance instead of starting one.

**Option notes:**
- A. A workflow is not triggered from an envelope ID; the workflow creates its own signing steps.
- B (TRAP). Requirements must be read first; triggering blind risks missing required inputs.
- C. cancelWorkflowInstance stops a running instance; it does not start one.
- D. Correct. Token with aow_manage, then trigger requirements, then TriggerWorkflow with the inputs.

**Q48. (App Center and Extension Apps - Public App Center) [LOW]** How do extension apps help a developer expand a solution's visibility and reach?

A. They let customers call the developer's API using their own integration keys
B. They are published to the Docusign App Center, reaching Docusign's customer base
C. They add custom endpoints to the Docusign eSignature REST API
D. They are installed automatically in every Docusign account after review

**Answer:** B. They are published to the Docusign App Center, reaching Docusign's customer base

**Explanation:** Publishing to the Docusign App Center puts the app in front of Docusign's large customer base, which is the visibility and reach benefit.

**Why this answer and not the others:** B is right because App Center publication is the reach mechanism. The trap is C: extension apps make Docusign call your endpoints; they do not add new endpoints to Docusign's APIs. A confuses integration keys with extension apps, and D is wrong because admins choose to install apps.

**Option notes:**
- A. Integration keys are for apps calling Docusign APIs; they do not make an extension app discoverable.
- B. Correct. Publishing to the App Center exposes the app to Docusign customers.
- C (TRAP). Extension apps do not change Docusign's API surface; Docusign calls the developer's endpoints.
- D. Admins install apps from the App Center; nothing is installed automatically in every account.

**Q49. (API Authentication - PKCE) [HIGH]** A native desktop app cannot store a client secret securely. Each individual user signs in to send envelopes. Which OAuth grant type should the team configure?

A. Confidential Authorization Code Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. JSON Web Token Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** A native app is a public client: it cannot keep a secret, and users sign in, so Public Authorization Code Grant with PKCE is the grant to configure.

**Why this answer and not the others:** C is right because the app cannot keep a secret and users are present. The trap is B: Implicit Grant also avoids a secret, but it is legacy and Docusign recommends the PKCE code flow instead. A needs a secret the app cannot protect, and D is for services with no user present.

**Option notes:**
- A. Confidential Auth Code Grant needs a client secret, which a native app cannot store securely.
- B (TRAP). Implicit Grant avoids a secret but is legacy; Docusign recommends Public Auth Code with PKCE.
- C. Correct. Native app, no secret, interactive user: Public Authorization Code Grant with PKCE.
- D. JWT Grant is for unattended services after consent, not an app where each user signs in.

**Q50. (Go Live Process - Go-live setup) [MEDIUM]** A developer promotes an integration key to production during Go-Live. The integration uses Confidential Authorization Code Grant with a secret key and a redirect URI configured in Apps and Keys. What is the state of these OAuth parameters in production right after the key is duplicated?

A. They are not copied over and must be set up manually in production
B. Only the redirect URIs are copied; the secret key must be regenerated in production
C. Production generates placeholder secrets and redirect URIs that must not be modified
D. The key, secrets and redirect URIs are all duplicated, so the app works immediately

**Answer:** A. They are not copied over and must be set up manually in production

**Explanation:** Go-Live duplicates the integration key (same value) into production, but configuration parameters such as secrets and redirect URIs are not duplicated and must be added in production.

**Why this answer and not the others:** A is right because neither secrets nor redirect URIs are copied. The trap is B: it correctly says a new secret is needed, but redirect URIs are not copied either. C invents placeholder values, and D is the common assumption that everything carries over, which leaves the production app unable to authenticate.

**Option notes:**
- A. Correct. Secrets and redirect URIs are not duplicated; add them to the production key.
- B (TRAP). Redirect URIs are not copied either; both must be added in production.
- C. Docusign does not create placeholder values; you add the real secrets and redirect URIs yourself.
- D. Only the key value is duplicated; its secrets and redirect URIs are not.

**Q51. (Docusign Connect - Troubleshooting) [MEDIUM]** A listener sometimes receives the same Connect message twice, and the downstream system creates duplicate records. Which option should be used?

A. Return HTTP 409 for duplicates so Docusign stops sending them
B. Idempotent processing based on event identifiers or envelope state
C. Delete and recreate the Connect configuration
D. Switch the configuration to XML aggregate mode

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Connect can deliver the same event more than once (for example after retries), so the listener must recognize and safely skip events it has already processed.

**Why this answer and not the others:** B is right because idempotent processing makes duplicate deliveries harmless. The trap is A: rejecting the duplicate looks logical, but any non-2xx response is a failure that makes Connect retry, producing even more deliveries. C does not change delivery semantics, and D only combines related events in legacy XML; it does not stop redeliveries.

**Option notes:**
- A (TRAP). A non-2xx response is treated as a failure and triggers more retries.
- B. Correct. Track processed events or check envelope state so repeats do no harm.
- C. Recreating the configuration does not prevent duplicate deliveries.
- D. Aggregate mode merges related events in legacy XML; it does not prevent retried duplicates.

**Q52. (eSignature API - Composite templates) [HIGH]** An envelope must combine two saved server templates plus runtime recipient data in one API call. Which envelope model supports this?

A. Template reference model (templateId plus templateRoles)
B. Direct documents model (documents plus recipients)
C. Composite templates model (compositeTemplates array)
D. Two separate envelopes linked by a custom field

**Answer:** C. Composite templates model (compositeTemplates array)

**Explanation:** Only composite templates can apply multiple server templates in a single envelope per API call and add runtime data with inline templates. The clue is 'two saved server templates'.

**Why this answer and not the others:** C is right because the compositeTemplates array can mix several server templates with inline templates. The trap is A: templateId is the simple way to use a saved template, but it cannot combine multiple templates. B uses no saved templates and D produces two envelopes instead of one.

**Option notes:**
- A (TRAP). The template reference model (templateId plus templateRoles) uses a single template and cannot combine multiple templates.
- B. The direct documents model supplies documents directly and does not apply saved templates.
- C. Correct. Composite templates can combine multiple server templates and inline runtime data in one envelope.
- D. Two envelopes would split the agreement; the requirement is one envelope built from both templates.

**Q53. (eSignature Features and Web Forms - Connected Fields) [MEDIUM]** A value the signer types into a field must be checked against an external system of record during signing. Which feature supports this?

A. A Data IO extension
B. A public App Center listing
C. Connected Fields (data verification extension)
D. The Connect extension-executed event

**Answer:** C. Connected Fields (data verification extension)

**Explanation:** Real-time verification of a signer-entered value during signing is the Connected Fields use case.

**Why this answer and not the others:** C is right because Connected Fields verify signer data against an external source during signing. The trap is A: it also talks to a system of record, but its extension point is Maestro workflows, not eSignature signing. B and D fail because App Center listing is about distribution and the Connect event only reports results.

**Option notes:**
- A (TRAP). Data IO extensions read from and write to a system of record from Maestro workflows; they do not verify fields during eSignature signing.
- B. A listing is a distribution choice for an extension app; it is not the feature that validates a field.
- C. Correct. Connected Fields bind tabs to an extension that verifies the entered data against an external system during signing.
- D. This event reports verification results after they happen; it does not perform the check.

**Q54. (Agreement Manager API - Agreement list) [MEDIUM]** A developer must look up agreements by counterparty and then open one of them in full. Which pair of Agreement Manager requests is correct?

A. GET /v1/accounts/{accountId}/agreements/{agreementId} with a party filter
B. GET /v1/accounts/{accountId}/agreements, then GET .../agreements/{agreementId}
C. GET /restapi/v2.1/accounts/{accountId}/envelopes, then GET .../envelopes/{envelopeId}
D. POST /v1/accounts/{accountId}/agreements/{agreementId}/ai/actions/summarize

**Answer:** B. GET /v1/accounts/{accountId}/agreements, then GET .../agreements/{agreementId}

**Explanation:** The list endpoint GET /v1/accounts/{accountId}/agreements finds matching agreements; GET .../agreements/{agreementId} then retrieves one in full.

**Why this answer and not the others:** B is right because the lookup needs the list endpoint before the single-agreement endpoint. The trap is C: it has the same list-then-get shape, but it targets eSignature envelopes, not Agreement Manager agreements and their extracted parties. A needs an agreementId the developer does not have yet, and D summarizes one known agreement.

**Option notes:**
- A. The single-agreement path needs an agreementId, which the developer does not have before searching.
- B. Correct. List agreements first, then get the selected agreement by ID.
- C (TRAP). These are eSignature envelope endpoints, not Agreement Manager agreement endpoints.
- D. This creates an AI summary of a known agreement; it does not search by counterparty.

**Q55. (Workflow Builder and Workflow API - Runtime errors) [HIGH]** A TriggerWorkflow call returns 400 because the request lacks a value the workflow requires at start. Authentication succeeds. What should the developer inspect?

A. The event list in the Connect configuration
B. The scopes on the access token
C. The trigger_input_schema from GetWorkflowTriggerRequirements and how trigger_inputs are mapped
D. Whether the workflow's new instances are paused

**Answer:** C. The trigger_input_schema from GetWorkflowTriggerRequirements and how trigger_inputs are mapped

**Explanation:** TriggerWorkflow validates the input data against the workflow's trigger input schema. A missing required starting value points to the schema and the mapping of trigger_inputs.

**Why this answer and not the others:** C is right because the clue is a missing required value while authentication succeeds. The trap is B: scope problems are a common runtime error, but they cause authorization failures, not a missing-input rejection. A affects event delivery only, and D concerns whether new instances can start at all, not input validation.

**Option notes:**
- A. Connect only delivers events; it has no effect on trigger input validation.
- B (TRAP). Authentication already succeeds, so the token's scopes are not the cause.
- C. Correct. Compare the request's trigger_inputs with the required fields in trigger_input_schema.
- D. Pausing blocks new instances regardless of the inputs; it does not produce a missing-field error.

**Q56. (App Center and Extension Apps - Connections) [HIGH]** An extension action must call an external API with OAuth credentials, and the developer wants those auth details defined once in the manifest. Which object holds them?

A. extensions
B. publisher
C. actions, with each action storing its own client secret
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines reusable authentication configuration that actions reference.

**Why this answer and not the others:** D is right because connections hold the OAuth configuration. The trap is C: actions reference a connection through connectionsReference rather than storing credentials themselves. A lists extension types and their actions, and B holds publisher details.

**Option notes:**
- A. extensions declare extension types and reference actions; they do not hold credentials.
- B. publisher contains organization contact information only.
- C (TRAP). Actions point to a connection via connectionsReference instead of storing credentials themselves.
- D. Correct. connections defines the authentication used by actions.

**Q57. (API Authentication - JWT Grant) [MEDIUM]** A banking application runs a daily automated process that generates compliance reports and voids expired agreements, using a system sender account with no user login. Which OAuth 2.0 flow is recommended?

A. Confidential Authorization Code Grant
B. Implicit Grant
C. Public Authorization Code Grant
D. JSON Web Token Grant

**Answer:** D. JSON Web Token Grant

**Explanation:** JWT Grant is the service-integration flow: it uses an RSA key pair and prior consent to get a token with no interactive login, which suits scheduled processes.

**Why this answer and not the others:** D is right because the process runs with no user login. The trap is A: a bank backend can store a secret, but Confidential Auth Code still needs someone to sign in through a browser. B and C are also interactive flows.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant needs an interactive user to sign in, and nobody is present for this process.
- B. Implicit Grant is a legacy, interactive browser flow.
- C. Public Auth Code Grant is interactive and meant for clients that cannot keep a secret, not for unattended automation.
- D. Correct. JWT Grant is the unattended service-integration flow using an RSA key pair and prior consent.

**Q58. (Go Live Process - Troubleshooting) [HIGH]** A developer clicks Start Go live, logs in to the production account, and sees an error message instead of a list of accounts to select. What is the most likely cause?

A. The app has not yet made 20 eSignature API calls in the developer account
B. The integration key has no secret key configured
C. The integration type selected for the key does not match the account type
D. The Go-Live request is in Pending approval for up to 48 hours

**Answer:** C. The integration type selected for the key does not match the account type

**Explanation:** The course states that an error instead of a list of accounts means the integration type specified for the key does not match the type of the account you logged into.

**Why this answer and not the others:** C is right because the account list is filtered by the integration type chosen for the key. The trap is A: the old 20 API call requirement no longer exists, so you can start Go-Live right after creating the key. B is unrelated to account selection, and D is a status shown after submission, not an error during account selection.

**Option notes:**
- A (TRAP). The 20 API call requirement was removed; Go-Live can start right after the key is set up.
- B. A missing secret does not stop the account list from appearing during Start Go live.
- C. Correct. An integration type that does not match the account type produces this error.
- D. Pending approval is a status shown after you select the account, not an error in place of the list.

**Q59. (Docusign Connect - Payload selection) [MEDIUM]** A team wants smaller Connect messages and will query full envelope details through the API only when needed. What should the Connect configuration do?

A. Use JSON SIM and include only the event data the listener needs
B. Include documents and the full envelope summary in every message
C. Switch to legacy XML, which sends smaller messages
D. Enable aggregate mode to shrink each message

**Answer:** A. Use JSON SIM and include only the event data the listener needs

**Explanation:** JSON SIM messages are event-focused and customizable, so the configuration can include only the data needed and leave documents out.

**Why this answer and not the others:** A is right because JSON SIM lets you choose what each message carries. The trap is C: legacy XML is envelope-focused and its messages are larger, not smaller. B is the opposite of the goal, and D reduces the number of messages, not the size of each one.

**Option notes:**
- A. Correct. JSON SIM messages can be limited to the data the listener needs.
- B. Including documents and full summaries makes every message larger.
- C (TRAP). Legacy XML messages are envelope-focused and larger than JSON SIM messages.
- D. Aggregate mode combines events into fewer messages; it does not shrink payloads.

**Q60. (eSignature API - Anchor tabs) [MEDIUM]** A document can vary in page length, but the signature field must appear next to a specific text string. Which tab placement method is best?

A. xPosition and yPosition on a fixed page
B. Anchor tagging with anchorString and offsets
C. templateId with templateRoles
D. tabLabel matching the text string

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to text in the document, so they follow the text when page length changes. The clue is 'next to a specific text string'.

**Why this answer and not the others:** B is right because anchorString plus offsets ties the tab to the text. The trap is A: fixed positioning is valid tab placement, but it uses page coordinates that break when content moves. C references a template rather than placing tabs, and tabLabel names a tab for data mapping without positioning it.

**Option notes:**
- A (TRAP). Fixed x and y coordinates on a page do not move when the text shifts to another place or page.
- B. Correct. Anchor tagging finds the text and places the tab relative to it using offsets.
- C. templateId references a saved template; it does not decide where a tab is placed in a variable document.
- D. tabLabel identifies a tab, for example to share or map values; it does not position the tab.

**Q61. (eSignature Features and Web Forms - ID Evidence) [MEDIUM]** A records office must retrieve the ID images and personal details retained from a signer's completed ID Verification event. Which API is relevant?

A. IdentityVerifications:list
B. ID Evidence API
C. The certificate of completion
D. The Agreement Manager API

**Answer:** B. ID Evidence API

**Explanation:** Retained data from a completed IDV event is retrieved with the ID Evidence API.

**Why this answer and not the others:** B is right because the ID Evidence API returns retained evidence from ID verification events. The trap is A: it is the IDV API you use when sending, but it lists configurations rather than results. C and D fail because the certificate does not hold ID images and Agreement Manager covers agreement data.

**Option notes:**
- A (TRAP). This lists the account's IDV workflows so you can set workflowId on a recipient; it returns no evidence from completed verifications.
- B. Correct. The ID Evidence API retrieves the ID verification data your administrator has configured the account to retain.
- C. The certificate records events and authentication methods; it does not contain the retained ID images.
- D. Agreement Manager returns agreements and AI-extracted agreement data, not ID verification evidence.

**Q62. (Agreement Manager API - Legacy import) [MEDIUM]** An operations group wants contracts signed on paper years ago to appear in Agreement Manager reports with extracted dates and parties. Which capability matters?

A. Bulk import the legacy contracts into Agreement Manager
B. Call Agreements:getAgreement on each paper contract's scanned file
C. Attach the scans to new envelopes as supplemental documents
D. Record the key dates as eSignature envelope custom fields

**Answer:** A. Bulk import the legacy contracts into Agreement Manager

**Explanation:** Importing legacy agreements adds them to Agreement Manager, where AI extraction surfaces dates and parties for reporting.

**Why this answer and not the others:** A is right because the contracts must first exist in the repository before any data can be read. The trap is C: it puts the files into Docusign, but as envelope attachments, which neither imports the old contracts as agreements nor extracts their terms. B only reads agreements that already exist in Agreement Manager, and D stores values on envelopes rather than creating agreement records.

**Option notes:**
- A. Correct. Bulk import brings the legacy contracts into Agreement Manager so their data is extracted.
- B. getAgreement reads existing agreement records by ID; it cannot take a scanned file as input.
- C (TRAP). Supplemental documents ride along with a new envelope; they do not import the old contracts as agreements.
- D. Envelope custom fields do not create agreements or feed Agreement Manager reports.

**Q63. (Workflow Builder and Workflow API - Embedding workflow) [HIGH]** A custom web app triggers a workflow and wants users to complete it inside the app's own page, without leaving the app. What should the app do with the TriggerWorkflow response?

A. Redirect the browser to the returned workflow instance URL
B. Load the returned workflow instance URL in an iframe
C. Call EnvelopeViews:createRecipient with the workflow ID
D. Poll getWorkflowInstance and rebuild each step in custom UI

**Answer:** B. Load the returned workflow instance URL in an iframe

**Explanation:** TriggerWorkflow returns an instance URL. Embedding it in an iframe keeps the app's UI visible while the user completes the workflow.

**Why this answer and not the others:** B is right because the requirement is to stay inside the app, which the iframe option provides. The trap is A: redirecting to the instance URL is also supported, but the user leaves the app and stays on Docusign when finished. C is the eSignature embedded signing call and does not take a workflow ID, and D only reads status; it cannot render steps.

**Option notes:**
- A (TRAP). Supported, but the user is routed to Docusign and does not return to the app when done.
- B. Correct. Embedding the instance URL in an iframe keeps the workflow inside the app.
- C. createRecipient creates an envelope signing view; it does not open a workflow instance.
- D. getWorkflowInstance returns status details; the app cannot run workflow steps itself.

**Q64. (App Center and Extension Apps - connectionsReference) [HIGH]** An action must use a named connection defined in the manifest. Which property links the action to that connection?

A. actionReferences
B. distribution
C. connectionsReference
D. publicationRegions

**Answer:** C. connectionsReference

**Explanation:** connectionsReference on the action names the connection whose authentication it uses.

**Why this answer and not the others:** C is right because connectionsReference links an action to a connection. The trap is A: actionReferences links an extension to its actions, one level up. B and D are distribution settings.

**Option notes:**
- A (TRAP). actionReferences links extensions to actions, not actions to connections.
- B. distribution sets PUBLIC or PRIVATE.
- C. Correct. connectionsReference ties the action to a named connection.
- D. publicationRegions sets installable regions for public apps.

**Q65. (API Authentication - Bearer tokens) [MEDIUM]** A REST API request returns 401 Unauthorized even though /oauth/token returned an access token. Where should the access token be supplied on API calls?

A. In the Authorization header as Bearer <access_token>
B. In the Authorization header as Basic base64(integrationKey:secretKey)
C. As an access_token query string parameter
D. In the JSON request body next to the envelope definition

**Answer:** A. In the Authorization header as Bearer <access_token>

**Explanation:** Docusign REST calls authenticate with the header Authorization: Bearer followed by the access token.

**Why this answer and not the others:** A is right because API requests carry the access token in a Bearer Authorization header. The trap is B: a Basic header with the integration key and secret is correct for the /oauth/token code exchange, but not for API calls. C and D are not where Docusign reads the token.

**Option notes:**
- A. Correct. Send Authorization: Bearer <access_token> on every API request.
- B (TRAP). The Basic header is used at /oauth/token in the confidential flow, not on REST API calls.
- C. Docusign APIs read the token from the Authorization header, not the query string.
- D. The request body holds the envelope definition; the token belongs in the Authorization header.

**Q66. (Go Live Process - Go-live setup) [HIGH]** A developer is setting up a new integration key in the developer account. Which step must be completed on the key before the Go-Live process can be completed?

A. Make 20 successful eSignature API calls with the key
B. Select an option under How will you use this integration?
C. Generate an RSA key pair for the production environment
D. Open a Docusign Support case asking for the key to be promoted

**Answer:** B. Select an option under How will you use this integration?

**Explanation:** The course notes that you must select an option in the How will you use this integration? section before you can complete Go-Live.

**Why this answer and not the others:** B is right because the integration type (classification) is required for Go-Live. The trap is A: older guidance required 20 API calls, but that requirement no longer exists. C is wrong because production credentials are added after Go-Live on the production key, and D describes the support-case route some other APIs use, not eSignature Go-Live from Apps and Keys.

**Option notes:**
- A (TRAP). The 20 API call requirement was removed; you can submit right after creating the key.
- B. Correct. The How will you use this integration? choice must be made before Go-Live can be completed.
- C. Production credentials are added on the production key after Go-Live, not generated beforehand.
- D. eSignature Go-Live is started from Apps and Keys with Actions > Start Go live, not by a support case.

**Q67. (Docusign Connect - Envelope-level Connect) [MEDIUM]** Developer guidance must explain how a partner app attaches its own webhook URL and event list to each envelope it sends, without touching the customer's eSignature Admin settings. What should the guidance recommend?

A. Add the listener in eSignature Admin > Connect for the customer's account
B. Call the ConnectConfigurations API to create a configuration with urlToPublishTo
C. Store the listener URL in an envelope custom field
D. Include an eventNotification object (URL and events) in each Envelopes:create request

**Answer:** D. Include an eventNotification object (URL and events) in each Envelopes:create request

**Explanation:** Envelope-level Connect is set through the eventNotification property when the envelope is created by API, so the app controls its webhook per envelope without changing account settings.

**Why this answer and not the others:** D is right because eventNotification travels with each envelope request and needs no admin configuration. The trap is B: the ConnectConfigurations API with urlToPublishTo creates an account-level configuration, which is exactly the account setting the app must not change. A is the same account-level setup done in the UI, and C stores data on the envelope but never causes Connect to send anything.

**Option notes:**
- A. eSignature Admin > Connect creates an account-level configuration, which changes the customer's account settings.
- B (TRAP). ConnectConfigurations with urlToPublishTo creates an account-level configuration, not a per-envelope webhook.
- C. Envelope custom fields hold metadata; Connect does not read a listener URL from them.
- D. Correct. eventNotification in Envelopes:create defines a per-envelope webhook controlled entirely by the sending app.

**Q68. (eSignature API - Embedded signing) [HIGH]** A recipient must sign inside the host app instead of through an email link. Which property on the signer in the envelope definition marks embedded signing?

A. clientUserId
B. recipientId
C. returnUrl
D. EnvelopeViews:createRecipient

**Answer:** A. clientUserId

**Explanation:** Setting clientUserId on the signer when the envelope is created marks the recipient as embedded. The clue is a property on the signer in the envelope definition.

**Why this answer and not the others:** A is right because clientUserId is the recipient property that makes the signer embedded. The trap is D: createRecipient is required for embedded signing, but it is the later API call that returns the signing URL, not a recipient property. B exists for every recipient and C belongs to the createRecipient request.

**Option notes:**
- A. Correct. Setting clientUserId on the signer marks the recipient as embedded (captive).
- B. recipientId identifies the recipient within the envelope; every recipient has one, embedded or not.
- C. returnUrl is sent in the createRecipient request to say where to redirect after signing; it is not a recipient property.
- D (TRAP). EnvelopeViews:createRecipient is the endpoint that returns the signing URL, not a recipient property.

**Q69. (eSignature Features and Web Forms - Web Forms embedding) [HIGH]** A financial-aid portal must show a template-based web form inline, so the student fills it in without leaving the portal. Which combination delivers this?

A. Create an embedded instance with clientUserId, then render its URL with Docusign JS
B. Create a remote instance with sendOption and recipients[], then render it with Docusign JS
C. Create a standalone configuration and call EnvelopeViews:createRecipient
D. Send an envelope with clientUserId and email the signing URL to the student

**Answer:** A. Create an embedded instance with clientUserId, then render its URL with Docusign JS

**Explanation:** Inline display inside the portal means an embedded instance: createInstance with clientUserId, then Docusign JS to render the URL.

**Why this answer and not the others:** A is right because embedded instances are identified by clientUserId and rendered with Docusign JS. The trap is B: Docusign JS is the right renderer, but a remote instance is the email-delivered mode, so the student would leave the portal. C and D fail because a standalone form has no envelope to view and an emailed envelope signing URL is not a web form embedded in the page.

**Option notes:**
- A. Correct. Embedded instances require clientUserId on Instances:createInstance, and Docusign JS renders the returned instance URL in the portal.
- B (TRAP). Remote instances are delivered to participants by email (sendOption with recipients by roleName); they are not the embedded pattern.
- C. A standalone configuration never creates an envelope, so there is no envelope recipient view to request.
- D. This is embedded signing of an envelope, not a web form, and emailing a short-lived signing URL is not an inline experience.

**Q70. (Agreement Manager API - Agreement documents) [LOW]** A document-management system has an agreementId and has already stored the agreement's extracted metadata. It now needs the actual agreement file for its archive. What should the plan include?

A. A document download step for the agreement file
B. Calling Agreements:getAgreement again, since the file is inside the provisions object
C. Calling Agreements:createAgreementSummary to obtain the archived copy
D. Calling Agreements:getAgreementsList filtered by the agreementId

**Answer:** A. A document download step for the agreement file

**Explanation:** Extracted metadata and the agreement file are separate; the archive needs a document download step for the file itself.

**Why this answer and not the others:** A is right because the metadata is already stored and only the file is missing. The trap is B: getAgreement is the right call for the extracted record, but the provisions object holds values like dates and amounts, not the document. C returns AI-written text, and D returns list-level agreement records, neither of which is the file.

**Option notes:**
- A. Correct. The agreement file is retrieved through a document download, separate from the metadata.
- B (TRAP). The provisions object contains extracted values, not the document content.
- C. A summary is AI-generated text, not the archived agreement.
- D. The list call returns agreement records, not document files.

**Q71. (Workflow Builder and Workflow API - Installed extensions) [MEDIUM]** A workflow designer cannot find the Salesforce writeback step in Workflow Builder. Which prerequisite is most likely missing?

A. An administrator has not installed and authorized the Salesforce extension app from App Center
B. The Salesforce endpoint is not listed in a Connect configuration
C. Connected fields are not enabled on the workflow
D. The integration key lacks the extended scope

**Answer:** A. An administrator has not installed and authorized the Salesforce extension app from App Center

**Explanation:** Workflow Builder app steps come from extension apps that an administrator has installed from Docusign App Center and authorized for the account. Without that, the step is not available.

**Why this answer and not the others:** A is right because extension app steps only appear once the app is installed and authorized in the account. The trap is C: connected fields are an extension feature, but they work in eSignature and are not supported in Maestro workflows. B is for outbound event notifications, and D concerns refresh tokens, not workflow steps.

**Option notes:**
- A. Correct. The extension app must be installed from App Center and authorized before its steps appear.
- B. Connect sends event notifications; it does not add steps to Workflow Builder.
- C (TRAP). Connected fields are not supported in Maestro workflows.
- D. The extended scope extends refresh token life; it does not enable extension app steps.

**Q72. (App Center and Extension Apps - Workflow steps) [HIGH]** A sales team uses Maestro to generate contracts. A workflow must retrieve a client's pricing tier and contract duration from the internal ERP to pre-fill documents. Which extension type performs this read inside the workflow?

A. File IO extension app
B. Connected Fields extension app
C. Data IO extension app
D. Docusign Connect webhook listener

**Answer:** C. Data IO extension app

**Explanation:** Data IO extension apps read (and write) structured data in external systems from Maestro workflows, which is what pulling pricing data from the ERP needs.

**Why this answer and not the others:** C is right because the workflow needs to read structured ERP data. The trap is B: connected fields also use a system of record, but they verify eSignature field values and are not supported in Maestro. A handles files, and D only receives event notifications.

**Option notes:**
- A. File IO moves documents to storage; it does not read field data.
- B (TRAP). Connected fields verify eSignature fields and are not supported in Maestro workflows.
- C. Correct. Data IO reads structured data from the ERP in the workflow.
- D. A Connect listener receives events; it cannot be a workflow read step.

**Q73. (API Authentication - OAuth flow selection) [HIGH]** A legal operations portal has a secured backend that stores the client secret. Each employee must sign in with their own Docusign credentials so every envelope is attributed to the person who sent it. Which OAuth flow fits?

A. Public Authorization Code Grant with PKCE
B. JWT Grant impersonating each employee after consent
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Employees are present and must sign in with their own credentials, and the backend can protect a secret, so Confidential Authorization Code Grant is the fit.

**Why this answer and not the others:** D is right because the requirement is an interactive sign-in by each employee on a backend that can keep a secret. The trap is B: JWT can impersonate users after consent, but it involves no sign-in at all and is designed for services with no user present. A is for clients that cannot store a secret, and C is the legacy browser flow.

**Option notes:**
- A. Public Auth Code Grant with PKCE is meant for clients without a safe place for a secret; this backend has one.
- B (TRAP). JWT impersonation skips user sign-in entirely and is intended for unattended service integrations, not employees who must log in themselves.
- C. Implicit Grant is a legacy flow that returns tokens to the browser and is not recommended by Docusign.
- D. Correct. Interactive per-user sign-in on a backend that can protect a secret is Confidential Authorization Code Grant.

**Q74. (Go Live Process - Integration classification) [HIGH]** A company buys a partner product that asks each customer to supply its own Docusign integration key. When the company creates that key, which integration type should it choose?

A. Third-party integration key
B. Private custom integration
C. Public integration
D. Embedded integration

**Answer:** A. Third-party integration key

**Explanation:** When you use a Docusign partner integration for your business need and it requires you to provide your own integration key, the classification is Third-party integration key.

**Why this answer and not the others:** A is right because the clue is a partner product that requires the customer's own key. The trap is B: the key lives in the company's account and its employees use it, but the app was built by a partner, not as a custom integration. C is for the vendor that builds a multi-customer app, and D is for a vendor embedding Docusign features through its own account.

**Option notes:**
- A. Correct. A partner integration that needs the customer's own key uses the Third-party integration key type.
- B (TRAP). Private custom integration is for an app the company builds for direct use by its employees or its customers' employees.
- C. Public integration is chosen by the vendor publishing an app for many Docusign customers, not by a customer.
- D. Embedded integration is for vendors offering Docusign features through their own account, with an ISV Embed license.

**Q75. (Docusign Connect - Envelope-level Connect) [HIGH]** A custom integration needs real-time updates for one specific envelope it creates with the eSignature REST API, independent of the account-level Connect configuration. How must the developer configure this webhook?

A. Include the eventNotification object in the envelope creation request body
B. Use the Maestro API to start a workflow instance holding the listener URL
C. Register a listener for the Envelope ID in Docusign Admin Connect settings
D. Base the envelope on a web form that has Connect enabled

**Answer:** A. Include the eventNotification object in the envelope creation request body

**Explanation:** Adding eventNotification to the Envelopes:create payload sets up an envelope-level webhook for that envelope, separate from any account-level configuration.

**Why this answer and not the others:** A is right because envelope-level Connect is configured only through eventNotification in the API request. The trap is C: Docusign Admin does host Connect settings, but they are account-level and cannot target one Envelope ID. B uses Maestro, which orchestrates workflows rather than attaching a webhook to an eSignature envelope, and D is a different sending model with no per-envelope webhook.

**Option notes:**
- A. Correct. eventNotification in the Envelopes:create body defines a per-envelope Connect webhook.
- B. Maestro orchestrates multi-step workflows; it is not how an eSignature envelope gets its own webhook.
- C (TRAP). Admin Connect settings create account-level configurations; there is no per-Envelope-ID listener there.
- D. Web forms are a different sending model and do not provide a per-envelope webhook.

**Q76. (eSignature API - Signing URL) [HIGH]** An app has created and sent an envelope for an embedded recipient. What must the app request before the recipient can sign in the host application?

A. A sender view URL from EnvelopeViews:createSender
B. The signing link from the recipient's email invitation
C. The envelope details from Envelopes:get
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL from EnvelopeViews:createRecipient and redirecting the user to it.

**Why this answer and not the others:** D is right because the recipient view is the signing ceremony URL. The trap is A: createSender is also an embedded view, but it opens the sending and tagging experience, not signing. B fails because embedded recipients do not get an email invitation and C returns envelope data, not a signing session.

**Option notes:**
- A (TRAP). createSender returns a sender view for preparing and sending, not a signing session.
- B. Embedded (clientUserId) recipients are not sent an email invitation to sign.
- C. Envelopes:get returns envelope information; it does not return a signing URL.
- D. Correct. EnvelopeViews:createRecipient returns the short-lived URL for the embedded signing session.

**Q77. (eSignature Features and Web Forms - Web Form correlation) [MEDIUM]** Sofia's partner app creates one embedded web form instance per customer and needs a value it controls to link each instance to the customer record. Which value should it supply?

A. The web form configuration formId
B. A brandId
C. The returnUrl
D. clientUserId

**Answer:** D. clientUserId

**Explanation:** The stem asks for a value the app controls per customer, which is clientUserId.

**Why this answer and not the others:** D is right because clientUserId is the per-user value your app supplies on createInstance. The trap is A: it appears in the same request path, but it is the same for every instance of that form. B and C fail because branding and redirect settings do not identify a customer.

**Option notes:**
- A (TRAP). formId selects which configuration to instantiate; all customers share it, so it cannot link an instance to one record.
- B. brandId applies branding to an envelope; it carries no customer identity.
- C. returnUrl is where the participant is sent after finishing; it is not an identifier for the instance.
- D. Correct. clientUserId identifies the user in your system and is required on Instances:createInstance for embedded instances.

**Q78. (Agreement Manager API - Agreement data) [MEDIUM]** A renewal is identified by querying the Agreement Manager API for upcoming expiration dates. That should start an automated multi-step renewal process (prefill new documents, collect signatures). Which service is recommended for programmatically starting that process?

A. Workflow Builder (Maestro) API
B. Web Forms API
C. eSignature REST API
D. Connected Fields API

**Answer:** A. Workflow Builder (Maestro) API

**Explanation:** The Workflow Builder (Maestro) API triggers a published multi-step workflow, which can prefill documents and route them for signature.

**Why this answer and not the others:** A is right because the requirement is to launch an orchestrated multi-step process. The trap is C: the eSignature REST API can send the renewal envelope, but it does not orchestrate the surrounding steps, so the integration would have to build them itself. B collects data in a form instance and D verifies field data against external systems; neither starts a multi-step workflow.

**Option notes:**
- A. Correct. The Workflow Builder API triggers a multi-step workflow from an integration.
- B. Web Forms creates form instances for data collection, not a full orchestrated renewal process.
- C (TRAP). Sends envelopes, which covers only the signing step, not the orchestration of the whole renewal.
- D. Connected Fields verifies data in fields against external sources; it does not start workflows.

**Q79. (Workflow Builder and Workflow API - Workflow steps) [MEDIUM]** A workflow must automatically archive the final signed agreement to Google Drive after all recipients complete signing. Which type of step must the designer add?

A. An extension app step (Store Files) using the Google Drive app
B. A second Send Documents for Signature step
C. A Branching Rule step
D. A Collect Data with Web Forms step

**Answer:** A. An extension app step (Store Files) using the Google Drive app

**Explanation:** Apps steps call installed extension apps; Store Files steps automate storage of completed agreements in services such as Google Drive.

**Why this answer and not the others:** A is right because only an extension app step can write the file to Google Drive. The trap is C: the course example uses a Branching Rule on envelope status before storing, but the branch only decides the path; it does not store anything. B sends another envelope, and D collects data.

**Option notes:**
- A. Correct. A Store Files app step with the Google Drive extension archives the completed agreement.
- B. Another signing step sends a document again; it does not archive anything.
- C (TRAP). A branch can check that the envelope is completed, but it cannot save the file itself.
- D. Web forms collect participant data; they do not store documents externally.

**Q80. (App Center and Extension Apps - API proxy) [HIGH]** An extension action must call a third-party API whose request and response format does not conform to the Docusign action schema. What should the developer add?

A. A Connect configuration using a custom XML format
B. An API proxy that translates requests and responses
C. Extra OAuth scopes on the connection
D. Concerto type definitions declared in the manifest

**Answer:** B. An API proxy that translates requests and responses

**Explanation:** If external endpoints do not conform to the Docusign action schema, an API proxy translates the requests and responses into the format Docusign expects.

**Why this answer and not the others:** B is right because a proxy reshapes payloads between Docusign and the API. The trap is D: Concerto describes the data model for Data IO and connected fields, but it does not convert an incompatible API's payloads. A is an event webhook and C only changes authorization.

**Option notes:**
- A. Connect sends event notifications; it does not translate extension action calls.
- B. Correct. An API proxy translates between Docusign's action schema and the third-party format.
- C. Scopes control what the token can access, not the payload format.
- D (TRAP). Concerto models data types; it does not convert a non-conforming API's requests and responses.

**Q81. (API Authentication - OAuth flow selection) [HIGH]** A single-page app is served from a CDN and has no backend server. Each user must sign in with their own Docusign account. The security reviewer notes that authorization code flows are safer than token-in-URL flows. Which flow should the developer choose?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** An authorization code flow is preferred, and because the SPA has no backend to hold a secret, the right code flow is the public one with PKCE.

**Why this answer and not the others:** C is right because it is an authorization code flow that works without a secret. The trap is A: it is also an authorization code flow, but it requires a client secret that a CDN-served SPA has nowhere safe to store. B does not sign users in, and D is the token-in-URL legacy flow the reviewer wants to avoid.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant is a code flow too, but its secret would be exposed in the browser because there is no backend.
- B. JWT Grant is a service-to-service flow with no user sign-in and needs a protected private key.
- C. Correct. A code flow for a client that cannot hold a secret is Public Authorization Code Grant with PKCE.
- D. Implicit Grant returns the token in the redirect URL, which is the legacy pattern the reviewer wants to avoid.

**Q82. (Go Live Process - Production endpoints) [HIGH]** After Go-Live, a production app still sends users to account-d.docusign.com to sign in. Which authentication host must it use in production?

A. account-d.docusign.com
B. demo.docusign.net
C. The account's base URI, such as https://na2.docusign.net
D. account.docusign.com

**Answer:** D. account.docusign.com

**Explanation:** The After Go-Live guidance says to change the OAuth authentication host from https://account-d.docusign.com to https://account.docusign.com.

**Why this answer and not the others:** D is right because account.docusign.com is the production authentication service. The trap is C: the base URI is the production host for API calls, not for OAuth sign-in. A is the developer environment authentication host, and B is the demo API host.

**Option notes:**
- A. account-d.docusign.com is the developer environment authentication host.
- B. demo.docusign.net is the demo eSignature API host, not an authentication host.
- C (TRAP). The base URI is used for eSignature API calls, not for OAuth authentication.
- D. Correct. Production OAuth uses https://account.docusign.com.

**Q83. (Docusign Connect - Connect vs polling) [HIGH]** An architect must justify replacing a polling loop with webhooks. The account is close to its hourly API limit. Which statement is the strongest justification?

A. Polling status calls are exempt from hourly API limits
B. Ask Docusign to raise the account's hourly API limit
C. Use Connect; pushed messages do not count against API limits
D. Use Connect, although each delivered message counts as one API call

**Answer:** C. Use Connect; pushed messages do not count against API limits

**Explanation:** Connect messages are pushed by Docusign and do not count against the account's API limits, which directly addresses the near-limit problem in the stem.

**Why this answer and not the others:** C is right because webhook deliveries are not API calls made by the app. The trap is D: it picks the right feature but attaches a false cost, since Connect messages do not consume API quota. A is false because status calls do count and polling is also limited per envelope, and B treats the symptom instead of removing the polling.

**Option notes:**
- A. Status polling calls count against API limits and are also restricted to once per 15 minutes per envelope.
- B. Raising limits does not fix wasteful polling and is not the recommended design.
- C. Correct. Connect pushes messages that do not count against API limits and arrive only when something changes.
- D (TRAP). Connect messages do not count as API calls; this misstates the key advantage.

**Q84. (eSignature API - Embedded signing timing) [HIGH]** An app generates embedded signing URLs when envelopes are created, often hours before users open the page. What is the risk?

A. The envelope is voided automatically
B. Recipients receive duplicate email invitations
C. The short-lived, single-use URL may expire before use
D. Nothing; the URL stays valid until the envelope expires

**Answer:** C. The short-lived, single-use URL may expire before use

**Explanation:** Recipient view URLs are short-lived (about 5 minutes) and single-use, so they should be requested only when the user is ready to sign.

**Why this answer and not the others:** C is right because a URL generated hours earlier will have expired. The trap is D: the envelope itself stays valid for a long time, but the signing URL does not. A and B describe effects that unused signing URLs do not cause.

**Option notes:**
- A. An expired signing URL does not void the envelope; the app can request a new URL.
- B. Embedded signers are not emailed, and generating a URL does not send invitations.
- C. Correct. Signing URLs expire within minutes and work once, so early generation leads to expired links.
- D (TRAP). Envelope expiration is separate; the signing URL itself expires within minutes.

**Q85. (eSignature Features and Web Forms - Identity verification) [HIGH]** A developer must require ID verification (government photo ID) for a signer. How does the developer obtain and apply the right configuration?

A. AccountSignatureProviders:list, then recipientSignatureProviders on the signer
B. Set idCheckConfigurationName to 'ID Check $'
C. IdentityVerifications:list (REST v2.1), then identityVerification.workflowId on the recipient
D. TabInfo:GetConnectedFieldsTabGroups, then tab extensionData

**Answer:** C. IdentityVerifications:list (REST v2.1), then identityVerification.workflowId on the recipient

**Explanation:** The workflowId for IDV comes from IdentityVerifications:list and is applied in the recipient's identityVerification object.

**Why this answer and not the others:** C is right because IDV workflow IDs come from IdentityVerifications:list and are set as identityVerification.workflowId. The trap is A: it is a parallel 'list then apply to signer' pattern, but it selects a signature provider for SBS, not an IDV workflow. B and D fail because ID Check is KBA and Connected Fields verifies data in tabs.

**Option notes:**
- A (TRAP). These configure EU standards-based signatures (AES/QES signature providers), not the ID verification workflow for a government photo ID check.
- B. That configures knowledge-based authentication, which asks public-record questions (US only); it does not check a photo ID.
- C. Correct. IdentityVerifications:list returns the account's IDV workflow IDs, and the chosen workflowId goes in the recipient's identityVerification object.
- D. This is the Connected Fields send flow, which verifies field values against an external system, not the signer's identity document.

**Q86. (Agreement Manager API - Agreement data) [HIGH]** An internal service must return the extracted provisions of one agreement whose agreementId it receives. Which Agreement Manager request should it send?

A. GET /v1/accounts/{accountId}/agreements
B. GET /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/form_data
C. GET /v1/accounts/{accountId}/agreements/{agreementId}
D. POST /v1/accounts/{accountId}/agreements/{agreementId}/ai/actions/summarize

**Answer:** C. GET /v1/accounts/{accountId}/agreements/{agreementId}

**Explanation:** GET .../agreements/{agreementId} (Agreements:getAgreement) returns one agreement's full record, including its provisions. The service already receives the agreementId.

**Why this answer and not the others:** C is right because the ID is known and one agreement's provisions are needed. The trap is A: it is the Agreement Manager list endpoint, which is for finding agreements, not for retrieving one known record. B is an eSignature endpoint that returns signer tab values, and D generates an AI summary instead of returning provisions.

**Option notes:**
- A (TRAP). The list endpoint is used for searching; the service already has the agreementId.
- B. An eSignature envelope endpoint for tab values, not Agreement Manager provisions.
- C. Correct. getAgreement by agreementId returns the agreement's provisions.
- D. Creates an AI-written summary rather than returning structured provisions.

**Q87. (Workflow Builder and Workflow API - Workflow steps) [HIGH]** Every applicant signs the exact same NDA; only the name and date fields change. Which step should prepare the document for signature?

A. Prepare Document Template
B. Use eSignature API
C. Collect Data with Web Forms
D. Prepare eSignature Template, followed by Send Documents for Signature

**Answer:** D. Prepare eSignature Template, followed by Send Documents for Signature

**Explanation:** Prepare eSignature Template is meant for a single template used by every workflow instance, where the document is always the same. It is followed by the Send Documents for Signature step.

**Why this answer and not the others:** D is right because the document never changes between instances. The trap is A: Prepare Document Template is for generating different document content from workflow variables with conditional logic, which this NDA does not need. B is for direct API-driven envelope actions, and C only collects data.

**Option notes:**
- A (TRAP). Meant for documents whose content varies by workflow variables; overkill for a fixed NDA.
- B. Not the step for preparing a fixed template for signature.
- C. Collects data but does not prepare a document to sign.
- D. Correct. One fixed template for all instances, then Send Documents for Signature.

**Q88. (App Center and Extension Apps - Firewall) [HIGH]** Docusign must call a customer-hosted endpoint for an extension action. Which network consideration is important?

A. Allow Docusign's requests through the endpoint's firewall to the HTTPS endpoint
B. Allow the endpoint to make outbound calls to the eSignature API
C. Enable CORS for the App Center domain
D. Allow inbound traffic only from signers' browsers

**Answer:** A. Allow Docusign's requests through the endpoint's firewall to the HTTPS endpoint

**Explanation:** Docusign's servers must be able to reach the endpoint, so the firewall must allow Docusign's requests (or the endpoint must be exposed through an API proxy).

**Why this answer and not the others:** A is right because Docusign is the caller and must get through the firewall. The trap is B: it reverses the direction; the endpoint is called by Docusign, not calling Docusign. C applies to browser calls, and D blocks the very server-to-server calls Docusign makes.

**Option notes:**
- A. Correct. The firewall must let Docusign's requests reach the endpoint.
- B (TRAP). Outbound calls to Docusign are the reverse direction; extension actions are inbound calls from Docusign.
- C. CORS governs browser JavaScript, not Docusign's server-to-server calls.
- D. Docusign's servers, not signers' browsers, call the action endpoint.

**Q89. (API Authentication - JWT Grant) [HIGH]** A nightly job uses a dedicated system sender account. Consent was granted once, but no one will be available to sign in when the job runs. The team suggests Confidential Auth Code Grant with refresh tokens instead. Which option should the team keep?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** With consent already granted and no user available at runtime, JWT Grant is the recommended flow; it gets a fresh token by signing a new assertion.

**Why this answer and not the others:** B is right because JWT needs only prior consent, not a sign-in at runtime. The trap is A: refresh tokens can extend a confidential session, but the flow still starts with a user sign-in and the refresh token eventually expires, which then needs a person again. C and D are interactive browser flows.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant needs a user sign-in to start, and refresh tokens expire after up to 30 days, so it cannot run unattended indefinitely.
- B. Correct. JWT Grant is designed for unattended service integrations after one-time consent.
- C. Public Auth Code Grant with PKCE requires an interactive user and has a 24-hour refresh token.
- D. Implicit Grant is a legacy interactive browser flow.

**Q90. (Go Live Process - Templates in production) [MEDIUM]** A team has gone live and wants the production app to behave as it did in development. Besides OAuth settings and endpoints, what must they migrate to the production account?

A. Nothing; Go-Live copies the whole developer account into production
B. Only the envelopes that were sent during testing
C. Users, templates and the account settings the app relied on
D. Only the integration key's Connect failure logs

**Answer:** C. Users, templates and the account settings the app relied on

**Explanation:** Production account settings and data are separate from developer account data, so users, templates and settings must be added to production with Docusign Admin or the eSignature REST API.

**Why this answer and not the others:** C is right because only the integration key is duplicated by Go-Live. The trap is A: it is easy to assume Go-Live copies the account, but it copies only the key (not even its secrets). B is wrong because test envelopes are not migrated (and demo envelopes are not legally binding), and D is not something an app needs to run.

**Option notes:**
- A (TRAP). Go-Live duplicates only the integration key; account data and settings stay in the developer account.
- B. Test envelopes are not migrated, and demo envelopes are not legally binding anyway.
- C. Correct. Users, templates and account settings must be recreated in the production account.
- D. Logs are diagnostic data; they are not what the production app needs to function.

**Q91. (Docusign Connect - Configuration level) [MEDIUM]** An organization admin must send events from three of the organization's five accounts to one listener, managed from a single place. Which option should be used?

A. Account-level Connect set up in eSignature Admin of one account
B. Organization-level Connect scoped to the selected accounts
C. eventNotification added by each sending application
D. An organization-level configuration using legacy XML aggregate messages

**Answer:** B. Organization-level Connect scoped to the selected accounts

**Explanation:** Organization-level Connect can listen to all or selected accounts in the organization and is set up in Organization Admin or by API.

**Why this answer and not the others:** B is right because org-level Connect supports selecting specific accounts in one configuration. The trap is D: org-level is the right level, but organization-level configurations always use JSON SIM, so legacy XML and aggregate mode are not available there. A covers only one account, and C misses envelopes sent from the web app.

**Option notes:**
- A. An account-level configuration covers only the account it is created in.
- B. Correct. Organization-level Connect can target all or selected accounts from one configuration.
- C. eventNotification is per envelope and API only, so web-app sends would be missed.
- D (TRAP). Organization-level configurations always use JSON SIM; legacy XML and aggregate are account and envelope level only.

**Q92. (eSignature API - Anchor tabs) [MEDIUM]** A developer uses the direct documents model to send a PDF contract and wants tabs to stay correctly placed even if minor revisions shift the page text. What is the recommended tab placement strategy?

A. anchorString with anchorUnits and anchorXOffset/anchorYOffset
B. Docusign AI automatic tab placement
C. Retrieve field values from a web form
D. xPosition and yPosition fixed positioning

**Answer:** A. anchorString with anchorUnits and anchorXOffset/anchorYOffset

**Explanation:** Anchor (string-based) tagging places tabs relative to text in the document, so when text moves the tabs move with it; offsets and anchorUnits fine-tune the position.

**Why this answer and not the others:** A is right because anchor tabs follow the anchor text when content shifts. The trap is D: fixed positioning is a valid way to place tabs, but it uses absolute coordinates that no longer line up after a revision. B is not the documented placement strategy for API-sent documents and C supplies values, not positions.

**Option notes:**
- A. Correct. Anchor tags with offsets keep tabs next to their anchor text when the document changes.
- B. Automatic AI placement is not the recommended API strategy for keeping tabs aligned to text.
- C. A web form can supply field values, but it does not decide where tabs sit on the document.
- D (TRAP). Fixed x and y coordinates stay at the same spot even when the text they belong to moves.

**Q93. (eSignature Features and Web Forms - Embedded signing) [HIGH]** A developer creates 100 web form instances for participants in an internal compliance process using the Web Forms API, and the internal system must map and track each instance back to the individual user record. Which parameter must be supplied in the Instances:createInstance request?

A. The web form configuration ID, for one-to-one mapping
B. The participant's email address as the unique key for all Docusign objects
C. A unique clientUserId value generated by the developer's internal systems
D. The API account ID to distinguish instances

**Answer:** C. A unique clientUserId value generated by the developer's internal systems

**Explanation:** Each instance needs its own identifier from the internal system, and that is clientUserId.

**Why this answer and not the others:** C is right because a developer-generated clientUserId maps each instance to one user record. The trap is A: it is a real Web Forms identifier, but every instance shares it. B and D fail because email is not a Docusign-wide unique key and the account ID is the same for the whole account.

**Option notes:**
- A (TRAP). All 100 instances are created from the same configuration, so its ID is shared and cannot map to individual users.
- B. Email is not a unique key for Docusign objects and is not the identifier createInstance uses for embedded instances.
- C. Correct. clientUserId is the developer-supplied identifier for the user in your system, which gives a one-to-one mapping to the user record.
- D. The account ID is the same for every instance in the account; it identifies the account, not a participant.

**Q94. (Agreement Manager API - Agreement list) [HIGH]** A nightly job must pick up every agreement in Agreement Manager, including imported legacy ones, and then pull full detail for each new agreement. Which design fits?

A. Call Agreements:getAgreement with a wildcard agreementId
B. Call Agreements:getAgreementsList to enumerate agreements, then Agreements:getAgreement for each new one
C. Rely on Connect envelope-completed events to find new agreements
D. Call Agreements:createAgreementSummary for each agreement to get its detail

**Answer:** B. Call Agreements:getAgreementsList to enumerate agreements, then Agreements:getAgreement for each new one

**Explanation:** Listing agreements finds every record in the repository, whatever its origin, and getAgreement then retrieves full detail for each new one.

**Why this answer and not the others:** B is right because only the agreement list covers all repository records. The trap is C: Connect does report completed envelopes, but imported legacy agreements never had an envelope, so they would be missed. A is invalid because getAgreement needs a specific ID, and D returns AI summaries rather than the structured detail.

**Option notes:**
- A. getAgreement takes one specific agreementId; it does not accept wildcards.
- B. Correct. Enumerate with the list call, then get detail for each new agreement.
- C (TRAP). Envelope events miss imported legacy agreements, which never went through eSignature.
- D. Summaries are AI-written text, not the structured agreement detail.

**Q95. (Workflow Builder and Workflow API - Identity step) [MEDIUM]** An HR onboarding workflow starts with the candidate entering address and tax information. The candidate must then complete identity verification before any signing package is released. Which step order matches?

A. Verify Someone's Identity, then Collect Data with Web Forms
B. Collect Data with Web Forms, then Verify Someone's Identity
C. Send Documents for Signature, then Verify Someone's Identity
D. Collect Data with Web Forms, then Send Documents for Signature without verification

**Answer:** B. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** The stem says the workflow starts with data entry and verifies identity before signing, so the form comes first, then the identity step, then signing.

**Why this answer and not the others:** B is right because it follows the stated business order. The trap is A: verifying identity before a form is a valid pattern when sensitive pre-filled data must be protected, but here the workflow is defined to start with data entry. C releases the signing package before verification, and D skips verification.

**Option notes:**
- A (TRAP). A valid pattern in other cases, but this workflow must start with the candidate's data entry.
- B. Correct. Collect the data first, then verify identity before signing.
- C. Signing happens before verification, which the requirement forbids.
- D. Skips the required identity verification step.

**Q96. (App Center and Extension Apps - API proxy) [MEDIUM]** A third-party API used by an extension app accepts XML payloads, but Docusign requires the external response in a specific JSON schema. What should the developer deploy to handle the translation?

A. An OAuth 2.0 identity provider
B. A Docusign Connect listener
C. An API proxy
D. Concerto type definitions in the manifest

**Answer:** C. An API proxy

**Explanation:** An API proxy sits between Docusign and the third-party service and transforms XML to the required JSON (and back).

**Why this answer and not the others:** C is right because the proxy performs format translation. The trap is D: Concerto describes data types for Data IO and connected fields, but it does not convert XML responses. A handles authorization, and B receives event notifications.

**Option notes:**
- A. An identity provider issues tokens; it does not translate payloads.
- B. A Connect listener receives envelope events; it does not translate extension calls.
- C. Correct. An API proxy translates the XML API to the JSON schema Docusign expects.
- D (TRAP). Concerto models data types; it does not translate an API's XML into JSON.

**Q97. (API Authentication - Consent) [MEDIUM]** A JWT integration will impersonate a system user to send envelopes. Before the first token request, which consent must that user (or an admin) grant?

A. Consent for the integration key covering the signature and impersonation scopes
B. Consent for the signature scope only
C. No consent; adding impersonation to the JWT assertion is enough
D. Consent for the extended scope so a refresh token is issued

**Answer:** A. Consent for the integration key covering the signature and impersonation scopes

**Explanation:** JWT consent must include impersonation, which authorizes the app to act as the user, plus the API scope it needs such as signature.

**Why this answer and not the others:** A is right because JWT impersonation needs consent to both signature and impersonation. The trap is B: signature covers eSignature calls, but without impersonation the app is not allowed to act as the user. C misunderstands consent, which must be granted by the user or an admin, and D applies only to Auth Code flows because JWT never returns a refresh token.

**Option notes:**
- A. Correct. Consent to signature and impersonation lets the app request tokens as that user.
- B (TRAP). signature alone does not authorize the app to impersonate the user, so JWT requests would still fail.
- C. Listing impersonation in the assertion does not replace consent from the user or an admin.
- D. extended controls the refresh-token lifecycle in Auth Code flows; JWT never returns a refresh token.

**Q98. (Go Live Process - Post go-live) [HIGH]** An app that uses JWT Grant has just gone live. Which production setup lets it obtain access tokens?

A. Reuse the developer RSA private key, because it was copied with the key
B. Add an RSA key pair to the production key and obtain consent in production
C. Add a secret key only, because JWT Grant does not use RSA keys
D. Switch to Authorization Code Grant, because JWT Grant needs a separate review

**Answer:** B. Add an RSA key pair to the production key and obtain consent in production

**Explanation:** For JWT Grant apps, the After Go-Live guidance says to add RSA key pairs (and redirect URIs as needed for consent) on the production key; consent must also be granted in production.

**Why this answer and not the others:** B is right because RSA keys are not copied and production consent is separate. The trap is A: the key value is the same in production, but its RSA keys are not duplicated. C confuses JWT with Authorization Code Grant, and D is wrong because JWT Grant apps go live through the same process.

**Option notes:**
- A (TRAP). RSA key pairs are not duplicated with the key; a new pair must be added in production.
- B. Correct. Add an RSA key pair in production and grant consent (individual or admin) in production.
- C. JWT Grant signs its assertion with an RSA private key; a secret alone is not enough.
- D. JWT Grant apps go live through the same Go-Live process; no flow change is needed.

**Q99. (Docusign Connect - JSON SIM) [HIGH]** A new integration's listener should receive small, event-focused messages and be able to subscribe to the widest range of event types. Which message format should the Connect configuration use?

A. JSON SIM format
B. Legacy XML with aggregate mode to reduce message count
C. Legacy XML SIM matching the SOAP object model
D. XML messages that always include the full envelope summary

**Answer:** A. JSON SIM format

**Explanation:** JSON SIM is event-focused: messages are smaller, customizable and easier to process, and it supports more event types, so Docusign recommends it for all apps.

**Why this answer and not the others:** A is right because the clues (small, event-focused, more event types) describe Connect 2.0. The trap is B: aggregate mode reduces the number of messages, but it is a legacy XML option and messages stay envelope-focused. C is only worth considering for an existing SOAP integration, and D is the opposite of a small payload.

**Option notes:**
- A. Correct. JSON SIM sends smaller, event-focused messages and supports more event types.
- B (TRAP). Aggregate mode cuts message count but is legacy XML with envelope-focused payloads.
- C. Legacy XML SIM suits existing SOAP integrations, not a new app needing small messages.
- D. Including the full envelope summary in every message makes payloads larger, not smaller.

**Q100. (eSignature API - Embedded sending) [MEDIUM]** A sender must prepare and edit an envelope from inside a custom app before it is sent. Which endpoint provides that experience?

A. EnvelopeViews:createRecipient
B. EnvelopeViews:createSender
C. Envelopes:update with status sent
D. clientUserId on the sender

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses EnvelopeViews:createSender on a draft envelope, giving a sender view URL where the user tags and sends inside the app.

**Why this answer and not the others:** B is right because the sender view is the embedded preparation experience. The trap is A: createRecipient is also an embedded view, but it opens a signing session for a recipient. C sends without any preparation step and D is a recipient property for embedded signing.

**Option notes:**
- A (TRAP). createRecipient opens the signing ceremony for a recipient, not the sender's preparation view.
- B. Correct. EnvelopeViews:createSender returns a sender view for tagging and sending inside the app.
- C. Updating to sent sends the envelope immediately with no chance to prepare it in the app.
- D. clientUserId marks embedded recipients for signing; it does not give a sender a preparation view.

**Q101. (eSignature Features and Web Forms - Recipient authentication) [MEDIUM]** Sofia's integration must make signers enter a code that Docusign sends to their mobile phone before they can access the envelope. Which recipient authentication method applies?

A. Knowledge-based authentication (KBA)
B. Phone authentication
C. Access code
D. ID verification with a government photo ID

**Answer:** B. Phone authentication

**Explanation:** A code sent by Docusign to the signer's phone is phone authentication.

**Why this answer and not the others:** B is right because phone authentication is the method where Docusign sends the code to the phone. The trap is A: KBA is a well-known stronger recipient authentication option, but it uses questions, not codes. C and D fail because an access code is sender-defined and shared out of band, and IDV checks an ID document.

**Option notes:**
- A (TRAP). KBA challenges the signer with questions from public records (US only); no code is sent to the phone.
- B. Correct. Phone authentication sends a code by SMS or call; the recipient must enter it to access the envelope.
- C. The sender defines the access code and must share it out of band; Docusign does not send it to the phone.
- D. IDV checks an identity document, which is heavier than needed and does not match the code-to-phone requirement.

**Q102. (Agreement Manager API - Legacy import) [MEDIUM]** After an acquisition, 5,000 contracts signed in another vendor's tool must appear in Agreement Manager search results with extracted data. Which capability fits?

A. Bulk import the acquired contracts into Agreement Manager
B. Send them through eSignature Bulk Send so they become agreements
C. Call Agreements:createAgreementSummary on each contract file
D. Save each contract as an eSignature template

**Answer:** A. Bulk import the acquired contracts into Agreement Manager

**Explanation:** Bulk import is how existing, non-Docusign agreements enter Agreement Manager, where AI extraction runs on them.

**Why this answer and not the others:** A is right because the contracts are already signed and only need to be added to the repository. The trap is B: Bulk Send is also a bulk eSignature feature, but it sends new envelopes for signing, which is not needed for already-executed contracts. C works only on agreements already in Agreement Manager, and D creates reusable sending templates, not agreement records.

**Option notes:**
- A. Correct. Bulk import brings the acquired contracts into Agreement Manager for AI extraction.
- B (TRAP). Bulk Send sends new envelopes for signature; it is not an import of signed contracts.
- C. Summaries can only be created for agreements already in Agreement Manager.
- D. Templates are reusable sending blueprints, not agreement records.

**Q103. (Workflow Builder and Workflow API - Extension step) [MEDIUM]** An ISV is building a new extension app so Maestro workflows can save completed agreements to its cloud storage service. Which extension type should it build?

A. A connected fields extension
B. A file output cloud storage extension
C. A file archive extension
D. A bank account verification extension

**Answer:** B. A file output cloud storage extension

**Explanation:** File output cloud storage is the extension type for saving files from Maestro workflows, and it is the one to use for new apps.

**Why this answer and not the others:** B is right because the app is new and stores workflow files. The trap is C: file archive does the same job, but it is the legacy type and new apps should use file output cloud storage. A is not supported in Maestro, and D verifies bank data rather than storing files.

**Option notes:**
- A. Connected fields verify tab data in eSignature and are not supported in Maestro.
- B. Correct. File output cloud storage is the current extension type for saving workflow files.
- C (TRAP). File archive is legacy; new apps should use file output cloud storage.
- D. Bank account verification checks account data; it does not store documents.

**Q104. (App Center and Extension Apps - Data IO) [HIGH]** A Maestro workflow must read and write structured records in a customer's system of record. Which extension type fits?

A. File IO (file output cloud storage)
B. Connected Fields
C. Data Verification
D. Data IO

**Answer:** D. Data IO

**Explanation:** Data IO extensions read data from and write data to a system of record from Maestro workflows.

**Why this answer and not the others:** D is right because the requirement is structured record read/write in a workflow. The trap is B: connected fields also talk to a system of record, but for field verification in eSignature, and they are not supported in Maestro. A writes documents, not records, and C verifies standard data types.

**Option notes:**
- A. File IO writes documents to storage, not structured records.
- B (TRAP). Connected fields verify field values in eSignature and are not supported in Maestro.
- C. Data Verification checks standard values like addresses; it does not read/write records.
- D. Correct. Data IO reads and writes system-of-record data from Maestro workflows.

**Q105. (API Authentication - Scopes) [MEDIUM]** An app only needs to send envelopes and read user account information. A developer adds signature, extended, and aow_manage in case new features are added later. What should the developer do when requesting consent?

A. Keep all three so future features need no re-consent
B. Request impersonation only, because it includes signature
C. Reuse the scope list from the team's other integration key
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Scopes should match the operations the app performs today; extra scopes such as aow_manage (Maestro) widen access without a current need.

**Why this answer and not the others:** D is right because least privilege means requesting only what current operations require. The trap is A: avoiding future re-consent sounds practical, but it grants Maestro access and long-lived refresh tokens the app does not use. B is wrong because impersonation does not include signature, and C copies scopes that may not match this app.

**Option notes:**
- A (TRAP). This over-requests: aow_manage and extended give access the app does not currently use.
- B. impersonation lets an app act as a user through JWT; it does not include the signature API scope.
- C. Another integration's scopes reflect its own operations, not this app's needs.
- D. Correct. Request only the scopes needed for sending envelopes and reading account info.

**Q106. (Go Live Process - Templates in production) [MEDIUM]** Nadia completed Go-Live for an app that uses the template reference model to create envelopes. What template work must she do so the app works in production as it did in development?

A. Convert the code to composite templates, because the template reference model is not supported in production
B. Delete the developer template first, then rebuild it in production and update the template ID
C. Reference the same template ID, because templates were deployed to production during Go-Live
D. Deploy the template to production, then update the app to use the new production template ID

**Answer:** D. Deploy the template to production, then update the app to use the new production template ID

**Explanation:** Templates are not copied during Go-Live; you must add the template to the production account, which gives it a new production template ID, and point the app at that ID.

**Why this answer and not the others:** D is right because the production template has its own ID. The trap is B: rebuilding in production and updating the ID is reasonable, but deleting the developer template is unnecessary, since the developer key and data keep working for testing. A is wrong because the template reference model works in production, and C is wrong because Go-Live copies only the integration key.

**Option notes:**
- A. The template reference model is fully supported in production.
- B (TRAP). Deleting the developer template is not required; the developer environment stays in use for testing.
- C. Go-Live does not deploy templates, so there is no automatically deployed ID to reference.
- D. Correct. Add the template to production and update the app to its new production template ID.

**Q107. (Docusign Connect - Security) [MEDIUM]** A listener sits behind an API gateway that rejects any request without an Authorization header. Which account-level Connect security option satisfies the gateway?

A. Put a username and password in the listener URL query string
B. Send the integration key in the eventNotification object
C. HMAC signatures in X-DocuSign-Signature headers only
D. Basic authentication or OAuth 2.0 for Connect on the configuration

**Answer:** D. Basic authentication or OAuth 2.0 for Connect on the configuration

**Explanation:** Basic authentication adds a username and password header, and OAuth for Connect sends an access token in the Authorization header with every message.

**Why this answer and not the others:** D is right because both options put credentials in the Authorization header the gateway checks. The trap is C: HMAC is a strong control, but its values go in X-DocuSign-Signature headers, not the Authorization header, so the gateway would still reject the request. A exposes credentials in the URL, and B is not a Connect authentication mechanism.

**Option notes:**
- A. Credentials in a query string are exposed in logs and are not a Connect security feature.
- B. The integration key identifies an app for API auth; it does not authenticate Connect messages.
- C (TRAP). HMAC uses X-DocuSign-Signature headers, not an Authorization header.
- D. Correct. Basic auth and OAuth for Connect both send credentials in the Authorization header.

**Q108. (eSignature API - Bulk send) [MEDIUM]** A developer needs to send separate, personalized copies of the same envelope to thousands of recipients, each signing their own copy. Which feature is designed for that?

A. Bulk Send (bulk send list applied to a draft envelope)
B. Envelopes:create called in a loop with transactionId
C. One envelope with all recipients at the same routing order
D. A composite template with one inline template per recipient

**Answer:** A. Bulk Send (bulk send list applied to a draft envelope)

**Explanation:** Bulk Send creates one envelope per recipient from a bulk send list and a draft envelope or template, processed from a queue. The clue is a separate copy per recipient.

**Why this answer and not the others:** A is right because Bulk Send is built for many personalized copies. The trap is C: parallel routing does send to many recipients at once, but they all sign one shared envelope instead of their own copy. B reimplements bulk sending in custom code and D still builds one envelope.

**Option notes:**
- A. Correct. Bulk Send generates a separate envelope for each recipient on the bulk send list.
- B. Looping Envelopes:create rebuilds bulk sending in custom code and consumes many API calls.
- C (TRAP). Same routing order means parallel signing on one envelope, not separate copies.
- D. A composite template still produces a single envelope, not one envelope per recipient.

**Q109. (eSignature Features and Web Forms - Brand destination URLs) [LOW]** A financial-aid office sends envelopes by email. After a student finishes signing, they should be redirected to the office's help page. Which option should be used?

A. Brand destination URLs
B. returnUrl in EnvelopeViews:createRecipient
C. Branding signing resource file
D. A Connect webhook

**Answer:** A. Brand destination URLs

**Explanation:** Email-delivered signing is remote signing, so the redirect is a brand destination URL.

**Why this answer and not the others:** A is right because brand destination URLs are the redirect setting for remote signers. The trap is B: it is a real redirect setting, but only for embedded signing. C and D fail because resource files change appearance and Connect is a server notification.

**Option notes:**
- A. Correct. Destination URLs on a brand redirect remote signers after events such as signing complete; apply the brand with brandId.
- B (TRAP). returnUrl applies to embedded signing sessions only, not to email (remote) signing.
- C. Resource files customize the text and appearance of the signing experience; they do not set the redirect destination.
- D. Connect sends event notifications to your server and cannot redirect a browser.

**Q110. (Agreement Manager API - Agreement documents) [MEDIUM]** An audit export must include extracted metadata and the signed file for every agreement of a given type. The agreement IDs are not known in advance. Which plan is correct?

A. Agreements:getAgreementsList to find them, Agreements:getAgreement for data, then a separate document download
B. Agreements:getAgreement alone, because it returns metadata and the file
C. Agreements:createAgreementSummary for each agreement, used as the audit copy
D. Agreements:getAgreementsList alone, because its response includes each file

**Answer:** A. Agreements:getAgreementsList to find them, Agreements:getAgreement for data, then a separate document download

**Explanation:** The IDs are unknown, so listing comes first; getAgreement then returns the extracted data, and the file needs a separate document download.

**Why this answer and not the others:** A is right because it covers all three needs: finding records, reading data, and getting the file. The trap is B: getAgreement does provide the metadata, but it needs a known ID and does not return the document file. C replaces the signed file with AI-written text, and D wrongly assumes the list response carries the documents.

**Option notes:**
- A. Correct. List to find agreements, getAgreement for extracted data, and a separate download for the file.
- B (TRAP). getAgreement needs a known ID and returns extracted data, not the signed file.
- C. An AI summary is not an acceptable audit copy of the signed agreement.
- D. The list response contains agreement records, not document files.

**Q111. (Workflow Builder and Workflow API - Branching) [MEDIUM]** A workflow must route by a Job Location field with three values: US, Canada, and Other. If the value is blank or unexpected, HR must be emailed. Which configuration fits?

A. A Multi Branch Rule step with a path per value plus a No Conditions Met path to a Send an Email step
B. A Branching Rule step that tests only Job Location = US (true or false)
C. Three separate published workflows, with participants choosing which to start
D. A Show a Confirmation Screen step telling the participant to restart

**Answer:** A. A Multi Branch Rule step with a path per value plus a No Conditions Met path to a Send an Email step

**Explanation:** A Multi Branch Rule step creates several paths from one field and includes a No Conditions Met path, which can notify HR with a Send an Email step.

**Why this answer and not the others:** A is right because it handles three values plus a fallback in one step. The trap is B: a single Branching Rule gives only true and false paths, so Canada, Other and blank values would all fall into one path. C duplicates the process and relies on the participant to choose correctly, and D never notifies HR.

**Option notes:**
- A. Correct. One path per location, and No Conditions Met emails HR for blank or unexpected values.
- B (TRAP). A two-way branch cannot separate Canada, Other and blank values.
- C. Duplicating workflows adds maintenance and depends on users choosing correctly.
- D. A confirmation screen does not route the process or notify HR.

**Q112. (App Center and Extension Apps - File IO) [HIGH]** A Maestro workflow needs to save completed documents to an external repository using an installable extension app. Which extension type fits?

A. Connected Fields
B. Data Verification
C. File IO (file output cloud storage)
D. Data IO with CreateRecord

**Answer:** C. File IO (file output cloud storage)

**Explanation:** File IO extensions write documents to cloud storage from Maestro workflows.

**Why this answer and not the others:** C is right because the requirement is storing documents. The trap is D: Data IO also writes to external systems, but it writes structured records, not files. A and B verify field values during preparation and signing.

**Option notes:**
- A. Connected fields verify field values in eSignature, not file storage.
- B. Data Verification checks standard values such as addresses.
- C. Correct. File IO (file output cloud storage) writes documents to external storage.
- D (TRAP). Data IO writes records, not documents.

**Q113. (API Authentication - User info) [MEDIUM]** An implementation note must tell developers where to get the account ID and base URI after an access token is issued. Which endpoint should it name?

A. /oauth/token
B. The coid claim of the ID token
C. /oauth/userinfo
D. /oauth/auth

**Answer:** C. /oauth/userinfo

**Explanation:** /oauth/userinfo, called with the access token, returns the accounts with their account_id and base_uri values.

**Why this answer and not the others:** C is right because userinfo is the endpoint that returns account context. The trap is A: the token endpoint is the step just before, but its response contains tokens and expiry, not accounts. B lists organizations that granted admin consent, and D starts sign-in and consent.

**Option notes:**
- A (TRAP). /oauth/token returns access and refresh tokens, not account IDs or base URIs.
- B. coid lists organizations that granted admin consent; it does not give account IDs or base URIs.
- C. Correct. /oauth/userinfo returns account_id and base_uri for each of the user's accounts.
- D. /oauth/auth starts the sign-in and consent step; it does not return account context.

**Q114. (Go Live Process - API limits) [HIGH]** An integration cannot use Connect and must poll envelope status. What is the most frequent polling allowed for a single envelope?

A. Once every 15 minutes
B. Once every minute
C. Once every 5 minutes
D. Once per hour for the whole account

**Answer:** A. Once every 15 minutes

**Explanation:** Docusign limits status polling to at most one request per envelope every 15 minutes; violating it can fail Go-Live review.

**Why this answer and not the others:** A is right because the polling rule is once per 15 minutes per envelope. The trap is C: it sounds conservative, but 5 minutes is still three times the allowed rate. B is far too frequent, and D wrongly applies the rule per account instead of per envelope.

**Option notes:**
- A. Correct. Poll a given envelope no more than once every 15 minutes.
- B. Polling every minute is 15 times the allowed rate and hurts the efficiency score.
- C (TRAP). Every 5 minutes still exceeds the once-per-15-minutes rule.
- D. The rule is per envelope, not one poll per hour for the whole account.

**Q115. (Docusign Connect - Retries) [HIGH]** Which listener responses does Docusign Connect treat as failed deliveries to be retried?

A. Only HTTP 5xx responses; 4xx responses are final
B. Only network connection failures
C. Any non-2xx response or a timeout
D. None; Connect delivers each event once

**Answer:** C. Any non-2xx response or a timeout

**Explanation:** Any response outside the 2xx range, or no response before the timeout, counts as a failure and the event is retried.

**Why this answer and not the others:** C is right because only a 2xx response acknowledges the message. The trap is A: many HTTP clients treat 4xx as non-retryable, but Connect retries any non-2xx response. B ignores error responses and timeouts, and D ignores Connect's retry process entirely.

**Option notes:**
- A (TRAP). Connect does not distinguish 4xx from 5xx; both are failures and are retried.
- B. Error status codes and timeouts are also failures, not only connection errors.
- C. Correct. Non-2xx responses and timeouts are failures that Connect retries.
- D. Connect retries failed deliveries with exponential back-off.

**Q116. (eSignature API - Envelope create) [HIGH]** An Envelopes:create request contains documents, recipients and an emailSubject, and must go out to recipients without any further API call. Which status value belongs in the request?

A. created
B. delivered
C. completed
D. sent

**Answer:** D. sent

**Explanation:** With the direct documents model, status sent sends the envelope in the same call. The clue is 'without any further API call', which rules out creating a draft first.

**Why this answer and not the others:** D is right because sent delivers the envelope immediately. The trap is A: created is accepted by Envelopes:create but leaves a draft that needs a second call to send. B and C are statuses Docusign assigns as recipients open and finish the envelope; the sender does not set them.

**Option notes:**
- A (TRAP). created builds a draft envelope; a later update to sent would be needed, which the stem rules out.
- B. delivered is set by Docusign when a recipient opens the envelope; the integration cannot request it on create.
- C. completed is set by Docusign after all recipients finish; it is not a value used to send an envelope.
- D. Correct. status sent sends the envelope to recipients as soon as Envelopes:create succeeds.

**Q117. (eSignature Features and Web Forms - Connected Fields) [MEDIUM]** Grace's app must send an envelope whose fields are verified against an external system through a Connected Fields extension. Which API sequence creates and sends it?

A. Envelopes:create first, then GetConnectedFieldsTabGroups to attach extensionData
B. AccountSignatureProviders:list, then recipientSignatureProviders on the signer
C. Configurations:getForm, then formValues on Instances:createInstance
D. TabInfo:GetConnectedFieldsTabGroups, put the data in each tab's extensionData, then Envelopes:create

**Answer:** D. TabInfo:GetConnectedFieldsTabGroups, put the data in each tab's extensionData, then Envelopes:create

**Explanation:** Connected Fields are sent by getting the tab groups, filling each tab's extensionData, then calling Envelopes:create.

**Why this answer and not the others:** D is right because it follows the documented order: GetConnectedFieldsTabGroups, extensionData, Envelopes:create. The trap is A: it names the right calls but reverses the order, so the tabs would be created without their extension data. B and C fail because they configure SBS signature providers and web form prefill.

**Option notes:**
- A (TRAP). The steps are right but the order is wrong: the extensionData must be on the tabs when the envelope is created.
- B. This sets up EU standards-based signatures, not connected fields.
- C. This prefills a web form instance; it does not create connected fields on an envelope.
- D. Correct. This is the documented Connected Fields send flow: get the tab groups, populate extensionData on each tab, then create the envelope.

**Q118. (Agreement Manager API - Agreement data) [HIGH]** Which endpoint returns the full structured data of one specific agreement so it can be sent to an external system?

A. Agreements:createAgreementSummary
B. Workflows:getWorkflowsList
C. Agreements:getAgreementsList
D. Agreements:getAgreement

**Answer:** D. Agreements:getAgreement

**Explanation:** Agreements:getAgreement returns one agreement's full structured record (type, parties, provisions) for sending to an external system.

**Why this answer and not the others:** D is right because the question asks for one specific agreement's full data. The trap is C: getAgreementsList also returns agreement data, but it is the search and index step across many agreements, not the single-record call. A generates an AI prose summary, and B lists Workflow Builder workflows, which have nothing to do with agreement data.

**Option notes:**
- A. Generates an AI-written summary of an agreement, not its structured fields.
- B. Lists Maestro workflow definitions; it returns no agreement data.
- C (TRAP). Lists agreements across the account; it is the search step, not the single-agreement retrieval.
- D. Correct. getAgreement returns the full structured data of one agreement.

**Q119. (Workflow Builder and Workflow API - Start method) [HIGH]** A citizen-services portal shows a 'Start application' button. The portal is a static page with no backend, and applicants should start the Maestro workflow themselves by opening a URL. Which start method matches?

A. Started by an envelope-completed event
B. From a link
C. Manually in Docusign by an administrator
D. From an API call with trigger_inputs

**Answer:** B. From a link

**Explanation:** From a link provides a URL that starts a new workflow instance when opened, designed for self-service workflows started by participants.

**Why this answer and not the others:** B is right because applicants open a URL themselves and the portal has no backend. The trap is D: From an API call is the method for passing starting values, but it needs server code with an OAuth token, which the static portal lacks. A is not how this workflow is started, and C needs an internal user to press Run Workflow.

**Option notes:**
- A. The applicant starts this process; it is not a reaction to a completed envelope.
- B. Correct. The workflow link starts a new instance when the applicant opens it.
- C. Manual start is done by internal users, not by public applicants.
- D (TRAP). An API trigger needs a backend with an access token; the portal has none.

**Q120. (App Center and Extension Apps - Connections) [HIGH]** A developer configures an extension app connection using OAuth 2.0 Authorization Code Grant. Which four values must come from the external API service or identity provider?

A. Publisher name, app name, short description and long description
B. Client ID, client secret, token URL and authorization URL
C. Client ID, public key, JWT and authorization URL
D. Integration key, API account ID, redirect URI and Docusign scopes

**Answer:** B. Client ID, client secret, token URL and authorization URL

**Explanation:** Authorization Code Grant needs the client ID, client secret, token URL and authorization URL from the external provider.

**Why this answer and not the others:** B is right because those are the provider values for an Authorization Code connection. The trap is D: those are Docusign-side values for your app calling Docusign, the opposite direction. A are listing details and C mixes in JWT Grant artifacts.

**Option notes:**
- A. These are App Center listing details, not OAuth parameters.
- B. Correct. Client ID, client secret, token URL and authorization URL come from the external provider.
- C. Public keys and JWTs belong to JWT Grant, not an Authorization Code connection.
- D (TRAP). These identify your app to Docusign; the connection authenticates Docusign to the external API.

**Q121. (API Authentication - OAuth flow selection) [HIGH]** A single-page application runs entirely in the user's browser to send documents, so a secret cannot be stored securely. Which OAuth flow does Docusign recommend for authenticating individual users?

A. Confidential Authorization Code Grant
B. Implicit Grant
C. JSON Web Token Grant
D. Public Authorization Code Grant with PKCE

**Answer:** D. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended flow for clients that cannot store a secret while still authenticating each user interactively.

**Why this answer and not the others:** D is right because the SPA cannot keep a secret and users sign in. The trap is B: Implicit Grant was the historical SPA answer but is legacy because it exposes the token in the redirect URL. A needs a secret the browser cannot protect, and C is for unattended service accounts.

**Option notes:**
- A. Confidential Auth Code Grant requires a securely stored client secret, which a pure browser SPA cannot provide.
- B (TRAP). Implicit Grant was the old SPA answer but is legacy; Docusign recommends the PKCE code flow instead.
- C. JWT Grant is for unattended service integrations, not for authenticating individual interactive users.
- D. Correct. Browser-only client with interactive users: Public Authorization Code Grant with PKCE.

**Q122. (Go Live Process - Troubleshooting) [HIGH]** After a developer submits Go-Live and selects the production account, the key shows the status Pending approval. What does this mean?

A. The request failed and must be resubmitted with a different integration type
B. The app must make more eSignature API calls before review starts
C. The production account must be upgraded before review can begin
D. The integration needs manual approval, which may take up to 48 hours

**Answer:** D. The integration needs manual approval, which may take up to 48 hours

**Explanation:** The course defines Pending approval as a manual approval process that may take up to 48 hours; App is live means the key is already available in production.

**Why this answer and not the others:** D is right because Pending approval signals manual review. The trap is A: if issues are found you are asked to make corrections, but Pending approval itself is not a failure. B refers to the removed 20 API call requirement, and C is not what the status means.

**Option notes:**
- A (TRAP). Pending approval is not a rejection; you are asked for corrections only if review finds issues.
- B. There is no longer a required number of API calls before Go-Live.
- C. The status does not indicate a plan upgrade; it indicates manual review.
- D. Correct. Pending approval means manual review, which may take up to 48 hours.

**Q123. (Docusign Connect - Troubleshooting) [MEDIUM]** Connect logs show the same event delivered twice after the listener timed out on the first attempt. What should the integration do?

A. Spend longer processing before returning 200
B. Idempotent processing based on event identifiers or envelope state
C. Return a non-2xx response to the second copy to reject it
D. Switch to envelope-level eventNotification to guarantee single delivery

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** The timeout caused a retry, so the same event arrived twice; idempotent processing keeps the second copy from changing anything.

**Why this answer and not the others:** B is right because duplicates are expected after timeouts and retries. The trap is C: rejecting the copy with a non-2xx response is itself a failure, so Connect retries again. A makes timeouts more likely, and D does not help because envelope-level webhooks follow the same delivery and retry behavior.

**Option notes:**
- A. Slower responses cause more timeouts and therefore more retries.
- B. Correct. Detect already-processed events so redelivery has no effect.
- C (TRAP). Any non-2xx response counts as a failed delivery and is retried.
- D. Envelope-level webhooks do not guarantee single delivery.

**Q124. (eSignature API - Draft envelope) [HIGH]** An app will call EnvelopeViews:createSender so a user can tag the envelope inside the app before it goes out. Which status must the envelope have when it is created?

A. sent
B. delivered
C. created
D. completed

**Answer:** C. created

**Explanation:** Embedded sending works on a draft envelope, so the envelope is created with status created and then opened in the sender view. The clue is that the user still has to tag it before it goes out.

**Why this answer and not the others:** C is right because the sender view is requested for a draft envelope created with status created. The trap is A: sent is the usual create value, but a sent envelope is already out of the sender's hands and cannot be prepared first. B and D are statuses Docusign assigns as recipients open and finish the envelope.

**Option notes:**
- A (TRAP). sent delivers the envelope at once, so the user would have no chance to tag it first.
- B. delivered is set by Docusign when a recipient opens the envelope; it is not a create value.
- C. Correct. A draft (status created) envelope is what EnvelopeViews:createSender opens for tagging and sending.
- D. completed is a terminal status after all recipients finish; nothing can be prepared at that point.

**Q125. (eSignature Features and Web Forms - ID Evidence) [MEDIUM]** After a signer completes ID Verification, a system must pull the retained evidence about that event. Which API is relevant?

A. AccountSignatureProviders:list
B. The Connect envelope-completed payload
C. ID Evidence API
D. Docusign JS client SDK

**Answer:** C. ID Evidence API

**Explanation:** Retained IDV data is retrieved after the event with the ID Evidence API.

**Why this answer and not the others:** C is right because the ID Evidence API is the API built to retrieve ID verification evidence. The trap is A: it sounds like an identity-related list call, but it returns SBS signature providers. B and D fail because the Connect envelope payload does not carry ID evidence and Docusign JS is client-side rendering.

**Option notes:**
- A (TRAP). This lists signature providers for standards-based signatures; it returns no ID verification evidence.
- B. This envelope event payload reports envelope status; it does not include the retained ID verification data.
- C. Correct. The ID Evidence API retrieves evidence (such as ID images and events) for a completed ID verification.
- D. Docusign JS renders embedded experiences in a browser; it does not retrieve evidence.

**Q126. (Agreement Manager API - Agreement data) [HIGH]** A compliance dashboard already has an agreementId from a renewal workflow. The product owner wants that agreement's extracted provisions and key fields as data, not a search result page. Which operation fits best?

A. Agreements:getAgreementsList
B. Agreements:getAgreement
C. eSignature EnvelopeFormData:get on the source envelope
D. Agreements:createAgreementSummary

**Answer:** B. Agreements:getAgreement

**Explanation:** With the agreementId known, getAgreement returns that agreement's extracted provisions and key fields as structured data.

**Why this answer and not the others:** B is right because the ID is known and structured fields are required. The trap is D: createAgreementSummary works on the same known agreement, but it returns an AI-written summary, not field values a dashboard can display. A returns search results across agreements, and C returns signer tab values from the envelope, not extracted provisions.

**Option notes:**
- A. Returns a list of agreements, which the product owner explicitly does not want.
- B. Correct. getAgreement returns one agreement's extracted provisions and key fields.
- C. Returns tab values entered during signing, not AI-extracted provisions.
- D (TRAP). Returns prose generated by AI, not discrete fields for a dashboard.

**Q127. (Workflow Builder and Workflow API - API trigger) [MEDIUM]** An app is ready to call TriggerWorkflow. Where does it get the URL to send the trigger request to?

A. Build it from the eSignature base path /restapi/v2.1/accounts/{accountId}/workflows
B. Reuse the workflow instance URL returned by an earlier trigger
C. From the GetWorkflowTriggerRequirements response; the URL carries mtid and mtsec query parameters
D. From the workflow-started Connect event

**Answer:** C. From the GetWorkflowTriggerRequirements response; the URL carries mtid and mtsec query parameters

**Explanation:** GetWorkflowTriggerRequirements returns the trigger URL. It includes the mtid and mtsec query parameters that the Maestro service generates at publish time to identify and authenticate a valid workflow.

**Why this answer and not the others:** C is right because the trigger requirements call returns the URL to trigger. The trap is B: an earlier instance URL looks similar, but it opens that existing instance for a participant; it does not start a new one. A uses the eSignature base path, while Maestro uses api-d.docusign.com/v1 or api.docusign.com/v1, and D arrives only after an instance has started.

**Option notes:**
- A. Maestro does not use the eSignature /restapi/v2.1 base path.
- B (TRAP). An instance URL opens an existing instance; it does not trigger a new one.
- C. Correct. The trigger requirements response provides the trigger URL with mtid and mtsec.
- D. workflow-started is sent after an instance exists, so it cannot provide the URL to start one.

**Q128. (App Center and Extension Apps - Connected Fields) [HIGH]** A company wants eSignature fields such as an internal policy number to be verified against its own system of record while senders add fields and signers sign. Which extension type applies?

A. Data IO in a Maestro workflow
B. Connected Fields
C. Data Verification (for example postal address verification)
D. File IO

**Answer:** B. Connected Fields

**Explanation:** Connected fields perform custom data verification of any value type against your system of record, at the Add Fields view and during signing.

**Why this answer and not the others:** B is right because the value is custom (an internal policy number) and checked against the company's own system. The trap is C: data verification extensions verify specific standard types like addresses or bank accounts, not custom internal values. A runs in workflows, not in Add Fields or signing, and D stores files.

**Option notes:**
- A. Data IO runs in Maestro workflows, not at Add Fields or signing.
- B. Correct. Connected fields verify custom values against your system of record during prepare and signing.
- C (TRAP). Data verification extensions cover standard types such as addresses, not internal policy numbers.
- D. File IO writes documents to storage.

**Q129. (API Authentication - PKCE) [MEDIUM]** A native mobile app lets each user sign in to send envelopes. Developers propose shipping the client secret inside the app binary so they can use the confidential flow. Which option should the team keep?

A. Confidential Authorization Code Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. JSON Web Token Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** A secret inside an app binary can be extracted, so the app is a public client and must use Public Authorization Code Grant with PKCE.

**Why this answer and not the others:** C is right because a native app cannot truly protect a secret. The trap is A: the confidential flow is a valid code flow, but shipping the secret in the binary exposes it to anyone who unpacks the app. B is the legacy flow, and D is for unattended services.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant would require a secret embedded in the binary, where it can be extracted.
- B. Implicit Grant is legacy and not recommended by Docusign.
- C. Correct. A native app is a public client, so it uses Public Authorization Code Grant with PKCE.
- D. JWT Grant is for services with no user present and would need a private key in the app, which is worse.

**Q130. (Go Live Process - Go-live setup) [HIGH]** A developer clicks Start Go live and must log in to the production account that will host the integration. What must be true of that login?

A. It must belong to a Docusign Partner Program member
B. It must use the same email address as the developer account
C. It must have administrator privileges on the production account
D. It must be on an account with a paid Docusign support plan

**Answer:** C. It must have administrator privileges on the production account

**Explanation:** The developer submitting the Go-Live request must have administrator privileges on the production account.

**Why this answer and not the others:** C is right because admin access to the production account is a Go-Live requirement. The trap is B: many people assume the accounts must match, but the production login can use a different email address from the developer account. A applies only to Public integrations, and D is needed only to open support cases.

**Option notes:**
- A. Partner Program membership is required only for a Public integration, not for every Go-Live.
- B (TRAP). The production account can use a different email address than the developer account.
- C. Correct. The submitter must be an administrator on the production account.
- D. A paid support plan is not a Go-Live requirement; it only affects access to support cases.

**Q131. (Docusign Connect - Payload selection) [MEDIUM]** Security policy says signed PDFs must not travel inside webhook payloads; the app will download them through the API with its own token. Which option should be used?

A. Leave documents out of the Connect payload and download them by API when needed
B. Include documents but encrypt the listener's disk
C. Include documents and delete them after processing
D. Enable HMAC so document contents are hidden in transit

**Answer:** A. Leave documents out of the Connect payload and download them by API when needed

**Explanation:** Configuring the Connect payload without documents keeps PDFs out of webhook messages, and the app retrieves them by API when required.

**Why this answer and not the others:** A is right because it is the only option that keeps PDFs out of the payload. The trap is D: HMAC is a Connect security feature, but it signs the message for authenticity and integrity; it does not hide or remove the document contents. B and C still send the PDFs in the payload, breaking the policy.

**Option notes:**
- A. Correct. Omit documents from the payload and fetch them through the API.
- B. Documents would still travel in the webhook payload.
- C. Documents would still be sent in the payload before deletion.
- D (TRAP). HMAC signs messages; it does not encrypt or remove document content.

**Q132. (eSignature API - Cancel envelope) [MEDIUM]** A sent envelope must be canceled permanently, and the cancellation must record why. What should the Envelopes:update request contain?

A. status created with an emailBlurb
B. status voided with a voidedReason
C. status declined with a declinedReason
D. status completed with a note

**Answer:** B. status voided with a voidedReason

**Explanation:** Voiding an envelope is done with status voided plus a voidedReason. The clue is a permanent cancellation that records the reason.

**Why this answer and not the others:** B is right because a void request sets status voided and supplies voidedReason. The trap is C: declinedReason is real, but it records why a recipient declined, not a sender cancellation. A creates or describes a draft message and D is a status only Docusign sets.

**Option notes:**
- A. created plus emailBlurb describes a draft and its email text; it does not cancel anything.
- B. Correct. status voided with voidedReason permanently cancels the envelope and records the reason.
- C (TRAP). declined and declinedReason belong to a recipient who refuses to sign, not to the sender cancelling.
- D. completed is set by Docusign when all recipients finish; it cannot be used to cancel.

**Q133. (eSignature Features and Web Forms - Web Forms embedding) [HIGH]** A developer embeds a Docusign web form in a customer portal. Instances:createInstance has returned the instance URL. Which component is loaded in the portal page to display it?

A. The embedded sending view from EnvelopeViews:createSender
B. Docusign JS client SDK
C. A PowerForm URL
D. A Connect webhook listener

**Answer:** B. Docusign JS client SDK

**Explanation:** The instance URL comes from createInstance, and the documented client-side component for showing it inline is Docusign JS.

**Why this answer and not the others:** B is right because Docusign provides Docusign JS to embed web form instances in a website. The trap is A: it is a real embedded view, but it is for senders preparing envelopes, not for participants filling a web form. C and D fail because a PowerForm is a different self-service feature and Connect is server-side event delivery.

**Option notes:**
- A (TRAP). The sender view lets a sender prepare an envelope inside your app; it does not display a web form instance to a participant.
- B. Correct. Docusign JS is the client SDK used to render a web form instance URL in a host page.
- C. A PowerForm is a separate self-service signing link for templates; it does not render a Web Forms API instance.
- D. Connect pushes event notifications to your server; it renders nothing in the browser.

**Q134. (Agreement Manager API - Agreement list) [MEDIUM]** A contract analytics page lets users filter agreements by counterparty, expiration month and type before opening one record. The integration does not know the agreementId until the filter results return. Which operation comes first?

A. Agreements:getAgreement
B. Agreements:createAgreementSummary
C. Agreements:getAgreementsList
D. eSignature Envelopes:listStatusChanges

**Answer:** C. Agreements:getAgreementsList

**Explanation:** getAgreementsList is the list and search step that runs before retrieving a specific agreement when its ID is not yet known.

**Why this answer and not the others:** C is right because filtering happens before any agreementId exists. The trap is A: getAgreement is the call for opening the record, but it comes second because it needs the agreementId. B also needs a known agreement, and D lists envelope status changes rather than agreements filtered by extracted fields.

**Option notes:**
- A (TRAP). Needed after the user picks a result; it requires the agreementId first.
- B. Summarizes one known agreement; it cannot filter agreements.
- C. Correct. List agreements first, then open the chosen one.
- D. Lists envelope changes; it cannot filter on extracted counterparty or expiration data.

**Q135. (Workflow Builder and Workflow API - Runtime errors) [MEDIUM]** A workflow starts correctly from a test, but production triggers fail whenever the app omits accountType, which the designer marked as a required starting variable. Where should the developer investigate first?

A. Workflow trigger requirements and starting-variable mapping
B. Whether the token includes aow_manage
C. Whether new instances of the workflow are paused
D. The Connect configuration's message format

**Answer:** A. Workflow trigger requirements and starting-variable mapping

**Explanation:** The failure appears only when accountType is missing, and the designer made it a required starting variable. That points to the trigger requirements and how the app maps values into the trigger inputs.

**Why this answer and not the others:** A is right because the deciding clue is that failures track one missing required value. The trap is B: a missing scope would fail every trigger call, not only those without accountType. C would block all new instances, and D affects event delivery, not starting a workflow.

**Option notes:**
- A. Correct. Check the required inputs in the trigger requirements and map accountType on every call.
- B (TRAP). A scope problem would fail every call, not only calls missing accountType.
- C. Paused workflows reject all new instances regardless of inputs.
- D. Connect message format affects notifications, not trigger validation.

**Q136. (App Center and Extension Apps - Data Verification) [HIGH]** A signer enters a bank account number that must be validated in real time against a standard bank verification service while signing. Which extension pattern fits?

A. Data Verification (bank account verification) at eSignature signing
B. File IO in a Maestro workflow
C. Data IO in a Maestro workflow
D. ID Verification of the signer before opening the envelope

**Answer:** A. Data Verification (bank account verification) at eSignature signing

**Explanation:** Data Verification checks signer-entered standard data such as bank accounts in real time during signing.

**Why this answer and not the others:** A is right because bank account is a standard data verification type checked at signing. The trap is C: Data IO also talks to external systems, but it runs in Maestro workflows and reads/writes records rather than verifying a field as it is entered. B stores files, and D verifies identity, not the bank data.

**Option notes:**
- A. Correct. Bank account verification is a Data Verification extension run at signing.
- B. File IO stores documents; it does not validate entered values.
- C (TRAP). Data IO reads/writes records in workflows; it does not verify a field during signing.
- D. ID Verification confirms who the signer is, not whether the bank account is valid.

**Q137. (API Authentication - Bearer tokens) [LOW]** A partner's REST calls return 401 Unauthorized. The code sends Authorization: Bearer, but with the wrong value. Which value belongs after Bearer?

A. The access token returned by /oauth/token
B. The refresh token
C. The ID token returned when openid is requested
D. The integration key

**Answer:** A. The access token returned by /oauth/token

**Explanation:** The Bearer header carries the access token; refresh tokens and ID tokens are never used to call the APIs.

**Why this answer and not the others:** A is right because only the access token authorizes API calls. The trap is B: the refresh token comes back in the same response, but it is only sent to /oauth/token to get a new access token. C has no system function for calling APIs, and D identifies the app rather than authorizing a request.

**Option notes:**
- A. Correct. API calls use Authorization: Bearer <access_token>.
- B (TRAP). A refresh token is only exchanged at /oauth/token for a new access token; APIs reject it.
- C. The ID token records identity and consent details; it is not used to call APIs.
- D. The integration key identifies the app; it is not a credential for API calls.

**Q138. (Go Live Process - Integration classification) [HIGH]** A company builds an app that its own employees and its customers' employees will use directly. Which integration type should it select?

A. Public integration
B. Private custom integration
C. Third-party integration key
D. Embedded integration

**Answer:** B. Private custom integration

**Explanation:** When the integration is directly used by your employees or your customers' employees, the classification is Private custom integration.

**Why this answer and not the others:** B is right because the clue is direct use by the company's own employees or its customers' employees. The trap is A: customers are involved, but Public integration is for a partner app that many Docusign customers connect to their own accounts. C is for a customer supplying its own key to a partner product, and D is for vendors offering Docusign features through their own account.

**Option notes:**
- A (TRAP). Public integration is a partner app for many Docusign customers using their own accounts.
- B. Correct. Use by your employees or your customers' employees is a Private custom integration.
- C. Third-party integration key is for a partner product that requires the customer's own key.
- D. Embedded integration needs an ISV Embed license and serves customers without their own Docusign accounts.

**Q139. (Docusign Connect - Envelope-level Connect) [MEDIUM]** A QA tester confirms that envelope X, sent by API, posts events to a special listener while every other envelope in the account still uses the existing account webhook. Which configuration produces exactly this behavior?

A. A new account-level Connect configuration with all users selected
B. An organization-level Connect configuration for selected accounts
C. Polling Envelopes:listStatusChanges for envelope X
D. An eventNotification object in the Envelopes:create request for envelope X

**Answer:** D. An eventNotification object in the Envelopes:create request for envelope X

**Explanation:** Only envelope-level Connect (eventNotification on Envelopes:create) targets one envelope while the account-level configuration keeps serving all other envelopes.

**Why this answer and not the others:** D is right because the special listener receives events for envelope X only. The trap is A: an account-level configuration with all users selected would post every envelope in the account to the special listener. B is wider again, and C is polling, which is not a webhook at all and adds API calls.

**Option notes:**
- A (TRAP). An account-level configuration for all users sends events for every envelope in the account, not only envelope X.
- B. Organization-level Connect covers whole accounts in the org, not a single envelope.
- C. listStatusChanges is a polling call; it does not push anything to a listener.
- D. Correct. eventNotification scopes the webhook to the envelope it is created with.

**Q140. (eSignature API - Embedded signing) [HIGH]** A developer is implementing embedded signing. Which parameter must be included in the recipient definition when creating the envelope to signal that the signer will be embedded rather than remote?

A. recipientId
B. clientUserId
C. returnUrl
D. accountId

**Answer:** B. clientUserId

**Explanation:** Setting clientUserId on the recipient flags it as embedded (captive) instead of remote, which enables the embedded signing session.

**Why this answer and not the others:** B is right because clientUserId in the recipient definition is what makes the signer embedded. The trap is C: returnUrl is required for embedded signing, but it goes in the createRecipient request, not in the recipient definition. A exists for every recipient and D is part of the request URL.

**Option notes:**
- A. recipientId identifies every recipient, embedded or remote; it does not mark embedding.
- B. Correct. clientUserId on the recipient marks it as an embedded signer.
- C (TRAP). returnUrl belongs to the createRecipient request, where it sets the redirect after signing.
- D. accountId is part of the request URL path; it says nothing about the recipient type.

**Q141. (eSignature Features and Web Forms - Workflow steps) [LOW]** An HR onboarding workflow in Workflow Builder must first capture the new hire's personal information and then verify their government-issued ID. Which step sequence matches this?

A. Set Up Invite step, then Add a Branching Rule step
B. Collect Data with Web Forms step, then Verify Someone's Identity step
C. Verify Someone's Identity step, then Collect Data with Web Forms step
D. Get Signatures step, then Collect Data with Web Forms step

**Answer:** B. Collect Data with Web Forms step, then Verify Someone's Identity step

**Explanation:** Collect Data with Web Forms captures the information first, then Verify Someone's Identity confirms the government ID, matching the stated order.

**Why this answer and not the others:** B is right because it uses the two correct steps in the order the stem requires. The trap is C: the steps are correct but reversed. A and D fail because they do not include an identity verification step.

**Option notes:**
- A. Neither step collects data or verifies an ID; one configures how participants are invited and the other adds conditional routing.
- B. Correct. Collect Data with Web Forms gathers the personal information, then Verify Someone's Identity checks the government ID, in the required order.
- C (TRAP). These are the right steps in the wrong order: the requirement is to collect the data first, then verify the ID.
- D. Get Signatures collects signatures, not ID verification, and it is placed before data collection.

**Q142. (Agreement Manager API - Legacy import) [MEDIUM]** A legal team has thousands of signed agreements from outside Docusign. They want them in Agreement Manager so future searches and analytics include them. Which capability is the right fit?

A. Re-send each agreement for signature as a new envelope
B. Bulk import the agreements into Agreement Manager
C. Configure Connect to publish events for the old agreements
D. Upload each agreement as an eSignature template

**Answer:** B. Bulk import the agreements into Agreement Manager

**Explanation:** Bulk import brings existing agreements and their content into Agreement Manager, where they become searchable with AI-extracted data.

**Why this answer and not the others:** B is right because the agreements are already signed and only need to enter the repository. The trap is A: completed envelopes do appear in Agreement Manager, but re-signing executed contracts is unnecessary and creates new signing events. C only publishes events about Docusign envelopes, which these agreements never had, and D creates sending templates, not agreement records.

**Option notes:**
- A (TRAP). Already-signed agreements do not need to be re-signed; import is the intended path.
- B. Correct. Bulk import adds the legacy agreements to Agreement Manager for search and analytics.
- C. Connect reports events for Docusign envelopes; agreements from outside Docusign have none.
- D. Templates are reusable sending blueprints and do not create agreement records.

**Q143. (Workflow Builder and Workflow API - Embedding workflow) [LOW]** A team embeds a workflow instance in an iframe. The workflow includes a Verify Someone's Identity step. Which verification method is supported in embedded workflow instances?

A. Phone authentication
B. ID verification with a government photo ID
C. Collect Data from an ID
D. Any method; embedding has no step restrictions

**Answer:** A. Phone authentication

**Explanation:** For Verify Someone's Identity steps in embedded workflow instances, only the Phone Authentication method is supported.

**Why this answer and not the others:** A is right because Docusign limits embedded identity steps to phone authentication. The trap is B: ID verification is a valid method in non-embedded workflows, but not in an embedded instance. C is a step type that is itself unsupported when embedded, and D ignores the documented restrictions.

**Option notes:**
- A. Correct. Phone authentication is the only verification method supported for embedded instances.
- B (TRAP). Works in a normal workflow, but is not supported when the instance is embedded.
- C. Collect Data from an ID is a step type, and it is not supported in embedded instances.
- D. Embedding has documented restrictions on identity and ID-related steps.

**Q144. (App Center and Extension Apps - Firewall) [MEDIUM]** Which IT infrastructure change helps ensure Docusign can reliably send requests to the external API service behind an extension app?

A. Configure the network firewall to allow Docusign's requests
B. Enable CORS on the endpoint
C. Require multi-factor authentication on the endpoint
D. Add a CNAME entry to DNS

**Answer:** A. Configure the network firewall to allow Docusign's requests

**Explanation:** The firewall must allow Docusign's requests to reach the external endpoint; otherwise the calls are blocked.

**Why this answer and not the others:** A is right because Docusign's server-to-server calls must get through the firewall. The trap is B: CORS controls browser cross-origin JavaScript, not server calls. C is an interactive user control that machine calls cannot satisfy, and D does not open network access.

**Option notes:**
- A. Correct. Allowing Docusign through the firewall keeps the endpoint reachable.
- B (TRAP). CORS applies to browsers, not to Docusign's server-to-server calls.
- C. MFA is for interactive users; Docusign authorizes through the app's OAuth connection.
- D. A DNS alias does not make a firewalled endpoint reachable.

**Q145. (API Authentication - OAuth flow selection) [MEDIUM]** Users sign in interactively. The backend then exchanges the authorization code at /oauth/token, sending an Authorization: Basic header built from base64(integrationKey:secretKey). Which OAuth flow is this?

A. Public Authorization Code Grant with PKCE
B. JSON Web Token Grant
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Sending the integration key and secret key in a Basic header during the code exchange is the defining step of Confidential Authorization Code Grant.

**Why this answer and not the others:** D is right because only the confidential flow authenticates the code exchange with the secret key in a Basic header. The trap is A: Public Auth Code also exchanges a code at /oauth/token, but it sends a code_verifier in the body and no secret. B posts a signed JWT assertion instead of a code, and C never performs a code exchange.

**Option notes:**
- A (TRAP). Public Auth Code Grant also redeems a code at /oauth/token, but it sends a code_verifier and never a secret key.
- B. JWT Grant posts a signed assertion to /oauth/token; there is no authorization code and no Basic secret header.
- C. Implicit Grant returns the token directly to the browser, so there is no code exchange at /oauth/token.
- D. Correct. The Basic header with base64(integrationKey:secretKey) on the code exchange is the confidential flow.

**Q146. (Go Live Process - Production endpoints) [HIGH]** After Go-Live, how should an eSignature app determine the production base URI for a user's account?

A. Call userinfo after production authentication and use the account's base_uri
B. Hardcode https://www.docusign.net/restapi for all production accounts
C. Reuse the base_uri that userinfo returned in the developer environment
D. Use the authentication host account.docusign.com as the API base

**Answer:** A. Call userinfo after production authentication and use the account's base_uri

**Explanation:** The account's production base URI comes from the base_uri field of the userinfo response after authenticating in production (it is also shown as Account Base URI on Apps and Keys).

**Why this answer and not the others:** A is right because each production account lives on a specific server returned by userinfo. The trap is B: it is a production host, but hardcoding one server fails for accounts on other data centers. C returns the demo host, and D confuses the authentication service with the API host.

**Option notes:**
- A. Correct. Read base_uri from the production userinfo response and cache it.
- B (TRAP). Production accounts live on different servers, so one hardcoded host is wrong for many accounts.
- C. The developer environment's userinfo returns the demo host, not the production one.
- D. account.docusign.com is the OAuth host; API calls go to the account's base URI.

**Q147. (Docusign Connect - Connect vs polling) [MEDIUM]** A developer proposes checking each in-flight envelope's status every 5 minutes to update a CRM. What should the guidance recommend instead?

A. Keep the 5-minute poll; per-envelope polling has no limit
B. Poll every 15 minutes per envelope and skip webhooks
C. Subscribe to Connect events instead of polling
D. Poll every 5 minutes but only during business hours

**Answer:** C. Subscribe to Connect events instead of polling

**Explanation:** Polling is limited to once per 15 minutes per envelope, and Connect removes the need to poll by pushing status changes as they happen.

**Why this answer and not the others:** C is right because Connect delivers each status change immediately without API calls. The trap is B: it fixes the limit violation but keeps a slower, call-heavy polling design that Docusign discourages. A and D both poll every 5 minutes, which breaks the once-per-15-minutes-per-envelope rule.

**Option notes:**
- A. Per-envelope polling is limited to once every 15 minutes; 5 minutes violates it.
- B (TRAP). Allowed, but still wastes calls and adds delay; Connect is the recommended design.
- C. Correct. Connect pushes events, so no per-envelope polling is needed.
- D. Limiting the hours does not change the 5-minute interval, which still breaks the polling limit.

**Q148. (eSignature API - Idempotency) [LOW]** A sender service creates envelopes during a high-volume window. If Envelopes:create times out, the service retries the same request. Which value should the app supply so Docusign can recognize the retry as the same transaction?

A. envelopeId
B. transactionId
C. recipientId
D. batchId

**Answer:** B. transactionId

**Explanation:** The client sets transactionId on the envelope definition, so a timed-out request can be recognized instead of producing a second envelope.

**Why this answer and not the others:** B is right because transactionId is generated by the sender and travels with the create request. The trap is A: envelopeId is the envelope's identifier, but Docusign assigns it and a timed-out call may never return it. C identifies a recipient and D a bulk send batch.

**Option notes:**
- A (TRAP). envelopeId is assigned by Docusign in the response; a timed-out call may never return it to the client.
- B. Correct. transactionId is the client-supplied value that identifies the create transaction across retries.
- C. recipientId identifies a recipient inside the envelope; it cannot identify the create transaction.
- D. batchId belongs to bulk send batches, not to single Envelopes:create calls.

**Q149. (eSignature Features and Web Forms - Web Form correlation) [MEDIUM]** A financial-aid office embeds one web form instance per applicant and must later match each instance to the applicant's record. Which value should the app supply on createInstance?

A. clientUserId
B. recipients[].roleName
C. The API account ID
D. The envelopeId

**Answer:** A. clientUserId

**Explanation:** Per-applicant correlation from your own system is done with clientUserId.

**Why this answer and not the others:** A is right because clientUserId carries the applicant identifier from your system. The trap is B: it is part of createInstance, but it is used for remote instances and identifies a role such as 'Applicant', not which applicant. C and D fail because the account ID is shared and the envelopeId does not exist yet at creation.

**Option notes:**
- A. Correct. clientUserId is the app's own identifier for the user, required for embedded instances.
- B (TRAP). roleName maps participants to template roles in remote instances; it names a role, not a specific applicant.
- C. The account ID is identical for every instance in the account.
- D. An embedded instance has no envelope until the first submit, so no envelopeId exists when the instance is created.

**Q150. (Agreement Manager API - Agreement documents) [LOW]** A renewal review task needs a copy of the prior signed agreement file attached. The agreement already exists in Agreement Manager and its ID is known. Which approach fits?

A. Download the agreement document for that agreement
B. Attach the output of Agreements:createAgreementSummary
C. Attach the response of Agreements:getAgreementsList
D. Create a new envelope containing the agreement

**Answer:** A. Download the agreement document for that agreement

**Explanation:** The task needs the signed file itself, so the agreement document is downloaded for that agreement.

**Why this answer and not the others:** A is right because only the document download yields a copy of the signed file. The trap is B: a summary helps reviewers, but it is AI-written text, not the prior signed agreement. C returns agreement records rather than a file, and D starts a new signing transaction instead of retrieving the existing document.

**Option notes:**
- A. Correct. Downloading the agreement document gives the review task the signed file.
- B (TRAP). An AI summary is not a copy of the signed agreement.
- C. The list response contains agreement records, not the agreement file.
- D. A new envelope starts a new signing process; it does not retrieve the existing signed copy.

**Q151. (Workflow Builder and Workflow API - Installed extensions) [MEDIUM]** A company built an extension app that reads its internal HR system for use in its own Maestro workflows. No other Docusign customer should see or install it. How should the app be distributed?

A. Publish it publicly in the App Center
B. Register it as a Connect listener
C. Expose it as a connected fields extension
D. Use private distribution so only the company's organization can install it

**Answer:** D. Use private distribution so only the company's organization can install it

**Explanation:** Private distribution is meant for org-only extension apps. The company's admin then installs it so the workflow can use its steps.

**Why this answer and not the others:** D is right because the app is for this organization only. The trap is A: public App Center listing is the normal path for extension apps, but it goes through public review and makes the app available to every customer. B only receives events, and C is an eSignature feature not supported in Maestro.

**Option notes:**
- A (TRAP). Public listing exposes the app to all customers, which the company does not want.
- B. Connect pushes event notifications; it does not provide workflow steps.
- C. Connected fields are not supported in Maestro workflows.
- D. Correct. Private distribution limits the app to the company's own organization.

**Q152. (App Center and Extension Apps - Extension app role) [MEDIUM]** An architect explains extension apps to a team that has only built eSignature API integrations. Which statement correctly describes how an extension app's calls flow?

A. Your service calls Docusign APIs using JWT Grant and an integration key
B. Docusign pushes envelope status events to your listener through Connect
C. Signers are redirected to your site and returned with a signing token
D. Docusign calls your external service through actions defined in the app

**Answer:** D. Docusign calls your external service through actions defined in the app

**Explanation:** With an extension app, Docusign is the caller: it invokes the external endpoints described by the app's actions, using the app's connection for authorization.

**Why this answer and not the others:** D is right because extension apps reverse the usual integration direction: Docusign calls your service via manifest actions. The trap is A, which describes a normal API integration where your code calls Docusign. B describes Connect notifications and C describes a redirect pattern, neither of which is the extension app call model.

**Option notes:**
- A (TRAP). This is a standard eSignature API integration (your code calls Docusign), not how an extension app works.
- B. Connect sends event notifications; it does not execute extension actions such as verify or write record.
- C. Redirect-based signing is an embedded/remote signing pattern, unrelated to how extension actions are invoked.
- D. Correct. Docusign invokes the external endpoints declared in the app's actions, authorized through the app's connection.

**Q153. (API Authentication - OAuth flow selection) [MEDIUM]** A legacy browser-only SPA uses Implicit Grant. The team must follow current Docusign guidance for a client that cannot protect a secret and signs in each user. Which flow should it use?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Keep Implicit Grant but request fewer scopes

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Docusign recommends replacing Implicit Grant with Public Authorization Code Grant with PKCE for clients that cannot store a secret.

**Why this answer and not the others:** C is right because the client is public and the guidance is to migrate off Implicit to the PKCE code flow. The trap is D: requesting fewer scopes is good practice, but it does not fix the legacy flow itself. A needs a secret the SPA cannot hold, and B does not sign users in.

**Option notes:**
- A. Confidential Auth Code Grant needs a client secret, which a browser-only SPA cannot protect.
- B. JWT Grant is for service integrations without a user present, not per-user browser sign-in.
- C. Correct. Public Authorization Code Grant with PKCE is the recommended replacement for Implicit Grant.
- D (TRAP). Least privilege is good, but it leaves the app on the legacy Implicit flow that Docusign no longer recommends.

**Q154. (Go Live Process - Templates in production) [MEDIUM]** A developer wants the same codebase to run in the developer environment and in production without breaking template references. What is the best approach?

A. Hardcode the developer templateId, because Go-Live maps it to production
B. Reference templates by the demo templateId and let production redirect it
C. Re-run Go-Live whenever a template changes so production stays in sync
D. Keep template IDs in environment-specific configuration, one set per environment

**Answer:** D. Keep template IDs in environment-specific configuration, one set per environment

**Explanation:** Template IDs differ between the developer and production accounts, so they should be stored as per-environment configuration rather than hardcoded.

**Why this answer and not the others:** D is right because each environment has its own template IDs. The trap is A: it assumes Go-Live carries templates and their IDs into production, but Go-Live only duplicates the integration key. B is the same mistake, and C is wrong because Go-Live never copies templates.

**Option notes:**
- A (TRAP). Go-Live does not map or copy templates; the developer templateId does not exist in production.
- B. Production does not redirect demo template IDs; the production template has its own ID.
- C. Go-Live promotes the integration key only; it never synchronizes templates.
- D. Correct. Store template IDs per environment so each deployment uses its own account's templates.

**Q155. (Docusign Connect - Configuration level) [HIGH]** A developer needs real-time updates for envelopes sent across three Docusign accounts under one corporate organization, to centralize logging and monitoring. Which Connect configuration should be implemented?

A. Recipient Connect
B. Envelope-level Connect (eventNotification)
C. Organization-level Connect
D. Account-level Connect

**Answer:** C. Organization-level Connect

**Explanation:** Organization-level Connect spans the accounts in the organization, centralizing event delivery in one configuration.

**Why this answer and not the others:** C is right because only org-level Connect covers multiple accounts from one place. The trap is D: account-level Connect works for one account, so it would need three separate configurations instead of one central one. B applies to a single API-sent envelope, and A is not the level that aggregates events across accounts.

**Option notes:**
- A. Recipient Connect does not centralize events from several accounts.
- B. Envelope-level Connect applies to one envelope at a time, not all envelopes in three accounts.
- C. Correct. Organization-level Connect covers all or selected accounts in the organization.
- D (TRAP). Account-level Connect covers only one account; three separate configurations would be needed.

**Q156. (eSignature API - Template reference) [HIGH]** A request uses the template reference model with one saved template. The developer must point the call at that template, then map recipients into its roles. Which identifier points at the template?

A. templateId
B. roleName
C. envelopeId
D. clientUserId

**Answer:** A. templateId

**Explanation:** templateId identifies the saved template; templateRoles with roleName then map recipients into it.

**Why this answer and not the others:** A is right because templateId is the template reference. The trap is B: roleName is required for the recipient mapping step, but it names a role, not the template. C identifies an envelope that already exists and D marks an embedded recipient.

**Option notes:**
- A. Correct. templateId tells Docusign which saved template to build the envelope from.
- B (TRAP). roleName is used in templateRoles to match a recipient to a role inside the template.
- C. envelopeId identifies an existing envelope, not the template used to create one.
- D. clientUserId marks a recipient for embedded signing; it does not reference a template.

**Q157. (eSignature Features and Web Forms - Identity verification) [HIGH]** Maya must ensure that a signer presents a government-issued photo ID before signing an envelope. Which recipient setting enforces this?

A. authenticationMethod recorded during embedded signing
B. An accessCode shared with the signer
C. idCheckConfigurationName set for KBA
D. identityVerification with the workflowId of the account's ID verification configuration

**Answer:** D. identityVerification with the workflowId of the account's ID verification configuration

**Explanation:** The clue is a government-issued photo ID, which is ID verification configured with identityVerification.workflowId.

**Why this answer and not the others:** D is right because IDV is the method that checks a government photo ID, applied via identityVerification.workflowId. The trap is A: it looks like an identity setting, but it only records and never enforces. B and C fail because an access code and KBA are lighter methods that do not inspect an ID document.

**Option notes:**
- A (TRAP). This only writes your app's own authentication method to the certificate; Docusign does not challenge the signer.
- B. An access code proves the signer knows a secret, not that they hold a valid government ID.
- C. KBA verifies identity with public-record questions (US only), not with a photo ID.
- D. Correct. Adding identityVerification.workflowId for an IDV configuration makes the recipient verify a photo ID before accessing the documents.

**Q158. (Agreement Manager API - Agreement data) [HIGH]** A custom app must show the parties array and provisions (for example governing_law and expiration_date) of one specific agreement. Which operation returns them?

A. Agreements:getAgreementsList
B. eSignature Envelopes:get
C. Agreements:getAgreement
D. Agreements:createAgreementSummary

**Answer:** C. Agreements:getAgreement

**Explanation:** getAgreement returns one agreement's record, including its parties array and provisions object with fields such as governing_law and expiration_date.

**Why this answer and not the others:** C is right because the app needs the structured fields of one specific agreement. The trap is A: getAgreementsList is also an Agreement Manager read call, but it is used to find agreements, not to retrieve one specific record. B returns envelope status and recipients, not extracted provisions, and D returns AI-written prose.

**Option notes:**
- A (TRAP). Lists agreements to find candidates; the app needs one specific agreement's record.
- B. Returns envelope metadata, not Agreement Manager parties and provisions.
- C. Correct. getAgreement returns the parties and provisions for one agreement.
- D. Returns an AI summary rather than the parties array and provisions object.

**Q159. (Workflow Builder and Workflow API - JSON SIM) [MEDIUM]** A developer wants Docusign Connect to send events about Maestro workflows (for example workflow-completed). Which Connect configuration detail is required?

A. The messages must exclude all envelope and recipient data.
B. The messages must have retries enabled.
C. The messages must be authenticated using HMAC.
D. The messages must use the JSON SIM format.

**Answer:** D. The messages must use the JSON SIM format.

**Explanation:** Maestro workflow events are only available in the JSON SIM event message format.

**Why this answer and not the others:** D is right because workflow events exist only in JSON SIM. The trap is C: HMAC is a recommended way to secure Connect messages, but it is optional and does not decide which events you receive. A and B are unrelated settings: excluding data or enabling retries does not make workflow events available.

**Option notes:**
- A. Excluding envelope data is not a requirement for workflow events.
- B. Retries improve delivery but do not enable workflow events.
- C (TRAP). HMAC is recommended for security but is optional and does not enable workflow events.
- D. Correct. Maestro workflow events are delivered only in JSON SIM format.

**Q160. (App Center and Extension Apps - Public vs private) [HIGH]** A private extension app has been approved. What must the developer do so that a specific customer's administrators can install it?

A. Click the button that makes the app available to all App Center customers
B. Set publicationRegions to the customer's region in the manifest
C. Add the customer's production account ID (GUID) to the app's allowed accounts
D. Send the customer the app's OAuth client ID and secret

**Answer:** C. Add the customer's production account ID (GUID) to the app's allowed accounts

**Explanation:** For a private app, after approval the developer adds the production account IDs (GUIDs) allowed to install it; administrators of those accounts can then install it.

**Why this answer and not the others:** C is right because private sharing is done by listing production account IDs. The trap is A: clicking to list the app for all customers is the public publishing step. B applies to public apps only, and D shares connection credentials, which does not grant install rights.

**Option notes:**
- A (TRAP). Listing the app for all customers is the public publishing step, which a private app does not use.
- B. publicationRegions applies to public apps and controls regions, not specific accounts.
- C. Correct. Private apps are shared by adding the production account IDs (GUIDs) of the allowed accounts.
- D. Connection credentials are for Docusign's calls to the external API; they do not control who can install the app.

**Q161. (API Authentication - JWT Grant) [HIGH]** A security architect reviews a service that has no user present. Its access token expires after one hour, no refresh token is returned, and the service signs a new assertion to get the next token. Which authentication model is this?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** A 1-hour access token, no refresh token, and a newly signed assertion for each new token are the defining traits of JWT Grant.

**Why this answer and not the others:** B is right because only JWT Grant returns no refresh token and renews by signing a new assertion. The trap is A: Confidential Auth Code is also server-side, but its access token lasts 8 hours and it returns a refresh token. C returns a 24-hour refresh token, and D is a legacy browser flow.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant returns an 8-hour access token plus a refresh token, which does not match the stem.
- B. Correct. JWT Grant: 1-hour access token, no refresh token, new signed assertion each time.
- C. Public Auth Code Grant with PKCE needs an interactive user and returns a refresh token valid 24 hours.
- D. Implicit Grant is a legacy interactive browser flow, not a service model.

**Q162. (Go Live Process - Go-live setup) [HIGH]** After Go-Live, which two values must the application itself switch from demo to production, as opposed to credentials you re-add on the production key in Apps and Keys? (Select two)

A. Redirect URI
B. Integration key (client ID)
C. Production API endpoints
D. Account Base URI
E. Secret or RSA key pair

**Answer:** C, D. Production API endpoints; Account Base URI

**Explanation:** The application must call production endpoints (for example account.docusign.com for OAuth) and the account's production base URI instead of the demo hosts. This is the keyed answer in the source exam question.

**Why this answer and not the others:** C and D are right because they are values the code uses to route calls to production. The trap is B: the integration key is duplicated with the same value, so the app does not need a new client ID. A and E must be re-added on the production key in Apps and Keys, which the stem excludes; the source question keys C and D, so remember that pairing.

**Option notes:**
- A. Redirect URIs must be re-added on the production key in Apps and Keys, which the stem excludes.
- B (TRAP). The production key keeps the same value as the demo key, so the client ID does not change.
- C. Correct. The app must switch to production endpoints such as https://account.docusign.com.
- D. Correct. The app must call the account's production base URI, obtained from userinfo.
- E. Secrets and RSA keys are re-added on the production key in Apps and Keys, which the stem excludes.

**Q163. (Docusign Connect - Configuration level) [HIGH]** A company needs one webhook that also captures envelopes that users in any of its organization's accounts receive from external senders. Which Connect level fits?

A. Account-level Connect configured in one account
B. Organization-level Connect
C. eventNotification on every envelope the company sends
D. Polling Envelopes:listStatusChanges for each account

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect covers envelopes sent from or received by the organization's accounts, including envelopes received from external parties.

**Why this answer and not the others:** B is right because it is a single configuration across accounts and includes received envelopes. The trap is C: eventNotification is set only by the sender at creation time, so it can never cover envelopes your users receive from external senders. A covers one account only, and D is polling, not a webhook.

**Option notes:**
- A. One account-level configuration sees only that account's envelopes.
- B. Correct. Org-level Connect covers envelopes sent or received by all or selected accounts.
- C (TRAP). Envelope-level webhooks exist only on envelopes you send by API; they cannot cover envelopes received from external senders.
- D. Polling is not a webhook and adds API traffic per account.

**Q164. (eSignature API - Composite templates) [HIGH]** A request must combine a server template, inline recipient data, and an extra document supplied at runtime, all in one envelope. Which model supports that structure?

A. Template reference model (templateId plus templateRoles)
B. Direct documents model with fixed-position tabs
C. Composite templates model
D. Bulk send list applied to a draft envelope

**Answer:** C. Composite templates model

**Explanation:** Composite templates mix server templates, inline templates and directly supplied documents in one envelope. The clue is combining all three.

**Why this answer and not the others:** C is right because only the composite templates model combines a saved template with a runtime document and inline data. The trap is A: it does use the saved template, but it cannot add a separate runtime document alongside it. B ignores the saved template and D sends copies to many recipients, which is a different requirement.

**Option notes:**
- A (TRAP). The template reference model uses one saved template as is; it cannot add an extra runtime document.
- B. Direct documents can supply the extra document but cannot apply the saved server template.
- C. Correct. Composite templates combine server templates, inline templates and documents in one envelope.
- D. Bulk send creates one envelope per list recipient; it does not combine templates and documents.

**Q165. (eSignature Features and Web Forms - Recipient authentication) [MEDIUM]** A design requires that a signer receive a one-time code by SMS and enter it before the envelope opens. Which Docusign feature category applies?

A. The phone number verification extension (Verify.Version1.PhoneNumber)
B. Brand destination URLs
C. Recipient authentication (phone authentication)
D. authenticationMethod on createRecipient

**Answer:** C. Recipient authentication (phone authentication)

**Explanation:** Requiring a code before the envelope opens is recipient authentication, specifically phone authentication.

**Why this answer and not the others:** C is right because recipient authentication controls access to the envelope, and phone authentication sends the SMS code. The trap is A: it is phone-related and runs inside eSignature, but it verifies a data value, not the signer's access. B and D fail because destination URLs only redirect and authenticationMethod only records.

**Option notes:**
- A (TRAP). This extension validates a phone number value entered in a field; it does not gate access to the envelope with a code.
- B. Destination URLs redirect remote signers after events; they do not authenticate anyone.
- C. Correct. Gating access to the envelope with an SMS code is a recipient authentication method: phone authentication.
- D. This only records your app's authentication on the certificate; nothing is sent to the signer.

**Q166. (Agreement Manager API - Agreement list) [HIGH]** An app has only a counterparty name and must display that counterparty's agreement in full. In which order should it call the Agreement Manager API?

A. Agreements:getAgreement first, then Agreements:getAgreementsList to confirm
B. Agreements:getAgreementsList to find the agreement, then Agreements:getAgreement for its detail
C. Agreements:createAgreementSummary first to locate the agreement
D. eSignature Envelopes:get first, using the counterparty name

**Answer:** B. Agreements:getAgreementsList to find the agreement, then Agreements:getAgreement for its detail

**Explanation:** With only a counterparty name, the app must list or search agreements to get the agreementId, then call getAgreement for the full record.

**Why this answer and not the others:** B is right because the agreementId comes from the list step. The trap is A: both calls are correct, but in the wrong order, since getAgreement cannot run without an agreementId. C needs a known agreement and does not search, and D is an eSignature call that needs an envelopeId, not a counterparty name.

**Option notes:**
- A (TRAP). Wrong order; getAgreement requires the agreementId that only the list step provides.
- B. Correct. Search with the list call, then retrieve the full record by ID.
- C. createAgreementSummary works on a known agreement; it cannot locate one.
- D. Envelopes:get needs an envelopeId and returns envelope data, not agreements.

**Q167. (Workflow Builder and Workflow API - Workflow steps) [HIGH]** A services contract must include or hide clauses depending on the customer's region, which is a workflow variable. Which step should generate the document before signing?

A. Prepare eSignature Template
B. Collect Data with Web Forms
C. Prepare Document Template with conditional show/hide logic, followed by Send Documents for Signature
D. Use eSignature API with one fixed document

**Answer:** C. Prepare Document Template with conditional show/hide logic, followed by Send Documents for Signature

**Explanation:** Prepare Document Template generates different document content from workflow variables using conditional show/hide logic defined on the template. It is followed by Send Documents for Signature.

**Why this answer and not the others:** C is right because the content itself changes with the region variable. The trap is A: Prepare eSignature Template fills fields on one template, but it is meant for a document that is exactly the same for every instance. B only collects data, and D sends a fixed document that cannot vary its clauses.

**Option notes:**
- A (TRAP). Meant for one unchanging template; it cannot show or hide clauses by region.
- B. Collects values but does not generate the contract.
- C. Correct. Conditional logic on the document template produces region-specific content.
- D. A fixed document cannot vary its clauses by region.

**Q168. (App Center and Extension Apps - Workflow steps) [HIGH]** A software vendor wants Docusign customers globally to use its compliance document storage service within Maestro workflows. How should the developer configure distribution?

A. Set distribution to PRIVATE, because public apps cannot be used in Maestro
B. Set distribution to PUBLIC and be (or become) a Docusign partner
C. Set distribution to PRIVATE and list every customer's account ID
D. Set distribution to PUBLIC and classify the integration key as customer or SI

**Answer:** B. Set distribution to PUBLIC and be (or become) a Docusign partner

**Explanation:** Broad availability requires PUBLIC distribution, and only Docusign partners may publish public extension apps.

**Why this answer and not the others:** B is right because global availability means public, and public publishing requires partner status. The trap is D: classifying an integration key as customer or SI belongs to eSignature go-live, not extension app publishing. A is false because public apps work in Maestro, and C misuses private sharing, which is limited to listed accounts.

**Option notes:**
- A. Public apps can be used in Maestro; distribution does not limit the extension point.
- B. Correct. PUBLIC distribution gives broad availability, and publishing a public app requires Docusign partner status.
- C. Private sharing is for a limited list of production accounts, not every customer worldwide.
- D (TRAP). Integration key classification is part of eSignature go-live, not extension app distribution.

**Q169. (API Authentication - Consent) [MEDIUM]** A small customer without Docusign Access Management or a claimed domain installs a JWT integration. The system user has never consented. How should consent be obtained?

A. Have the user grant individual consent once by opening the /oauth/auth consent URL in a browser
B. Use admin consent for external applications (scope=openid plus admin_consent_scope)
C. Call /oauth/userinfo with the integration key to activate the user
D. Regenerate the RSA key pair on the integration key

**Answer:** A. Have the user grant individual consent once by opening the /oauth/auth consent URL in a browser

**Explanation:** Without Access Management and a claimed domain, admin consent is not available, so the user grants individual consent once through the /oauth/auth URL.

**Why this answer and not the others:** A is right because individual consent is the fallback when admin consent is not possible. The trap is B: admin consent for external apps is the ISV pattern, but it requires Access Management and a claimed domain, which this customer lacks. C needs an existing access token and does not grant consent, and D only changes signing keys.

**Option notes:**
- A. Correct. Individual consent through the /oauth/auth URL is the path when admin consent is not available.
- B (TRAP). Admin consent needs Access Management and a claimed domain, which this customer does not have.
- C. /oauth/userinfo returns account and base URI details for an existing token; it does not grant consent.
- D. A new RSA key pair changes the signing key but does not record consent.

**Q170. (Go Live Process - Post go-live) [LOW]** After an integration key is promoted, which account manages the production version of the key?

A. The developer account where the key was created
B. Every customer account that uses the integration
C. The production account selected during Go-Live
D. A Docusign-owned account managed by Docusign Support

**Answer:** C. The production account selected during Go-Live

**Explanation:** The production key is tied to the production account selected during Go-Live (the OAuth management account), where its production OAuth settings are configured; the key can still make calls against other production accounts.

**Why this answer and not the others:** C is right because the production key belongs to the production account you selected. The trap is A: the developer account still manages the demo version of the key, but production settings are configured separately in the production account. B and D are wrong because a production key is managed by exactly one production account that you choose.

**Option notes:**
- A (TRAP). The developer account manages only the demo version; production settings live in the production account.
- B. Customers can use the key, but it is managed by one production account.
- C. Correct. The production account chosen during Go-Live manages the production key.
- D. Docusign does not manage the key for you; you select your own production account.

**Q171. (Docusign Connect - JSON SIM) [MEDIUM]** An admin creates an organization-level Connect configuration, and the listener developer asks which message format to parse. What is the answer?

A. JSON SIM format; organization-level configurations always use it
B. Legacy XML, the default for organization-level configurations
C. XML aggregate mode, selected in Organization Admin
D. Whatever format each account's account-level configuration uses

**Answer:** A. JSON SIM format; organization-level configurations always use it

**Explanation:** All organization-level Connect configurations use the JSON SIM model, so the listener must parse JSON SIM messages.

**Why this answer and not the others:** A is right because org-level Connect supports only JSON SIM. The trap is D: account-level configurations can use legacy formats, but that setting does not carry over to an org-level configuration. B and C name legacy options that exist only at account and envelope level.

**Option notes:**
- A. Correct. Organization-level configurations always use JSON SIM.
- B. Legacy XML is not available for organization-level configurations.
- C. Aggregate mode is a legacy XML option for account and envelope level only.
- D (TRAP). An org-level configuration has its own format, always JSON SIM, regardless of account-level settings.

**Q172. (eSignature API - Anchor tabs) [MEDIUM]** A tab uses anchorString 'Sign here:'. The signature field must appear slightly to the right of that text. Which properties shift the tab relative to the anchor?

A. xPosition and yPosition
B. anchorXOffset and anchorYOffset with anchorUnits
C. anchorIgnoreIfNotPresent
D. tabLabel and tabOrder

**Answer:** B. anchorXOffset and anchorYOffset with anchorUnits

**Explanation:** anchorXOffset and anchorYOffset, measured in anchorUnits, move the tab relative to the anchor text. The clue is shifting relative to the anchor.

**Why this answer and not the others:** B is right because the anchor offsets position the tab relative to the found text. The trap is A: xPosition and yPosition also move tabs, but they are absolute page coordinates for fixed positioning, not offsets from the anchor. C controls what happens when the anchor text is missing and D names and orders tabs.

**Option notes:**
- A (TRAP). xPosition and yPosition are absolute page coordinates used for fixed positioning.
- B. Correct. Anchor offsets in anchorUnits shift the tab relative to the anchor text.
- C. anchorIgnoreIfNotPresent handles a missing anchor string; it does not shift the tab.
- D. tabLabel and tabOrder identify and order tabs; they do not set a position relative to text.

**Q173. (eSignature Features and Web Forms - Brand destination URLs) [MEDIUM]** An implementation note covers remote signers who must be redirected to a custom page after finishing. Which branding feature is relevant?

A. Branding signing resource file
B. Brand destination URLs
C. Brand logo and color settings
D. returnUrl in EnvelopeViews:createRecipient

**Answer:** B. Brand destination URLs

**Explanation:** Among branding settings, the post-signing redirect for remote signers is the destination URLs setting.

**Why this answer and not the others:** B is right because destination URLs are the brand setting for remote-signer redirects. The trap is A: it is also a brand setting that affects the signing experience, but it controls content and appearance. C and D fail because logos and colors are visual only and returnUrl is an embedded-signing parameter, not branding.

**Option notes:**
- A (TRAP). Resource files are part of a brand too, but they change the signing UI text and appearance, not the post-signing redirect.
- B. Correct. Destination URLs are the brand setting that controls where remote signers are sent after signing events.
- C. Logos and colors change the look of emails and signing pages; they do not redirect anyone.
- D. returnUrl is not a branding feature and applies to embedded signing only.

**Q174. (Workflow Builder and Workflow API - Identity step) [MEDIUM]** A bank workflow will show participants a web form pre-filled with their account details from the system of record. Those details must not be shown until the participant's identity is confirmed. Which order fits?

A. Collect Data with Web Forms, then Verify Someone's Identity
B. Verify Someone's Identity, then Collect Data with Web Forms
C. Send Documents for Signature with an access code, then the web form
D. A Show a Confirmation Screen warning, then the web form

**Answer:** B. Verify Someone's Identity, then Collect Data with Web Forms

**Explanation:** Placing the identity step before the web form verifies the participant before any sensitive pre-filled data is displayed.

**Why this answer and not the others:** B is right because the clue is that pre-filled data must stay hidden until identity is confirmed. The trap is A: collecting data first is the usual order, but here the form already shows sensitive data, so verification must come before it. C relies on an access code for a different step, and D only warns the user.

**Option notes:**
- A (TRAP). The pre-filled form would show account data before identity is verified.
- B. Correct. Verify identity first, then show the pre-filled form.
- C. An access code on a signing step does not protect the earlier form.
- D. A warning screen does not verify identity.

**Q175. (App Center and Extension Apps - Public App Center) [MEDIUM]** An ISV that is not yet a Docusign partner submits a PUBLIC extension app for review. What happens?

A. The app is rejected immediately and must be resubmitted as private
B. Docusign contacts the ISV about partner onboarding; the app stays In Review until done
C. The app is published right away because partner status is checked later
D. The app is published only in the developer's own region

**Answer:** B. Docusign contacts the ISV about partner onboarding; the app stays In Review until done

**Explanation:** Only Docusign partners may publish public apps. Docusign verifies partner status during review and, if needed, works with the developer on partner onboarding while the app stays In Review.

**Why this answer and not the others:** B is right because partner status is checked during review and onboarding happens before publication. The trap is A: Docusign does not simply reject the app; it starts partner onboarding. C ignores the partner requirement, and D invents a region-based fallback.

**Option notes:**
- A (TRAP). Docusign does not reject it outright; it contacts the developer about joining the partner program.
- B. Correct. Partner status is verified during review, and the app remains In Review until onboarding completes.
- C. Partner status is verified during review, before publication, not afterwards.
- D. There is no region fallback for non-partners; regions are a separate publicationRegions setting.

**Q176. (API Authentication - Scopes) [LOW]** Knowledge check: an app only needs to send envelopes and read user account information. What should the developer do when requesting OAuth consent?

A. Request every scope now so users never see a second consent screen
B. Request impersonation so the app can act as any user later
C. Copy the scopes used in the Docusign quickstart sample
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection lowers risk and keeps the consent request limited to what the app actually does.

**Why this answer and not the others:** D is right because the app's needs are narrow and least privilege applies. The trap is A: avoiding repeat consent sounds user-friendly, but it grants access the app never uses. B adds impersonation that a signed-in user flow does not need, and C copies scopes chosen for a sample, not this app.

**Option notes:**
- A (TRAP). Asking for every scope breaks least privilege and asks users to approve access the app does not need.
- B. impersonation is for JWT service integrations and widens what the app can do without need.
- C. Sample scopes are chosen for the sample; they may not match this app's operations.
- D. Correct. Request only the scopes needed to send envelopes and read account info.

**Q177. (Go Live Process - API limits) [HIGH]** Two separate integrations on the same production account each make about 2,000 API calls per hour. What happens?

A. Each integration key has its own 3,000-call hourly limit, so both are fine
B. Together they exceed the 3,000 calls per hour shared by the account, so calls are blocked
C. Excess calls are queued and processed at the start of the next hour
D. Only the burst limit applies to production accounts, so the hourly total does not matter

**Answer:** B. Together they exceed the 3,000 calls per hour shared by the account, so calls are blocked

**Explanation:** The default hourly limit is 3,000 calls per account, shared by all integrations; once it is exceeded, calls are blocked until the next hour.

**Why this answer and not the others:** B is right because the limit is per account, so 4,000 combined calls exceed it. The trap is A: it would be true if the limit were per integration key, but it is shared across all apps on the account. C is wrong because excess calls fail rather than queue, and D ignores that hourly and burst limits both apply.

**Option notes:**
- A (TRAP). The hourly limit is per account and shared by all integration keys.
- B. Correct. 4,000 combined calls exceed the 3,000 per hour account limit, so further calls are blocked.
- C. Excess calls are rejected, not queued, until the hour resets.
- D. Hourly and burst limits both apply in production.

**Q178. (Docusign Connect - Security) [MEDIUM]** A security policy requires the listener to verify Docusign's client certificate during the TLS handshake before accepting any Connect message. Which control helps validate message authenticity this way?

A. A self-signed server certificate on the listener
B. Basic authentication with a shared password
C. HMAC signature validation of the message body
D. Mutual TLS between Docusign and the listener

**Answer:** D. Mutual TLS between Docusign and the listener

**Explanation:** Mutual TLS has Docusign present a client certificate that the listener verifies during the handshake, which is the check the policy demands.

**Why this answer and not the others:** D is right because only mutual TLS authenticates Docusign at the TLS layer with a certificate. The trap is C: HMAC also proves authenticity, but it checks a hash of the body after the connection is accepted, not a client certificate in the handshake. A secures only the listener side, and B uses a password header rather than a certificate.

**Option notes:**
- A. A server certificate identifies the listener, not Docusign.
- B. Basic auth sends a username and password header; no client certificate is involved.
- C (TRAP). HMAC verifies the body with a shared key after the connection is made, not a TLS client certificate.
- D. Correct. Mutual TLS lets the listener verify Docusign's client certificate.

**Q179. (eSignature API - Embedded signing) [HIGH]** During QA, a test signer still receives a Docusign email invitation, but the requirement is to sign inside the app. What is missing from the signer definition?

A. clientUserId
B. recipientId
C. routingOrder
D. EnvelopeViews:createRecipient

**Answer:** A. clientUserId

**Explanation:** Without clientUserId the signer is a remote recipient and gets an email invitation. Adding clientUserId makes the signer embedded.

**Why this answer and not the others:** A is right because clientUserId turns a remote signer into an embedded one. The trap is D: the app will also need to call createRecipient, but that is an endpoint and cannot be added to the signer definition. B and C exist for remote signers too and do not change how the signer is invited.

**Option notes:**
- A. Correct. clientUserId on the signer makes it embedded instead of an emailed remote recipient.
- B. recipientId is required for every recipient and does not change remote signing to embedded.
- C. routingOrder controls signing order; it does not decide whether a signer is embedded.
- D (TRAP). createRecipient is an API call made after the envelope exists, not part of the signer definition.

**Q180. (eSignature Features and Web Forms - Connected Fields) [MEDIUM]** A signer-provided value must be checked against an external data source while the signer completes the envelope. Which feature is designed for this?

A. Connected Fields (data verification extension)
B. Web Forms formValues prefill
C. A Data IO extension
D. Connect extension-executed event

**Answer:** A. Connected Fields (data verification extension)

**Explanation:** Verification of signer-entered values during signing is what Connected Fields provide.

**Why this answer and not the others:** A is right because Connected Fields verify field values against an external source during signing. The trap is B: it also uses external data, but it fills in values before the form is shown and does not verify signer input. C and D fail because Data IO is a Maestro extension and the Connect event only reports results.

**Option notes:**
- A. Correct. Connected Fields run the extension's verify action when the signer completes the required fields.
- B (TRAP). formValues prefill known data into a web form; they do not verify what a signer enters during signing.
- C. Data IO serves Maestro workflows (read/write a system of record), not field verification during eSignature signing.
- D. This event only reports verification results to your listener after the fact.

**Q181. (Workflow Builder and Workflow API - Extension step) [MEDIUM]** Before the web form step, a workflow must pull the customer's existing account data from Salesforce so the form can be pre-filled. Which step should be used?

A. A Read step from the installed Salesforce extension app, placed before Collect Data with Web Forms
B. A Writeback step to Salesforce, placed after signing
C. Connected fields added to the web form
D. A Send an Email step asking the sales rep for the data

**Answer:** A. A Read step from the installed Salesforce extension app, placed before Collect Data with Web Forms

**Explanation:** Read steps import data from external systems such as Salesforce into the workflow, so they must run before the form that uses the data.

**Why this answer and not the others:** A is right because it brings the data into the workflow before the form. The trap is B: a Salesforce writeback step uses the same app, but it pushes data to Salesforce after the fact, the opposite direction. C is not supported in Maestro, and D is a manual workaround.

**Option notes:**
- A. Correct. A Read step imports the Salesforce data before the form needs it.
- B (TRAP). Writeback sends data to Salesforce; it does not import it, and it runs too late.
- C. Connected fields are not supported in Maestro workflows.
- D. Emailing a rep is manual and does not fill the form automatically.

**Q182. (App Center and Extension Apps - Manifest) [HIGH]** In an extension app manifest, which object lists, for each extension, the actions that implement it?

A. extensions, through actionReferences
B. actions, through connectionsReference
C. connections
D. publisher

**Answer:** A. extensions, through actionReferences

**Explanation:** Each extension in the extensions object uses actionReferences to name the actions that implement it.

**Why this answer and not the others:** A is right because actionReferences links an extension to its actions. The trap is B: connectionsReference lives on actions and links them to a connection, not to an extension. C holds authentication settings, and D holds publisher contact details.

**Option notes:**
- A. Correct. Extensions reference their implementing actions through actionReferences.
- B (TRAP). connectionsReference links an action to a connection, the next link in the chain, not extension-to-action.
- C. connections defines authentication; it does not list actions.
- D. publisher holds organization name and contact details shown in the listing.

**Q183. (API Authentication - OAuth flow selection) [HIGH]** A corporate web portal lets employees sign in individually to send internal NDAs. The integration server is secured and can safely store client credentials. Which authentication flow should be implemented?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Implicit Grant
D. Public Authorization Code Grant

**Answer:** A. Confidential Authorization Code Grant

**Explanation:** Individual interactive sign-in plus a secure server that can store a secret is Confidential Authorization Code Grant.

**Why this answer and not the others:** A is right because the deciding clue is that the server can safely store credentials. The trap is D: Public Auth Code also signs in individual users, but it exists for clients that cannot store a secret; if the server could not, the answer would flip to D. B has no interactive user, and C is a legacy browser flow.

**Option notes:**
- A. Correct. Interactive users plus a server that can hold a secret means Confidential Authorization Code Grant.
- B. JWT Grant is for unattended service integrations, but here each employee signs in individually.
- C. Implicit Grant is a legacy browser flow that Docusign does not recommend, and the server here can store secrets.
- D (TRAP). Public Auth Code Grant is for clients that cannot store a secret, such as SPAs or mobile apps; this server can.

**Q184. (Go Live Process - Troubleshooting) [HIGH]** A Confidential Authorization Code Grant app worked in demo but returns authentication errors right after Go-Live. What should be checked first?

A. That the production key has its secret and redirect URIs, and the app uses account.docusign.com
B. That the app still sends the developer secret, since secrets are copied with the key
C. That the hourly API limit was raised for the production account
D. That all templates were recreated in the production account

**Answer:** A. That the production key has its secret and redirect URIs, and the app uses account.docusign.com

**Explanation:** Authentication errors right after Go-Live usually come from missing production OAuth settings (secret, redirect URIs) or from still using the developer authentication host.

**Why this answer and not the others:** A is right because the clue is authentication errors, which point to OAuth configuration. The trap is B: the key value is the same in production, but secrets are not copied, so the developer secret does not work. C relates to throttling, not authentication, and D would cause template errors, not authentication errors.

**Option notes:**
- A. Correct. Check the production secret, redirect URIs and the production authentication host first.
- B (TRAP). Secrets are not copied during Go-Live, so the developer secret fails in production.
- C. Rate limits cause blocked calls, not authentication failures.
- D. Missing templates produce template errors after authentication, not authentication errors.

**Q185. (Docusign Connect - Retries) [MEDIUM]** A listener processes each payload synchronously for about two minutes before replying, and the Connect logs show many retried deliveries. What should the developer change?

A. Keep synchronous processing but always return 200 at the end
B. Pause the Connect configuration during peak hours
C. Return 200 immediately and process the payload asynchronously from a queue
D. Replace Connect with polling for slow-processing envelopes

**Answer:** C. Return 200 immediately and process the payload asynchronously from a queue

**Explanation:** Slow responses time out and count as failures, so the listener should acknowledge with 200 right away and do the work asynchronously.

**Why this answer and not the others:** C is right because a fast acknowledgement stops timeouts and the resulting retries. The trap is A: returning 200 is correct, but returning it only after two minutes of work still risks the timeout. B only delays the events, and D brings back the API traffic Connect avoids.

**Option notes:**
- A (TRAP). A 200 that arrives after slow processing can still time out and trigger retries.
- B. Pausing defers deliveries; it does not fix the slow listener.
- C. Correct. Acknowledge fast, queue the payload, and process it asynchronously.
- D. Polling adds API calls and is limited to once per 15 minutes per envelope.

**Q186. (eSignature API - Make an API call to request the signing URL) [HIGH]** After a successful Envelopes:create call for an embedded recipient, what is the next API step to start the signing session?

A. Redirect the user's browser to docusign.net/embedded.
B. Display the sending interface so the user can enter tab information.
C. Send an email notification with the signing link.
D. Make an API call to request the signing URL.

**Answer:** D. Make an API call to request the signing URL.

**Explanation:** The app calls the recipient view endpoint (EnvelopeViews:createRecipient) to get a short-lived signing URL, then redirects the embedded user to it.

**Why this answer and not the others:** D is right because the signing URL must be requested from the API for each session. The trap is B: showing a sending interface is embedded sending (createSender), which prepares an envelope rather than signing it. A is not a real fixed URL and C describes remote signing.

**Option notes:**
- A. There is no fixed embedded URL; each session URL is generated by the API.
- B (TRAP). A sending interface is embedded sending, used to prepare an envelope, not to sign it.
- C. Emailing a link is remote signing; embedded signers sign through a URL the app requests.
- D. Correct. The app requests the signing URL with EnvelopeViews:createRecipient and redirects the user.

**Q187. (eSignature Features and Web Forms - Brand destination URLs) [MEDIUM]** A company wants recipients redirected to a contact page after completing remote signing. Which option controls where recipients are redirected after signing?

A. Branding Resource File
B. Brand Destination URLs
C. Custom Landing pages
D. In-Session Landing pages

**Answer:** B. Brand Destination URLs

**Explanation:** For remote signing, the redirect after completion is configured with brand destination URLs.

**Why this answer and not the others:** B is right because destination URLs are the brand setting that controls redirects after remote signing. The trap is A: it is a real brand component that customizes the signing experience, but it does not set where the recipient goes. C and D fail because they are not the documented remote-signing redirect setting.

**Option notes:**
- A (TRAP). Resource files customize the signing and email experience (text and appearance); they do not define the redirect destination.
- B. Correct. Brand destination URLs configure where remote-signing recipients are redirected after they finish.
- C. This is not the brand setting Docusign uses for post-signing redirects; the documented control is destination URLs.
- D. In-session (embedded) signing redirects are set with returnUrl, and this is not the remote-signing redirect setting.

**Q188. (Workflow Builder and Workflow API - Branching) [MEDIUM]** After the Send Documents for Signature step, the agreement must be stored in Google Drive only if the envelope is completed; otherwise the HR representative must be notified. Which design fits?

A. A Store Files step directly after signing, with no condition
B. A Connect webhook that calls custom code to decide
C. A Multi Branch Rule step on the Job Location field
D. A Branching Rule on envelope status = completed: true stores the file, false sends an email

**Answer:** D. A Branching Rule on envelope status = completed: true stores the file, false sends an email

**Explanation:** A Branching Rule on the envelope status routes completed envelopes to a Store Files step and others to a Send an Email step, as in the course onboarding example.

**Why this answer and not the others:** D is right because the condition is the envelope status, with two outcomes. The trap is A: it uses the right storage step, but without a condition it never notifies HR when the envelope is not completed. B moves the logic into custom code, and C branches on the wrong field.

**Option notes:**
- A (TRAP). Stores unconditionally and never notifies HR when signing is not completed.
- B. Custom code is unnecessary; the branching rule handles the condition natively.
- C. Job Location is not the condition; envelope status is.
- D. Correct. Branch on envelope status: completed goes to storage, otherwise HR is emailed.

**Q189. (App Center and Extension Apps - Security compliance and technical architecture) [HIGH]** After a developer submits an extension app for review from the Developer Console, what does Docusign's review evaluate?

A. Whether the app has made at least 20 successful API calls
B. The business, technical, security and functional aspects of the app
C. The developer's envelope usage fees
D. Whether the app uses the most recent SDK version

**Answer:** B. The business, technical, security and functional aspects of the app

**Explanation:** The extension app review evaluates the business, technical, security and functional aspects of the app.

**Why this answer and not the others:** B is right because those are the review areas. The trap is A: the 20-call requirement belongs to eSignature integration key go-live, not extension app review. C and D are not review criteria.

**Option notes:**
- A (TRAP). The 20 API call threshold is an eSignature go-live requirement, not extension app review.
- B. Correct. Review covers business, technical, security and functional aspects.
- C. Envelope fees are billing matters, not part of app review.
- D. SDK version is not a review criterion for extension apps.

**Q190. (API Authentication - User info) [MEDIUM]** In a pull request review, the code hard-codes https://demo.docusign.net/restapi as the API base path. The reviewer asks the developer to look up the base URI and account ID after getting the token instead. Which endpoint should the code call?

A. /oauth/token
B. /oauth/auth
C. /oauth/userinfo
D. Use account-d.docusign.com as the REST API base URI

**Answer:** C. /oauth/userinfo

**Explanation:** The code should call /oauth/userinfo and use the default account's base_uri and account_id, because accounts can live on different base URIs.

**Why this answer and not the others:** C is right because userinfo returns the correct base URI per account. The trap is D: account-d.docusign.com is the demo authentication server where userinfo lives, but it is not the REST API base URI. A and B are earlier steps of the OAuth flow.

**Option notes:**
- A. /oauth/token issues tokens; it does not report which base URI the account uses.
- B. /oauth/auth is the sign-in and consent URL, not an account lookup.
- C. Correct. /oauth/userinfo returns base_uri and account_id for the user's accounts.
- D (TRAP). account-d.docusign.com hosts the demo OAuth service, not eSignature REST API calls.

**Q191. (Go Live Process - Go-live setup) [HIGH]** Which sequence matches the main steps of the Docusign Go-Live process described in the course?

A. Make 20 API calls, request review, wait for the approval email
B. Request a production account, open a support case, copy the key manually
C. Submit to Go Live, create the key in production, then request a production account
D. Create your integration, request a production account, submit your integration to Go Live

**Answer:** D. Create your integration, request a production account, submit your integration to Go Live

**Explanation:** The course lists three main steps: create your integration, request a production account, and submit your integration to Go Live.

**Why this answer and not the others:** D is right because it lists the three steps in the course order. The trap is A: it reflects the old process, but the 20 API call requirement no longer exists. B adds a support case and manual copy that eSignature Go-Live does not use, and C reverses the order, since you need a production account before submitting.

**Option notes:**
- A (TRAP). The 20 API call step was removed from the Go-Live process.
- B. eSignature Go-Live uses Start Go live in Apps and Keys, and the key is duplicated for you.
- C. You need the integration and a production account before you submit to Go Live.
- D. Correct. Create the integration, request a production account, then submit to Go Live.

**Q192. (Docusign Connect - Troubleshooting) [LOW]** A support team needs a clear rule: what should a Connect listener do when it receives a duplicate webhook message?

A. Treat every message as new and create a new record
B. Idempotent processing based on event identifiers or envelope state
C. Ask Docusign to turn off retries for the account
D. Republish all events daily to resynchronize

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook listeners must tolerate retries and duplicate delivery by processing idempotently.

**Why this answer and not the others:** B is right because idempotency turns duplicates into no-ops. The trap is C: removing retries would stop duplicates but would also lose events whenever the listener fails, which is why retries exist. A creates duplicate records, and D generates even more duplicates.

**Option notes:**
- A. Treating repeats as new events creates duplicate records.
- B. Correct. Skip or safely reapply events already processed.
- C (TRAP). Retries protect against lost events; disabling them is not the fix for duplicates.
- D. Daily republishing creates more duplicate deliveries, not fewer.

**Q193. (eSignature API - Signing URL) [MEDIUM]** A createRecipient request for an embedded signer is being written. Which set of values does it require?

A. recipientId and routingOrder only
B. envelopeId in the body and the signer's email only
C. email, userName and clientUserId plus frameAncestors for every view
D. email, userName and clientUserId matching the envelope, plus returnUrl and authenticationMethod

**Answer:** D. email, userName and clientUserId matching the envelope, plus returnUrl and authenticationMethod

**Explanation:** The recipient view request needs email, userName and clientUserId that match the signer, plus returnUrl and authenticationMethod.

**Why this answer and not the others:** D is right because those are the required parameters for a recipient view. The trap is C: frameAncestors is required only for focused view, not for every view. A and B omit the matching recipient details the endpoint relies on.

**Option notes:**
- A. recipientId and routingOrder are not the values the recipient view request matches on.
- B. envelopeId goes in the URL path, and email alone does not identify the embedded signer.
- C (TRAP). frameAncestors (with messageOrigins) is needed only for focused view, not for every recipient view.
- D. Correct. Matching email, userName and clientUserId plus returnUrl and authenticationMethod are required.

**Q194. (eSignature Features and Web Forms - ID Evidence) [MEDIUM]** Daniel's compliance system needs the personal information and document details captured during signers' ID Verification. The account admin has enabled retention of this data. Which API should the integration call?

A. IdentityVerifications:list
B. The Connect envelope-completed payload
C. Envelopes:get on the completed envelope
D. ID Evidence API

**Answer:** D. ID Evidence API

**Explanation:** Admin-enabled retention plus retrieving captured IDV data points to the ID Evidence API.

**Why this answer and not the others:** D is right because the ID Evidence API retrieves the IDV data the admin chose to retain. The trap is A: it is the IDV call developers already know, but it lists workflows, not results. B and C fail because neither the Connect envelope payload nor envelope details contain ID evidence.

**Option notes:**
- A (TRAP). This returns IDV workflow configurations for sending, not the data captured during verification.
- B. The envelope event does not include retained ID verification data.
- C. Envelope details show status and recipients, not the retained ID evidence.
- D. Correct. Once the admin configures retention, the ID Evidence API returns the selected data from ID verification events.

**Q195. (Workflow Builder and Workflow API - Start method) [HIGH]** Leasing agents inside the company start a rental application workflow for an approved tenant from the Docusign web app, entering the tenant's name and email when they start it. Which start method fits?

A. From a link
B. From an API call
C. Manually in Docusign (Run Workflow)
D. Started by a Connect event

**Answer:** C. Manually in Docusign (Run Workflow)

**Explanation:** Manually in Docusign is for workflows started by someone in the organization, who uses Run Workflow and fills in participant details, similar to sending from a template. Users need Workflows: Prepare permission.

**Why this answer and not the others:** C is right because internal staff start it from Docusign and enter participant details. The trap is A: From a link also starts workflows without code, but it is for participants who start the workflow themselves, such as self-service forms. B needs an integration calling the API, and D is not how this process starts.

**Option notes:**
- A (TRAP). Links suit self-service starts by participants, not internal agents entering tenant details.
- B. No custom integration is involved; agents work in the Docusign web app.
- C. Correct. Internal users with Workflows: Prepare permission use Run Workflow and enter participant details.
- D. A Connect event is a notification, not how agents start this workflow.

**Q196. (App Center and Extension Apps - Connections) [MEDIUM]** An extension app manifest will call a CRM API that requires OAuth. The developer wants authentication defined once and reused by several actions. Which manifest object owns those reusable auth settings?

A. connections
B. connectionsReference
C. actions
D. extensions

**Answer:** A. connections

**Explanation:** The connections object defines reusable authentication settings; actions point to it.

**Why this answer and not the others:** A is right because connections own the auth configuration. The trap is B: connectionsReference is the pointer on each action, not the place where credentials are defined. C defines operations and D groups actions by extension type.

**Option notes:**
- A. Correct. connections defines reusable authentication for actions.
- B (TRAP). connectionsReference only points to a connection; it does not own the auth settings.
- C. actions describe operations and reference a connection; they do not own reusable auth.
- D. extensions declare extension types and their actionReferences, not auth.

**Q197. (API Authentication - PKCE) [MEDIUM]** A partner's native app cannot store a client secret securely, and each user signs in. Which OAuth configuration is correct?

A. Confidential Authorization Code Grant
B. Public Authorization Code Grant without PKCE
C. Public Authorization Code Grant with PKCE
D. JSON Web Token Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public clients use the Authorization Code Grant with PKCE; the code_challenge and code_verifier prove that the app finishing the flow is the one that started it.

**Why this answer and not the others:** C is right because a native app is a public client and PKCE is required for every Public Auth Code Grant implementation. The trap is B: it is the right grant family, but without PKCE nothing replaces the missing secret to protect the code exchange. A needs a secret, and D is for services with no user present.

**Option notes:**
- A. Confidential Auth Code Grant needs a client secret that a native app cannot keep.
- B (TRAP). Right grant family, but Docusign requires code_challenge and code_verifier for all Public Auth Code Grant implementations.
- C. Correct. Public Authorization Code Grant with PKCE is the configuration for a native app without a secret.
- D. JWT Grant is for unattended services, not a native app where users sign in.

**Q198. (Go Live Process - Integration classification) [MEDIUM]** A company builds an integration only for its own HR and legal staff. A separate vendor builds an app that many Docusign customers install and connect to their own Docusign accounts. Which detail decides that the vendor app is a Public integration?

A. It is used by many Docusign customers through their own Docusign accounts
B. It authenticates with JWT Grant instead of Authorization Code Grant
C. It sends envelopes created from server templates
D. It makes more than 3,000 API calls per hour

**Answer:** A. It is used by many Docusign customers through their own Docusign accounts

**Explanation:** Classification is determined by the business model; an app used by many Docusign customers who authorize it against their own accounts is a Public integration.

**Why this answer and not the others:** A is right because classification follows who uses the app and through which accounts. The trap is B: the OAuth flow is an important design choice, but it does not determine the classification. C and D describe technical behavior that both apps could share.

**Option notes:**
- A. Correct. Use by many customers through their own Docusign accounts makes it a Public integration.
- B (TRAP). The OAuth grant type does not determine the integration type.
- C. Using templates says nothing about who uses the app or through which accounts.
- D. Call volume affects API limits, not the classification.

**Q199. (Docusign Connect - Payload selection) [LOW]** A webhook listener only needs envelopeId, status and event timing. The team will call the API later if it needs documents or detailed metadata. Which Connect payload choice best supports that design?

A. Include every available document and recipient field
B. Configure the event payload to include only needed data
C. Switch to polling every minute
D. Use legacy XML aggregate mode to shrink each message

**Answer:** B. Configure the event payload to include only needed data

**Explanation:** Connect payloads should be minimized to the data the listener needs, especially when the app can query details later.

**Why this answer and not the others:** B is right because a minimal event payload matches what the listener uses. The trap is D: aggregate mode reduces how many messages arrive, but each legacy XML message is envelope-focused and not smaller. A inflates every message, and C abandons Connect and breaks the polling limit.

**Option notes:**
- A. Including all fields and documents makes payloads large and slow to process.
- B. Correct. Include only the data the listener needs and query the rest later.
- C. Polling every minute violates the once-per-15-minutes-per-envelope limit and loses event-driven delivery.
- D (TRAP). Aggregate mode reduces message count, not message size, and is a legacy XML option.

**Q200. (eSignature API - Embedded signing timing) [MEDIUM]** Users report expired-link errors because the app creates embedded signing URLs long before they are ready. What is the right fix?

A. Cache the URL and reuse it for later sessions
B. Increase the envelope expiration setting
C. Request the recipient view URL only when the user is ready to sign
D. Create the envelope with status created instead of sent

**Answer:** C. Request the recipient view URL only when the user is ready to sign

**Explanation:** Signing URLs are short-lived and single-use, so the app should call createRecipient at the moment the user is ready, and request a new URL for each session.

**Why this answer and not the others:** C is right because generating the URL on demand avoids its short lifetime. The trap is B: envelope expiration is a real setting, but it controls the envelope, not the minutes-long signing URL. A fails because the URL is single-use and D would leave a draft that cannot be signed.

**Option notes:**
- A. Signing URLs are single-use and short-lived, so reusing a cached URL fails.
- B (TRAP). Envelope expiration controls how long the envelope stays open, not the signing URL lifetime.
- C. Correct. Generate the recipient view URL only when the user is ready to sign.
- D. A draft envelope cannot be signed; embedded signing needs a sent envelope.

**Q201. (eSignature Features and Web Forms - Web Forms embedding) [HIGH]** Grace reviews an integration that embeds a Docusign web form in a records portal. Which pairing of URL source and client-side tool is correct?

A. Docusign JS with a signing URL from EnvelopeViews:createRecipient
B. A URL from Configurations:getForm
C. Docusign JS with the instance URL from Instances:createInstance
D. The formValues returned by Instances:getInstance

**Answer:** C. Docusign JS with the instance URL from Instances:createInstance

**Explanation:** Embedded web forms are rendered by passing the createInstance instance URL to Docusign JS.

**Why this answer and not the others:** C is right because the instance URL from createInstance is the URL that Docusign JS renders. The trap is A: it pairs the right SDK with the envelope signing URL, which belongs to embedded signing, not to a web form instance. B and D fail because getForm and getInstance return configuration details and form data, not a URL to display.

**Option notes:**
- A (TRAP). Docusign JS is right, but the URL is wrong: a recipient view URL is for an envelope, while an embedded web form uses the instance URL (its envelope is only created when the first user submits).
- B. Configurations:getForm returns the form configuration, including field names for prefill; it does not return a URL to render for a participant.
- C. Correct. The instance URL from createInstance is what Docusign JS renders for an embedded web form.
- D. formValues are the submitted or prefilled data; they are read after the fact and are not a rendering URL.

**Q202. (Workflow Builder and Workflow API - API trigger) [HIGH]** A backend calls TriggerWorkflow successfully. What does the response give the app?

A. The envelope ID of the first signing step
B. The new instance ID and a workflow instance URL
C. The workflow's trigger_input_schema
D. A consentUrl for the participant

**Answer:** B. The new instance ID and a workflow instance URL

**Explanation:** A successful TriggerWorkflow response returns the new instance's ID and a URL for the running instance, which the app can redirect to or embed.

**Why this answer and not the others:** B is right because the app needs the instance ID to track status and the URL to show the workflow. The trap is A: workflows often send envelopes, but the trigger response identifies the workflow instance, not an envelope. C comes from GetWorkflowTriggerRequirements before the trigger, and D relates to consent errors when publishing.

**Option notes:**
- A (TRAP). The response identifies the workflow instance, not an eSignature envelope.
- B. Correct. Use the instance ID with getWorkflowInstance and the URL to embed or redirect.
- C. The input schema comes from GetWorkflowTriggerRequirements, before triggering.
- D. consentUrl appears in publish errors for missing consent, not in a trigger response.

**Q203. (App Center and Extension Apps - connectionsReference) [MEDIUM]** What value must an action's connectionsReference contain?

A. The name of the extension in the extensions object
B. The external provider's OAuth client ID
C. The name of a connection defined in the connections object
D. The action's own endpoint URL

**Answer:** C. The name of a connection defined in the connections object

**Explanation:** connectionsReference names a connection defined in the connections object, so its value must match that connection's name.

**Why this answer and not the others:** C is right because the reference resolves to a named connection. The trap is A: extensions are linked to actions through actionReferences, not through connectionsReference. B is a credential stored in the connection, and D is defined by the action itself.

**Option notes:**
- A (TRAP). Extension names are used with actionReferences on the extension side, not in connectionsReference.
- B. The client ID is stored inside the connection, not in the reference.
- C. Correct. It must match the name of a connection in the connections object.
- D. The endpoint is part of the action definition, not the connection reference.

**Q204. (API Authentication - Bearer tokens) [LOW]** A sales contracting app gets an access token, but REST calls return 401 Unauthorized. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the Authorization header as Bearer <authorization code>
C. In the state parameter of the request
D. In a browser cookie set by the app

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Why this answer and not the others:** A is right because the access token goes in a Bearer Authorization header. The trap is B: it uses the right header format, but the authorization code is only exchanged at /oauth/token and expires after 120 seconds. C is a CSRF value used during sign-in, and D is not read by the API.

**Option notes:**
- A. Correct. Supply the access token as Authorization: Bearer <access_token>.
- B (TRAP). The authorization code must be exchanged at /oauth/token for an access token; it cannot call APIs.
- C. state protects the sign-in redirect against CSRF; it does not carry API credentials.
- D. Docusign REST APIs do not read the token from cookies; use the Authorization header.

**Q205. (Go Live Process - Production endpoints) [MEDIUM]** A production app calls userinfo before every single API request to look up the account's base URI. What does Docusign recommend instead?

A. Call userinfo for every request, because base URIs change often
B. Get base_uri once when the user first authenticates and cache it
C. Read the base URI from the developer account's Apps and Keys page
D. Skip userinfo and derive the base URI from the integration key

**Answer:** B. Get base_uri once when the user first authenticates and cache it

**Explanation:** Docusign recommends getting base_uri from userinfo once when the user first authenticates and caching it, because accounts move between base URIs infrequently.

**Why this answer and not the others:** B is right because base URIs rarely change and can be cached for a day or more. The trap is A: calling userinfo is correct, but doing it on every request is wasteful since base URIs change infrequently. C gives the demo value, and D is wrong because the integration key does not encode the account's server.

**Option notes:**
- A (TRAP). Base URIs change infrequently, so calling userinfo for every request wastes calls.
- B. Correct. Retrieve base_uri once at first authentication and cache it.
- C. The developer account shows the demo base URI, not the production account's base URI.
- D. The integration key does not identify the account's server; userinfo does.

**Q206. (Docusign Connect - Envelope-level Connect) [LOW]** A sender needs webhook events for a single API-sent envelope only, and the setting must not carry over to the next envelope the app sends. Which approach matches Docusign platform behavior?

A. An account-level Connect configuration for the sending user
B. An organization-level Connect configuration
C. A scheduled Envelopes:get call for that envelope
D. Add an eventNotification object to the Envelopes:create request

**Answer:** D. Add an eventNotification object to the Envelopes:create request

**Explanation:** Envelope-level Connect is configured per envelope and must be set again on the next envelope, which matches the requirement that the setting not carry over.

**Why this answer and not the others:** D is right because eventNotification lives on one envelope and does not persist. The trap is A: account-level configurations are configured once and stay active until disabled, so they would apply to the next envelope too. B also persists and spans accounts, and C is polling rather than a webhook.

**Option notes:**
- A (TRAP). Account-level configurations are configured once and used until disabled, so they would also cover later envelopes.
- B. Organization-level configurations persist and cover all or selected accounts in the org.
- C. Scheduled Envelopes:get calls are polling; they add API traffic and are limited to once per 15 minutes per envelope.
- D. Correct. eventNotification applies only to the envelope created with it and must be reconfigured for the next envelope.

**Q207. (eSignature API - Embedded sending) [MEDIUM]** Guidance for an embedded sending feature must say what state the envelope needs before the app requests the sender view. What should it recommend?

A. Status sent, so recipients are already notified
B. Status created (draft)
C. Status delivered
D. Status completed

**Answer:** B. Status created (draft)

**Explanation:** EnvelopeViews:createSender is used on a draft envelope, created with status created, so the user can tag and send it in the app.

**Why this answer and not the others:** B is right because the sender view prepares an envelope that has not been sent. The trap is A: sent is the usual create value, but a sent envelope is already out and cannot go through embedded preparation. C and D are statuses Docusign sets after recipients act.

**Option notes:**
- A (TRAP). A sent envelope has already gone to recipients, so there is nothing left to prepare and send.
- B. Correct. Embedded sending starts from a draft envelope created with status created.
- C. delivered is set by Docusign when a recipient opens the envelope; it is not a preparation state.
- D. completed is a terminal status after all recipients finish.

**Q208. (eSignature Features and Web Forms - Web Form correlation) [HIGH]** An API-driven intake flow creates one embedded web form instance per customer record. Which value should be supplied so that instances can be correlated back to the app's records?

A. The web form configuration formId
B. clientUserId
C. A brandId
D. The returnUrl

**Answer:** B. clientUserId

**Explanation:** The value that ties each instance to one record in your app is clientUserId.

**Why this answer and not the others:** B is right because clientUserId is the per-user identifier supplied on createInstance. The trap is A: a configuration ID sounds like a tracking key, but it is the same for every instance of the form. C and D fail because they control branding and redirect, not identity.

**Option notes:**
- A (TRAP). formId identifies the configuration all instances are created from, so it is shared across customers.
- B. Correct. clientUserId is the developer-supplied identifier of the user in your system, required for embedded instances.
- C. brandId only selects branding for the envelope; it does not identify a customer.
- D. returnUrl controls where the user goes after the session; it is not an identifier.

**Q209. (Workflow Builder and Workflow API - Runtime errors) [MEDIUM]** A workflow with a Google Drive Store Files step runs in a new Docusign account. Instances fail at that step with an error that the app is unavailable, while all earlier steps succeed. What is the most likely cause?

A. The Google Drive extension app is not installed and authorized in that account
B. The Branching Rule before signing is in the wrong order
C. The integration's token lacks the aow_manage scope
D. Connect is not configured for JSON SIM

**Answer:** A. The Google Drive extension app is not installed and authorized in that account

**Explanation:** Extension app steps rely on apps that an administrator has installed and authorized in the account. Runtime errors at an app step often trace to an uninstalled or unauthorized extension.

**Why this answer and not the others:** A is right because only the app step fails, and the error names the app. The trap is C: missing aow_manage is a common error, but it blocks API calls to the Maestro API, not the execution of one step inside a running instance. B would change routing, not cause an app error, and D only affects notifications.

**Option notes:**
- A. Correct. Install and authorize the Google Drive extension app in this account.
- B. Step order affects routing; it does not make an app unavailable.
- C (TRAP). aow_manage governs Maestro API calls, and earlier steps already run fine.
- D. Connect settings affect event delivery, not step execution.

**Q210. (App Center and Extension Apps - Connected Fields) [HIGH]** A government agency must confirm the validity of a U.S. Social Security Number entered in an envelope, using a standard verification type at the eSignature Add Fields view and signing. Which extension type fits?

A. Data IO
B. File IO
C. Data Verification (SSN verification)
D. Connected Fields

**Answer:** C. Data Verification (SSN verification)

**Explanation:** SSN verification is one of the Data Verification extensions, which verify specific standard data types at the Add Fields view and signing.

**Why this answer and not the others:** C is right because SSN is a predefined standard type covered by Data Verification. The trap is D: connected fields use the same extension point but are for custom data verified against your own system of record. A runs in Maestro workflows, and B stores files.

**Option notes:**
- A. Data IO reads and writes records in Maestro workflows.
- B. File IO stores documents.
- C. Correct. SSN verification is a Data Verification extension for a standard data type.
- D (TRAP). Connected fields verify custom values against your system of record, not a standard SSN check.

**Q211. (API Authentication - OAuth flow selection) [MEDIUM]** A portal team still uses a legacy flow that returns the access token directly in the browser redirect. Their app has a web server that can store a client secret, and users sign in interactively. Which flow should they move to?

A. Public Authorization Code Grant with PKCE
B. JSON Web Token Grant
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Because the app has a server that can protect a secret and users sign in interactively, the recommended replacement is Confidential Authorization Code Grant.

**Why this answer and not the others:** D is right because the deciding clue is the web server that can store a secret. The trap is A: Public Auth Code with PKCE is the usual replacement for Implicit in browser-only apps, but this app is not browser-only. B has no user sign-in, and C is the legacy flow they are leaving.

**Option notes:**
- A (TRAP). Public Auth Code Grant with PKCE replaces Implicit for SPAs that have no server; this app does have one that can keep a secret.
- B. JWT Grant is for service integrations with no user present, while these users sign in interactively.
- C. Implicit Grant is the legacy flow described in the stem and is not recommended.
- D. Correct. Server that can store a secret plus interactive users means Confidential Authorization Code Grant.

**Q212. (Go Live Process - In the Apps and Keys section of Docusign eSignature Adm) [LOW]** Where do you specify allowed origins for an eSignature integration that implements CORS?

A. In the Apps and Keys section of Docusign eSignature Admin
B. In a separate CORS section of Docusign eSignature Admin
C. In the list of scopes requested when obtaining an access token
D. In the request headers of each API request

**Answer:** A. In the Apps and Keys section of Docusign eSignature Admin

**Explanation:** Allowed CORS origins are part of the integration key's settings, configured in Apps and Keys together with authentication and redirect URIs.

**Why this answer and not the others:** A is right because CORS configuration is set on the integration key in Apps and Keys. The trap is B: it names the right product area, but there is no standalone CORS section; origins are configured under the key. C controls permissions, not origins, and D is wrong because Docusign enforces the configured allowlist, not values the client sends.

**Option notes:**
- A. Correct. CORS origins are configured on the integration key in Apps and Keys.
- B (TRAP). There is no standalone CORS section; origins are set on the integration key.
- C. Scopes control what the token may do, not which browser origins are allowed.
- D. The client cannot declare its own allowed origins; Docusign checks the configured allowlist.

**Q213. (Docusign Connect - Connect vs polling) [MEDIUM]** An implementation note must tell developers how a contract system should track envelope status in production. Which design is preferred?

A. Poll Envelopes:get every few minutes for every open envelope
B. Call Envelopes:listStatusChanges continuously as the only status mechanism
C. Subscribe to Connect events; use listStatusChanges only for catch-up
D. Have users click a Refresh button that calls Envelopes:get

**Answer:** C. Subscribe to Connect events; use listStatusChanges only for catch-up

**Explanation:** Docusign recommends Connect for status tracking, with Envelopes:listStatusChanges using overlapping time spans only to catch up on anything missed.

**Why this answer and not the others:** C is right because events arrive as they happen and polling is reserved for recovery. The trap is B: listStatusChanges is the right call for catch-up, but calling it continuously as the main mechanism is still polling. A breaks the 15-minute per-envelope polling limit, and D depends on manual refreshes that still poll.

**Option notes:**
- A. Polling every few minutes per envelope exceeds the once-per-15-minutes limit.
- B (TRAP). listStatusChanges is meant for catch-up; using it continuously is still a polling design.
- C. Correct. Connect for real-time events, plus listStatusChanges with overlapping windows for catch-up.
- D. Manual refresh still polls the API and does not give timely status.

**Q214. (eSignature API - Bulk send) [MEDIUM]** A developer is planning a bulk send with the eSignature API v2.1. Which sequence of steps is correct?

A. Create a draft envelope, create a bulk send list, optionally test, then initiate the bulk send
B. Create a bulk send list, send the envelope with status sent, then attach the list
C. Initiate the bulk send, then create the bulk send list from the results
D. Create one envelope per recipient, then group them into a bulk send list

**Answer:** A. Create a draft envelope, create a bulk send list, optionally test, then initiate the bulk send

**Explanation:** The bulk send process is: create a draft envelope, create a bulk send list, test the bulk send (optional), initiate the bulk send, and optionally check its status.

**Why this answer and not the others:** A is right because the list is applied to a draft envelope when the bulk send is initiated. The trap is B: it has the right building blocks, but sending the envelope with status sent delivers it instead of using it as the bulk send source. C reverses the order and D creates individual envelopes, which is what Bulk Send does for you.

**Option notes:**
- A. Correct. Draft envelope, bulk send list, optional test, then initiate the bulk send.
- B (TRAP). Sending the envelope first delivers it to its own recipients; bulk send needs a draft source.
- C. The list must exist before the bulk send is initiated, since it supplies the recipients.
- D. Bulk Send creates the per-recipient envelopes itself; creating them manually defeats the purpose.

**Q215. (eSignature Features and Web Forms - Identity verification) [HIGH]** An envelope sent with eSignature REST API v2.1 must make the signer scan a passport before signing. What should the recipient configuration include?

A. identityVerification.workflowId of the ID verification workflow
B. identityVerification.workflowId of the phone authentication workflow
C. authenticationMethod on the createRecipient request
D. A clientUserId for embedded signing

**Answer:** A. identityVerification.workflowId of the ID verification workflow

**Explanation:** A passport scan is ID verification, so the recipient needs the IDV workflow's workflowId.

**Why this answer and not the others:** A is right because the IDV workflow is the one that verifies identity documents such as passports. The trap is B: phone authentication uses the same identityVerification.workflowId field, so the shape is right but the workflow is the wrong one. C and D fail because recording authenticationMethod enforces nothing and clientUserId only controls embedded signing.

**Option notes:**
- A. Correct. The IDV workflow ID (from IdentityVerifications:list) in the recipient's identityVerification object enforces the document check.
- B (TRAP). The mechanism is right, but the phone authentication workflow sends a code by call or SMS; it does not check a passport.
- C. This only records your app's authentication on the certificate; it does not enforce a passport check.
- D. clientUserId only makes the recipient embedded; it adds no identity check.

**Q216. (Workflow Builder and Workflow API - Embedding workflow) [HIGH]** An app will embed workflow instances and pass starting variable values in the trigger_inputs object of TriggerWorkflow. Which start method does Docusign recommend for the workflow?

A. From a link
B. Manually in Docusign
C. Triggered from a CLM workflow
D. From an API call

**Answer:** D. From an API call

**Explanation:** For integrations that pass starting variable values in trigger_inputs, Docusign recommends setting the start method to From an API call.

**Why this answer and not the others:** D is right because the app supplies starting variables through the API. The trap is A: From a link is also supported for embedded instances, but Docusign recommends From an API call when trigger_inputs carry starting values. B and C are designed to be started from within Docusign, not by an external app.

**Option notes:**
- A (TRAP). Supported for embedding, but not the recommended method when passing trigger_inputs.
- B. Manual start is done by internal users in Docusign, not by an app.
- C. A CLM-triggered start runs from within Docusign CLM.
- D. Correct. From an API call is recommended when the app passes starting variables.

**Q217. (App Center and Extension Apps - API proxy) [MEDIUM]** A team's existing backend API works but does not match the format Docusign sends for extension actions. Why would they put an API proxy in front of it?

A. To let Docusign call the API without OAuth
B. To translate Docusign's request and response format without changing the backend
C. To let the app skip the App Center review
D. To cache completed envelope documents for Connect

**Answer:** B. To translate Docusign's request and response format without changing the backend

**Explanation:** An API proxy transforms Docusign's request and response format to match the existing API, so the backend does not need to change.

**Why this answer and not the others:** B is right because translation without backend changes is the proxy's purpose. The trap is A: the app still authenticates through its connection (the proxy itself needs authorization). C is wrong because every app goes through review, and D confuses the proxy with Connect.

**Option notes:**
- A (TRAP). Authorization is still required; the extension app must be authorized with the platform or proxy.
- B. Correct. The proxy adapts formats so the existing backend can stay unchanged.
- C. A proxy has no effect on the review requirement.
- D. Connect and document caching are unrelated to an API proxy for extension actions.

**Q218. (API Authentication - OAuth flow selection) [MEDIUM]** A browser-only SPA cannot protect a client secret, and each user must authenticate individually. A developer proposes JWT Grant so users never see a login page. Which flow should the developer choose?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Each user must authenticate individually in a client that cannot keep a secret, which is Public Authorization Code Grant with PKCE.

**Why this answer and not the others:** C is right because users must sign in themselves and the SPA cannot hold a secret. The trap is B: JWT avoids a login page, but it needs a protected RSA private key (impossible in a browser) and does not authenticate the person at the keyboard. A needs a client secret, and D is legacy.

**Option notes:**
- A. Confidential Auth Code Grant needs a client secret that a browser-only app cannot protect.
- B (TRAP). JWT would put the RSA private key in the browser and would skip individual user authentication, which the requirement forbids.
- C. Correct. Individual sign-in in a client without a secret is Public Authorization Code Grant with PKCE.
- D. Implicit Grant is legacy and not recommended for new or updated Docusign integrations.

**Q219. (Go Live Process - Templates in production) [MEDIUM]** After Go-Live, how can a team add its templates to the production account?

A. Create them in production with the eSignature web app or the eSignature REST API
B. They are added automatically when the integration key goes live
C. Attach them to the Go-Live request so the review copies them
D. Point the production app at the developer account's templates

**Answer:** A. Create them in production with the eSignature web app or the eSignature REST API

**Explanation:** Users, templates and settings are added to the production account with Docusign Admin, the web app, or the eSignature REST API; Go-Live does not copy them.

**Why this answer and not the others:** A is right because production data must be created in the production account. The trap is B: the key is duplicated automatically, which makes it easy to assume templates follow, but they do not. C is not part of the Go-Live request, and D fails because production calls cannot use developer account data.

**Option notes:**
- A. Correct. Recreate or upload the templates in the production account by UI or API.
- B (TRAP). Only the integration key is duplicated; templates are not.
- C. The Go-Live request selects a production account; it does not carry templates.
- D. Production calls work against production accounts; developer account templates are not reachable.

**Q220. (Docusign Connect - Configuration level) [HIGH]** Which statement about Docusign Connect configuration levels is correct?

A. Account-level Connect is the only level that supports JSON SIM
B. Organization-level Connect always uses the JSON SIM format
C. Envelope-level Connect can be created from the eSignature Send page
D. Organization-level Connect supports legacy XML aggregate messages

**Answer:** B. Organization-level Connect always uses the JSON SIM format

**Explanation:** Organization-level configurations always use the JSON SIM model; legacy XML and aggregate options exist only at account and envelope level.

**Why this answer and not the others:** B is right because org-level Connect is JSON SIM only. The trap is D: aggregate mode is a real legacy option, but only for account- and envelope-level configurations using XML. A is false because JSON SIM is supported at all three levels, and C is false because eventNotification can be set only through the API.

**Option notes:**
- A. JSON SIM is supported at organization, account and envelope level.
- B. Correct. All organization-level configurations use JSON SIM.
- C. Envelope-level webhooks are API only; the Send page cannot create them.
- D (TRAP). Legacy XML and aggregate mode are available only at account and envelope level.

**Q221. (eSignature API - Envelope create) [MEDIUM]** A records office reviews a create-envelope request built with the template reference model (templateId plus templateRoles). The envelope must reach signers immediately. Which status should the request set?

A. created
B. voided
C. completed
D. sent

**Answer:** D. sent

**Explanation:** Whatever the envelope model, status sent in the create request sends the envelope immediately. The clue is that it must reach signers immediately.

**Why this answer and not the others:** D is right because sent is the status that delivers the envelope on creation, including with templateId and templateRoles. The trap is A: created is valid in the same request but only saves a draft. B cancels an in-process envelope and C is a terminal status Docusign sets after all recipients finish.

**Option notes:**
- A (TRAP). created saves the envelope as a draft; nothing is delivered until the status is later changed to sent.
- B. voided is used to cancel an envelope that is already in process; it cannot be used to deliver a new one.
- C. completed is reached by Docusign after every recipient finishes; an integration does not set it on create.
- D. Correct. status sent tells Envelopes:create to send the envelope to recipients immediately.

**Q222. (eSignature Features and Web Forms - Recipient authentication) [MEDIUM]** A real-estate team's ticket says: before opening the envelope, the signer must type a code that Docusign texts to them. Which option implements this?

A. An access code on the recipient
B. The email verification extension (Verify.Version1.Email)
C. Docusign JS focused view
D. Phone authentication on the recipient

**Answer:** D. Phone authentication on the recipient

**Explanation:** The clue is a code texted by Docusign before the envelope opens, which is phone authentication.

**Why this answer and not the others:** D is right because phone authentication texts the code and requires it before access. The trap is A: it is the closest code-based method, but the sender chooses the code and delivers it separately. B and C fail because email verification validates field data and focused view only affects the signing UI.

**Option notes:**
- A (TRAP). An access code is a sender-defined secret shared out of band; Docusign does not text it.
- B. This extension verifies an email address value in a field or web form; it does not gate envelope access with a texted code.
- C. Focused view changes the embedded signing display and adds no authentication.
- D. Correct. Phone authentication sends the code by SMS (or voice) and blocks access until it is entered.

**Q223. (Workflow Builder and Workflow API - Installed extensions) [HIGH]** A customer wants its Maestro workflows to use a partner's Docusign extension app listed in the App Center. Who makes the app available to workflow designers, and where?

A. The developer registers it in the Developer Console under their own integration key
B. A designer uploads the app manifest into Workflow Builder
C. An account administrator installs it from Docusign App Center
D. A developer adds the partner's URL to a Connect configuration

**Answer:** C. An account administrator installs it from Docusign App Center

**Explanation:** Administrators install extension apps from Docusign App Center and authorize them for the account. The app's steps then become available in Workflow Builder.

**Why this answer and not the others:** C is right because installation is an admin action in App Center. The trap is A: the Developer Console is where extension apps are registered and tested by the app's builder, not where a customer installs a partner app. B is not how apps are added, and D configures event notifications.

**Option notes:**
- A (TRAP). The Developer Console is for building and registering extension apps, not installing partner apps.
- B. Designers do not upload manifests; they use apps already installed in the account.
- C. Correct. An administrator installs and authorizes it from App Center.
- D. Connect delivers event notifications; it does not install apps.

**Q224. (App Center and Extension Apps - Firewall) [MEDIUM]** During testing, Docusign cannot reach an action endpoint running at http://localhost:3000 on the developer's laptop. What is the underlying problem?

A. Docusign's servers need a publicly reachable HTTPS endpoint
B. The action's connectionsReference is misspelled
C. The app must be published to the App Center before it can be tested
D. The laptop needs a CNAME DNS entry for apps.docusign.com

**Answer:** A. Docusign's servers need a publicly reachable HTTPS endpoint

**Explanation:** Docusign calls extension endpoints from its own servers, so the endpoint must be reachable from the internet over HTTPS (directly, through a firewall allow-list, or via a proxy).

**Why this answer and not the others:** A is right because localhost is not reachable from Docusign. The trap is B: a bad connectionsReference is a manifest validation problem, not a reachability one. C is false because apps are tested in the developer account before publishing, and D is not a requirement.

**Option notes:**
- A. Correct. Docusign can only call an endpoint it can reach publicly over HTTPS.
- B (TRAP). A misspelled reference would fail manifest validation, not network reachability.
- C. Apps are tested in the Developer Console before review and publishing.
- D. No DNS entry for Docusign domains is needed; the endpoint must be reachable.

**Q225. (API Authentication - JWT Grant) [MEDIUM]** A nightly service has an RSA key pair on its integration key. It signs an assertion containing iss (integration key), sub (user ID), and aud (account-d.docusign.com), and no person signs in. Which authentication model is appropriate?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** Signing an assertion with an RSA private key using iss, sub, and aud claims is the JWT Grant flow for unattended services.

**Why this answer and not the others:** B is right because an RSA-signed assertion with iss, sub, and aud is how JWT Grant requests a token. The trap is A: Confidential Auth Code also runs on a server and uses integration key credentials, but it authenticates with a secret key and an authorization code from a user sign-in. C and D need a user in a browser.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant uses a secret key and an authorization code from an interactive sign-in, not an RSA-signed assertion.
- B. Correct. An RSA-signed assertion with iss, sub, and aud claims is JWT Grant.
- C. Public Auth Code Grant with PKCE uses a code_verifier and an interactive user, not an RSA assertion.
- D. Implicit Grant is a legacy browser flow with no assertion and no server-side signing.

**Q226. (Go Live Process - Post go-live) [MEDIUM]** A business user asks whether the envelopes signed during development testing are legally binding. What is the correct answer?

A. Yes, all signed envelopes are legally binding in either environment
B. Yes, if a real person signed them with a real email address
C. Only after the key shows App is live do demo envelopes become binding
D. No; developer account envelopes are not binding, production envelopes are

**Answer:** D. No; developer account envelopes are not binding, production envelopes are

**Explanation:** eSignature transactions captured with a developer account are not legally binding; once the integration moves to production, its transactions become legally binding.

**Why this answer and not the others:** D is right because legal effect depends on the environment. The trap is C: Go-Live does make the integration's transactions binding, but only new production transactions, not the envelopes sent earlier in demo. A and B ignore that the developer environment never produces binding agreements.

**Option notes:**
- A. Developer account envelopes are never legally binding.
- B. Who signed does not matter; the developer environment is not legally binding.
- C (TRAP). Going live affects production transactions only; earlier demo envelopes stay non-binding.
- D. Correct. Developer envelopes are not legally binding; production envelopes are.

**Q227. (Docusign Connect - Connect subscription to the recipient-completed event) [HIGH]** A company's internal dashboard shows whether each individual recipient has signed an envelope. What is the most efficient way to obtain this status?

A. Connect subscription to the recipient-completed event
B. Polling request to the Envelopes: listStatus endpoint
C. Polling request to the EnvelopeRecipients: list endpoint
D. Connect subscription to the envelope-completed event

**Answer:** A. Connect subscription to the recipient-completed event

**Explanation:** A Connect subscription to recipient-completed pushes a message as each recipient finishes, giving per-recipient status without polling.

**Why this answer and not the others:** A is right because the requirement is per-recipient status, delivered by webhook. The trap is D: envelope-completed is also a Connect event, but it fires only once the whole envelope is done, so it cannot show individual recipients' progress. B and C are polling calls that waste API calls, and B returns envelope-level status only.

**Option notes:**
- A. Correct. recipient-completed fires for each recipient who finishes, pushed by Connect.
- B. Polling Envelopes:listStatus wastes calls and gives envelope-level, not per-recipient, status.
- C. EnvelopeRecipients:list gives recipient status but only by polling, which is inefficient.
- D (TRAP). envelope-completed fires only when every recipient is done, too coarse for per-recipient status.

**Q228. (eSignature API - Embedded signing) [MEDIUM]** Signatures must be captured from within your application. What should be added to the eSignature REST API payload so recipients sign inside the application?

A. email property set to null
B. clientUserId property
C. emailSubject property
D. emailNotification property set to false

**Answer:** B. clientUserId property

**Explanation:** Adding clientUserId marks the recipient as embedded, so they sign inside your app instead of through emailed remote signing.

**Why this answer and not the others:** B is right because clientUserId is the documented way to make a recipient embedded. The trap is D: it sounds like turning off email makes signing embedded, but emailNotification customizes email settings and does not make the signer embedded. A breaks the recipient (email is still required for createRecipient) and C is only the email subject line.

**Option notes:**
- A. The recipient's email is still needed; it must match in the createRecipient request.
- B. Correct. clientUserId marks the recipient as embedded so signing happens in your app.
- C. emailSubject sets the subject line of the envelope email; it has nothing to do with embedding.
- D (TRAP). emailNotification customizes recipient email settings; it does not make a recipient embedded.

**Q229. (eSignature Features and Web Forms - Workflow steps) [LOW]** A bank lets customers start account opening from its online banking portal: a Docusign web form collects information, some fields are pre-filled with known customer data, the experience stays inside the portal, and it ends in signing. Which approach fits?

A. Start the workflow 'From a link', pass data through the trigger URL to populate starting variables, and embed the workflow in the portal
B. Use 'From an API call', share a public Web Form URL, and pre-fill with query parameters built in the Web Forms builder
C. Use the 'Manually by someone in your organization' start method and step variables to pre-fill
D. Trigger by API, set signing to remote signing, and rely on Docusign Connect to pre-fill data

**Answer:** A. Start the workflow 'From a link', pass data through the trigger URL to populate starting variables, and embed the workflow in the portal

**Explanation:** A link-started workflow lets the portal start it and pass starting-variable data for pre-fill, and embedding keeps the experience inside the portal.

**Why this answer and not the others:** A is right because it covers customer-initiated start, pre-fill through starting variables, and an embedded experience. The trap is B: it names real start methods and Web Forms features but sends the customer to a public form instead of pre-filling through starting variables. C fails because a manual start is internal, and D fails because remote signing leaves the portal and Connect does not pre-fill.

**Option notes:**
- A. Correct. The portal launches the workflow from a link, the starting variables carry the pre-fill data, and embedding keeps the customer in the portal.
- B (TRAP). It mixes an API-triggered start with a shared public form link, which takes the customer out of the integrated experience and is not how start-variable pre-fill works.
- C. A manual start is run by someone in your organization, not by the customer from the portal.
- D. Remote signing sends the customer to email, and Connect only sends event notifications; it cannot pre-fill data.

**Q230. (Workflow Builder and Workflow API - JSON SIM) [HIGH]** A webhook listener must track Maestro workflow instances through events such as workflow-completed. Which Connect message format must be configured?

A. JSON SIM
B. JSON aggregated
C. XML SIM
D. XML aggregated

**Answer:** A. JSON SIM

**Explanation:** Maestro workflow events (workflow-started, workflow-failed, workflow-completed) are only available with the JSON SIM event message format.

**Why this answer and not the others:** A is right because workflow events are delivered only as JSON SIM. The trap is C: XML SIM also sends individual messages, but it is a legacy format and does not carry Maestro workflow events. B and D are aggregate formats, which are legacy and envelope-focused.

**Option notes:**
- A. Correct. Maestro events are only available in JSON SIM.
- B. Aggregate JSON is a legacy envelope-focused format without workflow events.
- C (TRAP). Individual XML messages are legacy and do not carry workflow events.
- D. Legacy aggregate XML does not deliver Maestro events.

**Q231. (App Center and Extension Apps - Connections) [MEDIUM]** In the extension app JSON manifest, which core object defines the authentication mechanism the app uses to access the external platform?

A. publisher
B. actions
C. connections
D. extensions

**Answer:** C. connections

**Explanation:** The connections object defines the authentication (for example OAuth parameters) used to reach the external platform.

**Why this answer and not the others:** C is right because connections hold the auth configuration. The trap is B: actions call the platform but only reference a connection for auth. A is publisher contact information and D lists extension types and their actions.

**Option notes:**
- A. publisher holds organization and contact details.
- B (TRAP). Actions use a connection through connectionsReference; they do not define auth.
- C. Correct. connections defines how the app authenticates to the external platform.
- D. extensions declare extension types and actionReferences, not authentication.

**Q232. (API Authentication - Consent) [HIGH]** A company built its own internal JWT integration (the integration key is owned by its organization). It has Access Management and a claimed domain and wants one action to consent for all users in that domain. What should it do?

A. Grant admin consent in Docusign Admin > Connected Apps > Authorize Application
B. Use admin consent for external applications (scope=openid plus admin_consent_scope)
C. Have each user grant individual consent through /oauth/auth
D. Mark the integration key as internal during Go-Live review

**Answer:** A. Grant admin consent in Docusign Admin > Connected Apps > Authorize Application

**Explanation:** For an internal app whose key belongs to the organization, an admin grants consent for all reserved-domain users from Docusign Admin > Connected Apps > Authorize Application.

**Why this answer and not the others:** A is right because the app is internal and the org has Access Management and a claimed domain. The trap is B: it is also admin consent, but the openid plus admin_consent_scope URL flow is for external (ISV) apps owned by another organization. C works but requires every user to act, and D is not a consent mechanism.

**Option notes:**
- A. Correct. Internal apps get admin consent from Docusign Admin > Connected Apps > Authorize Application.
- B (TRAP). This is admin consent for external apps owned by another organization, not an internal integration key.
- C. Individual consent works, but it needs each user to act instead of one admin action.
- D. Go-Live review promotes a key to production; it does not grant consent to anyone.

**Q233. (Go Live Process - API limits) [HIGH]** A batch job sends a sudden spike of API calls. What is the default burst limit in production?

A. 3,000 calls per 30 seconds
B. 200 calls per 30 seconds
C. 500 calls per 30 seconds
D. 1,000 calls per minute

**Answer:** C. 500 calls per 30 seconds

**Explanation:** The burst limit is 500 calls per 30 seconds in production (200 in the developer environment), in addition to the 3,000 per hour account limit.

**Why this answer and not the others:** C is right because production allows 500 calls per 30 seconds. The trap is B: 200 per 30 seconds is the developer environment's burst limit, not production's. A borrows the hourly number, and D is not a Docusign limit.

**Option notes:**
- A. 3,000 is the hourly account limit, not the 30-second burst limit.
- B (TRAP). 200 per 30 seconds is the developer environment burst limit.
- C. Correct. Production allows 500 calls per 30 seconds.
- D. This is not the documented burst limit.

**Q234. (Docusign Connect - JSON SIM) [MEDIUM]** When the last signer completes an envelope, a listener must receive one message for recipient-completed and a separate message for envelope-completed. Which Connect setting fits?

A. JSON SIM format (one message per event)
B. XML aggregate mode
C. Organization-level Connect with legacy XML
D. Polling listStatusChanges for both statuses

**Answer:** A. JSON SIM format (one message per event)

**Explanation:** SIM (send individual messages) delivers a message for each triggering event, so recipient-completed and envelope-completed arrive separately.

**Why this answer and not the others:** A is right because the listener needs each event as its own message. The trap is B: aggregate mode would combine recipient-completed and envelope-completed into a single message, the exact opposite of the requirement. C is impossible because org-level is JSON SIM only, and D is polling, not event delivery.

**Option notes:**
- A. Correct. SIM sends one message per event, so both events arrive separately.
- B (TRAP). Aggregate mode combines recipient-completed and envelope-completed into one message.
- C. Organization-level configurations cannot use legacy XML.
- D. Polling is not a webhook and adds API calls.

**Q235. (eSignature API - Draft envelope) [MEDIUM]** A document generation flow must create the envelope, fill the docGen form fields, and only then send it. Which status should the initial Envelopes:create request use?

A. sent
B. draft
C. created
D. completed

**Answer:** C. created

**Explanation:** Document generation needs a draft envelope: create it with status created, update the docGen fields, then send it. The clue is that fields are filled before sending.

**Why this answer and not the others:** C is right because created is the API value that builds the envelope without sending it. The trap is B: the envelope is a draft, but draft is not a valid status value. A would send before the fields are filled and D is set only by Docusign at the end of the process.

**Option notes:**
- A. sent would deliver the envelope before the docGen fields are populated.
- B (TRAP). draft is the concept, not the value; the status property must be created.
- C. Correct. status created keeps the envelope as a draft while the docGen form fields are updated.
- D. completed is set by Docusign after all recipients finish; it cannot start a flow.

**Q236. (eSignature Features and Web Forms - Brand destination URLs) [LOW]** Remote signers should be redirected to a custom page after finishing. Which branding feature is relevant?

A. Branding email resource file
B. A brand logo
C. Brand destination URLs
D. Docusign JS sessionEnd event handler

**Answer:** C. Brand destination URLs

**Explanation:** Post-signing redirects for remote signers are controlled by brand destination URLs.

**Why this answer and not the others:** C is right because destination URLs are the brand setting for remote signer redirects. The trap is A: it is part of the same brand, but it changes email content rather than browser navigation. B and D fail because a logo is visual only and sessionEnd belongs to embedded signing.

**Option notes:**
- A (TRAP). Email resource files customize notification email content; they do not redirect signers after signing.
- B. A logo only changes appearance.
- C. Correct. A brand's destination URLs redirect remote signers after events such as signing complete or decline.
- D. This handler runs in your own page during embedded signing and does not apply to remote signers.

**Q237. (Workflow Builder and Workflow API - Workflow steps) [LOW]** After a participant submits the web form and signs, the workflow should display a thank-you message in the participant's browser before ending. Which step should be added?

A. Send an Email
B. Show a Confirmation Screen
C. Set Up Invite
D. Branching Rule

**Answer:** B. Show a Confirmation Screen

**Explanation:** Show a Confirmation Screen is the utility step that displays a message to the participant in the browser.

**Why this answer and not the others:** B is right because the message must appear on screen at the end. The trap is A: Send an Email is the other notification step, but it sends to an inbox rather than showing the message in the browser. C invites a participant to a step, and D routes the process.

**Option notes:**
- A (TRAP). Sends a message to an inbox, not to the participant's screen.
- B. Correct. Displays a message to the participant in the browser.
- C. Invites a participant to act; it does not display a closing message.
- D. Routes the workflow; it displays nothing.

**Q238. (App Center and Extension Apps - Data IO) [MEDIUM]** Which set of actions belongs to the Data IO extension?

A. GetTypeNames, GetTypeDefinitions and Verify
B. Verify.Version1.Email and Verify.Version1.PhoneNumber
C. TabInfo:GetConnectedFieldsTabGroups and Envelopes:create
D. GetTypeNames, GetTypeDefinitions, CreateRecord, PatchRecord, SearchRecords

**Answer:** D. GetTypeNames, GetTypeDefinitions, CreateRecord, PatchRecord, SearchRecords

**Explanation:** Data IO actions describe the data model (GetTypeNames, GetTypeDefinitions) and read/write records (CreateRecord, PatchRecord, SearchRecords). There is no UpdateRecord action.

**Why this answer and not the others:** D is right because it lists the Data IO record actions. The trap is A: GetTypeNames and GetTypeDefinitions plus Verify is the connected fields set. B are data verification extensions, and C are eSignature/Connected Fields API endpoints, not extension actions.

**Option notes:**
- A (TRAP). This is the connected fields set (type discovery plus Verify), not Data IO.
- B. These are data verification extension identifiers.
- C. These are API endpoints your integration calls, not actions Docusign calls on your app.
- D. Correct. These are the Data IO actions for type discovery and record read/write.

**Q239. (API Authentication - OAuth flow selection) [HIGH]** An organization has 4,000 agents who use a client-server portal to send Docusign quotes. Each agent signs in and must track their own envelopes. What is the recommended OAuth model?

A. Implicit Grant
B. JSON Web Token (JWT) Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Each agent signs in individually and the server can store a secret, so Confidential Authorization Code Grant keeps a per-agent identity for tracking their own envelopes.

**Why this answer and not the others:** D is right because the agents are present and need their own identity on a server that can hold a secret. The trap is B: the large user count makes a single service integration tempting, but JWT through one system user would merge all agents into one sender, so they could not track their own envelopes. A is legacy, and C is for clients that cannot keep a secret.

**Option notes:**
- A. Implicit Grant is a legacy browser flow and is not used for a secure client-server portal.
- B (TRAP). JWT through one system user removes individual identity, so agents could not see their own envelopes as distinct senders.
- C. Public Auth Code Grant is for clients that cannot store a secret; a client-server portal can.
- D. Correct. Interactive agents on a server that can keep a secret is Confidential Authorization Code Grant.

**Q240. (Go Live Process - Troubleshooting) [MEDIUM]** A support agent who has no access to the account's API integrations needs to capture the API requests a user's session makes. Which tool should the agent use?

A. API Dashboard under Admin > Apps and Keys
B. API request logging under My Preferences
C. API Usage Center efficiency scores
D. The Connect failure log

**Answer:** B. API request logging under My Preferences

**Explanation:** API request logging (My Preferences) is available to all users, is off by default, and keeps up to 50 logs that can be downloaded or cleared.

**Why this answer and not the others:** B is right because request logging is available to every user, which suits a support agent without integration access. The trap is A: the API Dashboard shows request logs and failures, but it is available only to users with access to the API integrations. C shows app efficiency rather than individual requests, and D covers webhook deliveries, not API requests.

**Option notes:**
- A (TRAP). The API Dashboard is only for users with access to the API integrations.
- B. Correct. Request logging is available to all users; enable it in My Preferences (up to 50 logs).
- C. The API Usage Center shows efficiency scores and call volume, not individual request logs.
- D. The Connect failure log lists failed webhook deliveries, not API requests.

**Q241. (Docusign Connect - Security) [HIGH]** A listener has HMAC security enabled. How should it validate that a Connect message is authentic?

A. Decrypt the payload with the account's RSA private key
B. Compare X-DocuSign-Signature-1 directly to the stored secret key
C. Recompute the HMAC over the parsed and re-serialized JSON
D. Compute HMAC-SHA256 of the raw body with the secret, Base64-encode, compare to X-DocuSign-Signature-1

**Answer:** D. Compute HMAC-SHA256 of the raw body with the secret, Base64-encode, compare to X-DocuSign-Signature-1

**Explanation:** Docusign hashes the entire request body with the HMAC key using HMAC-SHA256; the listener recomputes the Base64 hash over the raw bytes and compares it to the signature header.

**Why this answer and not the others:** D is right because the hash must be computed over the exact raw body bytes and compared to the header. The trap is C: it uses the right algorithm, but re-serializing JSON changes whitespace or ordering, so the hash will not match. A confuses HMAC with RSA encryption, and B compares the header to the key instead of to a hash of the body.

**Option notes:**
- A. HMAC payloads are not encrypted with an RSA key; the body is plain JSON with a hash header.
- B. The header holds a hash of the body, not the secret key itself.
- C (TRAP). Re-serialized JSON may differ from the raw bytes Docusign hashed, so validation fails.
- D. Correct. HMAC-SHA256 over the raw body, Base64-encoded, compared to X-DocuSign-Signature-1.

**Q242. (eSignature API - Cancel envelope) [MEDIUM]** A sent envelope has a fatal error. The developer must stop it for good, not just pause it while someone edits it. Which action fits?

A. Set status completed to close the envelope
B. Update the envelope to status voided with a voidedReason
C. Lock the envelope with an envelope lock
D. Change the envelope back to status created

**Answer:** B. Update the envelope to status voided with a voidedReason

**Explanation:** Voiding is permanent cancellation, which is what 'stop it for good' requires.

**Why this answer and not the others:** B is right because voiding with a voidedReason permanently cancels the in-process envelope. The trap is C: locking is a real envelope operation, but it is temporary and meant for editing, not cancelling. A is a status only Docusign sets and D does not cancel the envelope for its recipients.

**Option notes:**
- A. completed is set by Docusign after all recipients finish; an integration cannot close an envelope this way.
- B. Correct. Voiding is the permanent cancel action for an in-process envelope.
- C (TRAP). An envelope lock is temporary, used while an envelope is being edited; it does not cancel it.
- D. Returning to created is not the documented way to cancel; recipients would not be notified of a cancellation.

**Q243. (eSignature Features and Web Forms - Connected Fields) [MEDIUM]** During a demo test, a team notices that a signer-entered account number is not checked against their core system during signing. Which feature closes this gap?

A. The Connect extension-executed event
B. Connected Fields (data verification extension)
C. A Data IO extension
D. A public App Center listing

**Answer:** B. Connected Fields (data verification extension)

**Explanation:** The gap is real-time checking of a signer-entered value, which is the Connected Fields capability.

**Why this answer and not the others:** B is right because Connected Fields perform the check against the external system during signing. The trap is A: it is part of the same verification story, but it only reports results. C and D fail because Data IO targets Maestro and a public listing is a distribution choice.

**Option notes:**
- A (TRAP). This event delivers verification results (JSON SIM only) after a verification runs; on its own it does not check anything.
- B. Correct. Connected Fields verify the signer's entries against an external system while they sign.
- C. Data IO reads and writes system-of-record data from Maestro workflows, not during eSignature signing.
- D. Publishing publicly only changes who can install an extension app; it is not the verification feature.

**Q244. (Workflow Builder and Workflow API - Identity step) [MEDIUM]** After a Verify Someone's Identity step, only verified participants may go on to sign their contract. If verification fails, the HR representative must be notified. Which design fits?

A. A Branching Rule on the verification result: true goes to the signing steps, false to a Send an Email step
B. Rely on the identity step alone, assuming it notifies HR automatically on failure
C. A Multi Branch Rule on Job Location after the identity step
D. An app that calls cancelWorkflowInstance whenever verification fails

**Answer:** A. A Branching Rule on the verification result: true goes to the signing steps, false to a Send an Email step

**Explanation:** The course example uses a Branching Rule on Validated = True after the identity step: verified participants proceed to the contract, and failures go to a Send an Email step for the HR representative.

**Why this answer and not the others:** A is right because the routing on the result and the notification must be modelled explicitly. The trap is B: the identity step performs verification, but notifying HR is a separate action the designer must add. C branches on the wrong field, and D moves logic into custom code and never notifies HR.

**Option notes:**
- A. Correct. Branch on the verification result; the false path emails HR.
- B (TRAP). HR notification must be added as its own step; it is not implied by the identity step.
- C. Job Location does not tell you whether identity was verified.
- D. Canceling from custom code is unnecessary and still does not notify HR.

**Q245. (App Center and Extension Apps - File IO) [HIGH]** Where is a File IO extension (file output cloud storage) invoked?

A. In the eSignature Add Fields view and during signing
B. In Web Forms
C. In Maestro workflows
D. From the App Center listing page

**Answer:** C. In Maestro workflows

**Explanation:** File output cloud storage runs in Maestro workflows, for example to write a file generated during a workflow to cloud storage.

**Why this answer and not the others:** C is right because File IO's extension point is Maestro workflows. The trap is A: Add Fields and signing are the extension points for connected fields and data verification. B applies only to email and phone verification, and D is where apps are installed, not invoked.

**Option notes:**
- A (TRAP). Add Fields and signing are for connected fields and data verification.
- B. Web Forms supports only email and phone verification extensions.
- C. Correct. File IO is invoked from Maestro workflows.
- D. The App Center is where admins install apps, not where extensions run.

**Q246. (API Authentication - Scopes) [LOW]** A support ticket says users are alarmed by a long list of permissions on the consent screen, and some decline. The app only sends envelopes and reads user account information. Which response best matches Docusign behavior?

A. Switch to JWT Grant so users never see a consent screen
B. Ask Docusign to hide the consent screen for the integration key
C. Add the extended scope so consent is shown only once
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** The consent screen lists the requested scopes, so trimming them to what the app needs fixes the root cause.

**Why this answer and not the others:** D is right because the long list comes from over-requesting scopes. The trap is A: JWT runs without per-call prompts, but it still requires consent and is meant for services, not interactive users. B is not something Docusign offers, and C changes the refresh-token lifecycle, not what consent asks for.

**Option notes:**
- A (TRAP). JWT still needs consent and is designed for services without users, so it does not fit or fix the issue.
- B. Docusign does not hide the consent screen; consent is how users approve requested scopes.
- C. extended makes the refresh token roll forward 30 days from the last refresh; it does not shorten the consent list.
- D. Correct. Requesting fewer scopes shortens the consent screen and follows least privilege.

**Q247. (Go Live Process - Go-live setup) [MEDIUM]** An app relies on Basic Data Verification in the developer account. What must the team confirm before going live?

A. That the production plan includes every feature the app used, such as Basic Data Verification
B. Nothing, because developer account features carry over to the production key
C. That the Go-Live review will enable any missing features at no cost
D. That the key uses the Embedded integration type, which unlocks all features

**Answer:** A. That the production plan includes every feature the app used, such as Basic Data Verification

**Explanation:** Developer accounts can include features that production plans lack; the production plan must include every feature the app relied on, for example Basic Data Verification, which is only in certain plans.

**Why this answer and not the others:** A is right because the app will not work as expected if the production plan lacks a feature it used. The trap is B: everything works in the developer account, but features belong to the account plan, not the integration key. C is wrong because Go-Live submission is free but production plans may cost money, and D misuses the integration type, which reflects the business model.

**Option notes:**
- A. Correct. Verify the production plan includes every feature the app used, such as Basic Data Verification.
- B (TRAP). Features belong to the account plan, not to the key, so they do not carry over.
- C. Go-Live review does not add features; production plan features may need to be purchased.
- D. Integration type reflects the business model and does not unlock plan features.

**Q248. (Docusign Connect - Retries) [MEDIUM]** After fixing a listener bug, the team sees several events marked as failed in the Connect logs. What should they do so the downstream system gets those events?

A. Delete and recreate the Connect configuration
B. Resend the affected envelopes to the signers
C. Republish the failed events from the Connect failure list
D. Do nothing; failed events are retried forever

**Answer:** C. Republish the failed events from the Connect failure list

**Explanation:** Connect logs and the failure list are the troubleshooting tools; once the listener is fixed, failed events can be republished.

**Why this answer and not the others:** C is right because republishing delivers the recorded events again without touching the envelopes. The trap is D: Connect does retry automatically, but retries follow a back-off schedule that ends after a set period, so they are not indefinite. Recreating the configuration (A) does not resend past events, and B would make signers repeat work.

**Option notes:**
- A. Recreating the configuration does not resend past events.
- B. Resending envelopes bothers signers and creates new activity instead of delivering the missed events.
- C. Correct. Republish failed events from the Connect logs and failure list after fixing the listener.
- D (TRAP). Retries use exponential back-off over a limited period, not forever.

**Q249. (eSignature API - Idempotency) [LOW]** A stakeholder challenges the design for handling a create-envelope request that may be submitted twice after a network failure. Which envelope field should the team keep in the request?

A. transactionId
B. clientUserId
C. batchId
D. envelopeId

**Answer:** A. transactionId

**Explanation:** A sender-generated transactionId on the envelope lets the app determine whether the first attempt already created the envelope, avoiding duplicates.

**Why this answer and not the others:** A is right because transactionId is the client-supplied identifier for the create transaction. The trap is D: envelopeId is generated by Docusign after creation, so the client cannot send it on the first attempt. B marks an embedded recipient and C tracks a bulk send batch.

**Option notes:**
- A. Correct. transactionId identifies the create transaction so a resubmission does not create a duplicate.
- B. clientUserId marks a recipient as embedded; it has no role in duplicate detection.
- C. batchId is returned by a bulk send request; it does not apply to single envelope creation.
- D (TRAP). envelopeId is created by Docusign on success, so it cannot be supplied in the original request.

**Q250. (eSignature Features and Web Forms - ID Evidence) [LOW]** In a pull request, code assumes the integration can fetch retained data about a completed ID Verification event. Which API should that code call?

A. ID Evidence API
B. The certificate of completion download
C. IdentityVerifications:list
D. The Agreement Manager API

**Answer:** A. ID Evidence API

**Explanation:** Retained ID verification data is fetched with the ID Evidence API.

**Why this answer and not the others:** A is right because ID evidence is retrieved through the ID Evidence API. The trap is B: it is an audit document that mentions authentication, but it does not hold the retained ID data. C and D fail because IdentityVerifications:list returns configurations and Agreement Manager handles agreement data.

**Option notes:**
- A. Correct. The ID Evidence API is the API for retrieving evidence from Docusign ID Verification events.
- B (TRAP). The certificate lists envelope events and authentication used, not the retained ID images and document details.
- C. This lists IDV workflow configurations for use when sending, not evidence from completed verifications.
- D. This returns agreements and AI-extracted agreement data, not identity evidence.

**Q251. (Workflow Builder and Workflow API - Extension step) [MEDIUM]** After signing completes, the workflow must update the related opportunity in the company's CRM to Closed Won. The CRM extension app is installed. Which step fits?

A. A Read step from the CRM extension app
B. A Store Files step to the CRM
C. A Send an Email step to sales operations
D. A Writeback step with the CRM extension app, after Send Documents for Signature

**Answer:** D. A Writeback step with the CRM extension app, after Send Documents for Signature

**Explanation:** Writeback steps automate updating information in external systems such as Salesforce, HubSpot or Dynamics 365. Placing it after signing ensures the update reflects the completed agreement.

**Why this answer and not the others:** D is right because the requirement is to update a record in the CRM after signing. The trap is A: it uses the same CRM app, but a Read step imports data into the workflow rather than updating the CRM. B saves documents, not field values, and C depends on a person doing the update manually.

**Option notes:**
- A (TRAP). Read steps pull data into the workflow; they do not update the CRM.
- B. Store Files saves documents; it does not change the opportunity status.
- C. An email relies on a manual update.
- D. Correct. A Writeback step after signing updates the CRM record.

**Q252. (App Center and Extension Apps - Data Verification) [MEDIUM]** A real estate firm must verify that a postal address entered by a client is valid and deliverable, and have the signer correct it before signing proceeds. Which extension type addresses this real-time validation?

A. File IO
B. Data IO
C. Connected Fields
D. Data Verification

**Answer:** D. Data Verification

**Explanation:** Postal address verification is a Data Verification extension that checks existence and deliverability in real time at signing.

**Why this answer and not the others:** D is right because address deliverability is a standard data verification type. The trap is C: connected fields also verify in real time at signing, but they are for custom data against your own system of record. A stores files and B reads/writes records in Maestro.

**Option notes:**
- A. File IO stores documents.
- B. Data IO reads and writes records in Maestro workflows.
- C (TRAP). Connected fields are for custom values against your own system, not standard address checks.
- D. Correct. Postal address verification is a Data Verification extension.

**Q253. (API Authentication - User info) [HIGH]** After exchanging an authorization code for an access token, a user who belongs to more than one Docusign account signs in. The app must discover the correct accountId and API base URI before making REST calls. Which endpoint provides that context?

A. /oauth/token
B. /oauth/userinfo
C. eSignature Accounts:get
D. The coid claim of the ID token

**Answer:** B. /oauth/userinfo

**Explanation:** /oauth/userinfo returns every account available to the user with its account_id, base_uri, and is_default flag.

**Why this answer and not the others:** B is right because userinfo lists all of the user's accounts and their base URIs. The trap is C: Accounts:get is an account endpoint, but it requires the account ID and base URI you are trying to discover. A returns tokens only, and D lists organizations that granted admin consent.

**Option notes:**
- A. /oauth/token issues tokens; its response has no account list or base URIs.
- B. Correct. /oauth/userinfo returns account_id and base_uri for each account the user can access.
- C (TRAP). Accounts:get needs an account ID and base URI in its URL, so it cannot discover them.
- D. coid lists organizations that granted admin consent, not the user's accounts or base URIs.

**Q254. (Go Live Process - Integration classification) [HIGH]** A vendor embeds Docusign features into its own product. Its customers do not have Docusign accounts; they use the features through the vendor's own Docusign account. Which integration type applies?

A. Public integration
B. Embedded integration
C. Private custom integration
D. Third-party integration key

**Answer:** B. Embedded integration

**Explanation:** When customers use Docusign features through the vendor's account and do not need their own Docusign accounts, the classification is Embedded integration (it requires an ISV Embed partner license).

**Why this answer and not the others:** B is right because the clue is that customers have no Docusign accounts of their own. The trap is A: it also serves many customers, but a Public integration connects to each customer's own Docusign account. C is for apps used directly by your employees or your customers' employees, and D is for a customer supplying its own key to a partner product.

**Option notes:**
- A (TRAP). Public integration connects to customers' own Docusign accounts; here customers have none.
- B. Correct. Customers using Docusign through the vendor's account is an Embedded integration.
- C. Private custom integration covers direct use by employees, not a resold Docusign-powered service.
- D. Third-party integration key is chosen by a customer using a partner product, not by the vendor.

**Q255. (Docusign Connect - Troubleshooting) [LOW]** The team reviews Docusign guidance after a listener receives duplicate webhook messages. What design practice should the integration use?

A. Enable Connect logging so duplicate deliveries are suppressed
B. Idempotent processing based on event identifiers or envelope state
C. Republish the failed events from the Connect failure list
D. Change the listener URL from HTTPS to HTTP

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Duplicate deliveries are normal with retries, so the listener must process events idempotently.

**Why this answer and not the others:** B is right because idempotent processing is the design fix for duplicates. The trap is A: Connect logs are the right tool for troubleshooting, but logging records deliveries; it does not suppress duplicates. C is for events that failed, and republishing them can add duplicates, and D weakens security without affecting delivery.

**Option notes:**
- A (TRAP). Logs help diagnose delivery issues but do not stop duplicates.
- B. Correct. Idempotent processing makes repeated deliveries harmless.
- C. Republishing resends failed events; it does not address duplicates and can create more.
- D. HTTP weakens security and does not change duplicate delivery.

**Q256. (eSignature API - Composite templates) [HIGH]** Two envelope designs are compared: one uses a single saved template unchanged, the other must combine a saved template with runtime recipients and a directly supplied document. Which model does the second design require?

A. templateId reference with templateRoles
B. Composite templates using serverTemplates and inlineTemplates
C. Direct documents with fixed-position tabs
D. One envelope per document sent in sequence

**Answer:** B. Composite templates using serverTemplates and inlineTemplates

**Explanation:** Composite templates are used when an envelope must combine saved server templates, inline runtime data and documents.

**Why this answer and not the others:** B is right because composite templates combine serverTemplates, inlineTemplates and a document. The trap is A: templateId fits the first design, but it cannot add a separate document or combine templates. C drops the saved template and D splits the agreement into several envelopes.

**Option notes:**
- A (TRAP). templateId with templateRoles suits the first design only; it cannot combine a template with another document.
- B. Correct. Composite templates combine a server template, inline runtime recipients and a supplied document.
- C. Direct documents do not apply the saved template, and fixed positions are unrelated to the requirement.
- D. Sending several envelopes splits the agreement instead of building one combined envelope.

**Q257. (eSignature Features and Web Forms - Web Forms embedding) [HIGH]** Sofia's team must embed a Docusign web form inline in a partner's site. Which createInstance setup and client-side step is correct?

A. Omit clientUserId and render the instance URL with Docusign JS
B. Use sendOption 'now' with recipients[] by roleName
C. Add an identityVerification workflowId to the instance
D. Set clientUserId on createInstance, then render the instance URL with Docusign JS

**Answer:** D. Set clientUserId on createInstance, then render the instance URL with Docusign JS

**Explanation:** An embedded web form needs clientUserId on createInstance and Docusign JS to render the instance URL.

**Why this answer and not the others:** D is right because embedded instances require clientUserId and are rendered with Docusign JS. The trap is A: it has the right renderer but drops the required clientUserId, which is exactly what makes the instance embedded. B and C fail because sendOption with recipients is the remote email mode and identity verification is unrelated to rendering.

**Option notes:**
- A (TRAP). Docusign JS is right, but clientUserId is required to create an embedded instance; without it the instance is not set up for embedding.
- B. This creates a remote instance that emails participants; it is not displayed inline on the site.
- C. ID verification settings control identity checks; they do not make a form render inline.
- D. Correct. clientUserId is required for an embedded instance (max 100 characters), and Docusign JS renders the returned URL.

**Q258. (Workflow Builder and Workflow API - Branching) [MEDIUM]** A designer placed a Branching Rule on the loanAmount variable before the Collect Data with Web Forms step that captures loanAmount. Applicants are not routed as intended. What is the fix?

A. Replace the Branching Rule with a Multi Branch Rule step
B. Change the start method to From an API call
C. Move the branching step after the Collect Data with Web Forms step
D. Republish the workflow without changes

**Answer:** C. Move the branching step after the Collect Data with Web Forms step

**Explanation:** A branch can only evaluate a variable after the step that produces it has run. Step order must match the data flow: collect the value, then branch on it.

**Why this answer and not the others:** C is right because loanAmount does not exist yet when the branch runs. The trap is A: a Multi Branch Rule adds more paths, but it has the same problem because it still runs before the data exists. B changes how the workflow starts, not the order of steps, and D does not change the design.

**Option notes:**
- A (TRAP). More branches do not help when the variable has not been collected yet.
- B. The start method does not reorder steps inside the workflow.
- C. Correct. Branch after the form so loanAmount has a value.
- D. Republishing the same design keeps the same faulty order.

**Q259. (App Center and Extension Apps - Connected Fields) [MEDIUM]** A team wants to use connected fields inside a Maestro workflow. What is true?

A. They run automatically in Maestro as a Data IO step
B. Connected fields are not currently supported in Maestro
C. Only private connected fields apps work in Maestro
D. They must be added through a Store Files step

**Answer:** B. Connected fields are not currently supported in Maestro

**Explanation:** Connected fields are not currently supported in Docusign Maestro; they work in eSignature envelopes (Add Fields view and signing).

**Why this answer and not the others:** B is right because Maestro does not currently support connected fields. The trap is A: Data IO is the Maestro extension for system-of-record data, but connected fields do not become Data IO steps. C invents a distribution exception, and D is a file storage step.

**Option notes:**
- A (TRAP). Connected fields do not turn into Data IO steps; Data IO is a separate extension.
- B. Correct. Connected fields are not currently supported in Maestro.
- C. Distribution type does not change Maestro support.
- D. Store Files steps save documents; they have nothing to do with connected fields.

**Q260. (API Authentication - PKCE) [HIGH]** A native app uses Public Authorization Code Grant and has no client secret. Which mechanism lets Docusign verify that the app redeeming the authorization code is the same app that started the flow?

A. The client secret in an Authorization: Basic header
B. A PKCE code verifier and code challenge
C. An exactly matching registered redirect URI
D. The 120-second authorization code lifetime

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE sends a code_challenge (S256 hash of a random code_verifier) on /oauth/auth and the code_verifier on /oauth/token, which verifies that the app that started the flow is the one finishing it.

**Why this answer and not the others:** B is right because the code_verifier and code_challenge pair proves the token request comes from the app that began the flow. The trap is C: the redirect URI must match exactly, but it only controls where the code is sent and does not prove who redeems it. A needs a secret the app does not have, and D only limits how long a stolen code stays usable.

**Option notes:**
- A. A native public client has no secret, so it cannot send a Basic header with one.
- B. Correct. The code_challenge on /oauth/auth and the matching code_verifier on /oauth/token prove the same app finished the flow.
- C (TRAP). An exactly matching redirect URI is required, but it controls where the code goes and does not prove who redeems it.
- D. The 120-second lifetime narrows the window for misuse but does not bind the code to the app that requested it.

**Q261. (Go Live Process - Production endpoints) [MEDIUM]** Which pair of hosts should an eSignature app use in production?

A. Auth: account-d.docusign.com; API: demo.docusign.net/restapi
B. Auth: account.docusign.com; API: demo.docusign.net/restapi
C. Auth: account.docusign.com; API: the account's base URI plus /restapi
D. Auth: account-d.docusign.com; API: the account's base URI plus /restapi

**Answer:** C. Auth: account.docusign.com; API: the account's base URI plus /restapi

**Explanation:** In production, OAuth uses https://account.docusign.com and API calls use the account's base URI (https://{server}.docusign.net/restapi).

**Why this answer and not the others:** C is right because both hosts are the production values. The trap is B: the authentication host is correctly switched, but API calls still go to the demo host. A is the full developer pair, and D switches the API host but keeps the developer authentication host.

**Option notes:**
- A. This is the developer environment pair.
- B (TRAP). The authentication host is right, but the API host is still the demo host.
- C. Correct. Production uses account.docusign.com for OAuth and the account's base URI for API calls.
- D. account-d.docusign.com is the developer authentication host.

**Q262. (Docusign Connect - Payload selection) [LOW]** A team wants event messages that carry only the triggering event's data, adding the envelope summary only for the event types where it is useful. Which Connect design choice is relevant?

A. Configure the JSON SIM event payload to include only needed data
B. Use legacy XML so every message has a consistent envelope summary
C. Poll Envelopes:get after each event instead
D. Enable aggregate mode for smaller messages

**Answer:** A. Configure the JSON SIM event payload to include only needed data

**Explanation:** JSON SIM messages contain data about the triggering event by default, and you can choose to include the envelope summary depending on the event type.

**Why this answer and not the others:** A is right because JSON SIM makes the payload event-focused and customizable. The trap is B: legacy XML does give a consistent payload, but it is envelope-focused, so every message carries the summary the team wants to avoid. C adds API calls, and D reduces message count rather than message content.

**Option notes:**
- A. Correct. JSON SIM is event-focused and lets you add the envelope summary only where needed.
- B (TRAP). Legacy XML is envelope-focused, so every message includes the envelope summary.
- C. Polling after each event adds API calls and defeats the purpose of Connect.
- D. Aggregate mode combines events into fewer messages; it does not trim message content.

**Q263. (eSignature API - Composite templates) [HIGH]** In a composite template object, the app must supply the PDF at runtime even though the server template also has a document. Which location takes precedence for that object's document?

A. The inlineTemplate's documents property
B. The server template, because it has the lowest sequence
C. The composite template object's document property
D. The template with the highest sequence value

**Answer:** C. The composite template object's document property

**Explanation:** If the composite template object includes a document element, that document is used and all template documents are ignored. It is also the recommended place to supply a runtime document.

**Why this answer and not the others:** C is right because the composite object's document property always wins for document contribution. The trap is A: an inline template can contribute documents, but the best practice is the document property, and the inline document does not override it. B applies only when there is no document property, and D reverses the rule: for documents the lowest sequence wins, not the highest.

**Option notes:**
- A (TRAP). An inline template can carry documents, but Docusign recommends the document property, which takes precedence.
- B. The lowest-sequence template supplies the document only when no document property is present.
- C. Correct. The composite object's document property takes precedence over server and inline template documents.
- D. For documents the lowest sequence wins (first in wins); highest sequence wins only for attributes.

**Q264. (eSignature Features and Web Forms - Web Form correlation) [HIGH]** Robin's app embeds a web form for each sales customer and stores the customer's internal ID with each instance. Which statement about the value used for this is correct?

A. The signer's email address is the unique key Docusign uses for each instance
B. The API account ID distinguishes each customer's instance
C. clientUserId identifies the user in your system and is limited to 100 characters
D. The web form configuration formId is unique per customer

**Answer:** C. clientUserId identifies the user in your system and is limited to 100 characters

**Explanation:** The stem's clue is an internal ID stored per embedded instance, which is clientUserId (max 100 characters).

**Why this answer and not the others:** C is right because clientUserId carries your internal user ID and is capped at 100 characters. The trap is A: email identifies recipients in many eSignature flows, but it is not the embedded web form correlation key. B and D fail because the account ID and the configuration ID are shared across all customers.

**Option notes:**
- A (TRAP). Email is not the key that identifies an embedded web form user; clientUserId is.
- B. The account ID is the same for all instances in the account.
- C. Correct. clientUserId is required for embedded instances, is chosen by your app, and has a 100-character maximum.
- D. formId identifies the configuration, which all customers' instances share.

**Q265. (Workflow Builder and Workflow API - Start method) [LOW]** A workflow was set to start From a link, and the link was placed on a website. Later the designer changes the start method to From an API call. What happens to the existing link?

A. The link stops working immediately
B. The link can still start the workflow, because the start method does not block other ways of starting it
C. The link now requires an OAuth access token
D. The link starts only instances that the API already created

**Answer:** B. The link can still start the workflow, because the start method does not block other ways of starting it

**Explanation:** Docusign documents that the selected start method does not prevent starting the workflow in other ways; an existing link still works after the start method is changed to API.

**Why this answer and not the others:** B is right because the start method mainly sets up shortcuts and prompts; it is not an access restriction. The trap is A: it seems logical that changing the method disables the link, but the documentation says the existing link can still be used. C and D describe behavior that does not exist.

**Option notes:**
- A (TRAP). Changing the start method does not disable an existing link.
- B. Correct. The link still triggers the workflow after the start method changes.
- C. The link endpoint is unauthenticated; it does not start requiring a token.
- D. Opening the link creates a new instance; it does not depend on API-created instances.

**Q266. (App Center and Extension Apps - Data Verification) [MEDIUM]** A signer enters their company's federal Employer Identification Number (FEIN), which must be checked against government records at signing. Which extension fits?

A. Business FEIN verification (Verify.Version1.BusinessEntity)
B. Connected Fields with a custom FEIN type
C. Bank account owner verification
D. SSN verification

**Answer:** A. Business FEIN verification (Verify.Version1.BusinessEntity)

**Explanation:** Business FEIN verification is the Data Verification extension for confirming a business identifier, used at the Add Fields view and signing.

**Why this answer and not the others:** A is right because a standard business entity check is exactly what FEIN verification does. The trap is B: connected fields could verify custom data against your own database, but a standard FEIN check against government records is a predefined Data Verification type. C and D verify different data.

**Option notes:**
- A. Correct. Business FEIN verification checks business identifiers at signing.
- B (TRAP). Connected fields are for custom data against your own system, not a standard FEIN check.
- C. Bank account owner verification checks ownership of a US bank account.
- D. SSN verification validates an individual's social security number, not a business FEIN.

**Q267. (API Authentication - Bearer tokens) [LOW]** Guidance for maintainers of a JWT integration: REST calls return 401 Unauthorized even though the token endpoint returned an access token. What should the guidance recommend?

A. Send the access token in the Authorization header as a Bearer token
B. Send the signed JWT assertion itself as the Bearer value
C. Send the token in a JSON field named token in the request body
D. Add the impersonation scope to every API request

**Answer:** A. Send the access token in the Authorization header as a Bearer token

**Explanation:** The signed JWT assertion is only exchanged at /oauth/token; the access token it returns goes in Authorization: Bearer on API calls.

**Why this answer and not the others:** A is right because API calls need the access token in a Bearer header. The trap is B: the signed JWT looks like a token, but it is only the assertion posted to /oauth/token. C is not where Docusign reads credentials, and D confuses scopes, which are requested at consent and token time, with per-request headers.

**Option notes:**
- A. Correct. Use Authorization: Bearer <access_token> on API calls.
- B (TRAP). The JWT assertion is exchanged at /oauth/token; APIs only accept the access token it returns.
- C. Docusign reads credentials from the Authorization header, not the request body.
- D. Scopes are set at consent and in the token request, not on each API call.

**Q268. (Go Live Process - Templates in production) [LOW]** After Go-Live, should the team keep using the developer environment version of the integration key?

A. No; Go-Live moves the key to production, so demo calls stop working
B. Yes; the key is duplicated, so the developer version stays available for testing
C. No; the developer version expires 90 days after Go-Live
D. Yes, but only after generating a new GUID for the developer version

**Answer:** B. Yes; the key is duplicated, so the developer version stays available for testing

**Explanation:** Go-Live duplicates the integration key into production rather than moving it, so the developer version keeps working and is recommended for ongoing regression testing.

**Why this answer and not the others:** B is right because the key is copied, not moved. The trap is A: the word promote suggests the key leaves the developer environment, but Docusign duplicates it. C invents an expiry, and D is wrong because both versions share the same key value.

**Option notes:**
- A (TRAP). Go-Live duplicates the key; the developer version keeps working.
- B. Correct. The developer version remains available and is useful for regression testing.
- C. The developer version does not expire after Go-Live.
- D. Both versions keep the same key value; no new GUID is needed.

**Q269. (Docusign Connect - Envelope-level Connect) [MEDIUM]** A stakeholder suggests setting a special callback URL for one API-sent envelope from the eSignature web app instead of in code. Which option should the team keep?

A. Configure it on the account's Connect page in eSignature Admin
B. Configure it in the Organization Admin Connect settings
C. Set it as the envelope's brand destination URL
D. Add an eventNotification object to the Envelopes:create request

**Answer:** D. Add an eventNotification object to the Envelopes:create request

**Explanation:** eventNotification must be set through the API (Envelopes:create); an envelope-level webhook cannot be created from the Send page or admin UI.

**Why this answer and not the others:** D is right because envelope-level webhooks are API only. The trap is A: the eSignature Admin Connect page is real, but it creates an account-level configuration that applies to many envelopes. B is an org-level setting, and C changes where the signer is redirected after signing, not where events are posted.

**Option notes:**
- A (TRAP). The eSignature Admin Connect page creates account-level configurations, not a webhook for one envelope.
- B. Organization Admin creates organization-level configurations spanning accounts.
- C. A brand destination URL redirects the signer's browser after signing; it does not deliver webhook events.
- D. Correct. Envelope-level Connect is configured only through the API with eventNotification on Envelopes:create.

**Q270. (eSignature API - Idempotency) [MEDIUM]** An API call to create an envelope failed and the app wants to retry. Which parameter lets the retry avoid creating a duplicate envelope?

A. envelopeId
B. recipientId
C. transactionId
D. documentId

**Answer:** C. transactionId

**Explanation:** Supplying the same sender-generated transactionId on the retry identifies it as the same envelope transaction, so a retry does not create a second envelope.

**Why this answer and not the others:** C is right because transactionId is the sender-generated identifier for the create attempt. The trap is A: envelopeId identifies an envelope, but Docusign generates it and a failed call does not return one. B and D identify a recipient and a document inside the envelope.

**Option notes:**
- A (TRAP). envelopeId is assigned by Docusign only when the create succeeds; the client cannot set it on a retry.
- B. recipientId identifies a recipient within the envelope, not the create transaction.
- C. Correct. Reusing the same transactionId lets Docusign and the app treat the retry as the same transaction.
- D. documentId identifies a document within the envelope; it does not prevent duplicate envelopes.

**Q271. (eSignature Features and Web Forms - Identity verification) [HIGH]** Elena troubleshoots an integration: the developer set authenticationMethod on EnvelopeViews:createRecipient expecting Docusign to verify signers' photo IDs, but signers are never challenged. What should be used instead?

A. Also send authenticationInstant and assertionId so the record is complete
B. Add identityVerification with the account's IDV workflowId to the recipient
C. Render signing with Docusign JS focused view
D. Set clientUserId on the recipient

**Answer:** B. Add identityVerification with the account's IDV workflowId to the recipient

**Explanation:** authenticationMethod only records authentication; enforcing a photo ID check requires identityVerification.workflowId.

**Why this answer and not the others:** B is right because IDV is enforced by the identityVerification workflowId, not by authentication record fields. The trap is A: adding the other record fields looks like fixing an incomplete setup, but those fields are also record-only. C and D fail because focused view and clientUserId control the embedded experience, not identity.

**Option notes:**
- A (TRAP). These fields complete the authentication record on the certificate, but they still only record your app's check and never challenge the signer.
- B. Correct. identityVerification.workflowId is what makes Docusign enforce ID verification for the recipient.
- C. Focused view changes how the signing session is displayed; it adds no identity verification.
- D. clientUserId is already required for embedded signing and has no identity-checking effect.

**Q272. (Workflow Builder and Workflow API - API trigger) [MEDIUM]** A backend knows only the display name of a Maestro workflow. Before triggering it, the backend needs the workflow ID. Which call should it make?

A. GetWorkflowsList (GET /v1/accounts/{accountId}/workflows)
B. getWorkflowInstancesList
C. eSignature Templates:list
D. GetWorkflowTriggerRequirements

**Answer:** A. GetWorkflowsList (GET /v1/accounts/{accountId}/workflows)

**Explanation:** GetWorkflowsList returns the available workflows with their IDs, names and trigger input schema, so the app can find the ID by name.

**Why this answer and not the others:** A is right because it is the only call that lists workflows without already knowing an ID. The trap is D: trigger requirements are the next call in the flow, but they need the workflowId in the path. B also needs a workflowId and lists instances, and C lists eSignature templates, not workflows.

**Option notes:**
- A. Correct. Lists the account's workflows with IDs and names.
- B. Needs a workflowId already and returns instances, not workflows.
- C. Templates are eSignature resources, not Maestro workflows.
- D (TRAP). Requires the workflowId in its path, so it cannot be used to find it.

**Q273. (App Center and Extension Apps - Public vs private) [HIGH]** A financial institution builds an extension app that verifies client data against its proprietary internal system. Only administrators of its designated corporate Docusign accounts may install it. Which distribution must be chosen?

A. Public extension app
B. Private extension app
C. Public app with publicationRegions set to the bank's region
D. Keep the app in Draft in the developer account

**Answer:** B. Private extension app

**Explanation:** Private distribution restricts installation to a predefined list of production accounts, matching an app tied to an internal system.

**Why this answer and not the others:** B is right because private apps are installable only by the listed production accounts. The trap is C: publicationRegions narrows a public app by region, but every customer in that region could still install it. A exposes the app to all customers, and D never reaches production.

**Option notes:**
- A. Public apps are available to all App Center customers, which violates the requirement.
- B. Correct. Private distribution limits installation to the bank's designated production accounts.
- C (TRAP). Regions restrict geography, not organizations, so other customers in that region could install it.
- D. A Draft app exists only in the developer account (demo) and cannot be installed in production.

**Q274. (API Authentication - OAuth flow selection) [MEDIUM]** A contracting web app's server can store a client secret. Users sign in once, then the server should keep calling Docusign for them for weeks using refresh tokens. Which flow fits?

A. Public Authorization Code Grant with PKCE
B. JSON Web Token Grant
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Confidential Authorization Code Grant returns a refresh token valid for up to 30 days (rolling with the extended scope), and the server can protect the secret it needs.

**Why this answer and not the others:** D is right because the server can hold a secret and needs long-lived refresh tokens after one interactive sign-in. The trap is A: Public Auth Code also returns a refresh token, but it lasts only 24 hours and the flow is meant for clients that cannot store a secret. B never returns a refresh token, and C is legacy.

**Option notes:**
- A (TRAP). Public Auth Code Grant refresh tokens last only 24 hours, and the flow is for clients without a safe place for a secret.
- B. JWT Grant returns no refresh token; its 1-hour access token is renewed by signing a new assertion, and it has no user sign-in.
- C. Implicit Grant is a legacy browser flow and does not provide the refresh-token lifecycle described.
- D. Correct. Confidential Auth Code Grant gives a refresh token valid up to 30 days to a server that can protect the secret.

**Q275. (Go Live Process - Post go-live) [MEDIUM]** A developer worries that promoting a key will change its value and break existing configuration files. What actually happens to the integration key value?

A. The production key has the same value as the developer key
B. Production assigns a new key value that must replace the old one everywhere
C. The key value is kept, but it stops working in the developer environment
D. The key value changes only for Authorization Code Grant apps

**Answer:** A. The production key has the same value as the developer key

**Explanation:** When you go live, a production version of the integration key with the same value is created in the production environment; it is a separate key with its own settings.

**Why this answer and not the others:** A is right because the production copy keeps the same key value. The trap is C: the value is indeed kept, but the developer version also keeps working, since the key is duplicated rather than moved. B and D are wrong because the value never changes, whatever the OAuth flow.

**Option notes:**
- A. Correct. The production key has the same value but is configured separately.
- B. No new value is issued; only its settings must be re-added in production.
- C (TRAP). The developer version keeps working because the key is duplicated, not moved.
- D. The key value is the same for every OAuth flow.

**Q276. (Docusign Connect - Connect vs polling) [HIGH]** Which statement correctly describes an advantage of Docusign Connect over polling?

A. Polling gives real-time data with fewer API calls
B. Connect requires a confirming status call for each event
C. Connect sends a message only when something changes
D. Connect works only for envelopes sent through the API

**Answer:** C. Connect sends a message only when something changes

**Explanation:** Connect messages arrive only when an event occurs, which removes the polling logic and the wasted calls on unchanged envelopes.

**Why this answer and not the others:** C is right because event-driven delivery is the core advantage. The trap is D: it mixes Connect in general with envelope-level Connect, which is API only; account- and org-level configurations also cover envelopes sent from the web app. A reverses the comparison, and B invents a confirmation call that Connect does not require.

**Option notes:**
- A. Polling is slower and uses more calls, the opposite of this statement.
- B. Connect messages carry the event data; no confirming call is required.
- C. Correct. Connect pushes a message only when a subscribed event occurs.
- D (TRAP). Only envelope-level Connect is API only; account- and org-level configurations cover envelopes however they were sent.

**Q277. (eSignature API - Anchor tabs) [MEDIUM]** Contracts are generated with different clause lengths, so the signature line lands on different pages. The signature tab must always sit beside the text 'Customer Signature'. Which option is correct?

A. Fixed-position tabs with pageNumber set to the last page
B. Anchor tagging with anchorString and offsets
C. A composite template with a second inline template
D. templateRoles mapping the signer to a role

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tagging searches the document for the text and places the tab beside it on whatever page it appears.

**Why this answer and not the others:** B is right because the anchor finds the text wherever it lands. The trap is A: putting the tab on the last page sounds reasonable, but the signature line is not always there and fixed coordinates do not follow the text. C and D change envelope structure or recipient mapping, not tab position.

**Option notes:**
- A (TRAP). Fixed positions with a page number break when the signature line moves to another page or spot.
- B. Correct. Anchor tagging places the tab relative to 'Customer Signature' wherever it appears.
- C. An extra inline template adds recipients or tabs but does not by itself make a tab follow text.
- D. templateRoles assign a recipient to a role; they do not position tabs.

**Q278. (eSignature Features and Web Forms - Recipient authentication) [HIGH]** A signer must receive a one-time code by phone before accessing the envelope. Which method should the developer configure on the recipient?

A. Phone authentication (SMS or voice code)
B. Access code
C. Knowledge-based authentication (KBA)
D. authenticationMethod on createRecipient

**Answer:** A. Phone authentication (SMS or voice code)

**Explanation:** A one-time code delivered by phone is phone authentication.

**Why this answer and not the others:** A is right because phone authentication delivers a code by SMS or voice call. The trap is B: it also requires the signer to type a code, but the sender sets and shares it. C and D fail because KBA asks questions and authenticationMethod is record-only.

**Option notes:**
- A. Correct. Phone authentication is configured with an identityVerification workflowId (from IdentityVerifications:list) and sends the code by SMS or call.
- B (TRAP). An access code is a fixed code set by the sender and shared out of band, not a one-time code delivered by Docusign.
- C. KBA uses public-record questions (US only), not a code.
- D. This only records authentication your app performed; it sends nothing to the signer.

**Q279. (Workflow Builder and Workflow API - Runtime errors) [MEDIUM]** A designer corrected a step in a published workflow and published the change. Instances that were already running still behave the old way. What explains this?

A. The browser cached the old workflow definition
B. The change was published to the demo account only
C. The workflow must be paused, and changes published while it is paused
D. Edits apply to new instances only; instances already running are not modified

**Answer:** D. Edits apply to new instances only; instances already running are not modified

**Explanation:** When you edit participants or steps, current active instances are not modified, but new instances reflect the changes.

**Why this answer and not the others:** D is right because running instances keep the version they started with. The trap is C: pausing sounds like a safe way to change a workflow, but changes made to a paused workflow cannot be published, and pausing still does not change running instances. A and B invent causes not supported by the scenario.

**Option notes:**
- A. Caching does not explain the behavior; running instances simply keep their version.
- B. Nothing in the scenario suggests the wrong environment.
- C (TRAP). Changes to a paused workflow cannot be published, and running instances are still not updated.
- D. Correct. Only new instances pick up the edited steps.

**Q280. (App Center and Extension Apps - Extension app role) [MEDIUM]** A developer has registered, tested and published an extension app. Where do customer account administrators discover and install it?

A. In the Developer Console, where the app was registered and tested
B. On the Apps and Keys page of eSignature Admin settings
C. In a Connect configuration under eSignature Settings
D. In the Docusign App Center

**Answer:** D. In the Docusign App Center

**Explanation:** Published extension apps are listed in the Docusign App Center, where admins discover and install them. The Developer Console is the developer-side tool.

**Why this answer and not the others:** D is right because the App Center is the central place where customers find and install extension apps. The trap is A: the Developer Console is where developers register, test and submit the app, not where customers install it. B manages integration keys for API apps, and C configures webhooks.

**Option notes:**
- A (TRAP). The Developer Console is the developer's tool for registering, testing and publishing; customers do not install apps there.
- B. Apps and Keys manages integration keys for API integrations, not extension app installation.
- C. Connect configurations define event webhooks; they do not install extension apps.
- D. Correct. Admins discover and install published extension apps from the Docusign App Center.

**Q281. (API Authentication - OAuth flow selection) [MEDIUM]** A security architect reviews a browser-only SPA that cannot protect a client secret but must authenticate each individual user. The design will be rejected if the flow does not match the client type. Which flow should the developer choose?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** A public client (browser-only, no secret) with interactive users matches Public Authorization Code Grant with PKCE.

**Why this answer and not the others:** C is right because it matches a public client with an interactive user. The trap is D: Implicit Grant also targets browser apps without a secret, but it is the legacy flow and does not match current Docusign guidance. A requires a confidential client, and B is for services without a user.

**Option notes:**
- A. Confidential Auth Code Grant matches a confidential client that can hold a secret, not a browser-only SPA.
- B. JWT Grant matches a service integration with no user present, not a per-user SPA.
- C. Correct. Public client plus interactive user equals Public Authorization Code Grant with PKCE.
- D (TRAP). Implicit Grant fits the client type historically but is legacy; Docusign recommends the PKCE code flow instead.

**Q282. (Docusign Connect - Configuration level) [MEDIUM]** The operations team wants a single Connect configuration, set up once in Docusign Organization Admin, that applies to all of the organization's accounts until disabled. Which Connect level is most appropriate?

A. Account-level Connect created with the ConnectConfigurations API
B. Organization-level Connect
C. eventNotification added to each envelope
D. The pre-built Connect for Salesforce integration

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect is configured in Organization Admin or by API, spans accounts, and stays active until disabled.

**Why this answer and not the others:** B is right because the clues are Organization Admin and all accounts. The trap is A: ConnectConfigurations does create persistent configurations, but at account level, so it would cover one account only. C must be repeated on every envelope, and D pushes data to the Docusign for Salesforce app rather than to a custom listener.

**Option notes:**
- A (TRAP). ConnectConfigurations creates an account-level configuration that covers one account.
- B. Correct. Org-level Connect is set up in Organization Admin and covers all or selected accounts.
- C. eventNotification is per envelope and must be reconfigured on each new envelope.
- D. Connect for Salesforce is a pre-built integration that updates the Docusign for Salesforce app, not a custom org-wide webhook.

**Q283. (eSignature API - Embedded signing) [MEDIUM]** An app calls EnvelopeViews:createRecipient and gets an error that the recipient is not found. email and userName match the signer exactly. Which value most likely does not match the envelope?

A. clientUserId
B. recipientId
C. returnUrl
D. frameAncestors

**Answer:** A. clientUserId

**Explanation:** createRecipient requires email, userName and clientUserId that match the values used when the envelope was created. With email and name matching, the mismatch is clientUserId.

**Why this answer and not the others:** A is right because clientUserId is the remaining recipient-matching value. The trap is B: recipientId identifies the recipient inside the envelope, but the view request matches on email, userName and clientUserId. C and D are request settings for redirect and focused view, not recipient-matching values.

**Option notes:**
- A. Correct. clientUserId must match the value set on the signer when the envelope was created.
- B (TRAP). recipientId is not one of the matching values that the recipient view request depends on.
- C. returnUrl is where Docusign redirects after signing; a wrong value does not cause a recipient-not-found error.
- D. frameAncestors is used for focused view embedding; it does not identify the recipient.

**Q284. (eSignature Features and Web Forms - Brand destination URLs) [LOW]** Amir is comparing options for a sales team whose customers sign remotely from email. After signing, customers must be sent to the team's thank-you page. Which branding feature is relevant?

A. returnUrl in EnvelopeViews:createRecipient
B. Branding signing resource file
C. A Connect webhook
D. Brand destination URLs

**Answer:** D. Brand destination URLs

**Explanation:** Remote signing plus a post-signing redirect points to brand destination URLs.

**Why this answer and not the others:** D is right because destination URLs are how a brand redirects remote signers. The trap is A: it is the redirect parameter for embedded signing and does not apply here. B and C fail because resource files are cosmetic and Connect is server-side.

**Option notes:**
- A (TRAP). returnUrl only applies to embedded signing; these customers sign remotely from email.
- B. Signing resource files change the text and look of the signing pages, not the redirect target.
- C. Connect posts events to a server; it does not control the signer's browser.
- D. Correct. Destination URLs on the brand (applied with brandId) control where remote signers are redirected.

**Q285. (Workflow Builder and Workflow API - Embedding workflow) [LOW]** A team plans to embed workflow instances in its web app. Which step type is NOT supported in embedded workflow instances?

A. Collect Data with Web Forms
B. Send Documents for Signature
C. Collect Data from an ID
D. Branching Rule

**Answer:** C. Collect Data from an ID

**Explanation:** All step types are supported in embedded instances except Collect Data from an ID.

**Why this answer and not the others:** C is right because it is the one documented exception. The trap is B: signing in an embedded instance has a restriction (focused view is not supported), but the step itself is supported. A and D are supported normally.

**Option notes:**
- A. Web form steps are supported in embedded instances.
- B (TRAP). Supported; only the focused view display is unavailable when embedded.
- C. Correct. Collect Data from an ID is not supported in embedded instances.
- D. Branching runs without a UI and is supported.

**Q286. (App Center and Extension Apps - Public vs private) [MEDIUM]** A developer shares a private extension app with a customer's production account. In the Developer Console the account shows status Pending. What does this mean?

A. Docusign's app review is still in progress
B. The account ID entered is invalid and must be corrected
C. The account's administrator has not yet accepted the app in the App Center
D. The app must be republished as public before the account can use it

**Answer:** C. The account's administrator has not yet accepted the app in the App Center

**Explanation:** A shared account stays Pending until its administrator accepts the private app in the App Center; it then changes to Accepted.

**Why this answer and not the others:** C is right because Pending refers to the account administrator's acceptance of the shared app. The trap is A: review status (In Review) applies to the app as a whole and is finished before private sharing. B and D are not what Pending means, and private apps never need to become public to be used.

**Option notes:**
- A (TRAP). Review status is shown on the app itself (In Review); sharing with accounts happens after approval.
- B. Pending does not indicate a bad account ID; it indicates the admin has not accepted yet.
- C. Correct. The account remains Pending until its administrator accepts the app, then becomes Accepted.
- D. Private apps are used by the listed accounts as private apps; no public republishing is needed.

**Q287. (API Authentication - JWT Grant) [MEDIUM]** Guidance for a partner vendor: a scheduled service runs nightly using a dedicated system sender account, no person is present, and it must authenticate in both demo and production. What should the guidance recommend?

A. Confidential Authorization Code Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant with PKCE
D. Implicit Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** An unattended service acting as a system user uses JWT Grant in both environments; only the aud value and auth server change (account-d.docusign.com in demo, account.docusign.com in production).

**Why this answer and not the others:** B is right because no person is present. The trap is A: it is the right choice for server apps that can store a secret, but only when users sign in. C needs an interactive user, and D is legacy; none of those depend on the environment.

**Option notes:**
- A (TRAP). Confidential Auth Code Grant still needs a user to sign in through a browser, which this nightly service cannot do.
- B. Correct. JWT Grant fits an unattended system-user service in both demo and production.
- C. Public Auth Code Grant with PKCE requires an interactive user on a client without a secret.
- D. Implicit Grant is a legacy interactive browser flow.

**Q288. (Docusign Connect - JSON SIM) [HIGH]** Which Connect message format is supported at all three custom configuration levels: organization, account and envelope?

A. JSON SIM format
B. Legacy XML format
C. XML aggregate mode
D. SOAP messages based on the eSignature SOAP API

**Answer:** A. JSON SIM format

**Explanation:** JSON SIM is supported for organization-level, account-level and envelope-level Connect; legacy options are available only at account and envelope level.

**Why this answer and not the others:** A is right because JSON SIM is the only format available at every level. The trap is B: legacy XML is still supported, but only at account and envelope level, never for organization-level configurations. C and D are legacy XML variants with the same restriction.

**Option notes:**
- A. Correct. JSON SIM works at organization, account and envelope level.
- B (TRAP). Legacy XML is limited to account- and envelope-level configurations.
- C. Aggregate mode is an XML-only legacy option, not available at org level.
- D. SOAP-style messages are the legacy XML format, not available at org level.

**Q289. (eSignature API - Signing URL) [MEDIUM]** Which request path does an app call to get the embedded signing URL for a recipient?

A. POST /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/sender
B. POST /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients
C. GET /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}
D. POST /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient

**Answer:** D. POST /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient

**Explanation:** EnvelopeViews:createRecipient is a POST to .../envelopes/{envelopeId}/views/recipient, using the accountId and envelopeId of the envelope just created.

**Why this answer and not the others:** D is right because views/recipient returns the signing URL. The trap is A: views/sender is the neighbouring view endpoint, but it is for embedded sending. B manages the envelope's recipient list and C reads the envelope's details.

**Option notes:**
- A (TRAP). views/sender returns an embedded sending view, not a signing view.
- B. The recipients endpoint lists or modifies recipients; it does not return a signing URL.
- C. GET on the envelope returns envelope information, not a signing session.
- D. Correct. POST .../envelopes/{envelopeId}/views/recipient is EnvelopeViews:createRecipient.

**Q290. (Workflow Builder and Workflow API - Installed extensions) [MEDIUM]** An ISV wants Maestro workflows to read records from and write records to its system of record. Which extension type should it build?

A. A connected fields extension
B. A Data IO extension
C. A Connect webhook listener
D. A bank account verification extension

**Answer:** B. A Data IO extension

**Explanation:** Data IO extensions are used in Maestro workflows to read from and write to a system of record.

**Why this answer and not the others:** B is right because the requirement is read and write access from workflows. The trap is A: connected fields also link Docusign to external data, but they work in eSignature and are not supported in Maestro. C only receives events, and D verifies bank details.

**Option notes:**
- A (TRAP). Connected fields are not supported in Maestro workflows.
- B. Correct. Data IO reads and writes system-of-record data in workflows.
- C. Connect pushes events out; it does not provide workflow read or write steps.
- D. Verifies bank data only; it does not read or write records.

**Q291. (App Center and Extension Apps - Public App Center) [HIGH]** A PUBLIC extension app passes review and shows Approved in the Developer Console. What must the developer do next so administrators can find and install it in production?

A. Run an additional functional test with a production envelope
B. Publish the app to the Docusign App Center
C. Submit a go-live request for an integration key
D. Start calling the production eSignature endpoint

**Answer:** B. Publish the app to the Docusign App Center

**Explanation:** After approval, the developer clicks Publish to App Center; for a public app this makes it available to all customers in the App Center.

**Why this answer and not the others:** B is right because approval is followed by the publish step. The trap is C: go-live requests promote eSignature API integration keys and are not part of extension app publishing. A is not a required post-approval step, and D has nothing to do with listing the app.

**Option notes:**
- A. Testing happens before review; it is not the step that lists an approved app.
- B. Correct. Publishing to the App Center makes the approved public app installable.
- C (TRAP). Go-live applies to integration keys for API integrations, not to extension apps.
- D. Calling production APIs does not make an extension app discoverable.

**Q292. (API Authentication - Consent) [HIGH]** A background JWT integration gets an error during token exchange. Logs show the integration key and RSA key are correct, but the impersonated user has never approved the requested scopes. What must be completed before the request can succeed?

A. Individual or admin consent for the integration key and requested scopes
B. Adding impersonation to the scope claim of the JWT assertion
C. Requesting a refresh token with the extended scope
D. Changing aud to account.docusign.com

**Answer:** A. Individual or admin consent for the integration key and requested scopes

**Explanation:** JWT tokens are only issued after the impersonated user, or an admin, has consented to the integration key and its scopes.

**Why this answer and not the others:** A is right because the logs rule out key problems and point to missing consent. The trap is B: impersonation must be part of the consent, but putting it in the assertion does not grant consent. C does not apply because JWT never returns a refresh token, and D would point a demo integration at the production auth server.

**Option notes:**
- A. Correct. Consent for the integration key and scopes must exist before any JWT token is issued.
- B (TRAP). Listing impersonation in the assertion does not replace consent by the user or an admin.
- C. extended is for Auth Code refresh tokens; JWT Grant never returns a refresh token.
- D. account.docusign.com is the production aud; changing it does not create consent and breaks a demo integration.

**Q293. (eSignature API - Embedded signing timing) [HIGH]** An implementation note must state how long an embedded signing URL from EnvelopeViews:createRecipient can be used. What should it say?

A. 2 minutes, then it must be exchanged for a token
B. 8 hours, like an access token
C. About 5 minutes, and it can be used only once
D. Until the envelope expires

**Answer:** C. About 5 minutes, and it can be used only once

**Explanation:** The recipient view URL expires in about 5 minutes and is single-use, so it should be requested when the user is ready.

**Why this answer and not the others:** C is right because the signing URL is short-lived and single-use. The trap is A: 2 minutes is the lifetime of an OAuth authorization code, which is a different value. B is the access token lifetime and D confuses the URL with the envelope.

**Option notes:**
- A (TRAP). 2 minutes is the authorization code lifetime in Authorization Code Grant, not the signing URL.
- B. 8 hours is the access token lifetime, not the recipient view URL.
- C. Correct. The signing URL expires in about 5 minutes and is single-use.
- D. The envelope can stay open much longer, but each signing URL expires within minutes.

**Q294. (Workflow Builder and Workflow API - Workflow steps) [HIGH]** A custom sales dashboard has a button that starts a Docusign workflow to send account-opening documents to a prospect. The dashboard's backend passes the prospect's name and email as starting values. Which start method should the workflow use?

A. From an API call
B. From an event
C. Manually in Docusign (Run Workflow)
D. From a link

**Answer:** A. From an API call

**Explanation:** A custom app that starts the workflow programmatically and passes starting values uses the From an API call start method.

**Why this answer and not the others:** A is right because the backend triggers the workflow and supplies the starting values. The trap is D: a button could open a link, but links are for participants starting a workflow themselves, and Docusign recommends API start when passing starting values. B does not fit a button click, and C requires a user to work inside Docusign.

**Option notes:**
- A. Correct. The dashboard backend triggers the workflow through the API with the prospect's values.
- B. The workflow is started by a user action in the dashboard, not by an event.
- C. Run Workflow is done inside Docusign, not from a custom dashboard.
- D (TRAP). A link suits participant self-service; passing starting values calls for API start.

**Q295. (App Center and Extension Apps - Public App Center) [HIGH]** A storage vendor wants Docusign customers to find its extension in the App Center, install it, and use it in their own agreement workflows. Which distribution model matches?

A. Private extension app limited to one organization's accounts
B. Public extension app published to the Docusign App Center
C. Keep the app in the developer account so customers use it in demo
D. Private app whose only allowed account is the vendor's own

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is used when customers broadly need to discover and install an extension app.

**Why this answer and not the others:** B is right because public distribution is how many customers find and install an app. The trap is A: private distribution is for one organization's accounts, not a marketplace audience. C never reaches customers' production accounts, and D shares the app only with the vendor.

**Option notes:**
- A (TRAP). Private apps are limited to listed accounts, so customers could not find it in the App Center.
- B. Correct. A public app in the App Center is discoverable and installable by customers.
- C. An unpublished app is only usable in the developer account in demo.
- D. Sharing only with the vendor's own account keeps customers from installing it.

**Q296. (API Authentication - Scopes) [MEDIUM]** An app requests consent to send envelopes and read basic user and account context. A developer suggests requesting every available scope now to avoid future changes. What is the better OAuth practice?

A. Request only the minimum scopes required for the current operations
B. Request every scope now, as the developer suggests
C. Omit scopes and let Docusign infer permissions
D. Add impersonation now so the app can switch to JWT later

**Answer:** A. Request only the minimum scopes required for the current operations

**Explanation:** OAuth consent should follow least privilege: request only the scopes the app's current operations need.

**Why this answer and not the others:** A is right because least privilege limits risk and keeps consent focused. The trap is D: adding impersonation for a possible JWT move sounds forward-looking, but it grants the ability to act as the user without any current need. B is the over-requesting the question warns against, and C fails because scopes must be requested explicitly.

**Option notes:**
- A. Correct. Request only the scopes needed for the app's current operations.
- B. Requesting every scope grants access the app does not use and broadens the consent request.
- C. Scopes must be requested explicitly; Docusign does not infer them from later API calls.
- D (TRAP). impersonation lets the app act as the user through JWT; requesting it without a current need breaks least privilege.

**Q297. (eSignature API - Embedded sending) [MEDIUM]** Which request returns the embedded sending (sender view) URL for an existing draft envelope?

A. POST /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient
B. POST /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/sender
C. POST /restapi/v2.1/accounts/{accountId}/envelopes
D. PUT /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId} with status sent

**Answer:** B. POST /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/sender

**Explanation:** EnvelopeViews:createSender is a POST to .../envelopes/{envelopeId}/views/sender for a draft envelope.

**Why this answer and not the others:** B is right because views/sender is the sender view endpoint. The trap is A: views/recipient has the same shape, but it returns a signing URL for a recipient. C creates a new envelope and D sends an existing draft without any preparation view.

**Option notes:**
- A (TRAP). views/recipient returns the embedded signing view for a recipient.
- B. Correct. POST .../views/sender is EnvelopeViews:createSender, the embedded sending view.
- C. POST .../envelopes creates an envelope; it does not return a view URL.
- D. PUT with status sent sends the draft immediately, skipping the in-app preparation.

**Q298. (Workflow Builder and Workflow API - Workflow steps) [MEDIUM]** In a loan workflow, the applicant, a loan officer and a branch manager each complete actions. How should the designer handle these people?

A. Define all three as participants with roles, ideally at the start of workflow creation
B. Give a role only to the person who starts the workflow
C. Skip participants; they are created automatically from the templates
D. Add participants only after the workflow is published

**Answer:** A. Define all three as participants with roles, ideally at the start of workflow creation

**Explanation:** Anyone who takes action in a workflow is a participant and needs a defined role. Adding participants at the beginning is the recommended practice, although they can be added at any point while building.

**Why this answer and not the others:** A is right because each person who acts needs a participant role. The trap is B: the person who starts the workflow is often a participant, but the officer and manager also act and need roles. C and D are wrong: participants are defined in the workflow, during design and not after publishing.

**Option notes:**
- A. Correct. Every person who acts is a participant; define them early.
- B (TRAP). The officer and manager also act, so they need participant roles too.
- C. Participants are defined in the workflow; they are not created automatically from templates.
- D. Participants are configured while building the workflow, before publishing.

**Q299. (App Center and Extension Apps - Manifest) [MEDIUM]** Which two registration paths does the Developer Console offer for a new extension app?

A. A form-based experience, or uploading or editing a JSON manifest
B. Uploading a manifest through the eSignature REST API, or the App Center
C. The Apps and Keys page in eSignature Admin, or a support ticket
D. A Maestro workflow template, or a Web Forms configuration

**Answer:** A. A form-based experience, or uploading or editing a JSON manifest

**Explanation:** In the Developer Console, Create App offers a form-based experience or editing/uploading a manifest file (with a built-in editor that validates in real time).

**Why this answer and not the others:** A is right because those are the two Developer Console options. The trap is B: manifests are uploaded in the Developer Console, not through the eSignature API, and the App Center is for customers installing apps. C is for integration keys, and D are agreement process features, not registration methods.

**Option notes:**
- A. Correct. Register using the form-based experience or by uploading/editing a JSON manifest.
- B (TRAP). Manifests are uploaded in the Developer Console; the App Center is where customers install published apps.
- C. Apps and Keys manages integration keys, and support tickets are not a registration path.
- D. Maestro and Web Forms consume extension apps; they do not register them.

**Q300. (API Authentication - User info) [MEDIUM]** The /oauth/userinfo response lists several accounts for the user. Which account context should the app use by default for API calls?

A. The first account in the accounts array
B. Any account, because all accounts share one base URI
C. The account with is_default set to true, using its account_id and base_uri
D. The account whose ID matches the integration key

**Answer:** C. The account with is_default set to true, using its account_id and base_uri

**Explanation:** The app typically uses the account with is_default=true and takes its account_id and base_uri for all later API requests.

**Why this answer and not the others:** C is right because is_default marks the account to use. The trap is A: taking the first array entry often works in testing, but the order is not a guarantee of the default account. B is wrong because accounts can have different base URIs, and D confuses the app's integration key with an account ID.

**Option notes:**
- A (TRAP). Array order does not mark the default account; use the is_default flag.
- B. Accounts can sit on different base URIs, which is why base_uri is returned per account.
- C. Correct. Use the account with is_default=true and its account_id and base_uri.
- D. The integration key identifies the app, not a Docusign account.

**Q301. (eSignature API - Creating the envelope before the user indicates they ar) [HIGH]** An HR department implements embedded signing with its HR system. Users report a timeout expiration error when trying to sign. Which practice could cause this error?

A. Creating the envelope and signing URL before the user indicates they are ready to sign
B. Creating the envelope for remote signing instead of embedded signing
C. Creating the envelope in draft status
D. Creating the envelope using a composite template

**Answer:** A. Creating the envelope and signing URL before the user indicates they are ready to sign

**Explanation:** Embedded signing URLs are short-lived. If the app creates the envelope and signing URL before the user is ready, the URL can expire before they use it, causing the timeout.

**Why this answer and not the others:** A is right because early URL generation is the classic cause of expiration errors. The trap is C: a draft envelope does cause embedded signing problems, but it produces a status error, not a timeout. B would produce an email invitation instead of an embedded session and D is just an envelope structure.

**Option notes:**
- A. Correct. Generating the signing URL too early lets it expire before the user opens it.
- B. A remote signer would get an email instead; it would not produce a timeout in the embedded session.
- C (TRAP). A draft envelope cannot be signed, but that is a status problem, not a timeout expiration.
- D. Composite templates are a way to build envelope content and do not affect URL expiration.

**Q302. (Workflow Builder and Workflow API - Identity step) [LOW]** After a Verify Someone's Identity step, compliance wants the ID evidence saved automatically to the company's SharePoint. The SharePoint extension app is installed. Which step fits?

A. A Writeback step to SharePoint
B. A Send an Email step with the evidence attached
C. A Connect configuration that forwards events to SharePoint
D. A Store Files step with the SharePoint app, after the identity step

**Answer:** D. A Store Files step with the SharePoint app, after the identity step

**Explanation:** Store Files app steps automate storage of completed agreements and ID evidence data in services such as SharePoint, Box or Google Drive.

**Why this answer and not the others:** D is right because Store Files covers ID evidence as well as agreements. The trap is A: Writeback also sends data to an external system, but it updates record fields, not stored files. B relies on email, and C only delivers event notifications.

**Option notes:**
- A (TRAP). Writeback updates data in external systems; it is not used to store evidence files.
- B. Emailing evidence is not automated storage and raises data-handling concerns.
- C. Connect sends events; it does not save ID evidence to SharePoint.
- D. Correct. Store Files saves ID evidence data to SharePoint after verification.

**Q303. (App Center and Extension Apps - Workflow steps) [HIGH]** Where is the call to an external API defined within an extension app's structure?

A. In a Maestro workflow variable definition
B. In an extension's actionReferences list
C. In a connection that references the Docusign API gateway
D. In an action that references an external platform endpoint

**Answer:** D. In an action that references an external platform endpoint

**Explanation:** An action defines the call to the external platform endpoint; extensions only reference actions, and connections supply authentication.

**Why this answer and not the others:** D is right because actions describe the external endpoint calls. The trap is B: actionReferences names the actions an extension uses but does not define the call. A is a workflow concept, and C wrongly points the connection at Docusign instead of the external platform.

**Option notes:**
- A. Workflow variables hold data inside Maestro; they do not define extension app calls.
- B (TRAP). actionReferences only names the actions; the call itself is defined in the action.
- C. Connections authenticate to the external platform, not to a Docusign API gateway.
- D. Correct. An action references the external platform endpoint that Docusign calls.

**Q304. (API Authentication - PKCE) [HIGH]** Inside a native app's Public Authorization Code Grant flow, which mechanism prevents an intercepted authorization code from being redeemed by another app?

A. The client secret in an Authorization: Basic header
B. A PKCE code verifier and code challenge
C. The state parameter echoed to the redirect URI
D. A JWT assertion signed with the app's RSA private key

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** With PKCE, the code_challenge is sent on /oauth/auth and only the holder of the original code_verifier can redeem the code at /oauth/token, so an intercepted code is useless.

**Why this answer and not the others:** B is right because the stem asks for the mechanism inside the flow, and PKCE binds the code to the original code_verifier. The trap is C: state is also sent through the redirect, but it protects against CSRF and does not stop someone else from redeeming the code. A needs a secret a native app cannot keep, and D belongs to JWT Grant.

**Option notes:**
- A. A native app is a public client with no secret, so a Basic secret header is not available.
- B. Correct. The code_verifier and code_challenge bind the code to the app that requested it.
- C (TRAP). state protects the redirect against CSRF; it does not prevent an intercepted code from being redeemed.
- D. A signed JWT assertion is part of JWT Grant, not the Public Auth Code flow, and needs a protected private key.

**Q305. (eSignature API - Bulk send) [MEDIUM]** After initiating a bulk send, the app must report how many envelopes were sent, queued or failed. What should it use?

A. The batchId with BulkSend:getBulkSendBatchStatus, or Connect notifications
B. Poll each envelope with Envelopes:get every minute
C. The bulkListId with BulkSend:createBulkSendList
D. The canBeSent value from the test request

**Answer:** A. The batchId with BulkSend:getBulkSendBatchStatus, or Connect notifications

**Explanation:** Initiating a bulk send returns a batchId; checking the batch status returns sent, queued and failed counts, and Connect can push status without polling.

**Why this answer and not the others:** A is right because batch status reports per-batch counts. The trap is C: bulkListId is a real bulk send identifier, but it identifies the list and createBulkSendList creates lists rather than reporting results. B breaks polling guidance and D only says whether the request could be sent.

**Option notes:**
- A. Correct. batchId with getBulkSendBatchStatus (or Connect) gives sent, queued and failed counts.
- B. Polling each envelope every minute exceeds polling guidance; Connect is the recommended alternative.
- C (TRAP). bulkListId identifies the list, and createBulkSendList creates lists; neither reports batch results.
- D. canBeSent is returned by the test step and says only whether the bulk send can be sent.

**Q306. (Workflow Builder and Workflow API - Extension step) [MEDIUM]** Agreements saved to Box by a workflow are missing signatures. The Box app is installed, and its Store Files step runs without errors. What should be fixed?

A. Reinstall the Box extension app
B. Change the start method to From an API call
C. Move the Store Files step after the Send Documents for Signature step
D. Switch Connect to JSON SIM

**Answer:** C. Move the Store Files step after the Send Documents for Signature step

**Explanation:** The step runs successfully but stores an unsigned file, so it runs too early. Placing it after the signing step stores the completed agreement.

**Why this answer and not the others:** C is right because the clue is that the app works but the document is unsigned. The trap is A: reinstalling is the usual fix for app failures, but the step already runs without errors. B and D change how the workflow starts or reports events, not when the file is saved.

**Option notes:**
- A (TRAP). The app already works; reinstalling does not change when the file is stored.
- B. The start method does not change step order.
- C. Correct. Store the file after signing so the completed agreement is saved.
- D. Connect format affects notifications only.

**Q307. (App Center and Extension Apps - Connections) [HIGH]** A partner is building a PUBLIC extension app that connects Docusign to its external SaaS platform. Which OAuth 2.0 grant should the app's connection use?

A. Implicit Grant
B. JWT Grant with an RSA key pair
C. Client Credentials Grant
D. Authorization Code Grant

**Answer:** D. Authorization Code Grant

**Explanation:** Extension app connections support Authorization Code Grant or Client Credentials Grant; public apps connecting to external systems use Authorization Code Grant.

**Why this answer and not the others:** D is right because public extension apps use Authorization Code Grant. The trap is C: Client Credentials is an option only for private apps connecting to internal systems (and only for US clients). A and B are Docusign eSignature auth flows for your app calling Docusign, not grants for extension app connections.

**Option notes:**
- A. Implicit Grant is not a supported extension app connection grant.
- B. JWT Grant is how your app calls Docusign APIs; extension connections use Authorization Code or Client Credentials.
- C (TRAP). Client Credentials is allowed only for private apps connecting to internal systems, not public apps.
- D. Correct. Public extension apps use Authorization Code Grant for their connection.

**Q308. (eSignature API - Envelope create) [MEDIUM]** Envelopes:create calls return 201 Created, but no recipient gets an email and the envelopes sit in the sender's Drafts folder. Which status value should the request use so envelopes go out immediately?

A. created
B. voided
C. completed
D. sent

**Answer:** D. sent

**Explanation:** Envelopes appearing as drafts means the request used status created. Changing the request to status sent delivers them immediately.

**Why this answer and not the others:** D is right because sent is the value that sends the envelope on creation. The trap is A: created is exactly what produces the draft symptom described. B would cancel the envelope and C is set by Docusign only after every recipient finishes.

**Option notes:**
- A (TRAP). created is the cause of the symptom: it saves the envelope as a draft, so no email is sent.
- B. voided cancels an in-process envelope; it would stop the envelope rather than deliver it.
- C. completed is a terminal status set by Docusign when all recipients finish; it cannot be used to send.
- D. Correct. status sent sends the envelope as part of the create call, so recipients are notified.

**Q309. (Workflow Builder and Workflow API - Branching) [LOW]** In Workflow Builder, which category contains branching rules, along with steps such as Send an Email and Show a Confirmation Screen?

A. Docusign steps
B. Utility steps
C. Apps steps
D. Start methods

**Answer:** B. Utility steps

**Explanation:** Utility steps cover notification actions such as sending an email and workflow control actions such as branching rules.

**Why this answer and not the others:** B is right because branching is a workflow control action, which is a utility step. The trap is A: Docusign steps are the built-in Docusign feature steps (Web Forms, eSignature, identity verification), not control logic. C is for extension apps, and D decides how a workflow starts.

**Option notes:**
- A (TRAP). Docusign steps cover features like Web Forms, eSignature and ID verification, not branching.
- B. Correct. Utility steps include branching rules, Send an Email and confirmation screens.
- C. Apps steps call third-party extension apps.
- D. Start methods decide how a workflow begins; they are not steps.

**Q310. (App Center and Extension Apps - connectionsReference) [HIGH]** Which statement correctly describes cross-references in an extension app manifest?

A. Actions reference extensions, and connections reference actions
B. Connections reference extensions through actionReferences
C. Extensions reference actions (actionReferences); actions reference connections (connectionsReference)
D. Extensions reference connections directly through connectionsReference

**Answer:** C. Extensions reference actions (actionReferences); actions reference connections (connectionsReference)

**Explanation:** The chain is extension to action (actionReferences) and action to connection (connectionsReference).

**Why this answer and not the others:** C is right because it gives both links in the correct direction. The trap is D: extensions do not reference connections directly; the connection link sits on each action. A and B reverse the direction of the references.

**Option notes:**
- A. This reverses both links; extensions point to actions, and actions point to connections.
- B. actionReferences belongs to extensions, and connections do not reference anything.
- C. Correct. Extensions point to actions, and actions point to connections.
- D (TRAP). connectionsReference is on actions, not extensions.

**Q311. (eSignature API - Draft envelope) [MEDIUM]** A bulk send flow starts by creating the envelope that a bulk send list will later be applied to. Which status should that envelope be created with?

A. sent
B. voided
C. created
D. completed

**Answer:** C. created

**Explanation:** The bulk send process begins with a draft envelope (status created), whose envelopeId is then used with the bulk send list. The clue is that the list is applied later.

**Why this answer and not the others:** C is right because the bulk send envelope is created as a draft with status created. The trap is A: sent is the normal create value, but sending would deliver the envelope to its own recipients instead of serving as the bulk send source. B and D are not create values: voided cancels and completed is set by Docusign.

**Option notes:**
- A (TRAP). sent would deliver this single envelope immediately instead of keeping it as the bulk send source.
- B. voided cancels an in-process envelope; it is never used to create one.
- C. Correct. The bulk send flow starts with a draft envelope created with status created.
- D. completed is set by Docusign after all recipients finish; it is not a create value.

**Q312. (Workflow Builder and Workflow API - Start method) [MEDIUM]** Customers without Docusign accounts must be able to submit an account change request at any time via a link in an automatic email reply. Which start method should the workflow use?

A. From a link
B. Manually in Docusign (Run Workflow)
C. From an API call
D. Triggered from a CLM workflow

**Answer:** A. From a link

**Explanation:** From a link is recommended for self-service forms such as account change requests; the link can be placed in a website or an automatic email reply.

**Why this answer and not the others:** A is right because customers start the workflow themselves from a link. The trap is B: Run Workflow is also a no-code start, but only internal users with Workflows: Prepare permission can use it. C needs an integration with an access token, and D runs from inside Docusign CLM.

**Option notes:**
- A. Correct. The link in the auto-reply lets customers start the workflow themselves.
- B (TRAP). Requires an internal user with Workflows: Prepare permission.
- C. Needs custom code with an access token; nothing here calls the API.
- D. Started from within Docusign CLM, not by customers.

**Q313. (App Center and Extension Apps - Connected Fields) [HIGH]** A retailer must check a customer's custom loyalty ID against its own system of record while the customer enters details during signing. Which extension type and extension point should be used?

A. Data Verification at eSignature signing
B. File archive through a Maestro workflow
C. Connected Fields through the eSignature Add Fields view and signing
D. Data IO through a Maestro workflow

**Answer:** C. Connected Fields through the eSignature Add Fields view and signing

**Explanation:** Connected fields verify custom values against your own system of record at the Add Fields view and during signing.

**Why this answer and not the others:** C is right because a custom loyalty ID checked against the retailer's system is connected fields territory. The trap is A: Data Verification runs at the same point but only covers standard types like bank account, address or SSN. B and D run in Maestro, not during signing.

**Option notes:**
- A (TRAP). Data Verification handles standard types, not a custom loyalty ID.
- B. File archive stores documents and is legacy.
- C. Correct. Connected fields verify custom data at Add Fields and signing.
- D. Data IO runs in Maestro workflows, not during the signing ceremony.

**Q314. (eSignature API - Cancel envelope) [HIGH]** One of two signers has already signed a sent envelope when a fatal error is found. The envelope must be canceled so the second signer cannot sign. Which status should be set?

A. created
B. voided
C. sent
D. completed

**Answer:** B. voided

**Explanation:** An envelope can be voided while it is still in process, even after some recipients have signed. The clue is that it is not yet completed.

**Why this answer and not the others:** B is right because voided cancels an in-process envelope, including a partially signed one. The trap is D: one signer finished, but completed is only reached when all recipients finish and is not set by the sender. A is a draft status and C is the status it already has.

**Option notes:**
- A. created is the draft status; it does not cancel a sent, partially signed envelope.
- B. Correct. Voiding cancels the in-process envelope so the remaining signer cannot sign.
- C. sent is the current status; setting it again would not stop the second signer.
- D (TRAP). completed is set by Docusign only when all recipients finish; it does not cancel the envelope.

**Q315. (Workflow Builder and Workflow API - API trigger) [HIGH]** Which data does the body of a TriggerWorkflow request contain?

A. An envelope definition with documents and recipients
B. The workflowId and an envelope status of 'sent'
C. Only the mtid and mtsec values
D. An instance_name and trigger_inputs matching the workflow's trigger_input_schema

**Answer:** D. An instance_name and trigger_inputs matching the workflow's trigger_input_schema

**Explanation:** TriggerWorkflow requires an instance_name and the input data described by the workflow's trigger_input_schema, passed in trigger_inputs.

**Why this answer and not the others:** D is right because those are the documented body fields. The trap is C: mtid and mtsec are required to identify and authenticate the trigger, but they are query parameters on the trigger URL, not the body. A and B describe eSignature envelope requests.

**Option notes:**
- A. An envelope definition belongs to Envelopes:create, not to a workflow trigger.
- B. Envelope status is an eSignature concept; it is not part of a trigger body.
- C (TRAP). mtid and mtsec are query parameters on the trigger URL, not the body.
- D. Correct. instance_name plus trigger_inputs that match the input schema.

**Q316. (App Center and Extension Apps - API proxy) [MEDIUM]** Before configuring an extension app manifest, which information should the developer gather from the external service, identity provider and any API proxy?

A. The Docusign integration key, secret and redirect URI of an eSignature app
B. Endpoint URLs, authorization details, and required request and response parameters
C. The Connect HMAC secret for the customer's account
D. Recipient email addresses for the test envelopes

**Answer:** B. Endpoint URLs, authorization details, and required request and response parameters

**Explanation:** The developer needs endpoint URLs, authorization details, and the required parameters in requests and responses from the external service, identity provider and proxy.

**Why this answer and not the others:** B is right because those values configure the connections and actions. The trap is A: those are Docusign credentials for calling Docusign, not what the manifest needs to call the external service. C belongs to Connect, and D is test data.

**Option notes:**
- A (TRAP). These identify an app calling Docusign; the manifest needs the external platform's details.
- B. Correct. Endpoints, auth details and request/response parameters are needed to configure the app.
- C. The Connect HMAC secret secures webhooks, not extension app calls.
- D. Recipient emails are envelope data, not extension app configuration.

**Q317. (eSignature API - Idempotency) [LOW]** An architect asks which platform-native field addresses duplicate envelopes when a create request is retried after a dropped connection. Which option is correct?

A. transactionId
B. bulkListId
C. batchId
D. envelopeId

**Answer:** A. transactionId

**Explanation:** transactionId is a sender-generated value on the envelope definition used to tell whether an envelope from an earlier attempt was already created.

**Why this answer and not the others:** A is right because the client supplies transactionId with the create request. The trap is D: envelopeId identifies envelopes, but it is generated by Docusign and unknown to the client after a dropped connection. B and C are bulk send identifiers for a list and a batch.

**Option notes:**
- A. Correct. transactionId is supplied by the sender and identifies the create attempt across retries.
- B. bulkListId identifies a bulk send list; it is unrelated to single envelope retries.
- C. batchId identifies a bulk send batch; it does not cover single Envelopes:create calls.
- D (TRAP). envelopeId is generated by Docusign, so after a dropped connection the client does not have it.

**Q318. (Workflow Builder and Workflow API - Runtime errors) [HIGH]** A trigger call works with a token from API Explorer, but the app's JWT token, requested with only the 'signature impersonation' scopes, gets an authorization error. What should the developer change?

A. Use the eSignature base path /restapi/v2.1
B. Republish the workflow
C. Request the aow_manage scope as well and have consent granted for it
D. Add more fields to trigger_inputs

**Answer:** C. Request the aow_manage scope as well and have consent granted for it

**Explanation:** Maestro API calls need the signature scope plus Maestro scopes such as aow_manage. A newly requested scope also needs consent before JWT can use it.

**Why this answer and not the others:** C is right because the app's token lacks the Maestro scope. The trap is D: missing inputs are another common trigger error, but they cause input validation failures, not an authorization error. A uses the wrong base path for Maestro, and B does not change the token.

**Option notes:**
- A. Maestro uses api-d.docusign.com/v1 or api.docusign.com/v1, not /restapi/v2.1.
- B. Republishing does not change the scopes in the app's token.
- C. Correct. Add aow_manage to the requested scopes and grant consent for it.
- D (TRAP). Input problems cause validation errors, not authorization errors.

**Q319. (App Center and Extension Apps - Firewall) [MEDIUM]** Security rules forbid exposing an internal system of record directly to the internet, but an extension action must reach it. Which approach fits?

A. Expose a publicly reachable API proxy in front of it and allow Docusign traffic
B. Have the internal system poll Docusign for pending actions
C. Use Connect to push action requests into the private network
D. Distribute the app privately, which runs actions inside Docusign's network

**Answer:** A. Expose a publicly reachable API proxy in front of it and allow Docusign traffic

**Explanation:** Docusign must be able to call the endpoint, so a reachable API proxy (with Docusign traffic allowed) can front the internal system without exposing it directly.

**Why this answer and not the others:** A is right because a proxy gives Docusign a reachable endpoint while shielding the internal system. The trap is D: private distribution limits who can install the app, but Docusign still calls your endpoint over the network. B and C are not how extension actions are invoked.

**Option notes:**
- A. Correct. A reachable API proxy lets Docusign call in while the backend stays internal.
- B. Extension actions are called by Docusign; the service does not poll for work.
- C. Connect sends event notifications; it does not deliver extension action calls.
- D (TRAP). Private distribution controls installation, not network location; Docusign still calls your endpoint.

**Q320. (eSignature API - Make an API call to request the signing URL) [HIGH]** An embedded signing flow has created and sent the envelope with clientUserId on the signer. The app now needs the browser URL for that recipient's signing ceremony. Which step starts the ceremony?

A. Call EnvelopeViews:createRecipient to request the recipient view URL
B. Wait for Docusign to email the embedded signer
C. Call EnvelopeViews:createSender for the signer
D. Set the envelope status back to created

**Answer:** A. Call EnvelopeViews:createRecipient to request the recipient view URL

**Explanation:** For embedded signing, the app calls EnvelopeViews:createRecipient to get a short-lived recipient view URL and redirects the signer to it.

**Why this answer and not the others:** A is right because the recipient view is the signing ceremony. The trap is C: createSender is another view endpoint, but it opens the sender's preparation view, not the signer's ceremony. B fails because embedded signers are not emailed and D would turn the envelope back into a draft workflow.

**Option notes:**
- A. Correct. createRecipient returns the URL for the embedded signer's ceremony.
- B. Embedded signers with clientUserId are not emailed a signing invitation.
- C (TRAP). createSender opens the sending and tagging view for the sender, not the signing ceremony.
- D. Reverting to created is not part of embedded signing; the envelope must stay sent.

**Q321. (Workflow Builder and Workflow API - Embedding workflow) [MEDIUM]** An app redirects users to the workflow instance URL from TriggerWorkflow instead of embedding it. Where are users when they finish the workflow?

A. Redirected automatically to the app's returnUrl
B. They remain on the Docusign platform
C. Signed out and sent to the Docusign login page
D. Shown a download prompt for the agreement

**Answer:** B. They remain on the Docusign platform

**Explanation:** With the redirect option, users are routed to the Docusign platform and remain there when they complete the workflow. To keep them in the app, embed the instance URL in an iframe.

**Why this answer and not the others:** B is right because a redirect does not return users to the app. The trap is A: returnUrl comes from eSignature embedded signing, but workflow instance URLs do not send the user back to the app. C and D are not documented behavior.

**Option notes:**
- A (TRAP). returnUrl belongs to eSignature recipient views, not to workflow instance redirects.
- B. Correct. Users stay on Docusign; use an iframe to keep them in the app.
- C. Nothing signs the user out at the end of the workflow.
- D. No download prompt is part of this behavior.

**Q322. (App Center and Extension Apps - Data Verification) [HIGH]** A financial institution needs real-time validation of a customer's bank account details, using a standard bank verification service, while the customer signs a loan agreement. Which extension type and extension point apply?

A. Connected Fields, triggered in a Maestro workflow
B. Data IO, triggered at the eSignature Add Fields view
C. Data Verification, triggered at eSignature signing
D. File archive, triggered at eSignature signing

**Answer:** C. Data Verification, triggered at eSignature signing

**Explanation:** Data Verification at eSignature signing validates the bank account details in real time as the customer signs.

**Why this answer and not the others:** C is right because a standard bank account check during signing is Data Verification. The trap is A: connected fields are not supported in Maestro and are for custom data. B places Data IO at the wrong extension point, and D stores files.

**Option notes:**
- A (TRAP). Connected fields are not supported in Maestro and target custom data.
- B. Data IO runs in Maestro workflows and does not verify fields at Add Fields.
- C. Correct. Data Verification runs at signing to validate the bank account.
- D. File archive stores documents and is a legacy workflow extension.

**Q323. (eSignature API - Template reference) [HIGH]** A template-reference request worked in the demo environment and is moving to production at Go-Live. Which value in the request references the stored template and must be updated for production?

A. roleName in templateRoles
B. sequence
C. The template's display name
D. templateId

**Answer:** D. templateId

**Explanation:** Requests reference stored templates by templateId, and template IDs differ between demo and production, so they must be updated during Go-Live.

**Why this answer and not the others:** D is right because templateId is the reference, and it changes between environments. The trap is C: the template's name may be the same in both environments, but requests do not reference templates by name. A maps recipients to roles and B applies to server and inline templates in composite templates.

**Option notes:**
- A. roleName maps recipients to template roles; it is defined by the template, not an environment-specific ID.
- B. sequence orders server and inline templates inside composite templates; it does not identify a template.
- C (TRAP). The display name is not how the API references a template; requests use templateId.
- D. Correct. templateId references the stored template and differs between demo and production.

**Q324. (Workflow Builder and Workflow API - Installed extensions) [MEDIUM]** A team wants its Maestro workflow to use connected fields to verify data. What must they know?

A. Connected fields are not supported in Maestro workflows; use an extension app step such as Data IO instead
B. Connected fields can be added to the Prepare eSignature Template step
C. Connected fields are enabled through the Connect configuration
D. Connected fields are installed from the Developer Console

**Answer:** A. Connected fields are not supported in Maestro workflows; use an extension app step such as Data IO instead

**Explanation:** Connected fields are not currently supported in Maestro workflows. Workflows use extension app steps, such as Data IO, to work with external data.

**Why this answer and not the others:** A is right because Maestro does not support connected fields. The trap is B: templates used by workflows can contain tabs, so it seems possible, but connected fields are still not supported in Maestro. C confuses Connect with connected fields, and D confuses building an app with installing one.

**Option notes:**
- A. Correct. Connected fields are not supported in Maestro; use extension app steps such as Data IO.
- B (TRAP). Connected fields remain unsupported in Maestro, even through a template step.
- C. Connect is the webhook service and has nothing to do with connected fields.
- D. The Developer Console is for building apps; admins install apps from App Center.

**Q325. (App Center and Extension Apps - Data IO) [HIGH]** Where is a Data IO extension invoked?

A. In the eSignature Add Fields view and during signing
B. Only in Web Forms
C. Through Connect envelope events
D. In Maestro workflows

**Answer:** D. In Maestro workflows

**Explanation:** The extension point for Data IO is Maestro workflows.

**Why this answer and not the others:** D is right because Data IO runs as part of Maestro workflows. The trap is A: Add Fields and signing are the extension points for connected fields and data verification. B applies only to email and phone verification, and C is a notification mechanism, not an extension point.

**Option notes:**
- A (TRAP). Add Fields and signing are the extension points for connected fields and data verification.
- B. Web Forms is an extension point only for email and phone verification.
- C. Connect sends event notifications; it is not where Data IO runs.
- D. Correct. Data IO's extension point is Maestro workflows.

**Q326. (eSignature API - Composite templates) [HIGH]** A composite template object has a server template that defines the role 'customer' and an inline template that maps a recipient to that role. How should their sequence values be set?

A. Inline template lower, so its recipient is applied first
B. Both templates use the same sequence value
C. Server template lower than the inline template
D. Omit sequence on the inline template

**Answer:** C. Server template lower than the inline template

**Explanation:** Attributes are applied in sequence order and later ones overwrite earlier ones, so the server template must have the lower sequence to establish the role before the inline template maps a recipient to it.

**Why this answer and not the others:** C is right because the role must exist before a recipient is mapped to it. The trap is A: it sounds like the recipient should be applied first, but then the role 'customer' would not exist yet. B fails because sequence values must be unique within a composite template object, and D fails because every serverTemplate and inlineTemplate needs a sequence.

**Option notes:**
- A (TRAP). If the inline template runs first, the role it maps to does not exist yet.
- B. Sequence values must be unique within a composite template object.
- C. Correct. Server template first (lower sequence) establishes the role; the inline template then maps the recipient.
- D. Every serverTemplate and inlineTemplate object must have a sequence property.

**Q327. (App Center and Extension Apps - File IO) [LOW]** In Workflow Builder, which step category uses installed extension apps such as Box, Google Drive or SharePoint to save completed agreements?

A. Writeback steps
B. Read steps
C. Store Files steps
D. ID Verification steps

**Answer:** C. Store Files steps

**Explanation:** Store Files steps automate storing completed agreements and ID Evidence data with apps such as Google Drive, Box, Dropbox, OneDrive and SharePoint.

**Why this answer and not the others:** C is right because saving agreements to storage is a Store Files step. The trap is A: Writeback steps update data in external systems such as Salesforce or ServiceNow, not files. B imports data, and D verifies the signer's identity.

**Option notes:**
- A (TRAP). Writeback steps update data in external systems, not store files.
- B. Read steps import data into the workflow.
- C. Correct. Store Files steps save agreements to storage apps.
- D. ID Verification verifies the signer's identity, not file storage.

**Q328. (eSignature API - Anchor tabs) [MEDIUM]** A team converts a manual process to the API. The document's length varies, but the signature should appear near a specific text string. Which tab placement method is best?

A. Copy the coordinates from a sample document into xPosition/yPosition
B. Anchor tagging with anchorString and offsets
C. Reference the document by templateId
D. Use one tab per page and let the signer choose

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tagging places tabs relative to document text, so placement survives changes in length. The clue is 'near a specific text string'.

**Why this answer and not the others:** B is right because anchor tabs follow the text. The trap is A: coordinates from a sample work for that sample, but fixed positions do not move when another document is longer or shorter. C references a template rather than positioning tabs and D creates extra fields instead of placing one correctly.

**Option notes:**
- A (TRAP). Coordinates from one sample document are fixed and break when the next document's length differs.
- B. Correct. anchorString with offsets puts the tab next to the text regardless of length.
- C. templateId references a saved template; it does not place tabs on a variable document.
- D. Extra tabs on every page create unwanted fields and do not place the signature correctly.

**Q329. (App Center and Extension Apps - Connected Fields) [MEDIUM]** A connected fields extension app connects to a system of record that uses its own proprietary schema. Which data model must the app expose to Docusign?

A. JSON Schema types declared in the manifest's actions
B. The Concerto data model
C. The legacy XML Connect format
D. Only standard eSignature tab types

**Answer:** B. The Concerto data model

**Explanation:** Docusign models data input and output definitions with Concerto; if your system does not already use it, you implement logic to map to it.

**Why this answer and not the others:** B is right because type definitions returned to Docusign use Concerto. The trap is A: actions describe endpoints, but the type definitions are Concerto models. C is an event notification format, and D would not describe custom data types.

**Option notes:**
- A (TRAP). Type definitions use the Concerto model, not JSON Schema in the actions object.
- B. Correct. Connected fields (and Data IO) type definitions use the Concerto data model.
- C. XML Connect is a webhook payload format, not a data model for extensions.
- D. Custom data types are defined by your Concerto models, not limited to standard tabs.

**Q330. (eSignature API - Embedded signing) [HIGH]** A pull request adds embedded signing. The reviewer checks the envelope JSON for the recipient property that marks the signer as embedded. Which property should be present?

A. clientUserId
B. recipientId
C. returnUrl
D. EnvelopeViews:createRecipient

**Answer:** A. clientUserId

**Explanation:** clientUserId on the signer marks embedded (captive) signing. The clue is a recipient property in the envelope JSON.

**Why this answer and not the others:** A is right because clientUserId is the recipient property for embedded signing. The trap is D: createRecipient is part of the same feature, but it is an endpoint called afterwards, not a property in the envelope JSON. B identifies any recipient and C is set in the createRecipient request.

**Option notes:**
- A. Correct. Setting clientUserId on the signer marks the recipient as embedded (captive).
- B. recipientId identifies the recipient within the envelope; every recipient has one, embedded or not.
- C. returnUrl is sent in the createRecipient request to say where to redirect after signing; it is not a recipient property.
- D (TRAP). EnvelopeViews:createRecipient is the endpoint that returns the signing URL, not a recipient property.

**Q331. (App Center and Extension Apps - Data Verification) [MEDIUM]** Which extension point does a postal address verification extension use?

A. eSignature Add Fields view and signing
B. eSignature and Web Forms
C. Maestro workflows
D. The App Center listing

**Answer:** A. eSignature Add Fields view and signing

**Explanation:** Postal address verification runs at the eSignature Add Fields view and during signing.

**Why this answer and not the others:** A is right because that is the extension point for postal address verification. The trap is B: Web Forms support applies only to email and phone verification. C is the extension point for Data IO and File IO, and D is where apps are installed.

**Option notes:**
- A. Correct. Postal address verification runs at Add Fields and signing.
- B (TRAP). Only email and phone verification are also available in Web Forms.
- C. Maestro workflows are the extension point for Data IO and File IO.
- D. The App Center is for installing apps, not an extension point.

**Q332. (eSignature API - Signing URL) [HIGH]** An app will show the embedded signing session in focused view. Which two additional parameters must the createRecipient request include beyond the standard ones?

A. clientUserId and recipientId
B. returnUrl and authenticationMethod
C. identityVerification and returnUrl
D. frameAncestors and messageOrigins

**Answer:** D. frameAncestors and messageOrigins

**Explanation:** Focused view requires frameAncestors (your site plus the Docusign apps domain) and messageOrigins in addition to the standard recipient view parameters.

**Why this answer and not the others:** D is right because frameAncestors and messageOrigins are the focused view additions. The trap is B: returnUrl and authenticationMethod are required, but for every recipient view, not specifically for focused view. A mixes a matching value with an envelope identifier and C fails because identityVerification cannot be used with focused view.

**Option notes:**
- A. clientUserId is a standard matching value and recipientId is not a focused view parameter.
- B (TRAP). returnUrl and authenticationMethod are required for all recipient views, not the focused view additions.
- C. identityVerification cannot be used with focused view; ID verification requires classic view.
- D. Correct. Focused view needs frameAncestors and messageOrigins in the createRecipient request.

**Q333. (App Center and Extension Apps - Extension app role) [HIGH]** When registering an extension app with the form-based experience, the developer must choose at least one extension type. Which list matches the available types?

A. Connect, PowerForms, Web Forms and Bulk Send
B. Read, Store Files, Writeback and Sign steps
C. Data IO, File IO, Connected Fields and ID Verification
D. File IO, Data IO, Data Verification and Connected Fields

**Answer:** D. File IO, Data IO, Data Verification and Connected Fields

**Explanation:** The registration form offers File Input Output, Data Input Output, Data Verification and Connected Fields as extension types.

**Why this answer and not the others:** D is right because those four are the extension types offered at registration. The trap is C: it swaps Data Verification for ID Verification, which is a separate Docusign identity product, not an extension type. B lists Workflow Builder step categories, and A lists eSignature features.

**Option notes:**
- A. These are eSignature sending and notification features, not extension types.
- B. These are Workflow Builder step categories that use installed apps, not the extension types chosen at registration.
- C (TRAP). ID Verification is a separate identity product; the fourth extension type is Data Verification.
- D. Correct. File IO, Data IO, Data Verification and Connected Fields are the extension types offered at registration.

**Q334. (eSignature API - Embedded signing timing) [MEDIUM]** A design must avoid expired embedded signing sessions. Which pattern should the team choose?

A. Generate each signing URL at envelope creation and store it in the database
B. Generate signing URLs in a nightly batch
C. Create the envelope ahead of time and request the signing URL when the user clicks Sign
D. Email the signing URL to the user as a backup

**Answer:** C. Create the envelope ahead of time and request the signing URL when the user clicks Sign

**Explanation:** The envelope can be created in advance, but the short-lived signing URL should be requested only when the user is ready, such as on the Sign click.

**Why this answer and not the others:** C is right because it requests the URL just before use. The trap is A: storing the URL at creation looks efficient, but the URL expires within minutes and is single-use. B generates URLs even earlier and D sends a short-lived embedded URL by email, outside the app.

**Option notes:**
- A (TRAP). A stored URL will usually have expired by the time the user opens it.
- B. Nightly batch generation creates URLs hours before use, so they expire.
- C. Correct. Requesting the URL when the user clicks Sign avoids its short lifetime.
- D. Emailing an embedded signing URL does not help; it expires quickly and bypasses the app.

**Q335. (App Center and Extension Apps - Public vs private) [HIGH]** A company that is not a Docusign partner builds an extension app only for its own accounts. Which distribution plan is correct?

A. Public, because any developer account can list an app publicly
B. Public, then restrict it with publicationRegions
C. Private, limited to the company's listed production accounts
D. Private for now, then switch the same published app to public later

**Answer:** C. Private, limited to the company's listed production accounts

**Explanation:** Private distribution suits an app for the company's own accounts and does not require Docusign Partner Program membership, which public publishing does.

**Why this answer and not the others:** C is right because the app serves only the company's accounts and private distribution needs no partner membership. The trap is D: the distribution type cannot be changed after an app is published. A is wrong because only Docusign partners may publish public apps, and B uses a region setting that does not restrict to one organization.

**Option notes:**
- A. Only Docusign partners may publish public extension apps, and the app is meant for one company anyway.
- B. publicationRegions limits regions for public apps; it does not restrict installation to one company.
- C. Correct. Private distribution limits installation to listed production accounts and fits a non-partner's internal app.
- D (TRAP). The distribution type cannot be changed after the app is published, so this plan does not work.

**Q336. (eSignature API - Embedded sending) [MEDIUM]** A sender must prepare or edit an envelope from inside a custom app. Which endpoint is relevant?

A. EnvelopeViews:createRecipient
B. EnvelopeViews:createSender
C. Envelopes:create with status sent
D. Templates:create

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses EnvelopeViews:createSender to get a sender view URL for a draft envelope.

**Why this answer and not the others:** B is right because the sender view lets the user prepare and send inside the app. The trap is A: createRecipient is the other embedded view, but it serves signers. C sends immediately without preparation and D creates a reusable template, not an in-app sending experience for this envelope.

**Option notes:**
- A (TRAP). createRecipient is for embedded signing by a recipient, not for preparing an envelope.
- B. Correct. createSender opens the sending view where the user tags and sends the envelope.
- C. status sent sends the envelope at once; the user cannot prepare it first.
- D. Templates:create saves a template; it does not let a sender edit this envelope in the app.

**Q337. (App Center and Extension Apps - Public App Center) [MEDIUM]** A partner's public extension app must be installable only by customers in selected geographic regions. Which manifest property controls this?

A. distribution set to PRIVATE
B. publicationRegions
C. connections
D. actions

**Answer:** B. publicationRegions

**Explanation:** publicationRegions (public apps only) chooses the regions from which the app can be installed.

**Why this answer and not the others:** B is right because publicationRegions limits a public app by region. The trap is A: PRIVATE limits installation to specific listed accounts, not to regions, and it would stop broad availability. C holds authentication settings and D holds the external operations.

**Option notes:**
- A (TRAP). PRIVATE restricts installation to listed accounts, not regions, and removes broad availability.
- B. Correct. publicationRegions sets the regions from which a public app can be installed.
- C. connections defines authentication to the external platform, not installation regions.
- D. actions describes the external operations Docusign calls, not where the app is available.

**Q338. (eSignature API - Bulk send) [MEDIUM]** In the bulk send process, which step returns the batchId used to track the envelopes in the batch?

A. Initiating the bulk send (BulkSend:createBulkSendRequest)
B. Creating the bulk send list (BulkSend:createBulkSendList)
C. Testing the bulk send (BulkSend:createBulkSendTestRequest)
D. Creating the draft envelope (Envelopes:create)

**Answer:** A. Initiating the bulk send (BulkSend:createBulkSendRequest)

**Explanation:** Initiating the bulk send returns a batchId, which is then used to check the status of envelopes in that batch.

**Why this answer and not the others:** A is right because the batch exists only once the bulk send is initiated. The trap is B: creating the list is a bulk send step, but it returns a bulkListId, not a batchId. C returns a canBeSent Boolean and D returns the draft's envelopeId.

**Option notes:**
- A. Correct. Initiating the bulk send returns the batchId for status tracking.
- B (TRAP). Creating the bulk send list returns a bulkListId, not a batchId.
- C. The test request returns canBeSent, a Boolean saying whether the bulk send can go ahead.
- D. Creating the draft envelope returns its envelopeId for use in the bulk send request.

**Q339. (App Center and Extension Apps - Manifest) [MEDIUM]** A manifest review finds an extension app must invoke a customer-hosted pricing API from a workflow step. The connection exists, but the callable operation itself is not yet described. Where should it be defined?

A. In an action definition inside the extension app manifest
B. In the connections object, next to the token URL
C. In the App Center listing description
D. In the publisher object

**Answer:** A. In an action definition inside the extension app manifest

**Explanation:** The callable operation belongs in an action definition; the existing connection handles authentication separately.

**Why this answer and not the others:** A is right because actions describe what Docusign calls. The trap is B: the connection already exists and only covers authentication, so adding the operation there is wrong. C is listing text and D is publisher contact information.

**Option notes:**
- A. Correct. The action definition describes the external operation Docusign can invoke.
- B (TRAP). Connections hold authentication details such as the token URL, not the operation.
- C. The App Center listing description is customer-facing text, not call configuration.
- D. publisher holds the publisher's name and contact details only.

**Q340. (App Center and Extension Apps - Connections) [LOW]** Why must each connection in an extension app manifest have a unique name?

A. Docusign uses the name as the OAuth client ID
B. The name becomes the redirect URI for the authorization flow
C. The App Center shows it as the app's listing title
D. Actions refer to the connection by name through connectionsReference

**Answer:** D. Actions refer to the connection by name through connectionsReference

**Explanation:** Connection names are referenced again by actions through connectionsReference, so each must be unique.

**Why this answer and not the others:** D is right because the name is the key that actions use to find the connection. The trap is C: the App Center title comes from the app's name property, which also must be unique, but that is a different field. A and B confuse the connection name with OAuth parameters.

**Option notes:**
- A. The client ID is a separate auth parameter from the external provider.
- B. The redirect URI is not derived from the connection name.
- C (TRAP). The listing title comes from the app's name property, not a connection name.
- D. Correct. Actions use connectionsReference to point to a connection by its unique name.

**Q341. (App Center and Extension Apps - connectionsReference) [MEDIUM]** Two actions in one extension app call the same CRM with the same OAuth credentials. How should the manifest express this?

A. Copy the client ID and secret into each action definition
B. Create a separate extension app for each action
C. Define one connection and set both actions' connectionsReference to its name
D. List both actions in one extension's actionReferences

**Answer:** C. Define one connection and set both actions' connectionsReference to its name

**Explanation:** One connection can be shared: each action points to it by name with connectionsReference.

**Why this answer and not the others:** C is right because a single named connection can be reused by many actions. The trap is D: actionReferences groups the actions under an extension but provides no authentication. A duplicates credentials in the wrong place, and B adds needless apps.

**Option notes:**
- A. Actions do not store credentials; they reference a connection.
- B. Separate apps are unnecessary; one app can share a connection across actions.
- C. Correct. Both actions reference the same connection via connectionsReference.
- D (TRAP). actionReferences ties actions to an extension but does not supply auth.

**Q342. (App Center and Extension Apps - API proxy) [LOW]** In an extension app architecture, where does an API proxy sit?

A. Between the signer's browser and the Docusign signing page
B. Between Docusign and the third-party API, translating requests and responses
C. Inside the customer's Docusign account as an installed app
D. Between the Connect service and the developer's webhook listener

**Answer:** B. Between Docusign and the third-party API, translating requests and responses

**Explanation:** The proxy sits between Docusign and the external API, converting calls into the format each side expects.

**Why this answer and not the others:** B is right because the proxy mediates Docusign's calls to the third-party API. The trap is D: Connect delivers events to a listener and is not part of extension action calls. A concerns the signing UI, and C confuses the proxy with the installed app.

**Option notes:**
- A. The signer's browser is not part of the extension action call path.
- B. Correct. The proxy mediates and translates between Docusign and the external API.
- C. The installed app is configuration in the account; the proxy is infrastructure you host.
- D (TRAP). Connect listeners receive events; they do not sit in the extension action path.

**Q343. (App Center and Extension Apps - Firewall) [MEDIUM]** Which statement about extension app infrastructure is correct?

A. You host the action endpoints and must let Docusign's calls through your firewall
B. Docusign hosts your action code once the manifest is uploaded
C. Endpoints only need to be reachable from the developer's network
D. The firewall must be opened only for Connect event delivery

**Answer:** A. You host the action endpoints and must let Docusign's calls through your firewall

**Explanation:** The developer hosts the service behind the actions; Docusign calls it, so the firewall must allow Docusign's requests.

**Why this answer and not the others:** A is right because you host the endpoints and they must be reachable by Docusign. The trap is D: Connect is a separate webhook feature; extension actions are a different set of calls that also need firewall access. B is wrong because Docusign does not host your code, and C ignores that Docusign is the caller.

**Option notes:**
- A. Correct. Your service hosts the endpoints, and Docusign's calls must get through.
- B. The manifest only describes endpoints; your service still runs on your infrastructure.
- C. Docusign's servers, not the developer's network, make the calls.
- D (TRAP). Connect is separate; extension action calls also need to reach your endpoint.

**Q344. (App Center and Extension Apps - Data IO) [MEDIUM]** A Maestro workflow step must look up a customer's current account tier in an external system, then write the signed-agreement reference back after completion. Which extension type is designed for this structured record exchange?

A. File IO extension
B. Data IO extension
C. Connected Fields extension
D. Data Verification extension

**Answer:** B. Data IO extension

**Explanation:** Data IO extensions read and write structured records in external systems from Maestro workflows.

**Why this answer and not the others:** B is right because the step reads and writes records. The trap is A: File IO writes documents to storage, not structured fields back to a record. C is not supported in Maestro and verifies eSignature fields, and D checks standard data types.

**Option notes:**
- A (TRAP). File IO writes files, not structured record values.
- B. Correct. Data IO reads and writes structured records from a workflow.
- C. Connected fields verify eSignature field values and are not supported in Maestro.
- D. Data Verification validates values such as addresses; it does not read/write records.

**Q345. (App Center and Extension Apps - File IO) [MEDIUM]** What is Docusign's guidance on the file archive extension?

A. It is the recommended extension for all new File IO apps
B. It has been removed, and existing apps stopped working
C. Existing apps stay supported, but new apps should use file output cloud storage
D. It is available only to private extension apps

**Answer:** C. Existing apps stay supported, but new apps should use file output cloud storage

**Explanation:** Docusign continues to support existing apps that use file archive, but new apps should use the file output cloud storage extension.

**Why this answer and not the others:** C is right because file archive is legacy and file output cloud storage is for new apps. The trap is A: it reverses the recommendation. B overstates the change, since existing apps remain supported, and D invents a distribution restriction.

**Option notes:**
- A (TRAP). New apps should use file output cloud storage, not file archive.
- B. Existing file archive apps remain supported.
- C. Correct. File archive is legacy; use file output cloud storage for new apps.
- D. Distribution type does not determine whether file archive is available.

**Q346. (App Center and Extension Apps - Connected Fields) [LOW]** Besides a pass or fail result, what can a connected fields extension return to Docusign when a signer enters a value?

A. A new signing URL that redirects the signer
B. Custom guidance messages and autofill values for envelope fields
C. An instruction to void the envelope
D. A new routing order for the remaining recipients

**Answer:** B. Custom guidance messages and autofill values for envelope fields

**Explanation:** In its verification response, the system can supply custom messages guiding the user and autofill values based on known information.

**Why this answer and not the others:** B is right because connected fields support custom messages and autofill. The trap is A: signing URLs come from the eSignature API for embedded signing, not from a verification response. C and D are envelope management actions the extension cannot perform.

**Option notes:**
- A (TRAP). Signing URLs are created through the eSignature API, not returned by a verify action.
- B. Correct. The response can include custom messages and autofill values.
- C. Voiding is an eSignature operation, not part of the verification response.
- D. Routing order is envelope configuration, not a connected fields result.

**Q347. (App Center and Extension Apps - Data Verification) [HIGH]** What distinguishes Data Verification extensions from Connected Fields extensions?

A. Data Verification verifies specific standard types; Connected Fields verifies custom data against your system
B. Data Verification verifies custom data; Connected Fields verifies only standard types
C. Data Verification runs only in Maestro; Connected Fields runs only in Web Forms
D. Data Verification is only for private apps; Connected Fields is only for public apps

**Answer:** A. Data Verification verifies specific standard types; Connected Fields verifies custom data against your system

**Explanation:** Data verification extensions verify specific types (bank account, address, SSN, email, phone, FEIN); connected fields perform custom verification of any type against your system of record.

**Why this answer and not the others:** A is right because it states the standard-versus-custom split. The trap is B, which reverses the two. C misstates the extension points (both run at Add Fields and signing), and D invents a distribution rule.

**Option notes:**
- A. Correct. Standard types for Data Verification; custom data against your system for Connected Fields.
- B (TRAP). This reverses the roles of the two extension types.
- C. Both run at the eSignature Add Fields view and signing; connected fields are not in Maestro or Web Forms.
- D. Distribution type does not determine which extension type you can build.

**Q348. (API Authentication - Revoke consent) [HIGH]** A user revokes consent for a JWT-based integration through Manage Profile > Connected Apps. The integration still holds an access token issued 20 minutes ago. What happens?

A. The token keeps working, and the integration can keep minting new JWT tokens because JWT does not use consent
B. Docusign automatically re-prompts the user for consent on the next API call
C. The existing access token works until it expires; the next JWT exchange fails until consent is granted again
D. The existing access token is invalidated immediately and the next API call returns 401

**Answer:** C. The existing access token works until it expires; the next JWT exchange fails until consent is granted again

**Explanation:** Revoking consent invalidates refresh tokens and blocks new tokens, but live access tokens, including JWT ones, keep working until they expire.

**Why this answer and not the others:** C is right because revocation stops new tokens but does not kill live ones. The trap is D: it sounds like the secure outcome, but Docusign does not invalidate existing access tokens on revocation. A is wrong because JWT requires consent, and B is wrong because API calls never trigger a consent prompt.

**Option notes:**
- A. JWT requires consent; after revocation, new JWT token requests fail until consent is granted again.
- B. API calls never show a consent prompt; the user must be sent to /oauth/auth again.
- C. Correct. Live access tokens stay valid until they expire, but new tokens cannot be issued without consent.
- D (TRAP). Revocation does not end live access tokens; they stay valid until they expire.

**Q349. (API Authentication - Revoke consent) [HIGH]** Consent for an internal JWT integration was granted by an organization administrator for all users in the claimed domain. A user in that domain wants to revoke the app's access to their account. What is true?

A. The user must open a support case with Docusign
B. The integration key must be deleted to remove consent
C. The user can revoke it from Manage Profile > Connected Apps like any other app
D. An administrator must revoke it in Docusign Admin; reserved-domain users cannot revoke it individually

**Answer:** D. An administrator must revoke it in Docusign Admin; reserved-domain users cannot revoke it individually

**Explanation:** Admin-granted consent is revoked in Docusign Admin, and users in the organization's reserved domains cannot revoke it themselves.

**Why this answer and not the others:** D is right because the consent was granted by an admin for the reserved domain. The trap is C: Connected Apps is where users revoke individual consent, but not consent that an admin granted for their domain. A is unnecessary because revocation is self-service for the admin, and B removes the app for everyone.

**Option notes:**
- A. Revoking admin consent is self-service for the organization admin in Docusign Admin; no support case is needed.
- B. Deleting the key is unnecessary and affects every user; consent is revoked in Docusign Admin.
- C (TRAP). Connected Apps revocation applies to individual consent; reserved-domain users cannot revoke admin-granted consent.
- D. Correct. Admin-granted consent is revoked in Docusign Admin, not by individual reserved-domain users.

**Q350. (API Authentication - Consent) [HIGH]** An ISV sells a JWT-based integration to many customers. Some have Docusign Access Management with claimed domains; others do not. Which two design choices follow Docusign best practice? (Select two)

A. Always build an individual consent fallback for users or customers who cannot use admin consent
B. Ask each customer's admin to authorize the app from Docusign Admin > Connected Apps > Authorize Application
C. Offer admin consent for external applications (scope=openid plus admin_consent_scope) to customers with claimed domains
D. Skip consent by requesting the impersonation scope in the JWT assertion

**Answer:** A, C. Always build an individual consent fallback for users or customers who cannot use admin consent; Offer admin consent for external applications (scope=openid plus admin_consent_scope) to customers with claimed domains

**Explanation:** JWT best practice is to offer admin consent where possible (the external-app flow for ISV apps) and always fall back to individual consent, because admin consent needs Access Management and a claimed domain.

**Why this answer and not the others:** A and C are right because ISV apps use the external admin consent flow and still need an individual consent fallback. The trap is B: Authorize Application in Docusign Admin is real admin consent, but only for internal apps whose key the organization owns. D fails because impersonation itself must be consented to.

**Option notes:**
- A. Correct. Not every customer has Access Management and a claimed domain, so an individual consent path is required.
- B (TRAP). Authorize Application in Docusign Admin is for internal apps; an ISV's key is external to the customer's organization.
- C. Correct. ISV apps used by other organizations get admin consent through scope=openid with admin_consent_scope.
- D. Impersonation must itself be consented to; listing it in the assertion does not replace consent.

**Q351. (API Authentication - Consent) [MEDIUM]** A developer sends an org admin to /oauth/auth with scope=openid and admin_consent_scope=signature%20impersonation. After the admin consents, how does the app find out which organizations granted consent?

A. From the accounts list in the /oauth/userinfo response
B. From the coid claim in the ID token returned with the access token
C. From the state parameter echoed back to the redirect URI
D. By calling the eSignature Accounts:get endpoint

**Answer:** B. From the coid claim in the ID token returned with the access token

**Explanation:** Requesting openid returns an ID token whose coid claim lists the consenting organization IDs; this is the only way to get that list.

**Why this answer and not the others:** B is right because the coid claim in the ID token records the consenting organizations. The trap is A: /oauth/userinfo lists the user's accounts and base URIs, not the organizations that granted admin consent. C is an app-supplied CSRF value, and D returns account settings.

**Option notes:**
- A (TRAP). /oauth/userinfo returns the user's accounts and base URIs, not which organizations granted admin consent.
- B. Correct. The ID token's coid claim lists the consenting organization IDs.
- C. state is a CSRF value the app supplies; it carries no consent information from Docusign.
- D. Accounts:get returns eSignature account details, not the organizations that granted admin consent.

**Q352. (API Authentication - Scopes) [HIGH]** Which two statements about scopes in the admin consent for external applications flow are correct? (Select two)

A. The extended scope can be used with JWT Grant to get a refresh token
B. The scope parameter is set to openid
C. The Maestro aow_manage scope is implied by signature
D. The scopes granted for each org user go in admin_consent_scope (for example signature impersonation)

**Answer:** B, D. The scope parameter is set to openid; The scopes granted for each org user go in admin_consent_scope (for example signature impersonation)

**Explanation:** External admin consent uses scope=openid plus admin_consent_scope for the per-user scopes; extended only works with Authorization Code Grant, and API scopes such as aow_manage must be requested explicitly.

**Why this answer and not the others:** B and D are right because the external admin consent URL uses scope=openid and lists user scopes in admin_consent_scope. The trap is A: extended is a real scope, but it applies only to Authorization Code Grant, and JWT never returns a refresh token. C fails because Maestro scopes must be requested explicitly.

**Option notes:**
- A (TRAP). extended applies only to Authorization Code Grant; JWT Grant never returns a refresh token.
- B. Correct. External admin consent uses scope=openid, so the consenting organization IDs are returned in the ID token.
- C. Maestro scopes must be requested explicitly; signature does not imply aow_manage.
- D. Correct. admin_consent_scope holds the space-separated scopes granted for each user in the organization.

**Q353. (Go Live Process - API limits) [HIGH]** An account's integrations exceed the default hourly API call limit. What is the default limit, and what happens?

A. 3,000 calls per hour per account; further calls are blocked until the next hour
B. 1,000 calls per hour; extra calls are queued and processed the next hour
C. 3,000 calls per hour per integration key; the key is permanently disabled
D. There is no hourly limit, only a burst limit

**Answer:** A. 3,000 calls per hour per account; further calls are blocked until the next hour

**Explanation:** The default hourly limit is 3,000 calls per account, shared by all integrations; once exceeded, calls fail with a message that the maximum number of hourly API invocations has been exceeded until the hour resets.

**Why this answer and not the others:** A is right because the limit is per account and calls are blocked until the next hour. The trap is C: it has the right number, but the limit is per account, not per key, and the key is not disabled. B has the wrong number and wrongly queues calls, and D ignores the hourly limit.

**Option notes:**
- A. Correct. 3,000 calls per hour per account; excess calls are blocked until the hour resets.
- B. The default is 3,000, and excess calls are rejected, not queued.
- C (TRAP). The limit is shared per account, and exceeding it does not disable the key.
- D. Both an hourly limit and a burst limit apply.

**Q354. (Go Live Process - API limits) [HIGH]** Which two practices follow Docusign guidance for staying within API resource limits? (Select two)

A. Subscribe to Docusign Connect instead of polling envelope status
B. Split traffic across several integration keys to multiply the hourly limit
C. If polling is unavoidable, poll a given envelope at most once every 15 minutes
D. Retry failed calls immediately in a tight loop until they succeed

**Answer:** A, C. Subscribe to Docusign Connect instead of polling envelope status; If polling is unavoidable, poll a given envelope at most once every 15 minutes

**Explanation:** Use Connect instead of polling and, when you must poll, respect the once-per-15-minutes rule per envelope; also read the X-RateLimit headers and back off.

**Why this answer and not the others:** A and C are right because they reduce unnecessary calls. The trap is B: it would work if limits were per key, but the hourly limit is shared by all integrations on the account. D makes burst-limit violations worse; the guidance is to back off.

**Option notes:**
- A. Correct. Connect pushes status changes so the app does not need to poll.
- B (TRAP). The hourly limit is per account and shared, so extra keys add no capacity.
- C. Correct. Poll a given envelope no more than once every 15 minutes.
- D. Tight retry loops worsen burst violations; read X-RateLimit headers and back off.

**Q355. (Go Live Process - API limits) [LOW]** An app receives the error code Burst_APIInvocation_Envelope_Limit_Exceeded. What does it indicate?

A. The bulk send batch is too large
B. The envelope has too many recipients
C. The account exceeded its 3,000 calls per hour
D. Too many calls were made against one envelope in a short burst window

**Answer:** D. Too many calls were made against one envelope in a short burst window

**Explanation:** Docusign enforces hourly and burst limits on calls against a single envelope; exceeding the burst version returns Burst_APIInvocation_Envelope_Limit_Exceeded.

**Why this answer and not the others:** D is right because the code names a per-envelope burst limit. The trap is C: it is an API limit, but the account hourly limit returns a different message about hourly API invocations. A and B describe envelope content limits, not call rates.

**Option notes:**
- A. Bulk send size is not what this rate-limit code reports.
- B. Recipient count is unrelated to an API invocation limit.
- C (TRAP). The account hourly limit produces a different error about hourly API invocations.
- D. Correct. It signals too many calls against one envelope within the burst window.

**Q356. (Go Live Process - Efficiency score) [HIGH]** Where can an account admin see efficiency scores for each integration and the factors that lower them?

A. The envelope audit history
B. API Usage Center
C. The Connect failure log
D. The API Dashboard in Apps and Keys

**Answer:** B. API Usage Center

**Explanation:** The API Usage Center shows each app's efficiency score, and Actions > View Efficiency Score lists the negative factors with recommendations.

**Why this answer and not the others:** B is right because efficiency scores live in the API Usage Center. The trap is D: the API Dashboard is also a monitoring tool, but it shows request timelines and failed requests, not efficiency scores. A covers single envelopes, and C covers failed webhook deliveries.

**Option notes:**
- A. Audit history covers events on one envelope, not app-level efficiency.
- B. Correct. The API Usage Center shows efficiency scores and the factors behind them.
- C. The Connect failure log lists failed webhook deliveries.
- D (TRAP). The API Dashboard shows request history and failures (up to 90 days), not efficiency scores.

**Q357. (Go Live Process - Efficiency score) [MEDIUM]** Which three are factors in the API Usage Center efficiency score? (Select three)

A. Number of templates in the account
B. Average size of the documents in each envelope
C. Excessive envelope status requests
D. Excessive document retrieval requests
E. Excessive requests for nonexistent envelopes

**Answer:** C, D, E. Excessive envelope status requests; Excessive document retrieval requests; Excessive requests for nonexistent envelopes

**Explanation:** Efficiency factors include blocked calls, exceeded burst and hourly limits, excessive document retrieval, excessive envelope, status and recipient status requests, requests for nonexistent envelopes, excessive requests per envelope, and low call activity.

**Why this answer and not the others:** C, D and E are right because they are listed efficiency factors about wasteful calls. The trap is B: documents matter for document retrieval requests, but their size is not scored; only excessive retrieval calls are. A is an account content metric, not a call pattern.

**Option notes:**
- A. Template count is not an efficiency factor.
- B (TRAP). Document size is not scored; only excessive document retrieval requests are.
- C. Correct. Excessive envelope status requests (polling) lower the score.
- D. Correct. Excessive document retrieval requests lower the score.
- E. Correct. Requests for nonexistent envelopes lower the score.

**Q358. (Go Live Process - API limits) [MEDIUM]** An admin tries to raise the account's hourly API limit in the API Usage Center, but the Update Hourly Limit option is not available. Which two conditions could explain it? (Select two)

A. The integration key uses JWT Grant instead of Authorization Code Grant
B. Some apps on the account have unresolved efficiency issues
C. The account has a Connect configuration
D. The account plan does not include the limit management feature

**Answer:** B, D. Some apps on the account have unresolved efficiency issues; The account plan does not include the limit management feature

**Explanation:** Raising the limit yourself requires a plan with limit management, account admin rights, no Support-set limit, efficient apps, and enough call history.

**Why this answer and not the others:** B and D are right because both are listed prerequisites. The trap is C: Connect is part of API limit guidance, but using it is a best practice and never blocks a limit change. A is wrong because the OAuth flow is unrelated to limit management.

**Option notes:**
- A. The OAuth grant type has no effect on limit management.
- B. Correct. Flagged efficiency issues must be fixed before the limit can be raised.
- C (TRAP). Using Connect is recommended and does not block limit changes.
- D. Correct. Without limit management in the plan, the option is not available.

**Q359. (Go Live Process - API limits) [LOW]** An integration must reconcile envelope statuses after its Connect listener was down for two hours. What is the recommended way to catch up?

A. Call Envelopes:listStatusChanges with a from_date covering the outage, using overlapping time spans
B. Raise the hourly API limit and poll each envelope every minute
C. Delete and recreate the Connect configuration so it replays every event
D. Call Envelopes:get for every envelope ever sent

**Answer:** A. Call Envelopes:listStatusChanges with a from_date covering the outage, using overlapping time spans

**Explanation:** Docusign recommends Envelopes:listStatusChanges with overlapping time spans to catch up on status changes, instead of per-envelope polling.

**Why this answer and not the others:** A is right because one listStatusChanges call returns all envelopes changed in the window. The trap is C: it stays within Connect, but recreating a configuration does not replay past events. B breaks the once-per-15-minutes polling rule, and D wastes calls and risks hourly and per-envelope limits.

**Option notes:**
- A. Correct. listStatusChanges over the outage window, with overlapping spans, catches every change.
- B. Per-envelope polling is limited to once every 15 minutes regardless of the hourly limit.
- C (TRAP). Recreating a Connect configuration does not replay historical events.
- D. Fetching every envelope individually wastes calls and can hit hourly and per-envelope limits.

**Q360. (Docusign Connect - Security) [HIGH]** Which TWO mechanisms help a Connect listener verify that a webhook really came from Docusign and was not altered? (Select two)

A. HMAC signature validation using the X-DocuSign-Signature-1 header
B. Requiring the listener URL to use HTTP on port 80
C. Mutual TLS (client certificate) between Docusign and the listener
D. Checking that the envelopeId exists in the payload

**Answer:** A, C. HMAC signature validation using the X-DocuSign-Signature-1 header; Mutual TLS (client certificate) between Docusign and the listener

**Explanation:** Connect listener security options include HMAC signatures, mutual TLS, Basic authentication and OAuth 2.0 for Connect; HMAC and mutual TLS are the two listed here.

**Why this answer and not the others:** A and C are right because each cryptographically proves Docusign is the sender. The trap is D: checking the envelope ID feels like validation, but anyone who knows an ID can include it in a forged payload. B weakens security because production listeners must use HTTPS.

**Option notes:**
- A. Correct. Connect hashes the payload with the HMAC key; the listener recomputes and compares.
- B. Plain HTTP removes encryption; production Connect listeners must use HTTPS.
- C. Correct. Mutual TLS lets the listener verify Docusign's client certificate.
- D (TRAP). An envelope ID can be copied into a forged message; it proves nothing about the sender.

**Q361. (Docusign Connect - Retries) [HIGH]** Which TWO listener behaviors reduce Connect failures and the impact of retries? (Select two)

A. Return HTTP 500 for events the app does not care about
B. Return HTTP 200 quickly, then process the payload asynchronously
C. Call Envelopes:get for every event before acknowledging
D. Make processing idempotent so a redelivered event does no harm

**Answer:** B, D. Return HTTP 200 quickly, then process the payload asynchronously; Make processing idempotent so a redelivered event does no harm

**Explanation:** Connect retries failed deliveries, so the listener should acknowledge fast, queue the work and process idempotently.

**Why this answer and not the others:** B and D are right because a fast 200 prevents timeouts and idempotency makes redelivered events harmless. The trap is A: rejecting unwanted events seems tidy, but any non-2xx is a failure that triggers retries; acknowledge and ignore instead. C slows the response and wastes API calls before acknowledging.

**Option notes:**
- A (TRAP). Any non-2xx response is a failure that triggers retries; acknowledge and ignore instead.
- B. Correct. Slow processing causes timeouts that Connect treats as failures and retries.
- C. Extra synchronous API calls slow the acknowledgement and use API quota.
- D. Correct. Retries and republishes can deliver the same event more than once.

**Q362. (eSignature API - Composite templates) [HIGH]** A request uses compositeTemplates with one serverTemplate (sequence 1) and one inlineTemplate (sequence 2) that both define a signer for role 'Client'. Which TWO statements are correct? (Select two)

A. The server template's recipient data wins because server templates always take precedence.
B. Server and inline templates in the composite object are applied in order of their sequence numbers.
C. The inline template's recipient data overwrites the server template where they overlap.
D. Composite templates require envelope status created and cannot be sent directly.

**Answer:** B, C. Server and inline templates in the composite object are applied in order of their sequence numbers.; The inline template's recipient data overwrites the server template where they overlap.

**Explanation:** Templates in a composite object are applied in sequence order, and for attributes such as recipients and tabs, higher sequence values overwrite lower ones. So the inline template (sequence 2) supplies the runtime recipient for 'Client'.

**Why this answer and not the others:** B and C are right because attributes are layered by sequence and the last applied wins. The trap is A: server templates do win for documents when there is no document property (lowest sequence), but for recipient attributes the higher sequence overwrites. D is wrong because a composite template envelope can be created with status sent.

**Option notes:**
- A (TRAP). Server templates do not always win; for attributes, the higher sequence (here the inline template) overwrites.
- B. Correct. Server and inline templates are examined in order of their sequence values.
- C. Correct. Attributes with higher sequence values overwrite lower ones, so the inline recipient data applies.
- D. Composite template envelopes can be sent directly with status sent; created is only needed for a draft.

**Q363. (eSignature API - Embedded signing) [HIGH]** Which TWO are required for embedded signing with EnvelopeViews:createRecipient? (Select two)

A. The signer has a clientUserId set when the envelope is created.
B. The signing URL is emailed to the signer.
C. The envelope must be in created (draft) status.
D. The request includes a returnUrl where Docusign redirects after the signing session.

**Answer:** A, D. The signer has a clientUserId set when the envelope is created.; The request includes a returnUrl where Docusign redirects after the signing session.

**Explanation:** Embedded signing needs a signer created with clientUserId, then a createRecipient request with matching email, userName and clientUserId, an authenticationMethod and a returnUrl.

**Why this answer and not the others:** A and D are right because clientUserId marks the signer as embedded and returnUrl is a required part of the recipient view request. The trap is C: draft status is needed for embedded sending (createSender), but embedded signing needs a sent envelope. B is wrong because the app redirects the user to the URL itself; it is not emailed.

**Option notes:**
- A. Correct. clientUserId on the signer at creation is what makes embedded signing possible.
- B. The app redirects the user to the signing URL itself; Docusign does not email it.
- C (TRAP). A draft envelope is used for embedded sending; for embedded signing the envelope is sent.
- D. Correct. returnUrl is required in the createRecipient request so Docusign knows where to redirect.

**Q364. (eSignature Features and Web Forms - Recipient authentication) [HIGH]** A sender wants signers to enter a code the sender shares out of band (for example, reads out over the phone) before opening the documents. No extra cost or third-party check is wanted. Which method fits?

A. Phone authentication (code sent by SMS or call)
B. Knowledge-based authentication (KBA)
C. Access code authentication
D. Recording authenticationMethod on createRecipient

**Answer:** C. Access code authentication

**Explanation:** The clues are a sender-defined code shared out of band and no extra cost, which is access code authentication.

**Why this answer and not the others:** C is right because the access code is a sender-chosen secret shared out of band and carries no per-use fee. The trap is A: it also involves a code and a phone, but Docusign delivers that code and the method can cost extra. B fails because KBA uses third-party questions with fees, and D fails because it records rather than enforces.

**Option notes:**
- A (TRAP). Here Docusign sends the code by call or SMS, rather than the sender sharing it, and phone authentication can incur extra cost.
- B. KBA uses public-record questions from a third-party service (US only) and incurs per-use fees.
- C. Correct. An access code is set by the sender, shared out of band, and is the lightest enforced method with no per-use fee.
- D. authenticationMethod only records your app's authentication on the certificate; the signer is never asked for a code.

**Q365. (eSignature Features and Web Forms - Recipient authentication) [HIGH]** Which statement about ID verification (IDV) as a recipient authentication method is correct?

A. It needs the account's IDV workflowId, retrieved with IdentityVerifications:list (eSignature REST API v2.1)
B. It only records the authentication your app performed
C. It asks questions based on the signer's public records
D. It is enabled by default in every developer (demo) account

**Answer:** A. It needs the account's IDV workflowId, retrieved with IdentityVerifications:list (eSignature REST API v2.1)

**Explanation:** IDV verifies government photo IDs or eIDs, uses the account's workflowId from IdentityVerifications:list, and is available in REST v2.1.

**Why this answer and not the others:** A is right because IDV is configured with a workflowId obtained from IdentityVerifications:list. The trap is D: the other authentication methods are enabled in demo, but IDV is not and must be enabled by Docusign. B describes the record-only authenticationMethod and C describes KBA.

**Option notes:**
- A. Correct. IDV is applied with identityVerification.workflowId from IdentityVerifications:list in REST v2.1.
- B. That describes authenticationMethod on createRecipient, which is record-only; IDV actively verifies an ID.
- C. That describes KBA, not IDV, which checks government photo IDs or eIDs.
- D (TRAP). IDV is the one method not enabled by default in demo accounts; Docusign must enable it.

**Q366. (eSignature Features and Web Forms - Recipient authentication) [HIGH]** Which TWO statements correctly compare recipient authentication methods? (Select two)

A. Access code authentication checks a government-issued photo ID.
B. KBA verifies the signer with public-record questions (US only) and can be heavy for low-risk documents.
C. Phone authentication sends a code by call or SMS and uses a workflowId from IdentityVerifications:list.
D. IDV is enabled by default in demo accounts, like the other methods.

**Answer:** B, C. KBA verifies the signer with public-record questions (US only) and can be heavy for low-risk documents.; Phone authentication sends a code by call or SMS and uses a workflowId from IdentityVerifications:list.

**Explanation:** Choose authentication by risk: access code is lightest, phone adds a second factor by call or SMS, KBA uses US public-record questions, and IDV checks ID documents.

**Why this answer and not the others:** B and C are right because they correctly describe KBA and phone authentication. The trap is D: all methods except IDV are enabled in demo, so it is close to true but wrong for IDV. A fails because it attributes the IDV photo ID check to the access code.

**Option notes:**
- A. An access code is a sender-defined secret shared out of band; checking a government photo ID is IDV.
- B. Correct. KBA uses public-record questions, is US only, and is often too heavy for low-risk documents.
- C. Correct. Phone authentication delivers a code by call or SMS and is configured with an identityVerification workflowId.
- D (TRAP). IDV is the exception: it is not enabled by default in demo and must be enabled by Docusign.

**Q367. (eSignature Features and Web Forms - Recipient authentication) [HIGH]** An app authenticates users with its own SSO before embedded signing and wants that fact recorded on the certificate of completion. What should it do?

A. Add an identityVerification workflowId to the recipient
B. Set authenticationMethod (for example SingleSignOn_SAML) in the EnvelopeViews:createRecipient request
C. Add an access code to the recipient
D. Enable KBA on the recipient

**Answer:** B. Set authenticationMethod (for example SingleSignOn_SAML) in the EnvelopeViews:createRecipient request

**Explanation:** For embedded signing, authenticationMethod on createRecipient records the app's own authentication on the certificate, which supports non-repudiation.

**Why this answer and not the others:** B is right because authenticationMethod is the field that records your app's authentication on the certificate. The trap is A: identityVerification is the field for enforcing identity, so it looks right, but it adds a Docusign check rather than recording SSO. C and D fail because they add new challenges instead of recording the existing one.

**Option notes:**
- A (TRAP). This makes Docusign run its own verification; it does not record the SSO check your app already did.
- B. Correct. authenticationMethod records (but does not enforce) the method your app used, and it appears on the certificate of completion.
- C. An access code adds a new Docusign challenge instead of recording the SSO login.
- D. KBA adds a Docusign-run question challenge; it does not record your app's SSO.

**Q368. (eSignature Features and Web Forms - Standards-based signatures) [MEDIUM]** A European customer needs signers to apply an EU Qualified Electronic Signature (QES) through a QTSP signature provider returned by AccountSignatureProviders:list. What must the Envelopes:create request include for the signer?

A. Phone authentication with an SMS code
B. An access code only
C. A brandId for an EU brand
D. recipientSignatureProviders naming the QES signature provider

**Answer:** D. recipientSignatureProviders naming the QES signature provider

**Explanation:** Standards-based signatures such as QES are requested with recipientSignatureProviders on the signer, naming the provider from AccountSignatureProviders:list.

**Why this answer and not the others:** D is right because recipientSignatureProviders selects the QTSP provider that applies the QES. The trap is A: an SMS one-time password can be a signature provider option, but phone authentication on its own only gates access. B and C fail because an access code and a brand do not change the signature standard.

**Option notes:**
- A (TRAP). Phone authentication controls access to the envelope; it does not produce a qualified signature.
- B. An access code only gates access; it does not change the signature type.
- C. A brand changes appearance and redirects, not the signature standard.
- D. Correct. SBS is requested by adding recipientSignatureProviders (signatureProviderName plus options) to at least one signer.

**Q369. (eSignature Features and Web Forms - Standards-based signatures) [MEDIUM]** Which TWO statements about Standards-Based Signatures (SBS) are correct? (Select two)

A. A downloaded combined PDF is not digitally signed.
B. Advanced Correct can freely add or delete fields after the first signature.
C. AccountSignatureProviders:list returns the IDV workflow IDs.
D. Some features, such as Markup, Notary and attachment by fax, are not compatible with SBS.

**Answer:** A, D. A downloaded combined PDF is not digitally signed.; Some features, such as Markup, Notary and attachment by fax, are not compatible with SBS.

**Explanation:** SBS changes feature behavior: combined PDFs are unsigned, no field add/delete after the first signature, watermarks become annotations, and some features are incompatible.

**Why this answer and not the others:** A and D are right because they match the documented SBS limitations. The trap is C: it names a real SBS call, but that call lists signature providers, not IDV workflows. B fails because Advanced Correct is restricted after the first signature.

**Option notes:**
- A. Correct. With SBS, the combined PDF download is not digitally signed; the individual documents carry the signatures.
- B. With SBS, Advanced Correct cannot add or delete fields after the first signature.
- C (TRAP). AccountSignatureProviders:list returns signature providers; IDV workflow IDs come from IdentityVerifications:list.
- D. Correct. Markup, Notary, attachment by fax, concatenated signer attachments and legacy digital signatures are not compatible with SBS.

**Q370. (eSignature Features and Web Forms - Web form configuration type) [HIGH]** A team wants a web form that only collects survey data into their database. No signature or envelope is needed. Which configuration type fits?

A. Template-based web form
B. Template-based web form delivered as an embedded instance
C. Standalone web form
D. Template-based web form delivered as a remote instance

**Answer:** C. Standalone web form

**Explanation:** Web Forms has two configuration types: template-based (an envelope is generated) and standalone (no envelope, data collection only).

**Why this answer and not the others:** C is right because standalone configurations collect data without an envelope. The trap is A: template-based forms are the common choice, but they always produce an envelope. B and D fail because embedded and remote are delivery modes and both template-based modes generate an envelope.

**Option notes:**
- A (TRAP). A template-based configuration generates an envelope after submission, which the team does not want.
- B. Embedding changes how the form is shown, but a template-based configuration still generates an envelope when the first user submits.
- C. Correct. A standalone configuration is for data collection only and never creates an envelope.
- D. A remote template-based instance generates an envelope when createInstance is processed.

**Q371. (eSignature Features and Web Forms - Web form configuration type) [HIGH]** Which TWO statements about web form instances created from a STANDALONE configuration are correct? (Select two)

A. Envelope status should be tracked with a Connect listener.
B. Submitted values are read from formValues in the Instances:getInstance response.
C. authenticationMethod and assertionId can record recipient authentication on the certificate.
D. No envelope is generated, so the envelopes array in Instances:getInstance is empty.

**Answer:** B, D. Submitted values are read from formValues in the Instances:getInstance response.; No envelope is generated, so the envelopes array in Instances:getInstance is empty.

**Explanation:** Standalone means no envelope: track instance status (INITIATED, INPROGRESS, SUBMITTED, EXPIRED, FAILED) and read formValues from getInstance.

**Why this answer and not the others:** B and D are right because a standalone instance has no envelope and its data lives in formValues. The trap is A: Connect is the usual way to track envelopes, but a standalone form has none. C fails because authentication record fields are supported only for embedded template-based forms.

**Option notes:**
- A (TRAP). There is no envelope for a standalone form, so there is no envelope status for Connect to report; use the instance status instead.
- B. Correct. getInstance returns formValues with the submitted data and the instance status.
- C. These record fields only work for embedded signing of template-based forms, not standalone configurations.
- D. Correct. Standalone configurations never create an envelope, so envelopes[] is empty.

**Q372. (eSignature Features and Web Forms - Web form configuration type) [HIGH]** For a TEMPLATE-BASED web form delivered as an EMBEDDED instance, when is the envelope generated?

A. When the first user submits the web form instance
B. Never; embedded instances do not create envelopes
C. When Instances:createInstance is called
D. Only after the web form configuration is republished

**Answer:** A. When the first user submits the web form instance

**Explanation:** Remote instance: the envelope is generated when createInstance is processed. Embedded instance: it is generated when the first user submits.

**Why this answer and not the others:** A is right because embedded template-based instances create the envelope on first submission. The trap is C: that is exactly the remote-instance timing. B confuses embedded with standalone, and D describes no real trigger.

**Option notes:**
- A. Correct. For embedded template-based instances, the envelope is created when the first user submits.
- B. That describes standalone configurations; template-based forms do generate an envelope.
- C (TRAP). That is the timing for remote instances, not embedded ones.
- D. Republishing a configuration does not generate envelopes for instances.

**Q373. (eSignature Features and Web Forms - Web Forms embedding) [HIGH]** Which TWO are required or valid when creating an EMBEDDED web form instance with Instances:createInstance? (Select two)

A. sendOption 'now' with a recipients array of roleName entries.
B. clientUserId, which identifies the user in your system (max 100 characters).
C. formValues, to prefill known data from your system of record.
D. An envelopeId from a previously sent envelope.

**Answer:** B, C. clientUserId, which identifies the user in your system (max 100 characters).; formValues, to prefill known data from your system of record.

**Explanation:** Embedded instances need clientUserId and can use formValues to prefill; remote instances use sendOption and recipients with roleName.

**Why this answer and not the others:** B and C are right because clientUserId is required for embedding and formValues is a valid prefill. The trap is A: it is a valid createInstance pattern, but for remote instances. D fails because an instance is not built from an existing envelope.

**Option notes:**
- A (TRAP). sendOption with recipients by roleName is used for remote instances, which email participants.
- B. Correct. clientUserId is required for embedded instances and is limited to 100 characters.
- C. Correct. formValues prefill fields, using field names from Configurations:getForm.
- D. createInstance does not take an existing envelopeId; any envelope is generated by the web form itself.

**Q374. (eSignature Features and Web Forms - ID Evidence) [MEDIUM]** A compliance team needs the ID evidence (for example, scanned ID images) collected during a signer's ID verification. Which approach fits?

A. Download the certificate of completion, which contains the ID images
B. Use the ID Evidence API to retrieve the retained evidence for the recipient after verification
C. Query the Agreement Manager API for the agreement
D. Read the Connect envelope-completed payload

**Answer:** B. Use the ID Evidence API to retrieve the retained evidence for the recipient after verification

**Explanation:** Retrieving ID data from an IDV event is done with the ID Evidence API, once the account is configured to retain that data.

**Why this answer and not the others:** B is right because the ID Evidence API is built to retrieve retained IDV evidence. The trap is A: the certificate is the usual audit artifact, but it does not include the ID images. C and D fail because they return agreement data and envelope events, not identity evidence.

**Option notes:**
- A (TRAP). The certificate records events and authentication used, but it does not contain the retained ID images.
- B. Correct. The ID Evidence API retrieves the IDV data the admin has configured the account to retain, such as ID images.
- C. Agreement Manager returns agreements and extracted agreement data, not identity evidence.
- D. The envelope-completed event reports envelope status, not ID evidence.

**Q375. (Agreement Manager API - AI / RAG) [MEDIUM]** A team wants an internal AI assistant to answer questions about signed contracts using retrieval-augmented generation (RAG). Which TWO steps fit an Agreement Manager API design? (Select two)

A. Retrieve agreements and their AI-extracted fields (parties, dates, provisions) through the Agreement Manager API.
B. Index only AI summaries and drop agreement IDs to keep the index small.
C. Index the agreement data (and documents) in the AI system's retrieval store, keyed by agreement ID.
D. Index only eSignature envelope status so answers stay current.

**Answer:** A, C. Retrieve agreements and their AI-extracted fields (parties, dates, provisions) through the Agreement Manager API.; Index the agreement data (and documents) in the AI system's retrieval store, keyed by agreement ID.

**Explanation:** The RAG objective is to pull extracted agreement data through the API and index it in the AI system's retrieval store, keyed by agreementId so answers can cite their source agreement.

**Why this answer and not the others:** A and C are right because RAG needs the extracted data as source content and an index keyed by agreementId for traceability. The trap is B: summaries can be useful content, but dropping agreement IDs means answers can no longer be traced back to the source agreement. D indexes envelope status, which says nothing about contract terms the assistant must answer questions about.

**Option notes:**
- A. Correct. The Agreement Manager API supplies the extracted agreement data the assistant retrieves from.
- B (TRAP). Removing agreement IDs breaks traceability, so answers cannot cite their source agreement.
- C. Correct. Indexing by agreement ID lets the AI system retrieve and cite the right agreement.
- D. Envelope status does not contain the contract terms that the assistant needs to answer questions.

**Q376. (Agreement Manager API - Legacy import) [MEDIUM]** Which TWO statements about bringing legacy agreements into Agreement Manager are correct? (Select two)

A. Legacy (non-Docusign) agreements can be bulk imported, and AI extraction runs on them too.
B. Legacy agreements must first be re-signed through eSignature.
C. Imported legacy agreements are stored but skipped by AI extraction.
D. After import, extracted data can be reviewed and corrected before it is relied on downstream.

**Answer:** A, D. Legacy (non-Docusign) agreements can be bulk imported, and AI extraction runs on them too.; After import, extracted data can be reviewed and corrected before it is relied on downstream.

**Explanation:** Agreement Manager supports bulk import of legacy agreements, AI extraction runs on imported agreements, and the extracted values should be reviewed and corrected before downstream use.

**Why this answer and not the others:** A and D are right because import feeds AI extraction, and a review step validates the results. The trap is C: imported agreements are stored, but they are not excluded from extraction, since bringing them under AI extraction is the point of the import. B is wrong because executed agreements are imported as they are, without re-signing.

**Option notes:**
- A. Correct. Bulk-imported legacy agreements go through AI extraction like completed envelopes.
- B. Signed legacy agreements are imported as they are; re-signing is not required.
- C (TRAP). False; AI extraction runs on imported agreements as well.
- D. Correct. Extractions should be reviewed and corrected, for example in an external review step, before downstream use.

**Q377. (Workflow Builder and Workflow API - Workflow instance management) [HIGH]** A custom portal triggered a Maestro workflow and stored the returned instance ID. How should it show the user the workflow's current status?

A. Call pauseNewWorkflowInstances.
B. Call getWorkflowTriggerRequirements.
C. Call Envelopes:get with the instance ID.
D. Call getWorkflowInstance (GET /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}).

**Answer:** D. Call getWorkflowInstance (GET /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}).

**Explanation:** getWorkflowInstance returns a single instance's details, including status, start and end times and started_by.

**Why this answer and not the others:** D is right because it reads the status of one instance by its ID. The trap is C: Envelopes:get returns status, but only for eSignature envelopes, not workflow instances. A blocks new instances, and B returns the trigger URL and input schema.

**Option notes:**
- A. Stops new instances from starting; it does not report status.
- B. Returns trigger URL and input schema, not instance status.
- C (TRAP). An eSignature call for envelopes; a workflow instance ID is not an envelope ID.
- D. Correct. Returns the instance's status, timing and started_by.

**Q378. (Workflow Builder and Workflow API - Workflow instance management) [HIGH]** Which scope must an access token include, in addition to signature, to call Maestro workflow management endpoints such as trigger, pause, resume and cancel?

A. aow_manage
B. impersonation
C. signature only
D. extended

**Answer:** A. aow_manage

**Explanation:** Maestro uses the same OAuth tokens as eSignature, but you must request the signature scope plus Maestro scopes, such as aow_manage for these endpoints.

**Why this answer and not the others:** A is right because aow_manage is the Maestro scope for these calls. The trap is C: signature is required, but on its own it does not authorize Maestro endpoints. B is for JWT user impersonation, and D extends refresh token life.

**Option notes:**
- A. Correct. aow_manage is required for Maestro workflow management calls.
- B. impersonation is needed for JWT Grant, not for Maestro permissions.
- C (TRAP). signature is required but not sufficient for the Maestro API.
- D. extended lengthens refresh token life; it grants no Maestro access.

**Q379. (Workflow Builder and Workflow API - Workflow instance management) [HIGH]** Which TWO statements about Maestro instance management are correct? (Select two)

A. Pausing a workflow also pauses its running instances until it is resumed.
B. pauseNewWorkflowInstances stops new instances from being created; running instances continue.
C. cancelWorkflowInstance stops a specific running instance so it runs no further steps.
D. Instance management endpoints use the eSignature base path /restapi/v2.1.

**Answer:** B, C. pauseNewWorkflowInstances stops new instances from being created; running instances continue.; cancelWorkflowInstance stops a specific running instance so it runs no further steps.

**Explanation:** Pausing affects only new instances; active instances keep running. Canceling stops one instance: data collected so far is kept, but no further steps run.

**Why this answer and not the others:** B and C are right because pause blocks new instances and cancel stops one instance. The trap is A: it sounds natural that pausing freezes everything, but running instances continue. D is wrong because Maestro uses https://api-d.docusign.com/v1 (demo) or https://api.docusign.com/v1 (production).

**Option notes:**
- A (TRAP). Running instances continue when a workflow is paused; only new instances are blocked.
- B. Correct. Pause blocks new instances; active instances continue.
- C. Correct. Cancel stops one instance; collected data is kept and no further steps run.
- D. Maestro uses the api-d.docusign.com/v1 or api.docusign.com/v1 base path.

**Q380. (Workflow Builder and Workflow API - API trigger) [HIGH]** Which TWO steps are needed before an app can trigger a published Maestro workflow by API? (Select two)

A. Create an eSignature envelope with status 'sent'.
B. Configure an envelope-level Connect webhook.
C. Call GetWorkflowTriggerRequirements to get the trigger URL and required inputs.
D. Get an access token that includes the required Maestro scope (aow_manage).

**Answer:** C, D. Call GetWorkflowTriggerRequirements to get the trigger URL and required inputs.; Get an access token that includes the required Maestro scope (aow_manage).

**Explanation:** The flow is: get a token with the signature and aow_manage scopes, call GetWorkflowTriggerRequirements for the trigger URL and input schema, then call TriggerWorkflow with the inputs.

**Why this answer and not the others:** C and D are right because the app needs authorization and the trigger requirements before calling TriggerWorkflow. The trap is A: workflows often send envelopes, but the workflow creates them in its own steps; no envelope is needed beforehand. B is optional monitoring and not a prerequisite for triggering.

**Option notes:**
- A (TRAP). No envelope is needed; the workflow's own steps send documents.
- B. Connect is optional monitoring, not a trigger prerequisite.
- C. Correct. Provides the trigger URL and the required trigger inputs.
- D. Correct. Maestro calls need a token that includes aow_manage.

**Q381. (Workflow Builder and Workflow API - Publishing) [HIGH]** A Maestro workflow publish call fails its pre-publication check because of consent errors. What should the developer do?

A. Repeat the call with isPreRunCheck=true without granting consent.
B. Open the URL in the consentUrl field, have the user grant consent, then repeat the publish call.
C. Recreate the workflow from scratch.
D. Switch the integration to Implicit Grant.

**Answer:** B. Open the URL in the consentUrl field, have the user grant consent, then repeat the publish call.

**Explanation:** Publishing runs an automated check. If it fails for consent, the response includes a consentUrl: grant consent there, then publish again.

**Why this answer and not the others:** B is right because consent errors are fixed by granting consent through the consentUrl. The trap is A: isPreRunCheck relates to the pre-publication check, but rerunning the check does not grant the missing consent, and the real publish is repeated without isPreRunCheck=true. C does not address consent, and D changes the OAuth flow without fixing anything.

**Option notes:**
- A (TRAP). Rerunning the check without granting consent fails again.
- B. Correct. Grant consent via consentUrl, then publish again.
- C. Recreating the workflow does not grant the missing consent.
- D. Changing the grant type does not resolve a missing consent.

**Q382. (App Center and Extension Apps - Extension selection) [HIGH]** A lender must confirm during signing that the signer is the owner (or an authorized signatory) of the US bank account they enter. Which extension fits?

A. Data IO
B. File output cloud storage
C. Bank account verification (Verify.Version3.BankAccount)
D. Bank account owner verification (Verify.Version1.BankAccountOwner)

**Answer:** D. Bank account owner verification (Verify.Version1.BankAccountOwner)

**Explanation:** Bank account owner verification confirms the signer owns or is an authorized signatory on the account (US ABA routing numbers only).

**Why this answer and not the others:** D is right because the requirement is ownership, not just validity. The trap is C: bank account verification checks the account itself, not that the signer owns it. A and B are workflow extensions for records and files.

**Option notes:**
- A. Data IO reads/writes records in Maestro; it does not verify ownership at signing.
- B. File output cloud storage writes documents to storage.
- C (TRAP). Bank account verification validates the account, not the signer's ownership.
- D. Correct. Bank account owner verification checks ownership or signatory status.

**Q383. (App Center and Extension Apps - Extension selection) [MEDIUM]** Which TWO data verification extensions can also be used in Web Forms, not only in the eSignature Add Fields view and signing? (Select two)

A. Email address verification
B. Business FEIN verification
C. Phone verification
D. SSN verification

**Answer:** A, C. Email address verification; Phone verification

**Explanation:** Email and phone verification extend into Web Forms; the other verification types target the eSignature Add Fields view and signing only.

**Why this answer and not the others:** A and C are right because email and phone verification are the Web Forms-enabled types. The trap is D: SSN verification is a common identity check but is limited to Add Fields and signing. B is likewise limited to eSignature.

**Option notes:**
- A. Correct. Email verification is also available in Web Forms.
- B. FEIN verification runs only at the eSignature Add Fields view and signing.
- C. Correct. Phone verification is also available in Web Forms.
- D (TRAP). SSN verification runs only at the eSignature Add Fields view and signing.

**Q384. (App Center and Extension Apps - Extension selection) [HIGH]** A new extension app must save completed documents to a customer's cloud storage from a Maestro workflow. Which extension should it implement?

A. Connected fields
B. File output cloud storage
C. File archive
D. Postal address verification

**Answer:** B. File output cloud storage

**Explanation:** File IO includes file output cloud storage (recommended for new apps) and the legacy file archive extension.

**Why this answer and not the others:** B is right because file output cloud storage is the File IO extension for new apps. The trap is C: file archive also stores files, but it is legacy and new apps should not use it. A and D verify field values rather than store files.

**Option notes:**
- A. Connected fields verify field values; they do not store files.
- B. Correct. File output cloud storage is the File IO extension for new apps.
- C (TRAP). File archive is legacy; new apps should use file output cloud storage.
- D. Postal address verification checks addresses during preparation and signing.

**Q385. (App Center and Extension Apps - Connected Fields) [HIGH]** Which TWO actions does Docusign call on a connected fields extension app when a connection is created or refreshed? (Select two)

A. Get Type Names (DataIO.Version6.GetTypeNames)
B. Verify (ConnectedFields.Version1.Verify)
C. Get Type Definitions (DataIO.Version6.GetTypeDefinitions)
D. CreateRecord

**Answer:** A, C. Get Type Names (DataIO.Version6.GetTypeNames); Get Type Definitions (DataIO.Version6.GetTypeDefinitions)

**Explanation:** On connect or refresh, Docusign calls Get Type Names then Get Type Definitions to load the Concerto data model. Verify runs later when the signer fills in the fields.

**Why this answer and not the others:** A and C are right because type discovery happens at connect or refresh. The trap is B: Verify is a connected fields action, but it runs when the signer completes the fields, not at connection time. D is a Data IO record action.

**Option notes:**
- A. Correct. Get Type Names is called on connect or refresh.
- B (TRAP). Verify runs at signing when the required fields are completed, not when connecting.
- C. Correct. Get Type Definitions is called after Get Type Names.
- D. CreateRecord is a Data IO action for writing records.

**Q386. (App Center and Extension Apps - Connected Fields) [HIGH]** How can an integration programmatically receive the verification results from connected fields in an envelope?

A. Poll Envelopes:get every minute
B. Use a Connect listener subscribed to the extension-executed event (JSON SIM only)
C. Use the legacy XML Connect format
D. Call TabInfo:GetConnectedFieldsTabGroups after signing

**Answer:** B. Use a Connect listener subscribed to the extension-executed event (JSON SIM only)

**Explanation:** Verification results arrive through the Connect extension-executed event, which requires the JSON SIM event model; they also appear in envelope history and the certificate of completion.

**Why this answer and not the others:** B is right because extension-executed events deliver the results. The trap is D: GetConnectedFieldsTabGroups returns field definitions for building envelopes, not results. A is discouraged polling, and C is wrong because the event is JSON SIM only.

**Option notes:**
- A. Polling is discouraged and is not how results are delivered.
- B. Correct. Connect extension-executed events (JSON SIM) deliver the results.
- C. The extension-executed event is available only in the JSON SIM model, not legacy XML.
- D (TRAP). This endpoint returns connected field definitions, not verification results.

**Q387. (App Center and Extension Apps - Connected Fields) [MEDIUM]** Which TWO steps are needed to send an envelope with connected fields through the API? (Select two)

A. Call TabInfo:GetConnectedFieldsTabGroups to get the installed apps' connected field definitions
B. Create the envelope with the Web Forms API
C. Add the connected fields as a Maestro workflow step
D. Put that data in each tab's extensionData property in the Envelopes:create request

**Answer:** A, D. Call TabInfo:GetConnectedFieldsTabGroups to get the installed apps' connected field definitions; Put that data in each tab's extensionData property in the Envelopes:create request

**Explanation:** Get the definitions with TabInfo:GetConnectedFieldsTabGroups, build tabs with extensionData, then call Envelopes:create; verification happens when the recipient enters data.

**Why this answer and not the others:** A and D are right because they are the Connected Fields API sending flow. The trap is C: connected fields are not supported in Maestro. B uses the wrong API; the envelope is created with the eSignature Envelopes:create call.

**Option notes:**
- A. Correct. This returns the connected field definitions needed to build the tabs.
- B. Envelopes with connected fields are created with eSignature Envelopes:create, not the Web Forms API.
- C (TRAP). Connected fields are not supported in Maestro.
- D. Correct. Each tab carries its connected field data in extensionData.

**Q388. (App Center and Extension Apps - Public vs private) [HIGH]** A bank builds a connected fields extension that verifies values against its own internal customer database. How should it usually be distributed?

A. As a public App Center listing for all Docusign customers
B. As a public app restricted with publicationRegions
C. As a private extension app available only to the bank's own accounts
D. Through a Connect configuration on the bank's account

**Answer:** C. As a private extension app available only to the bank's own accounts

**Explanation:** Docusign notes that connected fields extensions against internal systems are a typical private extension app use case, published only for specific accounts.

**Why this answer and not the others:** C is right because verification against the bank's internal database is org-specific, the classic private-app case. The trap is A: publishing publicly would offer an app that no other customer can use. B still exposes it by region rather than by organization, and D (Connect) is an event webhook, not an extension distribution method.

**Option notes:**
- A (TRAP). Other customers cannot use the bank's internal database, so public distribution makes no sense.
- B. Regions restrict geography only; other customers in the region could still install the app.
- C. Correct. Org-specific connected fields verification is a typical private extension app.
- D. Connect delivers event notifications; it is not a way to distribute an extension app.

**Q389. (App Center and Extension Apps - Register, test, publish) [HIGH]** Which THREE belong to the process of building and releasing an extension app? (Select three)

A. Submit the app for review, then publish it publicly or share it privately
B. Request a go-live review for an eSignature integration key
C. Add the app to a PowerForm
D. Run connection and extension tests in the Developer Console
E. Register the app in the Developer Console (form-based or manifest)

**Answer:** A, D, E. Submit the app for review, then publish it publicly or share it privately; Run connection and extension tests in the Developer Console; Register the app in the Developer Console (form-based or manifest)

**Explanation:** Register (form or manifest), test (Console connection/extension tests plus functional tests), then submit for review and publish (public) or share with accounts (private).

**Why this answer and not the others:** A, D and E are right because they are register, test and publish. The trap is B: go-live is the eSignature API path for integration keys, not extension apps. C is unrelated; PowerForms are self-service signing links.

**Option notes:**
- A. Correct. After testing, the app is submitted for review and published or privately shared.
- B (TRAP). Go-live applies to eSignature integration keys, not extension apps.
- C. PowerForms are self-service signing links, unrelated to extension app release.
- D. Correct. Connection and extension tests run in the Developer Console.
- E. Correct. Registration happens in the Developer Console by form or manifest.

**Q390. (App Center and Extension Apps - Infrastructure) [HIGH]** Which TWO are infrastructure considerations when hosting an extension app's backend service? (Select two)

A. The service must poll Docusign every minute for work
B. Authorization for Docusign's calls must be configured (Authorization Code or Client Credentials)
C. The endpoint must be reachable over HTTPS by Docusign, directly or through an API proxy
D. The service must run inside the customer's Docusign account

**Answer:** B, C. Authorization for Docusign's calls must be configured (Authorization Code or Client Credentials); The endpoint must be reachable over HTTPS by Docusign, directly or through an API proxy

**Explanation:** Plan for reachability (HTTPS, firewall allow-listing or an API proxy) and for the OAuth 2.0 grant Docusign uses to call your service.

**Why this answer and not the others:** B and C are right because Docusign must both reach and be authorized to call your service. The trap is D: the app is installed in the customer's account, but the service itself runs on your infrastructure. A is wrong because Docusign calls the service; the service does not poll.

**Option notes:**
- A. Docusign calls the service when needed; polling is not part of the model.
- B. Correct. The connection's OAuth grant must be configured for Docusign's calls.
- C. Correct. Docusign must be able to reach the endpoint over HTTPS.
- D (TRAP). Installing the app in an account does not run your backend inside Docusign.


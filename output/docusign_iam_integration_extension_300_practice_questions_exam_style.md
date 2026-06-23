# Certified Docusign IAM Integration & Extension Developer - Exam-Style Practice Questions

This version uses longer scenario-based wording for most questions and mixes domains in the default order.

**Q1. (API Authentication - OAuth flow selection)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a server-side portal can store a client secret and each employee signs in interactively. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- B. Public Authorization Code Grant with PKCE can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Confidential Authorization Code Grant.
- D. Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q2. (Go Live Process - Go-live setup)** Mateo, a DevOps engineer at a procurement shared-services group, is building a self-service portal for internal teams and external customers. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, a developer promotes an integration key from demo to production. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which configuration commonly must be recreated in production?

A. Redirect URIs and secret keys
B. Completed demo envelopes
C. Envelope IDs
D. Connect event logs

**Answer:** A. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Option notes:**
- A. Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- B. Completed demo envelopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- C. Envelope IDs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- D. Connect event logs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q3. (Docusign Connect - Envelope-level Connect)** Priya, a platform engineer at a legal operations team, is replacing a manual agreement process with a Docusign IAM integration. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a single high-value envelope needs a callback URL different from account-level settings. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Option notes:**
- A. Create a Web Form instance can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- B. Use Workflow Builder only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- C. Set the envelope status to created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- D. The eventNotification object configures per-envelope Connect callbacks.

**Q4. (eSignature API - Envelope create)** Grace, a product owner at a university financial-aid office, is automating high-volume agreement work while keeping auditability intact. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, an integration needs to send an envelope for signature immediately. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- B. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- D. Status sent sends the envelope; created saves it as a draft.

**Q5. (eSignature Features and Web Forms - Web Forms embedding)** Elena, an implementation consultant at a partner-built customer portal, is automating high-volume agreement work while keeping auditability intact. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, a custom website needs to render a Docusign Web Form instance inline. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What client-side component is used with the instance URL?

A. EnvelopeViews:createRecipient
B. Connect JSON SIM
C. Workflow start link only
D. Docusign JS client SDK

**Answer:** D. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Option notes:**
- A. EnvelopeViews:createRecipient can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- B. Connect JSON SIM can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- C. Workflow start link only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- D. Docusign JS renders Web Form instances in the host page.

**Q6. (Agreement Manager API - Agreement data)** Mateo, a DevOps engineer, is reviewing a Docusign implementation for a procurement shared-services group. The relevant requirement is that a custom app needs structured extracted data for a specific agreement. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Option notes:**
- A. Workflow trigger requirements can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- B. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- C. Agreements:getAgreement retrieves agreement data for a specific agreement.
- D. Envelopes:create can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q7. (Workflow Builder and Workflow API - Workflow steps)** Amir, a workflow automation engineer at a regional healthcare provider, is building a self-service portal for internal teams and external customers. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow must collect form data before sending a document for signature. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which step order best fits?

A. Collect Data with Web Forms, then Get Signatures
B. Get Signatures, then collect data
C. Archive first, then start
D. Void envelope, then collect data

**Answer:** A. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Option notes:**
- A. Workflow step order should match the business process.
- B. Get Signatures, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- C. Archive first, then start can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- D. Void envelope, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.

**Q8. (App Center and Extension Apps - Extension app role)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, a customer wants Docusign to call an external service during an agreement process. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Option notes:**
- A. A replacement for OAuth consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- B. Unlimited eSignature API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- C. A mandatory PDF renderer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- D. Extension apps extend Docusign with external service actions and data.

**Q9. (API Authentication - OAuth flow selection)** Daniel, a solutions architect at a commercial real-estate group, is connecting several line-of-business systems to Docusign APIs. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, a browser-only single-page application cannot protect a client secret but must authenticate each individual user. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- B. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Public Authorization Code Grant with PKCE.
- C. Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q10. (Go Live Process - Integration classification)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, a partner app will be distributed for many customers to install. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which go-live classification best reflects the use case?

A. Internal employee-only integration
B. One-time manual sending workflow
C. Template-only configuration
D. ISV or partner-distributed integration

**Answer:** D. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Option notes:**
- A. Internal employee-only integration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- B. One-time manual sending workflow can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- C. Template-only configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- D. Classification should match how the integration is used and distributed.

**Q11. (Docusign Connect - Connect vs polling)** Luca, a developer on the IAM team at a sales contract automation team, is connecting several line-of-business systems to Docusign APIs. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a system must learn when recipients complete signing without excessive API calls. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Option notes:**
- A. Wait for users to forward emails can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- B. Use a template reference model can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- C. Connect pushes events and avoids high-volume polling.
- D. Poll EnvelopeRecipients:list every second can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.

**Q12. (eSignature API - Draft envelope)** Mateo, a DevOps engineer at a procurement shared-services group, is moving a pilot integration from a developer account toward production. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a developer wants to create an envelope but not send it yet. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Option notes:**
- A. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- B. completed can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- C. The created status keeps an envelope in draft state.
- D. sent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.

**Q13. (eSignature Features and Web Forms - Web Form correlation)** Amir, a workflow automation engineer at a regional healthcare provider, is moving a pilot integration from a developer account toward production. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, an app creates one Web Form instance per customer record. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value should be supplied to correlate back to the app?

A. brandId
B. envelopeId before creation
C. clientUserId
D. templateId

**Answer:** C. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Option notes:**
- A. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- B. envelopeId before creation can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- C. clientUserId can map a form instance to an external record.
- D. templateId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.

**Q14. (Agreement Manager API - Agreement list)** Maya, an integration lead, is reviewing a Docusign implementation for a public-sector records department. The relevant requirement is that an app needs to find agreements matching criteria before retrieving details. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Option notes:**
- A. Configure CORS origins can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- B. Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- C. Create an envelope with status voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- D. Use only brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q15. (Workflow Builder and Workflow API - Identity step)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a process must gather participant data and then verify identity. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which sequence is best?

A. Verify identity after archiving only
B. Get Signatures before collecting data
C. Connect retry before web form
D. Collect Data with Web Forms, then Verify Someone's Identity

**Answer:** D. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Option notes:**
- A. Verify identity after archiving only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- B. Get Signatures before collecting data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- C. Connect retry before web form can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- D. Collect required data before the identity verification step if the scenario requires it.

**Q16. (App Center and Extension Apps - Public vs private)** Luca, a developer on the IAM team at a sales contract automation team, is moving a pilot integration from a developer account toward production. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an app is only for one organization's internal Docusign accounts. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Public vs private, and the better fit is Private extension app.
- B. Recipient Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.
- C. Private apps are limited to selected accounts or the publisher's organization.
- D. Public App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.

**Q17. (API Authentication - JWT Grant)** Priya, a platform engineer at a legal operations team, is standardizing how agreements are prepared, sent, monitored, and stored. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, a scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing JWT Grant, and the better fit is JSON Web Token Grant.
- B. JWT Grant supports non-interactive service integrations after consent has been granted.
- C. Public Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.

**Q18. (Go Live Process - Production endpoints)** Daniel, a solutions architect at a commercial real-estate group, is connecting several line-of-business systems to Docusign APIs. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, after go-live, API calls still point to demo endpoints. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be changed?

A. Use a Connect listener as the base URI
B. Replace all templates with web forms
C. Use production base URIs and production API endpoints
D. Keep demo endpoints and change only the email subject

**Answer:** C. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Option notes:**
- A. Use a Connect listener as the base URI can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- B. Replace all templates with web forms can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- C. Production integrations must call production endpoints and the correct account base URI.
- D. Keep demo endpoints and change only the email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.

**Q19. (Docusign Connect - Configuration level)** Sofia, a business systems analyst at a multinational HR operations team, is standardizing how agreements are prepared, sent, monitored, and stored. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a company wants one webhook for events across all accounts in its Docusign organization. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Option notes:**
- A. A Web Forms clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- B. Organization-level Connect centralizes events across accounts in the organization.
- C. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- D. Recipient-only Connect in each template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.

**Q20. (eSignature API - Cancel envelope)** Maya, an integration lead at a public-sector records department, is reducing support tickets caused by inconsistent envelope handling. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a sent envelope has a fatal error and no one should sign it. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- B. Voiding cancels an in-process envelope and stops signing.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- D. purged can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.

**Q21. (eSignature Features and Web Forms - Identity verification)** Grace, a product owner at a university financial-aid office, is reducing support tickets caused by inconsistent envelope handling. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, an envelope must require recipients to prove identity before signing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be included in the recipient configuration?

A. A template name only
B. An identity verification or recipient authentication configuration
C. A Connect retry policy
D. A workflow extension action

**Answer:** B. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Option notes:**
- A. A template name only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- B. Recipient authentication or ID verification settings enforce identity checks.
- C. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- D. A workflow extension action can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.

**Q22. (Agreement Manager API - Legacy import)** In a quick architecture review, the team wants the best answer without extra workflow context. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Option notes:**
- A. Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- B. Recipient view URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Legacy import, and the better fit is Agreement upload or bulk import using the Agreement Manager API.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q23. (Workflow Builder and Workflow API - Extension step)** Mateo, a DevOps engineer at a procurement shared-services group, is connecting several line-of-business systems to Docusign APIs. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, after signing, the completed document must be stored in an external file service. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow step type is appropriate?

A. Get Signatures step only
B. CORS configuration
C. Extension step using a file/archive extension app
D. Branching rule only

**Answer:** C. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Option notes:**
- A. Get Signatures step only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- B. CORS configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- C. Extension steps call external services through installed extension apps.
- D. Branching rule only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.

**Q24. (App Center and Extension Apps - Public App Center)** Sofia, a business systems analyst at a multinational HR operations team, is reducing support tickets caused by inconsistent envelope handling. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a partner wants customers broadly to discover and install an app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Option notes:**
- A. Demo-only template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- B. Public App Center distribution is for broad customer availability.
- C. Private app for one account only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.

**Q25. (API Authentication - Consent)** Luca, a developer on the IAM team at a sales contract automation team, is adding reusable agreement automation to an existing business application. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a JWT integration fails because the user has never granted consent for the requested scopes. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Option notes:**
- A. JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- B. A production account ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- C. A Connect listener URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- D. A new envelope template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q26. (Go Live Process - Templates in production)** Priya, a platform engineer at a legal operations team, is standardizing how agreements are prepared, sent, monitored, and stored. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, an app uses a template reference model in demo. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What is required for production?

A. Enable CORS only
B. Deploy or recreate the template in production and update the template ID
C. Reuse the demo template ID
D. Switch to JWT Grant

**Answer:** B. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Option notes:**
- A. Enable CORS only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- B. Template IDs differ between environments; the production template must be referenced.
- C. Reuse the demo template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- D. Switch to JWT Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.

**Q27. (Docusign Connect - JSON SIM)** Noah, an API developer at a banking compliance unit, is adding reusable agreement automation to an existing business application. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a workflow event must be delivered to a custom listener. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Option notes:**
- A. Workflow events rely on the JSON SIM event model.
- B. Legacy XML only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- C. CSV export format can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- D. PDF attachment only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.

**Q28. (eSignature API - Idempotency)** Daniel, a solutions architect at a commercial real-estate group, is building a self-service portal for internal teams and external customers. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a network retry might submit the same create-envelope request twice. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Option notes:**
- A. Supplying a transactionId supports idempotent envelope creation.
- B. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- C. retryId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- D. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.

**Q29. (eSignature Features and Web Forms - Recipient authentication)** Mateo, a DevOps engineer at a procurement shared-services group, is building a self-service portal for internal teams and external customers. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, a signer should receive a one-time code before accessing the envelope. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature category applies?

A. Recipient authentication
B. Bulk Send only
C. Agreement Manager extraction
D. App Center listing

**Answer:** A. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Option notes:**
- A. Recipient authentication controls access to signing.
- B. Bulk Send only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- C. Agreement Manager extraction can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- D. App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.

**Q30. (Agreement Manager API - Agreement documents)** Priya, a platform engineer at a legal operations team, is replacing a manual agreement process with a Docusign IAM integration. The records team wants agreement data available to downstream reporting and lifecycle processes after signature. In the current design, a downstream system needs a copy of an agreement document. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Option notes:**
- A. A Web Forms client SDK only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- B. A Connect listener with no API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- C. A bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- D. Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q31. (Workflow Builder and Workflow API - Branching)** Maya, an integration lead at a public-sector records department, is standardizing how agreements are prepared, sent, monitored, and stored. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow should follow different paths based on a form response. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow capability is used?

A. Brand destination URL
B. Branching or conditional rules
C. JWT consent
D. Envelope purge

**Answer:** B. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Option notes:**
- A. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- B. Branching rules route workflows based on conditions.
- C. JWT consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- D. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.

**Q32. (App Center and Extension Apps - Manifest)** Noah, an API developer at a banking compliance unit, is building a self-service portal for internal teams and external customers. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, an extension app action must call an external API endpoint. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Option notes:**
- A. Actions in the manifest describe calls to external endpoints.
- B. In an envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- C. In a recipient tab label can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- D. In the Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.

**Q33. (API Authentication - Scopes)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, an app only needs to send envelopes and read user account information. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Option notes:**
- A. Request every Docusign scope to avoid future changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- B. Omit scopes because Docusign infers them can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- C. Use account-level Connect settings as scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- D. Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q34. (Go Live Process - Post go-live)** Luca, a developer on the IAM team at a sales contract automation team, is adding reusable agreement automation to an existing business application. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, a promoted integration key uses Confidential Authorization Code Grant. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should be validated immediately after go-live?

A. Production redirect URIs, secrets, base URI, and consent
B. Recipient tab labels only
C. The user's browser zoom level
D. Template color branding only

**Answer:** A. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Option notes:**
- A. OAuth and endpoint settings often need production-specific validation.
- B. Recipient tab labels only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- C. The user's browser zoom level can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- D. Template color branding only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.

**Q35. (Docusign Connect - Security)** Elena, an implementation consultant at a partner-built customer portal, is automating high-volume agreement work while keeping auditability intact. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a listener must verify that incoming webhook messages really came from Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Option notes:**
- A. Changing the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- B. Using clientUserId on every signer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- C. Adding a brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- D. HMAC and authentication settings help secure Connect listeners.

**Q36. (eSignature API - Template reference)** Priya, a platform engineer at a legal operations team, is replacing a manual agreement process with a Docusign IAM integration. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a request uses a server template already stored in Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Option notes:**
- A. clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- B. returnUrl can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- C. basePath can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- D. templateId references an existing template in an envelope request.

**Q37. (eSignature Features and Web Forms - Brand destination URLs)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, remote signers should be redirected to a custom page after finishing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which branding feature is relevant?

A. Envelope transactionId
B. JWT consent URL
C. Bulk send list ID
D. Brand destination URLs

**Answer:** D. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Option notes:**
- A. Envelope transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- B. JWT consent URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- C. Bulk send list ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- D. Brand destination URLs control post-signing redirect destinations for remote signing.

**Q38. (Agreement Manager API - Agreement data)** Luca, a developer on the IAM team at a sales contract automation team, is connecting several line-of-business systems to Docusign APIs. The organization is modernizing legacy agreement records and needs API access to agreement metadata and documents. In the current design, a custom app needs structured extracted data for a specific agreement. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Option notes:**
- A. Workflow trigger requirements can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- B. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- C. Agreements:getAgreement retrieves agreement data for a specific agreement.
- D. Envelopes:create can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q39. (Workflow Builder and Workflow API - Start method)** Daniel, a solutions architect at a commercial real-estate group, is adding reusable agreement automation to an existing business application. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a portal link should launch a workflow and pass values in the trigger URL. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method fits?

A. From a Link
B. Manually by someone in your organization only
C. From an envelope void event only
D. From a bulk send batch only

**Answer:** A. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Option notes:**
- A. A link start method can launch a workflow and pass URL values.
- B. Manually by someone in your organization only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- C. From an envelope void event only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- D. From a bulk send batch only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.

**Q40. (App Center and Extension Apps - Connections)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an action must use external OAuth credentials. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Option notes:**
- A. publisher only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- B. brandColors can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- C. bulkCopies can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- D. The connections object defines authentication configuration used by actions.

**Q41. (API Authentication - User info)** Noah, an API developer at a banking compliance unit, is moving a pilot integration from a developer account toward production. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, after receiving an access token, the app must determine which base URI and account ID to use for API calls. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Option notes:**
- A. /oauth/token can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- B. /connect/events can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- C. The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- D. /restapi/v2.1/accounts can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q42. (Go Live Process - API limits)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, an integration repeatedly polls envelopes every few seconds for status. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which improvement best aligns with API usage guidelines?

A. Increase polling frequency
B. Create duplicate envelopes for retry
C. Move all status into email subject lines
D. Use Connect webhooks for event-driven status updates

**Answer:** D. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Option notes:**
- A. Increase polling frequency can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- B. Create duplicate envelopes for retry can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- C. Move all status into email subject lines can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- D. Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q43. (Docusign Connect - Retries)** Amir, a workflow automation engineer at a regional healthcare provider, is moving a pilot integration from a developer account toward production. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a listener is temporarily unavailable when Docusign sends an event. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Option notes:**
- A. The integration key is revoked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- B. The recipient must sign again can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- C. Connect has retry behavior for delivery failures; listeners should be idempotent.
- D. The envelope is automatically voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q44. (eSignature API - Composite templates)** Luca, a developer on the IAM team at a sales contract automation team, is connecting several line-of-business systems to Docusign APIs. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a request must combine server templates, inline recipient data, and documents. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Option notes:**
- A. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- B. Connect 2.0 only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- C. Composite templates allow combining server templates, inline templates, and documents.
- D. Bulk send list only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.

**Q45. (eSignature Features and Web Forms - Connected Fields)** Daniel, a solutions architect at a commercial real-estate group, is connecting several line-of-business systems to Docusign APIs. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, a signer-provided value must be checked against an external data source during signing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature supports this?

A. Envelope purge
B. Safe Exam Browser
C. Connected Fields or data verification
D. Agreement import only

**Answer:** C. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Option notes:**
- A. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- B. Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- C. Connected Fields and data verification support real-time validation scenarios.
- D. Agreement import only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.

**Q46. (Agreement Manager API - Agreement list)** Sofia, a business systems analyst at a multinational HR operations team, is standardizing how agreements are prepared, sent, monitored, and stored. The integration must retrieve agreement information without confusing envelope execution data with agreement repository data. In the current design, an app needs to find agreements matching criteria before retrieving details. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Option notes:**
- A. Configure CORS origins can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- B. Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- C. Create an envelope with status voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- D. Use only brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q47. (Workflow Builder and Workflow API - API trigger)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, a backend service must programmatically trigger a workflow. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method/API pattern is relevant?

A. Remote signing email only
B. Brand resource file upload
C. Template reference ID only
D. From an API call with Workflow Builder API trigger requirements

**Answer:** D. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Option notes:**
- A. Remote signing email only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- B. Brand resource file upload can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- C. Template reference ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- D. API-triggered workflows use trigger requirements and workflow API calls.

**Q48. (App Center and Extension Apps - connectionsReference)** Amir, a workflow automation engineer at a regional healthcare provider, is connecting several line-of-business systems to Docusign APIs. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, an action needs to use a named connection from the manifest. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Option notes:**
- A. transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- B. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- C. connectionsReference ties an action to a connection definition.
- D. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.

**Q49. (API Authentication - PKCE)** Elena, an implementation consultant at a partner-built customer portal, is reducing support tickets caused by inconsistent envelope handling. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a native app cannot store a client secret securely. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Option notes:**
- A. A template password can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- B. PKCE mitigates interception risk for public clients that cannot keep a client secret.
- C. An HMAC secret on each envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- D. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q50. (Go Live Process - Troubleshooting)** Noah, an API developer, is reviewing a Docusign implementation for a banking compliance unit. The relevant requirement is that a production app fails after go-live with authentication errors, but worked in demo. What should be checked first?

A. Whether recipients use the same browser
B. Whether document tabs are locked
C. Production OAuth settings, redirect URI, consent, and account base URI
D. Whether demo envelopes are legally binding

**Answer:** C. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Option notes:**
- A. Whether recipients use the same browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- B. Whether document tabs are locked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- C. Common post-go-live issues are environment and OAuth configuration mismatches.
- D. Whether demo envelopes are legally binding can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.

**Q51. (Docusign Connect - Troubleshooting)** Grace, a product owner at a university financial-aid office, is reducing support tickets caused by inconsistent envelope handling. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a listener receives duplicate webhook messages. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Option notes:**
- A. Use a different template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- B. Webhook systems should tolerate retries and duplicate delivery.
- C. Treat every duplicate as a new envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- D. Disable OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.

**Q52. (eSignature API - Anchor tabs)** Sofia, a business systems analyst at a multinational HR operations team, is standardizing how agreements are prepared, sent, monitored, and stored. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a document can vary in page length, but the signature should appear near a specific text string. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Option notes:**
- A. CORS origin settings can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- B. Anchor tabs place fields relative to document text.
- C. Fixed x/y coordinates only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- D. Branding resource files can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.

**Q53. (eSignature Features and Web Forms - ID Evidence)** Priya, a platform engineer at a legal operations team, is standardizing how agreements are prepared, sent, monitored, and stored. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, a system must retrieve retained data about a completed ID Verification event. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which API is relevant?

A. WorkflowInstanceManagement only
B. ID Evidence API
C. Web Forms API only
D. BulkSend API

**Answer:** B. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Option notes:**
- A. WorkflowInstanceManagement only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- B. The ID Evidence API retrieves retained evidence from ID verification events.
- C. Web Forms API only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- D. BulkSend API can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.

**Q54. (Agreement Manager API - Legacy import)** Noah, an API developer at a banking compliance unit, is adding reusable agreement automation to an existing business application. The records team wants agreement data available to downstream reporting and lifecycle processes after signature. In the current design, a company wants to bring existing contracts into Agreement Manager. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Option notes:**
- A. Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- B. Recipient view URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Legacy import, and the better fit is Agreement upload or bulk import using the Agreement Manager API.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q55. (Workflow Builder and Workflow API - Runtime errors)** Luca, a developer on the IAM team, is reviewing a Docusign implementation for a sales contract automation team. The relevant requirement is that a workflow trigger fails because required starting variables are missing. What should the developer inspect?

A. Connect HMAC secret only
B. Bulk send list status only
C. Workflow trigger requirements and variable mapping
D. Brand destination URLs

**Answer:** C. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Option notes:**
- A. Connect HMAC secret only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- B. Bulk send list status only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- C. Workflow trigger requirements define required input variables.
- D. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.

**Q56. (App Center and Extension Apps - API proxy)** Grace, a product owner at a university financial-aid office, is standardizing how agreements are prepared, sent, monitored, and stored. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, the third-party API format does not match what the extension app action needs. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Option notes:**
- A. Bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- B. An API proxy can mediate between Docusign and the external service.
- C. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- D. Envelope void status can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.

**Q57. (API Authentication - Bearer tokens)** Amir, a workflow automation engineer at a regional healthcare provider, is building a self-service portal for internal teams and external customers. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, a REST API request is returning unauthorized even though the token endpoint returned an access token. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Option notes:**
- A. Docusign REST calls use Authorization: Bearer <access_token>.
- B. In the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- C. In the Connect eventNotification object can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- D. In the templateId field can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.

**Q58. (Go Live Process - Go-live setup)** Elena, an implementation consultant, is reviewing a Docusign implementation for a partner-built customer portal. The relevant requirement is that a developer promotes an integration key from demo to production. Which configuration commonly must be recreated in production?

A. Connect event logs
B. Redirect URIs and secret keys
C. Completed demo envelopes
D. Envelope IDs

**Answer:** B. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Option notes:**
- A. Connect event logs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- B. Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- C. Completed demo envelopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- D. Envelope IDs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q59. (Docusign Connect - Payload selection)** Mateo, a DevOps engineer at a procurement shared-services group, is building a self-service portal for internal teams and external customers. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a team wants smaller event payloads and will query details separately. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Option notes:**
- A. Connect payload options should match data minimization and processing needs.
- B. Switch to implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- C. Use recipient authentication instead can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- D. Create a bulk send list can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.

**Q60. (eSignature API - Embedded signing)** Noah, an API developer at a banking compliance unit, is adding reusable agreement automation to an existing business application. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a recipient must sign inside the host app rather than through an email link. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Option notes:**
- A. clientUserId identifies a captive/embedded recipient.
- B. emailNotification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- C. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- D. listId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.

**Q61. (eSignature Features and Web Forms - Web Forms embedding)** Luca, a developer on the IAM team at a sales contract automation team, is adding reusable agreement automation to an existing business application. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, a custom website needs to render a Docusign Web Form instance inline. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What client-side component is used with the instance URL?

A. Docusign JS client SDK
B. EnvelopeViews:createRecipient
C. Connect JSON SIM
D. Workflow start link only

**Answer:** A. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Option notes:**
- A. Docusign JS renders Web Form instances in the host page.
- B. EnvelopeViews:createRecipient can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- C. Connect JSON SIM can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- D. Workflow start link only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.

**Q62. (Agreement Manager API - Agreement documents)** Elena, an implementation consultant at a partner-built customer portal, is automating high-volume agreement work while keeping auditability intact. The organization is modernizing legacy agreement records and needs API access to agreement metadata and documents. In the current design, a downstream system needs a copy of an agreement document. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Option notes:**
- A. A Web Forms client SDK only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- B. A Connect listener with no API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- C. A bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- D. Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q63. (Workflow Builder and Workflow API - Embedding workflow)** Sofia, a business systems analyst, is reviewing a Docusign implementation for a multinational HR operations team. The relevant requirement is that a custom app needs to display a workflow experience inside the app. Which capability should be considered?

A. Agreement type extraction only
B. Embedding or launching the workflow according to its configured start method
C. Envelope purge
D. JWT admin consent only

**Answer:** B. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Option notes:**
- A. Agreement type extraction only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- B. Workflow integration depends on the configured start method and embedding/launch pattern.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- D. JWT admin consent only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.

**Q64. (App Center and Extension Apps - Firewall)** Mateo, a DevOps engineer at a procurement shared-services group, is adding reusable agreement automation to an existing business application. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, docusign must call a customer-hosted endpoint for an extension action. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Option notes:**
- A. The external endpoint must be reachable by Docusign.
- B. Disable all OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- C. Use only demo endpoints can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- D. Delete the app manifest can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.

**Q65. (API Authentication - OAuth flow selection)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, a server-side portal can store a client secret and each employee signs in interactively. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- B. Public Authorization Code Grant with PKCE can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Confidential Authorization Code Grant.
- D. Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q66. (Go Live Process - Integration classification)** In a quick architecture review, the team wants the best answer without extra workflow context. Which go-live classification best reflects the use case?

A. ISV or partner-distributed integration
B. Internal employee-only integration
C. One-time manual sending workflow
D. Template-only configuration

**Answer:** A. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Option notes:**
- A. Classification should match how the integration is used and distributed.
- B. Internal employee-only integration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- C. One-time manual sending workflow can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- D. Template-only configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.

**Q67. (Docusign Connect - Envelope-level Connect)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a single high-value envelope needs a callback URL different from account-level settings. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Option notes:**
- A. Create a Web Form instance can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- B. Use Workflow Builder only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- C. Set the envelope status to created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- D. The eventNotification object configures per-envelope Connect callbacks.

**Q68. (eSignature API - Signing URL)** Elena, an implementation consultant at a partner-built customer portal, is automating high-volume agreement work while keeping auditability intact. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, an app has created an envelope for an embedded recipient. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Option notes:**
- A. A Connect JSON SIM event can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- B. A bulk send batch ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- C. A brand resource file can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- D. Embedded signing requires requesting a short-lived recipient view URL.

**Q69. (eSignature Features and Web Forms - Web Form correlation)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, an app creates one Web Form instance per customer record. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value should be supplied to correlate back to the app?

A. templateId
B. brandId
C. envelopeId before creation
D. clientUserId

**Answer:** D. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Option notes:**
- A. templateId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- B. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- C. envelopeId before creation can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- D. clientUserId can map a form instance to an external record.

**Q70. (Agreement Manager API - Agreement data)** Amir, a workflow automation engineer at a regional healthcare provider, is moving a pilot integration from a developer account toward production. The integration must retrieve agreement information without confusing envelope execution data with agreement repository data. In the current design, a custom app needs structured extracted data for a specific agreement. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Option notes:**
- A. Workflow trigger requirements can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- B. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- C. Agreements:getAgreement retrieves agreement data for a specific agreement.
- D. Envelopes:create can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q71. (Workflow Builder and Workflow API - Installed extensions)** In a quick architecture review, the team wants the best answer without extra workflow context. What must be true?

A. The extension app must be installed and available for the workflow step
B. The envelope must be voided first
C. The app must use implicit grant
D. The Web Form must be public

**Answer:** A. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Option notes:**
- A. Workflow Builder can use installed extension applications in extension steps.
- B. The envelope must be voided first can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- C. The app must use implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- D. The Web Form must be public can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.

**Q72. (App Center and Extension Apps - Data IO)** Maya, an integration lead at a public-sector records department, is automating high-volume agreement work while keeping auditability intact. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a workflow needs to read and write structured records in another system. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Option notes:**
- A. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- B. Branding extension can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Data IO, and the better fit is Data IO extension app.
- D. Data IO extensions read/write structured data.

**Q73. (API Authentication - OAuth flow selection)** Mateo, a DevOps engineer, is reviewing a Docusign implementation for a procurement shared-services group. The relevant requirement is that a browser-only single-page application cannot protect a client secret but must authenticate each individual user. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- B. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Public Authorization Code Grant with PKCE.
- C. Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q74. (Go Live Process - Production endpoints)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, after go-live, API calls still point to demo endpoints. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be changed?

A. Keep demo endpoints and change only the email subject
B. Use a Connect listener as the base URI
C. Replace all templates with web forms
D. Use production base URIs and production API endpoints

**Answer:** D. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Option notes:**
- A. Keep demo endpoints and change only the email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- B. Use a Connect listener as the base URI can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- C. Replace all templates with web forms can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- D. Production integrations must call production endpoints and the correct account base URI.

**Q75. (Docusign Connect - Connect vs polling)** Daniel, a solutions architect, is reviewing a Docusign implementation for a commercial real-estate group. The relevant requirement is that a system must learn when recipients complete signing without excessive API calls. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Option notes:**
- A. Wait for users to forward emails can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- B. Use a template reference model can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- C. Connect pushes events and avoids high-volume polling.
- D. Poll EnvelopeRecipients:list every second can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.

**Q76. (eSignature API - Embedded signing timing)** Amir, a workflow automation engineer, is reviewing a Docusign implementation for a regional healthcare provider. The relevant requirement is that an app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Option notes:**
- A. The account base URI disappears can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- B. Connect retries stop can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- C. Embedded signing URLs are short-lived and should be generated when the user is ready.
- D. The template ID changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q77. (eSignature Features and Web Forms - Identity verification)** Noah, an API developer, is reviewing a Docusign implementation for a banking compliance unit. The relevant requirement is that an envelope must require recipients to prove identity before signing. What must be included in the recipient configuration?

A. A workflow extension action
B. A template name only
C. An identity verification or recipient authentication configuration
D. A Connect retry policy

**Answer:** C. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Option notes:**
- A. A workflow extension action can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- B. A template name only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- C. Recipient authentication or ID verification settings enforce identity checks.
- D. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.

**Q78. (Agreement Manager API - Agreement list)** Grace, a product owner at a university financial-aid office, is reducing support tickets caused by inconsistent envelope handling. The records team wants agreement data available to downstream reporting and lifecycle processes after signature. In the current design, an app needs to find agreements matching criteria before retrieving details. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Option notes:**
- A. Configure CORS origins can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- B. Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- C. Create an envelope with status voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- D. Use only brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q79. (Workflow Builder and Workflow API - Workflow steps)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow must collect form data before sending a document for signature. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which step order best fits?

A. Get Signatures, then collect data
B. Archive first, then start
C. Void envelope, then collect data
D. Collect Data with Web Forms, then Get Signatures

**Answer:** D. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Option notes:**
- A. Get Signatures, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- B. Archive first, then start can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- C. Void envelope, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- D. Workflow step order should match the business process.

**Q80. (App Center and Extension Apps - File IO)** Daniel, a solutions architect, is reviewing a Docusign implementation for a commercial real-estate group. The relevant requirement is that a workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Option notes:**
- A. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- B. CORS origin only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- C. File IO extensions handle document storage and retrieval use cases.
- D. Connected Fields only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.

**Q81. (API Authentication - JWT Grant)** Maya, an integration lead, is reviewing a Docusign implementation for a public-sector records department. The relevant requirement is that a scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing JWT Grant, and the better fit is JSON Web Token Grant.
- B. JWT Grant supports non-interactive service integrations after consent has been granted.
- C. Public Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.

**Q82. (Go Live Process - Templates in production)** Mateo, a DevOps engineer at a procurement shared-services group, is connecting several line-of-business systems to Docusign APIs. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, an app uses a template reference model in demo. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What is required for production?

A. Switch to JWT Grant
B. Enable CORS only
C. Deploy or recreate the template in production and update the template ID
D. Reuse the demo template ID

**Answer:** C. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Option notes:**
- A. Switch to JWT Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- B. Enable CORS only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- C. Template IDs differ between environments; the production template must be referenced.
- D. Reuse the demo template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.

**Q83. (Docusign Connect - Configuration level)** Priya, a platform engineer, is reviewing a Docusign implementation for a legal operations team. The relevant requirement is that a company wants one webhook for events across all accounts in its Docusign organization. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Option notes:**
- A. A Web Forms clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- B. Organization-level Connect centralizes events across accounts in the organization.
- C. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- D. Recipient-only Connect in each template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.

**Q84. (eSignature API - Embedded sending)** Grace, a product owner, is reviewing a Docusign implementation for a university financial-aid office. The relevant requirement is that a sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Option notes:**
- A. Connect retry log can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- B. Embedded sending uses a sender view URL.
- C. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- D. Agreements:getAgreement can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.

**Q85. (eSignature Features and Web Forms - Recipient authentication)** Elena, an implementation consultant, is reviewing a Docusign implementation for a partner-built customer portal. The relevant requirement is that a signer should receive a one-time code before accessing the envelope. Which feature category applies?

A. App Center listing
B. Recipient authentication
C. Bulk Send only
D. Agreement Manager extraction

**Answer:** B. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Option notes:**
- A. App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- B. Recipient authentication controls access to signing.
- C. Bulk Send only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- D. Agreement Manager extraction can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.

**Q86. (Agreement Manager API - Legacy import)** Mateo, a DevOps engineer at a procurement shared-services group, is building a self-service portal for internal teams and external customers. The organization is modernizing legacy agreement records and needs API access to agreement metadata and documents. In the current design, a company wants to bring existing contracts into Agreement Manager. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Option notes:**
- A. Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- B. Recipient view URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Legacy import, and the better fit is Agreement upload or bulk import using the Agreement Manager API.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q87. (Workflow Builder and Workflow API - Identity step)** Amir, a workflow automation engineer at a regional healthcare provider, is connecting several line-of-business systems to Docusign APIs. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a process must gather participant data and then verify identity. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which sequence is best?

A. Get Signatures before collecting data
B. Connect retry before web form
C. Collect Data with Web Forms, then Verify Someone's Identity
D. Verify identity after archiving only

**Answer:** C. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Option notes:**
- A. Get Signatures before collecting data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- B. Connect retry before web form can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- C. Collect required data before the identity verification step if the scenario requires it.
- D. Verify identity after archiving only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.

**Q88. (App Center and Extension Apps - Connected Fields)** Priya, a platform engineer, is reviewing a Docusign implementation for a legal operations team. The relevant requirement is that an extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Option notes:**
- A. Agreement list search can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- B. Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- C. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- D. Go-live classification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q89. (API Authentication - Consent)** In a quick architecture review, the team wants the best answer without extra workflow context. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Option notes:**
- A. JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- B. A production account ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- C. A Connect listener URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- D. A new envelope template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q90. (Go Live Process - Post go-live)** Maya, an integration lead at a public-sector records department, is standardizing how agreements are prepared, sent, monitored, and stored. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, a promoted integration key uses Confidential Authorization Code Grant. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should be validated immediately after go-live?

A. Template color branding only
B. Production redirect URIs, secrets, base URI, and consent
C. Recipient tab labels only
D. The user's browser zoom level

**Answer:** B. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Option notes:**
- A. Template color branding only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- B. OAuth and endpoint settings often need production-specific validation.
- C. Recipient tab labels only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- D. The user's browser zoom level can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.

**Q91. (Docusign Connect - JSON SIM)** In a quick architecture review, the team wants the best answer without extra workflow context. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Option notes:**
- A. Workflow events rely on the JSON SIM event model.
- B. Legacy XML only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- C. CSV export format can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- D. PDF attachment only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.

**Q92. (eSignature API - Bulk send)** In a quick architecture review, the team wants the best answer without extra workflow context. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

**Option notes:**
- A. Bulk Send supports large batches of personalized envelopes.
- B. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- C. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- D. Organization Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.

**Q93. (eSignature Features and Web Forms - Brand destination URLs)** In a quick architecture review, the team wants the best answer without extra workflow context. Which branding feature is relevant?

A. Brand destination URLs
B. Envelope transactionId
C. JWT consent URL
D. Bulk send list ID

**Answer:** A. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Option notes:**
- A. Brand destination URLs control post-signing redirect destinations for remote signing.
- B. Envelope transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- C. JWT consent URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- D. Bulk send list ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.

**Q94. (Agreement Manager API - Agreement documents)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. The integration must retrieve agreement information without confusing envelope execution data with agreement repository data. In the current design, a downstream system needs a copy of an agreement document. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Option notes:**
- A. A Web Forms client SDK only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- B. A Connect listener with no API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- C. A bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- D. Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q95. (Workflow Builder and Workflow API - Extension step)** Grace, a product owner at a university financial-aid office, is standardizing how agreements are prepared, sent, monitored, and stored. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, after signing, the completed document must be stored in an external file service. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow step type is appropriate?

A. CORS configuration
B. Extension step using a file/archive extension app
C. Branching rule only
D. Get Signatures step only

**Answer:** B. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Option notes:**
- A. CORS configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- B. Extension steps call external services through installed extension apps.
- C. Branching rule only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- D. Get Signatures step only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.

**Q96. (App Center and Extension Apps - Data Verification)** In a quick architecture review, the team wants the best answer without extra workflow context. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

**Option notes:**
- A. Data Verification checks signer-entered data during the signing experience.
- B. Public Auth Code only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- D. Agreement Manager import can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.

**Q97. (API Authentication - Scopes)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, an app only needs to send envelopes and read user account information. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Option notes:**
- A. Request every Docusign scope to avoid future changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- B. Omit scopes because Docusign infers them can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- C. Use account-level Connect settings as scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- D. Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q98. (Go Live Process - API limits)** Daniel, a solutions architect at a commercial real-estate group, is adding reusable agreement automation to an existing business application. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, an integration repeatedly polls envelopes every few seconds for status. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which improvement best aligns with API usage guidelines?

A. Use Connect webhooks for event-driven status updates
B. Increase polling frequency
C. Create duplicate envelopes for retry
D. Move all status into email subject lines

**Answer:** A. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Option notes:**
- A. Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- B. Increase polling frequency can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- C. Create duplicate envelopes for retry can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- D. Move all status into email subject lines can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q99. (Docusign Connect - Security)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a listener must verify that incoming webhook messages really came from Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Option notes:**
- A. Changing the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- B. Using clientUserId on every signer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- C. Adding a brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- D. HMAC and authentication settings help secure Connect listeners.

**Q100. (eSignature API - Envelope create)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, an integration needs to send an envelope for signature immediately. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- B. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- D. Status sent sends the envelope; created saves it as a draft.

**Q101. (eSignature Features and Web Forms - Connected Fields)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, a signer-provided value must be checked against an external data source during signing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature supports this?

A. Agreement import only
B. Envelope purge
C. Safe Exam Browser
D. Connected Fields or data verification

**Answer:** D. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Option notes:**
- A. Agreement import only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- B. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- C. Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- D. Connected Fields and data verification support real-time validation scenarios.

**Q102. (Agreement Manager API - Agreement data)** Daniel, a solutions architect, is reviewing a Docusign implementation for a commercial real-estate group. The relevant requirement is that a custom app needs structured extracted data for a specific agreement. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Option notes:**
- A. Workflow trigger requirements can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- B. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- C. Agreements:getAgreement retrieves agreement data for a specific agreement.
- D. Envelopes:create can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q103. (Workflow Builder and Workflow API - Branching)** Mateo, a DevOps engineer at a procurement shared-services group, is adding reusable agreement automation to an existing business application. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow should follow different paths based on a form response. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow capability is used?

A. Branching or conditional rules
B. JWT consent
C. Envelope purge
D. Brand destination URL

**Answer:** A. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Option notes:**
- A. Branching rules route workflows based on conditions.
- B. JWT consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- D. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.

**Q104. (App Center and Extension Apps - Extension app role)** Sofia, a business systems analyst at a multinational HR operations team, is replacing a manual agreement process with a Docusign IAM integration. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, a customer wants Docusign to call an external service during an agreement process. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Option notes:**
- A. A replacement for OAuth consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- B. Unlimited eSignature API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- C. A mandatory PDF renderer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- D. Extension apps extend Docusign with external service actions and data.

**Q105. (API Authentication - User info)** Luca, a developer on the IAM team at a sales contract automation team, is moving a pilot integration from a developer account toward production. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, after receiving an access token, the app must determine which base URI and account ID to use for API calls. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Option notes:**
- A. /oauth/token can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- B. /connect/events can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- C. The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- D. /restapi/v2.1/accounts can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q106. (Go Live Process - Troubleshooting)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, a production app fails after go-live with authentication errors, but worked in demo. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should be checked first?

A. Whether demo envelopes are legally binding
B. Whether recipients use the same browser
C. Whether document tabs are locked
D. Production OAuth settings, redirect URI, consent, and account base URI

**Answer:** D. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Option notes:**
- A. Whether demo envelopes are legally binding can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- B. Whether recipients use the same browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- C. Whether document tabs are locked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- D. Common post-go-live issues are environment and OAuth configuration mismatches.

**Q107. (Docusign Connect - Retries)** Noah, an API developer at a banking compliance unit, is moving a pilot integration from a developer account toward production. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a listener is temporarily unavailable when Docusign sends an event. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Option notes:**
- A. The integration key is revoked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- B. The recipient must sign again can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- C. Connect has retry behavior for delivery failures; listeners should be idempotent.
- D. The envelope is automatically voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q108. (eSignature API - Draft envelope)** Daniel, a solutions architect at a commercial real-estate group, is connecting several line-of-business systems to Docusign APIs. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a developer wants to create an envelope but not send it yet. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Option notes:**
- A. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- B. completed can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- C. The created status keeps an envelope in draft state.
- D. sent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.

**Q109. (eSignature Features and Web Forms - ID Evidence)** Mateo, a DevOps engineer at a procurement shared-services group, is connecting several line-of-business systems to Docusign APIs. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, a system must retrieve retained data about a completed ID Verification event. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which API is relevant?

A. BulkSend API
B. WorkflowInstanceManagement only
C. ID Evidence API
D. Web Forms API only

**Answer:** C. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Option notes:**
- A. BulkSend API can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- B. WorkflowInstanceManagement only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- C. The ID Evidence API retrieves retained evidence from ID verification events.
- D. Web Forms API only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.

**Q110. (Agreement Manager API - Agreement list)** Priya, a platform engineer, is reviewing a Docusign implementation for a legal operations team. The relevant requirement is that an app needs to find agreements matching criteria before retrieving details. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Option notes:**
- A. Configure CORS origins can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- B. Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- C. Create an envelope with status voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- D. Use only brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q111. (Workflow Builder and Workflow API - Start method)** Maya, an integration lead at a public-sector records department, is automating high-volume agreement work while keeping auditability intact. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a portal link should launch a workflow and pass values in the trigger URL. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method fits?

A. Manually by someone in your organization only
B. From an envelope void event only
C. From a bulk send batch only
D. From a Link

**Answer:** D. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Option notes:**
- A. Manually by someone in your organization only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- B. From an envelope void event only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- C. From a bulk send batch only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- D. A link start method can launch a workflow and pass URL values.

**Q112. (App Center and Extension Apps - Public vs private)** Noah, an API developer at a banking compliance unit, is connecting several line-of-business systems to Docusign APIs. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an app is only for one organization's internal Docusign accounts. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Public vs private, and the better fit is Private extension app.
- B. Recipient Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.
- C. Private apps are limited to selected accounts or the publisher's organization.
- D. Public App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.

**Q113. (API Authentication - PKCE)** Sofia, a business systems analyst at a multinational HR operations team, is reducing support tickets caused by inconsistent envelope handling. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, a native app cannot store a client secret securely. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Option notes:**
- A. A template password can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- B. PKCE mitigates interception risk for public clients that cannot keep a client secret.
- C. An HMAC secret on each envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- D. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q114. (Go Live Process - Go-live setup)** Luca, a developer on the IAM team at a sales contract automation team, is moving a pilot integration from a developer account toward production. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, a developer promotes an integration key from demo to production. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which configuration commonly must be recreated in production?

A. Envelope IDs
B. Connect event logs
C. Redirect URIs and secret keys
D. Completed demo envelopes

**Answer:** C. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Option notes:**
- A. Envelope IDs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- B. Connect event logs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- C. Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- D. Completed demo envelopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q115. (Docusign Connect - Troubleshooting)** Elena, an implementation consultant at a partner-built customer portal, is reducing support tickets caused by inconsistent envelope handling. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a listener receives duplicate webhook messages. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Option notes:**
- A. Use a different template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- B. Webhook systems should tolerate retries and duplicate delivery.
- C. Treat every duplicate as a new envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- D. Disable OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.

**Q116. (eSignature API - Cancel envelope)** Priya, a platform engineer at a legal operations team, is standardizing how agreements are prepared, sent, monitored, and stored. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a sent envelope has a fatal error and no one should sign it. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- B. Voiding cancels an in-process envelope and stops signing.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- D. purged can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.

**Q117. (eSignature Features and Web Forms - Web Forms embedding)** Maya, an integration lead at a public-sector records department, is standardizing how agreements are prepared, sent, monitored, and stored. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, a custom website needs to render a Docusign Web Form instance inline. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What client-side component is used with the instance URL?

A. Workflow start link only
B. Docusign JS client SDK
C. EnvelopeViews:createRecipient
D. Connect JSON SIM

**Answer:** B. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Option notes:**
- A. Workflow start link only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- B. Docusign JS renders Web Form instances in the host page.
- C. EnvelopeViews:createRecipient can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- D. Connect JSON SIM can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.

**Q118. (Agreement Manager API - Legacy import)** In a quick architecture review, the team wants the best answer without extra workflow context. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Option notes:**
- A. Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- B. Recipient view URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Legacy import, and the better fit is Agreement upload or bulk import using the Agreement Manager API.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreement upload or bulk import using the Agreement Manager API: Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q119. (Workflow Builder and Workflow API - API trigger)** Daniel, a solutions architect at a commercial real-estate group, is moving a pilot integration from a developer account toward production. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, a backend service must programmatically trigger a workflow. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method/API pattern is relevant?

A. Brand resource file upload
B. Template reference ID only
C. From an API call with Workflow Builder API trigger requirements
D. Remote signing email only

**Answer:** C. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Option notes:**
- A. Brand resource file upload can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- B. Template reference ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- C. API-triggered workflows use trigger requirements and workflow API calls.
- D. Remote signing email only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.

**Q120. (App Center and Extension Apps - Public App Center)** Elena, an implementation consultant at a partner-built customer portal, is standardizing how agreements are prepared, sent, monitored, and stored. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a partner wants customers broadly to discover and install an app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Option notes:**
- A. Demo-only template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- B. Public App Center distribution is for broad customer availability.
- C. Private app for one account only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.

**Q121. (API Authentication - Bearer tokens)** Noah, an API developer at a banking compliance unit, is building a self-service portal for internal teams and external customers. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a REST API request is returning unauthorized even though the token endpoint returned an access token. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Option notes:**
- A. Docusign REST calls use Authorization: Bearer <access_token>.
- B. In the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- C. In the Connect eventNotification object can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- D. In the templateId field can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.

**Q122. (Go Live Process - Integration classification)** Sofia, a business systems analyst at a multinational HR operations team, is reducing support tickets caused by inconsistent envelope handling. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, a partner app will be distributed for many customers to install. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which go-live classification best reflects the use case?

A. Template-only configuration
B. ISV or partner-distributed integration
C. Internal employee-only integration
D. One-time manual sending workflow

**Answer:** B. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Option notes:**
- A. Template-only configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- B. Classification should match how the integration is used and distributed.
- C. Internal employee-only integration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- D. One-time manual sending workflow can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.

**Q123. (Docusign Connect - Payload selection)** Amir, a workflow automation engineer at a regional healthcare provider, is building a self-service portal for internal teams and external customers. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a team wants smaller event payloads and will query details separately. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Option notes:**
- A. Connect payload options should match data minimization and processing needs.
- B. Switch to implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- C. Use recipient authentication instead can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- D. Create a bulk send list can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.

**Q124. (eSignature API - Idempotency)** Luca, a developer on the IAM team at a sales contract automation team, is adding reusable agreement automation to an existing business application. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a network retry might submit the same create-envelope request twice. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Option notes:**
- A. Supplying a transactionId supports idempotent envelope creation.
- B. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- C. retryId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- D. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.

**Q125. (eSignature Features and Web Forms - Web Form correlation)** Daniel, a solutions architect at a commercial real-estate group, is adding reusable agreement automation to an existing business application. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, an app creates one Web Form instance per customer record. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value should be supplied to correlate back to the app?

A. clientUserId
B. templateId
C. brandId
D. envelopeId before creation

**Answer:** A. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Option notes:**
- A. clientUserId can map a form instance to an external record.
- B. templateId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- C. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- D. envelopeId before creation can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.

**Q126. (Agreement Manager API - Agreement documents)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. The records team wants agreement data available to downstream reporting and lifecycle processes after signature. In the current design, a downstream system needs a copy of an agreement document. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Option notes:**
- A. A Web Forms client SDK only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- B. A Connect listener with no API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- C. A bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Document download using Agreement Manager capabilities: Agreement Manager API scenarios include retrieving agreement documents and metadata.
- D. Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q127. (Workflow Builder and Workflow API - Runtime errors)** Priya, a platform engineer at a legal operations team, is reducing support tickets caused by inconsistent envelope handling. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow trigger fails because required starting variables are missing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer inspect?

A. Bulk send list status only
B. Workflow trigger requirements and variable mapping
C. Brand destination URLs
D. Connect HMAC secret only

**Answer:** B. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Option notes:**
- A. Bulk send list status only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- B. Workflow trigger requirements define required input variables.
- C. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- D. Connect HMAC secret only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.

**Q128. (App Center and Extension Apps - Manifest)** Amir, a workflow automation engineer at a regional healthcare provider, is adding reusable agreement automation to an existing business application. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, an extension app action must call an external API endpoint. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Option notes:**
- A. Actions in the manifest describe calls to external endpoints.
- B. In an envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- C. In a recipient tab label can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- D. In the Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.

**Q129. (API Authentication - OAuth flow selection)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, a server-side portal can store a client secret and each employee signs in interactively. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- B. Public Authorization Code Grant with PKCE can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Confidential Authorization Code Grant.
- D. Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q130. (Go Live Process - Production endpoints)** Noah, an API developer at a banking compliance unit, is building a self-service portal for internal teams and external customers. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, after go-live, API calls still point to demo endpoints. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be changed?

A. Use production base URIs and production API endpoints
B. Keep demo endpoints and change only the email subject
C. Use a Connect listener as the base URI
D. Replace all templates with web forms

**Answer:** A. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Option notes:**
- A. Production integrations must call production endpoints and the correct account base URI.
- B. Keep demo endpoints and change only the email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- C. Use a Connect listener as the base URI can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- D. Replace all templates with web forms can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.

**Q131. (Docusign Connect - Envelope-level Connect)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a single high-value envelope needs a callback URL different from account-level settings. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Option notes:**
- A. Create a Web Form instance can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- B. Use Workflow Builder only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- C. Set the envelope status to created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- D. The eventNotification object configures per-envelope Connect callbacks.

**Q132. (eSignature API - Template reference)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a request uses a server template already stored in Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Option notes:**
- A. clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- B. returnUrl can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- C. basePath can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- D. templateId references an existing template in an envelope request.

**Q133. (eSignature Features and Web Forms - Identity verification)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, an envelope must require recipients to prove identity before signing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be included in the recipient configuration?

A. A Connect retry policy
B. A workflow extension action
C. A template name only
D. An identity verification or recipient authentication configuration

**Answer:** D. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Option notes:**
- A. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- B. A workflow extension action can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- C. A template name only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- D. Recipient authentication or ID verification settings enforce identity checks.

**Q134. (Agreement Manager API - Agreement data)** Noah, an API developer at a banking compliance unit, is moving a pilot integration from a developer account toward production. The organization is modernizing legacy agreement records and needs API access to agreement metadata and documents. In the current design, a custom app needs structured extracted data for a specific agreement. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Option notes:**
- A. Workflow trigger requirements can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- B. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.
- C. Agreements:getAgreement retrieves agreement data for a specific agreement.
- D. Envelopes:create can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Agreements:getAgreement: Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q135. (Workflow Builder and Workflow API - Embedding workflow)** Luca, a developer on the IAM team at a sales contract automation team, is building a self-service portal for internal teams and external customers. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a custom app needs to display a workflow experience inside the app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which capability should be considered?

A. Embedding or launching the workflow according to its configured start method
B. Envelope purge
C. JWT admin consent only
D. Agreement type extraction only

**Answer:** A. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Option notes:**
- A. Workflow integration depends on the configured start method and embedding/launch pattern.
- B. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- C. JWT admin consent only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- D. Agreement type extraction only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.

**Q136. (App Center and Extension Apps - Connections)** Grace, a product owner at a university financial-aid office, is automating high-volume agreement work while keeping auditability intact. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an action must use external OAuth credentials. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Option notes:**
- A. publisher only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- B. brandColors can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- C. bulkCopies can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- D. The connections object defines authentication configuration used by actions.

**Q137. (API Authentication - OAuth flow selection)** Amir, a workflow automation engineer at a regional healthcare provider, is connecting several line-of-business systems to Docusign APIs. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, a browser-only single-page application cannot protect a client secret but must authenticate each individual user. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- B. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Public Authorization Code Grant with PKCE.
- C. Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q138. (Go Live Process - Templates in production)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, an app uses a template reference model in demo. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What is required for production?

A. Reuse the demo template ID
B. Switch to JWT Grant
C. Enable CORS only
D. Deploy or recreate the template in production and update the template ID

**Answer:** D. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Option notes:**
- A. Reuse the demo template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- B. Switch to JWT Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- C. Enable CORS only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- D. Template IDs differ between environments; the production template must be referenced.

**Q139. (Docusign Connect - Connect vs polling)** Mateo, a DevOps engineer at a procurement shared-services group, is connecting several line-of-business systems to Docusign APIs. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a system must learn when recipients complete signing without excessive API calls. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Option notes:**
- A. Wait for users to forward emails can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- B. Use a template reference model can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- C. Connect pushes events and avoids high-volume polling.
- D. Poll EnvelopeRecipients:list every second can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.

**Q140. (eSignature API - Composite templates)** Noah, an API developer at a banking compliance unit, is moving a pilot integration from a developer account toward production. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a request must combine server templates, inline recipient data, and documents. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Option notes:**
- A. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- B. Connect 2.0 only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- C. Composite templates allow combining server templates, inline templates, and documents.
- D. Bulk send list only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.

**Q141. (eSignature Features and Web Forms - Recipient authentication)** Luca, a developer on the IAM team at a sales contract automation team, is moving a pilot integration from a developer account toward production. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, a signer should receive a one-time code before accessing the envelope. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature category applies?

A. Agreement Manager extraction
B. App Center listing
C. Recipient authentication
D. Bulk Send only

**Answer:** C. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Option notes:**
- A. Agreement Manager extraction can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- B. App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- C. Recipient authentication controls access to signing.
- D. Bulk Send only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.

**Q142. (Agreement Manager API - Agreement list)** Elena, an implementation consultant at a partner-built customer portal, is reducing support tickets caused by inconsistent envelope handling. The integration must retrieve agreement information without confusing envelope execution data with agreement repository data. In the current design, an app needs to find agreements matching criteria before retrieving details. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Option notes:**
- A. Configure CORS origins can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- B. Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- C. Create an envelope with status voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.
- D. Use only brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to List or search agreements, then retrieve the target agreement: Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q143. (Workflow Builder and Workflow API - Installed extensions)** Sofia, a business systems analyst at a multinational HR operations team, is replacing a manual agreement process with a Docusign IAM integration. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, a workflow should call a third-party service through an extension app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be true?

A. The envelope must be voided first
B. The app must use implicit grant
C. The Web Form must be public
D. The extension app must be installed and available for the workflow step

**Answer:** D. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Option notes:**
- A. The envelope must be voided first can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- B. The app must use implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- C. The Web Form must be public can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- D. Workflow Builder can use installed extension applications in extension steps.

**Q144. (App Center and Extension Apps - connectionsReference)** Mateo, a DevOps engineer at a procurement shared-services group, is moving a pilot integration from a developer account toward production. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, an action needs to use a named connection from the manifest. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Option notes:**
- A. transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- B. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- C. connectionsReference ties an action to a connection definition.
- D. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.

**Q145. (API Authentication - JWT Grant)** Grace, a product owner at a university financial-aid office, is standardizing how agreements are prepared, sent, monitored, and stored. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing JWT Grant, and the better fit is JSON Web Token Grant.
- B. JWT Grant supports non-interactive service integrations after consent has been granted.
- C. Public Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.

**Q146. (Go Live Process - Post go-live)** Amir, a workflow automation engineer, is reviewing a Docusign implementation for a regional healthcare provider. The relevant requirement is that a promoted integration key uses Confidential Authorization Code Grant. What should be validated immediately after go-live?

A. The user's browser zoom level
B. Template color branding only
C. Production redirect URIs, secrets, base URI, and consent
D. Recipient tab labels only

**Answer:** C. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Option notes:**
- A. The user's browser zoom level can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- B. Template color branding only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- C. OAuth and endpoint settings often need production-specific validation.
- D. Recipient tab labels only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.

**Q147. (Docusign Connect - Configuration level)** Maya, an integration lead at a public-sector records department, is standardizing how agreements are prepared, sent, monitored, and stored. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a company wants one webhook for events across all accounts in its Docusign organization. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Option notes:**
- A. A Web Forms clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- B. Organization-level Connect centralizes events across accounts in the organization.
- C. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- D. Recipient-only Connect in each template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.

**Q148. (eSignature API - Anchor tabs)** Elena, an implementation consultant at a partner-built customer portal, is reducing support tickets caused by inconsistent envelope handling. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a document can vary in page length, but the signature should appear near a specific text string. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Option notes:**
- A. CORS origin settings can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- B. Anchor tabs place fields relative to document text.
- C. Fixed x/y coordinates only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- D. Branding resource files can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.

**Q149. (eSignature Features and Web Forms - Brand destination URLs)** Sofia, a business systems analyst at a multinational HR operations team, is reducing support tickets caused by inconsistent envelope handling. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, remote signers should be redirected to a custom page after finishing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which branding feature is relevant?

A. Bulk send list ID
B. Brand destination URLs
C. Envelope transactionId
D. JWT consent URL

**Answer:** B. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Option notes:**
- A. Bulk send list ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- B. Brand destination URLs control post-signing redirect destinations for remote signing.
- C. Envelope transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- D. JWT consent URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.

**Q150. (Workflow Builder and Workflow API - Workflow steps)** Noah, an API developer, is reviewing a Docusign implementation for a banking compliance unit. The relevant requirement is that a workflow must collect form data before sending a document for signature. Which step order best fits?

A. Archive first, then start
B. Void envelope, then collect data
C. Collect Data with Web Forms, then Get Signatures
D. Get Signatures, then collect data

**Answer:** C. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Option notes:**
- A. Archive first, then start can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- B. Void envelope, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- C. Workflow step order should match the business process.
- D. Get Signatures, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.

**Q151. (App Center and Extension Apps - API proxy)** Maya, an integration lead at a public-sector records department, is reducing support tickets caused by inconsistent envelope handling. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, the third-party API format does not match what the extension app action needs. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Option notes:**
- A. Bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- B. An API proxy can mediate between Docusign and the external service.
- C. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- D. Envelope void status can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.

**Q152. (API Authentication - Consent)** Mateo, a DevOps engineer at a procurement shared-services group, is adding reusable agreement automation to an existing business application. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, a JWT integration fails because the user has never granted consent for the requested scopes. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Option notes:**
- A. JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- B. A production account ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- C. A Connect listener URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- D. A new envelope template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q153. (Go Live Process - API limits)** Grace, a product owner, is reviewing a Docusign implementation for a university financial-aid office. The relevant requirement is that an integration repeatedly polls envelopes every few seconds for status. Which improvement best aligns with API usage guidelines?

A. Move all status into email subject lines
B. Use Connect webhooks for event-driven status updates
C. Increase polling frequency
D. Create duplicate envelopes for retry

**Answer:** B. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Option notes:**
- A. Move all status into email subject lines can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- B. Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- C. Increase polling frequency can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- D. Create duplicate envelopes for retry can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q154. (Docusign Connect - JSON SIM)** Daniel, a solutions architect at a commercial real-estate group, is adding reusable agreement automation to an existing business application. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a workflow event must be delivered to a custom listener. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Option notes:**
- A. Workflow events rely on the JSON SIM event model.
- B. Legacy XML only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- C. CSV export format can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- D. PDF attachment only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.

**Q155. (eSignature API - Embedded signing)** Amir, a workflow automation engineer at a regional healthcare provider, is building a self-service portal for internal teams and external customers. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a recipient must sign inside the host app rather than through an email link. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Option notes:**
- A. clientUserId identifies a captive/embedded recipient.
- B. emailNotification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- C. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- D. listId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.

**Q156. (eSignature Features and Web Forms - Connected Fields)** Noah, an API developer at a banking compliance unit, is building a self-service portal for internal teams and external customers. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, a signer-provided value must be checked against an external data source during signing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature supports this?

A. Connected Fields or data verification
B. Agreement import only
C. Envelope purge
D. Safe Exam Browser

**Answer:** A. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Option notes:**
- A. Connected Fields and data verification support real-time validation scenarios.
- B. Agreement import only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- D. Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.

**Q157. (Workflow Builder and Workflow API - Identity step)** Elena, an implementation consultant, is reviewing a Docusign implementation for a partner-built customer portal. The relevant requirement is that a process must gather participant data and then verify identity. Which sequence is best?

A. Connect retry before web form
B. Collect Data with Web Forms, then Verify Someone's Identity
C. Verify identity after archiving only
D. Get Signatures before collecting data

**Answer:** B. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Option notes:**
- A. Connect retry before web form can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- B. Collect required data before the identity verification step if the scenario requires it.
- C. Verify identity after archiving only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- D. Get Signatures before collecting data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.

**Q158. (App Center and Extension Apps - Firewall)** Daniel, a solutions architect at a commercial real-estate group, is building a self-service portal for internal teams and external customers. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, docusign must call a customer-hosted endpoint for an extension action. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Option notes:**
- A. The external endpoint must be reachable by Docusign.
- B. Disable all OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- C. Use only demo endpoints can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- D. Delete the app manifest can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.

**Q159. (API Authentication - Scopes)** Maya, an integration lead at a public-sector records department, is automating high-volume agreement work while keeping auditability intact. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, an app only needs to send envelopes and read user account information. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Option notes:**
- A. Request every Docusign scope to avoid future changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- B. Omit scopes because Docusign infers them can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- C. Use account-level Connect settings as scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- D. Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q160. (Go Live Process - Troubleshooting)** In a quick architecture review, the team wants the best answer without extra workflow context. What should be checked first?

A. Production OAuth settings, redirect URI, consent, and account base URI
B. Whether demo envelopes are legally binding
C. Whether recipients use the same browser
D. Whether document tabs are locked

**Answer:** A. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Option notes:**
- A. Common post-go-live issues are environment and OAuth configuration mismatches.
- B. Whether demo envelopes are legally binding can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- C. Whether recipients use the same browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- D. Whether document tabs are locked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.

**Q161. (Docusign Connect - Security)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a listener must verify that incoming webhook messages really came from Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Option notes:**
- A. Changing the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- B. Using clientUserId on every signer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- C. Adding a brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- D. HMAC and authentication settings help secure Connect listeners.

**Q162. (eSignature API - Signing URL)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, an app has created an envelope for an embedded recipient. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Option notes:**
- A. A Connect JSON SIM event can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- B. A bulk send batch ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- C. A brand resource file can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- D. Embedded signing requires requesting a short-lived recipient view URL.

**Q163. (eSignature Features and Web Forms - ID Evidence)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, a system must retrieve retained data about a completed ID Verification event. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which API is relevant?

A. Web Forms API only
B. BulkSend API
C. WorkflowInstanceManagement only
D. ID Evidence API

**Answer:** D. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Option notes:**
- A. Web Forms API only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- B. BulkSend API can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- C. WorkflowInstanceManagement only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- D. The ID Evidence API retrieves retained evidence from ID verification events.

**Q164. (Workflow Builder and Workflow API - Extension step)** In a quick architecture review, the team wants the best answer without extra workflow context. Which workflow step type is appropriate?

A. Extension step using a file/archive extension app
B. Branching rule only
C. Get Signatures step only
D. CORS configuration

**Answer:** A. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Option notes:**
- A. Extension steps call external services through installed extension apps.
- B. Branching rule only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- C. Get Signatures step only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- D. CORS configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.

**Q165. (App Center and Extension Apps - Data IO)** Priya, a platform engineer at a legal operations team, is replacing a manual agreement process with a Docusign IAM integration. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a workflow needs to read and write structured records in another system. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Option notes:**
- A. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- B. Branding extension can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Data IO, and the better fit is Data IO extension app.
- D. Data IO extensions read/write structured data.

**Q166. (API Authentication - User info)** Daniel, a solutions architect, is reviewing a Docusign implementation for a commercial real-estate group. The relevant requirement is that after receiving an access token, the app must determine which base URI and account ID to use for API calls. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Option notes:**
- A. /oauth/token can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- B. /connect/events can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- C. The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- D. /restapi/v2.1/accounts can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q167. (Go Live Process - Go-live setup)** Maya, an integration lead at a public-sector records department, is automating high-volume agreement work while keeping auditability intact. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, a developer promotes an integration key from demo to production. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which configuration commonly must be recreated in production?

A. Completed demo envelopes
B. Envelope IDs
C. Connect event logs
D. Redirect URIs and secret keys

**Answer:** D. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Option notes:**
- A. Completed demo envelopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- B. Envelope IDs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- C. Connect event logs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- D. Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q168. (Docusign Connect - Retries)** Luca, a developer on the IAM team, is reviewing a Docusign implementation for a sales contract automation team. The relevant requirement is that a listener is temporarily unavailable when Docusign sends an event. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Option notes:**
- A. The integration key is revoked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- B. The recipient must sign again can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- C. Connect has retry behavior for delivery failures; listeners should be idempotent.
- D. The envelope is automatically voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q169. (eSignature API - Embedded signing timing)** Mateo, a DevOps engineer, is reviewing a Docusign implementation for a procurement shared-services group. The relevant requirement is that an app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Option notes:**
- A. The account base URI disappears can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- B. Connect retries stop can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- C. Embedded signing URLs are short-lived and should be generated when the user is ready.
- D. The template ID changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q170. (eSignature Features and Web Forms - Web Forms embedding)** Amir, a workflow automation engineer, is reviewing a Docusign implementation for a regional healthcare provider. The relevant requirement is that a custom website needs to render a Docusign Web Form instance inline. What client-side component is used with the instance URL?

A. Connect JSON SIM
B. Workflow start link only
C. Docusign JS client SDK
D. EnvelopeViews:createRecipient

**Answer:** C. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Option notes:**
- A. Connect JSON SIM can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- B. Workflow start link only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- C. Docusign JS renders Web Form instances in the host page.
- D. EnvelopeViews:createRecipient can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.

**Q171. (Workflow Builder and Workflow API - Branching)** Grace, a product owner at a university financial-aid office, is automating high-volume agreement work while keeping auditability intact. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow should follow different paths based on a form response. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow capability is used?

A. JWT consent
B. Envelope purge
C. Brand destination URL
D. Branching or conditional rules

**Answer:** D. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Option notes:**
- A. JWT consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- B. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- C. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- D. Branching rules route workflows based on conditions.

**Q172. (App Center and Extension Apps - File IO)** Luca, a developer on the IAM team, is reviewing a Docusign implementation for a sales contract automation team. The relevant requirement is that a workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Option notes:**
- A. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- B. CORS origin only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- C. File IO extensions handle document storage and retrieval use cases.
- D. Connected Fields only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.

**Q173. (API Authentication - PKCE)** Priya, a platform engineer, is reviewing a Docusign implementation for a legal operations team. The relevant requirement is that a native app cannot store a client secret securely. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Option notes:**
- A. A template password can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- B. PKCE mitigates interception risk for public clients that cannot keep a client secret.
- C. An HMAC secret on each envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- D. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q174. (Go Live Process - Integration classification)** Daniel, a solutions architect at a commercial real-estate group, is moving a pilot integration from a developer account toward production. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, a partner app will be distributed for many customers to install. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which go-live classification best reflects the use case?

A. One-time manual sending workflow
B. Template-only configuration
C. ISV or partner-distributed integration
D. Internal employee-only integration

**Answer:** C. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Option notes:**
- A. One-time manual sending workflow can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- B. Template-only configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- C. Classification should match how the integration is used and distributed.
- D. Internal employee-only integration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.

**Q175. (Docusign Connect - Troubleshooting)** Sofia, a business systems analyst, is reviewing a Docusign implementation for a multinational HR operations team. The relevant requirement is that a listener receives duplicate webhook messages. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Option notes:**
- A. Use a different template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- B. Webhook systems should tolerate retries and duplicate delivery.
- C. Treat every duplicate as a new envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- D. Disable OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.

**Q176. (eSignature API - Embedded sending)** Maya, an integration lead, is reviewing a Docusign implementation for a public-sector records department. The relevant requirement is that a sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Option notes:**
- A. Connect retry log can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- B. Embedded sending uses a sender view URL.
- C. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- D. Agreements:getAgreement can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.

**Q177. (eSignature Features and Web Forms - Web Form correlation)** Grace, a product owner, is reviewing a Docusign implementation for a university financial-aid office. The relevant requirement is that an app creates one Web Form instance per customer record. Which value should be supplied to correlate back to the app?

A. envelopeId before creation
B. clientUserId
C. templateId
D. brandId

**Answer:** B. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Option notes:**
- A. envelopeId before creation can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- B. clientUserId can map a form instance to an external record.
- C. templateId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- D. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.

**Q178. (Workflow Builder and Workflow API - Start method)** Mateo, a DevOps engineer at a procurement shared-services group, is moving a pilot integration from a developer account toward production. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a portal link should launch a workflow and pass values in the trigger URL. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method fits?

A. From an envelope void event only
B. From a bulk send batch only
C. From a Link
D. Manually by someone in your organization only

**Answer:** C. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Option notes:**
- A. From an envelope void event only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- B. From a bulk send batch only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- C. A link start method can launch a workflow and pass URL values.
- D. Manually by someone in your organization only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.

**Q179. (App Center and Extension Apps - Connected Fields)** Sofia, a business systems analyst, is reviewing a Docusign implementation for a multinational HR operations team. The relevant requirement is that an extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Option notes:**
- A. Agreement list search can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- B. Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- C. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- D. Go-live classification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q180. (API Authentication - Bearer tokens)** In a quick architecture review, the team wants the best answer without extra workflow context. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Option notes:**
- A. Docusign REST calls use Authorization: Bearer <access_token>.
- B. In the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- C. In the Connect eventNotification object can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- D. In the templateId field can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.

**Q181. (Go Live Process - Production endpoints)** Priya, a platform engineer at a legal operations team, is reducing support tickets caused by inconsistent envelope handling. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, after go-live, API calls still point to demo endpoints. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be changed?

A. Replace all templates with web forms
B. Use production base URIs and production API endpoints
C. Keep demo endpoints and change only the email subject
D. Use a Connect listener as the base URI

**Answer:** B. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Option notes:**
- A. Replace all templates with web forms can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- B. Production integrations must call production endpoints and the correct account base URI.
- C. Keep demo endpoints and change only the email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- D. Use a Connect listener as the base URI can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.

**Q182. (Docusign Connect - Payload selection)** In a quick architecture review, the team wants the best answer without extra workflow context. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Option notes:**
- A. Connect payload options should match data minimization and processing needs.
- B. Switch to implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- C. Use recipient authentication instead can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- D. Create a bulk send list can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.

**Q183. (eSignature API - Bulk send)** In a quick architecture review, the team wants the best answer without extra workflow context. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

**Option notes:**
- A. Bulk Send supports large batches of personalized envelopes.
- B. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- C. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- D. Organization Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.

**Q184. (eSignature Features and Web Forms - Identity verification)** In a quick architecture review, the team wants the best answer without extra workflow context. What must be included in the recipient configuration?

A. An identity verification or recipient authentication configuration
B. A Connect retry policy
C. A workflow extension action
D. A template name only

**Answer:** A. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Option notes:**
- A. Recipient authentication or ID verification settings enforce identity checks.
- B. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- C. A workflow extension action can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- D. A template name only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.

**Q185. (Workflow Builder and Workflow API - API trigger)** Maya, an integration lead at a public-sector records department, is reducing support tickets caused by inconsistent envelope handling. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, a backend service must programmatically trigger a workflow. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method/API pattern is relevant?

A. Template reference ID only
B. From an API call with Workflow Builder API trigger requirements
C. Remote signing email only
D. Brand resource file upload

**Answer:** B. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Option notes:**
- A. Template reference ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- B. API-triggered workflows use trigger requirements and workflow API calls.
- C. Remote signing email only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- D. Brand resource file upload can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.

**Q186. (App Center and Extension Apps - Data Verification)** In a quick architecture review, the team wants the best answer without extra workflow context. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

**Option notes:**
- A. Data Verification checks signer-entered data during the signing experience.
- B. Public Auth Code only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- D. Agreement Manager import can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.

**Q187. (API Authentication - OAuth flow selection)** Sofia, a business systems analyst at a multinational HR operations team, is replacing a manual agreement process with a Docusign IAM integration. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a server-side portal can store a client secret and each employee signs in interactively. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- B. Public Authorization Code Grant with PKCE can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Confidential Authorization Code Grant.
- D. Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q188. (Go Live Process - Templates in production)** Luca, a developer on the IAM team at a sales contract automation team, is building a self-service portal for internal teams and external customers. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, an app uses a template reference model in demo. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What is required for production?

A. Deploy or recreate the template in production and update the template ID
B. Reuse the demo template ID
C. Switch to JWT Grant
D. Enable CORS only

**Answer:** A. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Option notes:**
- A. Template IDs differ between environments; the production template must be referenced.
- B. Reuse the demo template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- C. Switch to JWT Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- D. Enable CORS only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.

**Q189. (Docusign Connect - Envelope-level Connect)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a single high-value envelope needs a callback URL different from account-level settings. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Option notes:**
- A. Create a Web Form instance can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- B. Use Workflow Builder only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- C. Set the envelope status to created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- D. The eventNotification object configures per-envelope Connect callbacks.

**Q190. (eSignature API - Envelope create)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, an integration needs to send an envelope for signature immediately. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- B. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- D. Status sent sends the envelope; created saves it as a draft.

**Q191. (eSignature Features and Web Forms - Recipient authentication)** Maya, an integration lead at a public-sector records department, is automating high-volume agreement work while keeping auditability intact. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, a signer should receive a one-time code before accessing the envelope. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature category applies?

A. Bulk Send only
B. Agreement Manager extraction
C. App Center listing
D. Recipient authentication

**Answer:** D. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Option notes:**
- A. Bulk Send only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- B. Agreement Manager extraction can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- C. App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- D. Recipient authentication controls access to signing.

**Q192. (Workflow Builder and Workflow API - Runtime errors)** Daniel, a solutions architect at a commercial real-estate group, is building a self-service portal for internal teams and external customers. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow trigger fails because required starting variables are missing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer inspect?

A. Workflow trigger requirements and variable mapping
B. Brand destination URLs
C. Connect HMAC secret only
D. Bulk send list status only

**Answer:** A. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Option notes:**
- A. Workflow trigger requirements define required input variables.
- B. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- C. Connect HMAC secret only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- D. Bulk send list status only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.

**Q193. (App Center and Extension Apps - Extension app role)** Elena, an implementation consultant at a partner-built customer portal, is automating high-volume agreement work while keeping auditability intact. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, a customer wants Docusign to call an external service during an agreement process. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Option notes:**
- A. A replacement for OAuth consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- B. Unlimited eSignature API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- C. A mandatory PDF renderer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- D. Extension apps extend Docusign with external service actions and data.

**Q194. (API Authentication - OAuth flow selection)** Noah, an API developer at a banking compliance unit, is connecting several line-of-business systems to Docusign APIs. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, a browser-only single-page application cannot protect a client secret but must authenticate each individual user. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- B. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Public Authorization Code Grant with PKCE.
- C. Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q195. (Go Live Process - Post go-live)** Sofia, a business systems analyst at a multinational HR operations team, is replacing a manual agreement process with a Docusign IAM integration. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, a promoted integration key uses Confidential Authorization Code Grant. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should be validated immediately after go-live?

A. Recipient tab labels only
B. The user's browser zoom level
C. Template color branding only
D. Production redirect URIs, secrets, base URI, and consent

**Answer:** D. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Option notes:**
- A. Recipient tab labels only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- B. The user's browser zoom level can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- C. Template color branding only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- D. OAuth and endpoint settings often need production-specific validation.

**Q196. (Docusign Connect - Connect vs polling)** Amir, a workflow automation engineer at a regional healthcare provider, is connecting several line-of-business systems to Docusign APIs. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a system must learn when recipients complete signing without excessive API calls. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Option notes:**
- A. Wait for users to forward emails can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- B. Use a template reference model can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- C. Connect pushes events and avoids high-volume polling.
- D. Poll EnvelopeRecipients:list every second can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.

**Q197. (eSignature API - Draft envelope)** Luca, a developer on the IAM team at a sales contract automation team, is moving a pilot integration from a developer account toward production. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a developer wants to create an envelope but not send it yet. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Option notes:**
- A. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- B. completed can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- C. The created status keeps an envelope in draft state.
- D. sent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.

**Q198. (eSignature Features and Web Forms - Brand destination URLs)** Daniel, a solutions architect at a commercial real-estate group, is moving a pilot integration from a developer account toward production. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, remote signers should be redirected to a custom page after finishing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which branding feature is relevant?

A. JWT consent URL
B. Bulk send list ID
C. Brand destination URLs
D. Envelope transactionId

**Answer:** C. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Option notes:**
- A. JWT consent URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- B. Bulk send list ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- C. Brand destination URLs control post-signing redirect destinations for remote signing.
- D. Envelope transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.

**Q199. (Workflow Builder and Workflow API - Embedding workflow)** Priya, a platform engineer at a legal operations team, is replacing a manual agreement process with a Docusign IAM integration. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a custom app needs to display a workflow experience inside the app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which capability should be considered?

A. Envelope purge
B. JWT admin consent only
C. Agreement type extraction only
D. Embedding or launching the workflow according to its configured start method

**Answer:** D. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Option notes:**
- A. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- B. JWT admin consent only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- C. Agreement type extraction only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- D. Workflow integration depends on the configured start method and embedding/launch pattern.

**Q200. (App Center and Extension Apps - Public vs private)** Amir, a workflow automation engineer at a regional healthcare provider, is moving a pilot integration from a developer account toward production. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an app is only for one organization's internal Docusign accounts. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Public vs private, and the better fit is Private extension app.
- B. Recipient Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.
- C. Private apps are limited to selected accounts or the publisher's organization.
- D. Public App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.

**Q201. (API Authentication - JWT Grant)** Elena, an implementation consultant at a partner-built customer portal, is standardizing how agreements are prepared, sent, monitored, and stored. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, a scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing JWT Grant, and the better fit is JSON Web Token Grant.
- B. JWT Grant supports non-interactive service integrations after consent has been granted.
- C. Public Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.

**Q202. (Go Live Process - API limits)** Noah, an API developer at a banking compliance unit, is connecting several line-of-business systems to Docusign APIs. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, an integration repeatedly polls envelopes every few seconds for status. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which improvement best aligns with API usage guidelines?

A. Create duplicate envelopes for retry
B. Move all status into email subject lines
C. Use Connect webhooks for event-driven status updates
D. Increase polling frequency

**Answer:** C. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Option notes:**
- A. Create duplicate envelopes for retry can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- B. Move all status into email subject lines can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- C. Webhooks reduce unnecessary polling and help avoid resource-limit issues.
- D. Increase polling frequency can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use Connect webhooks for event-driven status updates: Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q203. (Docusign Connect - Configuration level)** Grace, a product owner at a university financial-aid office, is standardizing how agreements are prepared, sent, monitored, and stored. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a company wants one webhook for events across all accounts in its Docusign organization. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Option notes:**
- A. A Web Forms clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- B. Organization-level Connect centralizes events across accounts in the organization.
- C. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- D. Recipient-only Connect in each template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.

**Q204. (eSignature API - Cancel envelope)** Sofia, a business systems analyst at a multinational HR operations team, is reducing support tickets caused by inconsistent envelope handling. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a sent envelope has a fatal error and no one should sign it. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- B. Voiding cancels an in-process envelope and stops signing.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- D. purged can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.

**Q205. (eSignature Features and Web Forms - Connected Fields)** Priya, a platform engineer at a legal operations team, is reducing support tickets caused by inconsistent envelope handling. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, a signer-provided value must be checked against an external data source during signing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature supports this?

A. Safe Exam Browser
B. Connected Fields or data verification
C. Agreement import only
D. Envelope purge

**Answer:** B. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Option notes:**
- A. Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- B. Connected Fields and data verification support real-time validation scenarios.
- C. Agreement import only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.
- D. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields or data verification: Connected Fields and data verification support real-time validation scenarios.

**Q206. (Workflow Builder and Workflow API - Installed extensions)** Luca, a developer on the IAM team at a sales contract automation team, is connecting several line-of-business systems to Docusign APIs. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, a workflow should call a third-party service through an extension app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be true?

A. The app must use implicit grant
B. The Web Form must be public
C. The extension app must be installed and available for the workflow step
D. The envelope must be voided first

**Answer:** C. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Option notes:**
- A. The app must use implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- B. The Web Form must be public can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- C. Workflow Builder can use installed extension applications in extension steps.
- D. The envelope must be voided first can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.

**Q207. (App Center and Extension Apps - Public App Center)** Grace, a product owner at a university financial-aid office, is reducing support tickets caused by inconsistent envelope handling. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a partner wants customers broadly to discover and install an app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Option notes:**
- A. Demo-only template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- B. Public App Center distribution is for broad customer availability.
- C. Private app for one account only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.

**Q208. (API Authentication - Consent)** Amir, a workflow automation engineer at a regional healthcare provider, is adding reusable agreement automation to an existing business application. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a JWT integration fails because the user has never granted consent for the requested scopes. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Option notes:**
- A. JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- B. A production account ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- C. A Connect listener URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- D. A new envelope template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q209. (Go Live Process - Troubleshooting)** Elena, an implementation consultant at a partner-built customer portal, is standardizing how agreements are prepared, sent, monitored, and stored. The pilot works in demo, but stakeholders now want the integration promoted without breaking existing users. In the current design, a production app fails after go-live with authentication errors, but worked in demo. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should be checked first?

A. Whether document tabs are locked
B. Production OAuth settings, redirect URI, consent, and account base URI
C. Whether demo envelopes are legally binding
D. Whether recipients use the same browser

**Answer:** B. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Option notes:**
- A. Whether document tabs are locked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- B. Common post-go-live issues are environment and OAuth configuration mismatches.
- C. Whether demo envelopes are legally binding can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.
- D. Whether recipients use the same browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production OAuth settings, redirect URI, consent, and account base URI: Common post-go-live issues are environment and OAuth configuration mismatches.

**Q210. (Docusign Connect - JSON SIM)** Mateo, a DevOps engineer at a procurement shared-services group, is adding reusable agreement automation to an existing business application. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a workflow event must be delivered to a custom listener. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Option notes:**
- A. Workflow events rely on the JSON SIM event model.
- B. Legacy XML only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- C. CSV export format can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- D. PDF attachment only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.

**Q211. (eSignature API - Idempotency)** Noah, an API developer at a banking compliance unit, is building a self-service portal for internal teams and external customers. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a network retry might submit the same create-envelope request twice. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Option notes:**
- A. Supplying a transactionId supports idempotent envelope creation.
- B. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- C. retryId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- D. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.

**Q212. (eSignature Features and Web Forms - ID Evidence)** Luca, a developer on the IAM team at a sales contract automation team, is building a self-service portal for internal teams and external customers. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, a system must retrieve retained data about a completed ID Verification event. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which API is relevant?

A. ID Evidence API
B. Web Forms API only
C. BulkSend API
D. WorkflowInstanceManagement only

**Answer:** A. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Option notes:**
- A. The ID Evidence API retrieves retained evidence from ID verification events.
- B. Web Forms API only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- C. BulkSend API can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.
- D. WorkflowInstanceManagement only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ID Evidence API: The ID Evidence API retrieves retained evidence from ID verification events.

**Q213. (Workflow Builder and Workflow API - Workflow steps)** Sofia, a business systems analyst at a multinational HR operations team, is standardizing how agreements are prepared, sent, monitored, and stored. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow must collect form data before sending a document for signature. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which step order best fits?

A. Void envelope, then collect data
B. Collect Data with Web Forms, then Get Signatures
C. Get Signatures, then collect data
D. Archive first, then start

**Answer:** B. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Option notes:**
- A. Void envelope, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- B. Workflow step order should match the business process.
- C. Get Signatures, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- D. Archive first, then start can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.

**Q214. (App Center and Extension Apps - Manifest)** Mateo, a DevOps engineer at a procurement shared-services group, is building a self-service portal for internal teams and external customers. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, an extension app action must call an external API endpoint. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Option notes:**
- A. Actions in the manifest describe calls to external endpoints.
- B. In an envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- C. In a recipient tab label can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- D. In the Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.

**Q215. (API Authentication - Scopes)** Grace, a product owner at a university financial-aid office, is automating high-volume agreement work while keeping auditability intact. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, an app only needs to send envelopes and read user account information. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Option notes:**
- A. Request every Docusign scope to avoid future changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- B. Omit scopes because Docusign infers them can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- C. Use account-level Connect settings as scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- D. Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q216. (Go Live Process - Go-live setup)** Amir, a workflow automation engineer at a regional healthcare provider, is adding reusable agreement automation to an existing business application. The release manager is preparing production readiness evidence and wants to avoid common go-live delays. In the current design, a developer promotes an integration key from demo to production. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which configuration commonly must be recreated in production?

A. Redirect URIs and secret keys
B. Completed demo envelopes
C. Envelope IDs
D. Connect event logs

**Answer:** A. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Option notes:**
- A. Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- B. Completed demo envelopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- C. Envelope IDs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.
- D. Connect event logs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Redirect URIs and secret keys: Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q217. (Docusign Connect - Security)** Maya, an integration lead at a public-sector records department, is automating high-volume agreement work while keeping auditability intact. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a listener must verify that incoming webhook messages really came from Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Option notes:**
- A. Changing the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- B. Using clientUserId on every signer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- C. Adding a brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to HMAC validation or supported Connect authentication: HMAC and authentication settings help secure Connect listeners.
- D. HMAC and authentication settings help secure Connect listeners.

**Q218. (eSignature API - Template reference)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a request uses a server template already stored in Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Option notes:**
- A. clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- B. returnUrl can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- C. basePath can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- D. templateId references an existing template in an envelope request.

**Q219. (eSignature Features and Web Forms - Web Forms embedding)** Sofia, a business systems analyst at a multinational HR operations team, is replacing a manual agreement process with a Docusign IAM integration. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, a custom website needs to render a Docusign Web Form instance inline. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What client-side component is used with the instance URL?

A. EnvelopeViews:createRecipient
B. Connect JSON SIM
C. Workflow start link only
D. Docusign JS client SDK

**Answer:** D. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Option notes:**
- A. EnvelopeViews:createRecipient can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- B. Connect JSON SIM can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- C. Workflow start link only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign JS client SDK: Docusign JS renders Web Form instances in the host page.
- D. Docusign JS renders Web Form instances in the host page.

**Q220. (Workflow Builder and Workflow API - Identity step)** Noah, an API developer at a banking compliance unit, is adding reusable agreement automation to an existing business application. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a process must gather participant data and then verify identity. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which sequence is best?

A. Collect Data with Web Forms, then Verify Someone's Identity
B. Verify identity after archiving only
C. Get Signatures before collecting data
D. Connect retry before web form

**Answer:** A. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Option notes:**
- A. Collect required data before the identity verification step if the scenario requires it.
- B. Verify identity after archiving only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- C. Get Signatures before collecting data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- D. Connect retry before web form can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.

**Q221. (App Center and Extension Apps - Connections)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an action must use external OAuth credentials. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Option notes:**
- A. publisher only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- B. brandColors can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- C. bulkCopies can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- D. The connections object defines authentication configuration used by actions.

**Q222. (API Authentication - User info)** Mateo, a DevOps engineer at a procurement shared-services group, is moving a pilot integration from a developer account toward production. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, after receiving an access token, the app must determine which base URI and account ID to use for API calls. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Option notes:**
- A. /oauth/token can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- B. /connect/events can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- C. The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- D. /restapi/v2.1/accounts can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q223. (Go Live Process - Integration classification)** Grace, a product owner at a university financial-aid office, is automating high-volume agreement work while keeping auditability intact. The team has to distinguish configuration that belongs in demo from configuration that must exist in production. In the current design, a partner app will be distributed for many customers to install. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which go-live classification best reflects the use case?

A. Internal employee-only integration
B. One-time manual sending workflow
C. Template-only configuration
D. ISV or partner-distributed integration

**Answer:** D. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Option notes:**
- A. Internal employee-only integration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- B. One-time manual sending workflow can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- C. Template-only configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to ISV or partner-distributed integration: Classification should match how the integration is used and distributed.
- D. Classification should match how the integration is used and distributed.

**Q224. (Docusign Connect - Retries)** Daniel, a solutions architect at a commercial real-estate group, is moving a pilot integration from a developer account toward production. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a listener is temporarily unavailable when Docusign sends an event. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Option notes:**
- A. The integration key is revoked can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- B. The recipient must sign again can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.
- C. Connect has retry behavior for delivery failures; listeners should be idempotent.
- D. The envelope is automatically voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Docusign retries failed deliveries according to retry rules: Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q225. (eSignature API - Composite templates)** Amir, a workflow automation engineer at a regional healthcare provider, is connecting several line-of-business systems to Docusign APIs. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a request must combine server templates, inline recipient data, and documents. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Option notes:**
- A. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- B. Connect 2.0 only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- C. Composite templates allow combining server templates, inline templates, and documents.
- D. Bulk send list only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.

**Q226. (eSignature Features and Web Forms - Web Form correlation)** Noah, an API developer at a banking compliance unit, is connecting several line-of-business systems to Docusign APIs. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, an app creates one Web Form instance per customer record. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value should be supplied to correlate back to the app?

A. brandId
B. envelopeId before creation
C. clientUserId
D. templateId

**Answer:** C. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Option notes:**
- A. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- B. envelopeId before creation can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.
- C. clientUserId can map a form instance to an external record.
- D. templateId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId can map a form instance to an external record.

**Q227. (Workflow Builder and Workflow API - Extension step)** Elena, an implementation consultant at a partner-built customer portal, is automating high-volume agreement work while keeping auditability intact. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, after signing, the completed document must be stored in an external file service. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow step type is appropriate?

A. Branching rule only
B. Get Signatures step only
C. CORS configuration
D. Extension step using a file/archive extension app

**Answer:** D. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Option notes:**
- A. Branching rule only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- B. Get Signatures step only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- C. CORS configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- D. Extension steps call external services through installed extension apps.

**Q228. (App Center and Extension Apps - connectionsReference)** Daniel, a solutions architect at a commercial real-estate group, is connecting several line-of-business systems to Docusign APIs. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, an action needs to use a named connection from the manifest. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Option notes:**
- A. transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- B. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- C. connectionsReference ties an action to a connection definition.
- D. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.

**Q229. (API Authentication - PKCE)** Maya, an integration lead at a public-sector records department, is reducing support tickets caused by inconsistent envelope handling. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, a native app cannot store a client secret securely. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Option notes:**
- A. A template password can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- B. PKCE mitigates interception risk for public clients that cannot keep a client secret.
- C. An HMAC secret on each envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- D. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q230. (Go Live Process - Production endpoints)** Mateo, a DevOps engineer, is reviewing a Docusign implementation for a procurement shared-services group. The relevant requirement is that after go-live, API calls still point to demo endpoints. What must be changed?

A. Use a Connect listener as the base URI
B. Replace all templates with web forms
C. Use production base URIs and production API endpoints
D. Keep demo endpoints and change only the email subject

**Answer:** C. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Option notes:**
- A. Use a Connect listener as the base URI can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- B. Replace all templates with web forms can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.
- C. Production integrations must call production endpoints and the correct account base URI.
- D. Keep demo endpoints and change only the email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Use production base URIs and production API endpoints: Production integrations must call production endpoints and the correct account base URI.

**Q231. (Docusign Connect - Troubleshooting)** Priya, a platform engineer at a legal operations team, is reducing support tickets caused by inconsistent envelope handling. Operations wants downstream systems updated automatically instead of asking users to refresh screens or run manual checks. In the current design, a listener receives duplicate webhook messages. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Option notes:**
- A. Use a different template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- B. Webhook systems should tolerate retries and duplicate delivery.
- C. Treat every duplicate as a new envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.
- D. Disable OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Idempotent processing based on event identifiers or envelope state: Webhook systems should tolerate retries and duplicate delivery.

**Q232. (eSignature API - Anchor tabs)** Grace, a product owner at a university financial-aid office, is standardizing how agreements are prepared, sent, monitored, and stored. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a document can vary in page length, but the signature should appear near a specific text string. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Option notes:**
- A. CORS origin settings can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- B. Anchor tabs place fields relative to document text.
- C. Fixed x/y coordinates only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- D. Branding resource files can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.

**Q233. (eSignature Features and Web Forms - Identity verification)** Elena, an implementation consultant at a partner-built customer portal, is standardizing how agreements are prepared, sent, monitored, and stored. Business users want structured intake and signer verification without asking developers to rebuild every form from scratch. In the current design, an envelope must require recipients to prove identity before signing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be included in the recipient configuration?

A. A template name only
B. An identity verification or recipient authentication configuration
C. A Connect retry policy
D. A workflow extension action

**Answer:** B. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Option notes:**
- A. A template name only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- B. Recipient authentication or ID verification settings enforce identity checks.
- C. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.
- D. A workflow extension action can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to An identity verification or recipient authentication configuration: Recipient authentication or ID verification settings enforce identity checks.

**Q234. (Workflow Builder and Workflow API - Branching)** Amir, a workflow automation engineer, is reviewing a Docusign implementation for a regional healthcare provider. The relevant requirement is that a workflow should follow different paths based on a form response. Which workflow capability is used?

A. Envelope purge
B. Brand destination URL
C. Branching or conditional rules
D. JWT consent

**Answer:** C. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Option notes:**
- A. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- B. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- C. Branching rules route workflows based on conditions.
- D. JWT consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.

**Q235. (App Center and Extension Apps - API proxy)** Priya, a platform engineer at a legal operations team, is standardizing how agreements are prepared, sent, monitored, and stored. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, the third-party API format does not match what the extension app action needs. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Option notes:**
- A. Bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- B. An API proxy can mediate between Docusign and the external service.
- C. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- D. Envelope void status can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.

**Q236. (API Authentication - Bearer tokens)** Daniel, a solutions architect at a commercial real-estate group, is building a self-service portal for internal teams and external customers. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, a REST API request is returning unauthorized even though the token endpoint returned an access token. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Option notes:**
- A. Docusign REST calls use Authorization: Bearer <access_token>.
- B. In the envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- C. In the Connect eventNotification object can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.
- D. In the templateId field can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In the Authorization header as a Bearer token: Docusign REST calls use Authorization: Bearer <access_token>.

**Q237. (Go Live Process - Templates in production)** Maya, an integration lead, is reviewing a Docusign implementation for a public-sector records department. The relevant requirement is that an app uses a template reference model in demo. What is required for production?

A. Enable CORS only
B. Deploy or recreate the template in production and update the template ID
C. Reuse the demo template ID
D. Switch to JWT Grant

**Answer:** B. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Option notes:**
- A. Enable CORS only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- B. Template IDs differ between environments; the production template must be referenced.
- C. Reuse the demo template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.
- D. Switch to JWT Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Deploy or recreate the template in production and update the template ID: Template IDs differ between environments; the production template must be referenced.

**Q238. (Docusign Connect - Payload selection)** Luca, a developer on the IAM team at a sales contract automation team, is building a self-service portal for internal teams and external customers. The receiving service must handle webhook behavior correctly because events can arrive more than once or be retried. In the current design, a team wants smaller event payloads and will query details separately. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Option notes:**
- A. Connect payload options should match data minimization and processing needs.
- B. Switch to implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- C. Use recipient authentication instead can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.
- D. Create a bulk send list can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Configure the event payload to include only needed data: Connect payload options should match data minimization and processing needs.

**Q239. (eSignature API - Embedded signing)** Mateo, a DevOps engineer at a procurement shared-services group, is adding reusable agreement automation to an existing business application. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a recipient must sign inside the host app rather than through an email link. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Option notes:**
- A. clientUserId identifies a captive/embedded recipient.
- B. emailNotification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- C. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- D. listId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.

**Q240. (eSignature Features and Web Forms - Recipient authentication)** Amir, a workflow automation engineer at a regional healthcare provider, is adding reusable agreement automation to an existing business application. The workflow includes identity, data capture, and routing requirements that must remain tied to the resulting agreement. In the current design, a signer should receive a one-time code before accessing the envelope. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which feature category applies?

A. Recipient authentication
B. Bulk Send only
C. Agreement Manager extraction
D. App Center listing

**Answer:** A. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Option notes:**
- A. Recipient authentication controls access to signing.
- B. Bulk Send only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- C. Agreement Manager extraction can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.
- D. App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Recipient authentication: Recipient authentication controls access to signing.

**Q241. (Workflow Builder and Workflow API - Start method)** Grace, a product owner, is reviewing a Docusign implementation for a university financial-aid office. The relevant requirement is that a portal link should launch a workflow and pass values in the trigger URL. Which start method fits?

A. From a bulk send batch only
B. From a Link
C. Manually by someone in your organization only
D. From an envelope void event only

**Answer:** B. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Option notes:**
- A. From a bulk send batch only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- B. A link start method can launch a workflow and pass URL values.
- C. Manually by someone in your organization only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- D. From an envelope void event only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.

**Q242. (App Center and Extension Apps - Firewall)** Luca, a developer on the IAM team at a sales contract automation team, is adding reusable agreement automation to an existing business application. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, docusign must call a customer-hosted endpoint for an extension action. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Option notes:**
- A. The external endpoint must be reachable by Docusign.
- B. Disable all OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- C. Use only demo endpoints can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- D. Delete the app manifest can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.

**Q243. (API Authentication - OAuth flow selection)** Priya, a platform engineer at a legal operations team, is replacing a manual agreement process with a Docusign IAM integration. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, a server-side portal can store a client secret and each employee signs in interactively. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- B. Public Authorization Code Grant with PKCE can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Confidential Authorization Code Grant: Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Confidential Authorization Code Grant.
- D. Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q244. (Go Live Process - Post go-live)** In a quick architecture review, the team wants the best answer without extra workflow context. What should be validated immediately after go-live?

A. Production redirect URIs, secrets, base URI, and consent
B. Recipient tab labels only
C. The user's browser zoom level
D. Template color branding only

**Answer:** A. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Option notes:**
- A. OAuth and endpoint settings often need production-specific validation.
- B. Recipient tab labels only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- C. The user's browser zoom level can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.
- D. Template color branding only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Production redirect URIs, secrets, base URI, and consent: OAuth and endpoint settings often need production-specific validation.

**Q245. (Docusign Connect - Envelope-level Connect)** Sofia, a business systems analyst at a multinational HR operations team, is replacing a manual agreement process with a Docusign IAM integration. The integration owner is deciding whether to configure notifications globally or for only one envelope workflow. In the current design, a single high-value envelope needs a callback URL different from account-level settings. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Option notes:**
- A. Create a Web Form instance can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- B. Use Workflow Builder only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- C. Set the envelope status to created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Include eventNotification in the envelope creation request: The eventNotification object configures per-envelope Connect callbacks.
- D. The eventNotification object configures per-envelope Connect callbacks.

**Q246. (eSignature API - Signing URL)** Maya, an integration lead at a public-sector records department, is automating high-volume agreement work while keeping auditability intact. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, an app has created an envelope for an embedded recipient. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Option notes:**
- A. A Connect JSON SIM event can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- B. A bulk send batch ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- C. A brand resource file can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- D. Embedded signing requires requesting a short-lived recipient view URL.

**Q247. (eSignature Features and Web Forms - Brand destination URLs)** Grace, a product owner at a university financial-aid office, is automating high-volume agreement work while keeping auditability intact. The team is deciding when to use Docusign platform features instead of custom code around the eSignature API. In the current design, remote signers should be redirected to a custom page after finishing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which branding feature is relevant?

A. Envelope transactionId
B. JWT consent URL
C. Bulk send list ID
D. Brand destination URLs

**Answer:** D. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Option notes:**
- A. Envelope transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- B. JWT consent URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- C. Bulk send list ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Brand destination URLs: Brand destination URLs control post-signing redirect destinations for remote signing.
- D. Brand destination URLs control post-signing redirect destinations for remote signing.

**Q248. (Workflow Builder and Workflow API - API trigger)** In a quick architecture review, the team wants the best answer without extra workflow context. Which start method/API pattern is relevant?

A. From an API call with Workflow Builder API trigger requirements
B. Remote signing email only
C. Brand resource file upload
D. Template reference ID only

**Answer:** A. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Option notes:**
- A. API-triggered workflows use trigger requirements and workflow API calls.
- B. Remote signing email only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- C. Brand resource file upload can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- D. Template reference ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.

**Q249. (App Center and Extension Apps - Data IO)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a workflow needs to read and write structured records in another system. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Option notes:**
- A. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- B. Branding extension can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Data IO, and the better fit is Data IO extension app.
- D. Data IO extensions read/write structured data.

**Q250. (API Authentication - OAuth flow selection)** Luca, a developer on the IAM team, is reviewing a Docusign implementation for a sales contract automation team. The relevant requirement is that a browser-only single-page application cannot protect a client secret but must authenticate each individual user. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Option notes:**
- A. JSON Web Token Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- B. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing OAuth flow selection, and the better fit is Public Authorization Code Grant with PKCE.
- C. Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public Authorization Code Grant with PKCE: Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q251. (Docusign Connect - Connect vs polling)** Noah, an API developer, is reviewing a Docusign implementation for a banking compliance unit. The relevant requirement is that a system must learn when recipients complete signing without excessive API calls. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Option notes:**
- A. Wait for users to forward emails can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- B. Use a template reference model can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.
- C. Connect pushes events and avoids high-volume polling.
- D. Poll EnvelopeRecipients:list every second can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Subscribe to Connect events: Connect pushes events and avoids high-volume polling.

**Q252. (eSignature API - Embedded signing timing)** Daniel, a solutions architect, is reviewing a Docusign implementation for a commercial real-estate group. The relevant requirement is that an app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Option notes:**
- A. The account base URI disappears can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- B. Connect retries stop can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- C. Embedded signing URLs are short-lived and should be generated when the user is ready.
- D. The template ID changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q253. (Workflow Builder and Workflow API - Runtime errors)** Maya, an integration lead at a public-sector records department, is replacing a manual agreement process with a Docusign IAM integration. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow trigger fails because required starting variables are missing. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer inspect?

A. Brand destination URLs
B. Connect HMAC secret only
C. Bulk send list status only
D. Workflow trigger requirements and variable mapping

**Answer:** D. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Option notes:**
- A. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- B. Connect HMAC secret only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- C. Bulk send list status only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- D. Workflow trigger requirements define required input variables.

**Q254. (App Center and Extension Apps - File IO)** Noah, an API developer, is reviewing a Docusign implementation for a banking compliance unit. The relevant requirement is that a workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Option notes:**
- A. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- B. CORS origin only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- C. File IO extensions handle document storage and retrieval use cases.
- D. Connected Fields only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.

**Q255. (API Authentication - JWT Grant)** Sofia, a business systems analyst, is reviewing a Docusign implementation for a multinational HR operations team. The relevant requirement is that a scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing JWT Grant, and the better fit is JSON Web Token Grant.
- B. JWT Grant supports non-interactive service integrations after consent has been granted.
- C. Public Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.
- D. Confidential Authorization Code Grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON Web Token Grant: JWT Grant supports non-interactive service integrations after consent has been granted.

**Q256. (Docusign Connect - Configuration level)** Elena, an implementation consultant, is reviewing a Docusign implementation for a partner-built customer portal. The relevant requirement is that a company wants one webhook for events across all accounts in its Docusign organization. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Option notes:**
- A. A Web Forms clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- B. Organization-level Connect centralizes events across accounts in the organization.
- C. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.
- D. Recipient-only Connect in each template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Organization-level Connect: Organization-level Connect centralizes events across accounts in the organization.

**Q257. (eSignature API - Embedded sending)** Priya, a platform engineer, is reviewing a Docusign implementation for a legal operations team. The relevant requirement is that a sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Option notes:**
- A. Connect retry log can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- B. Embedded sending uses a sender view URL.
- C. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- D. Agreements:getAgreement can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.

**Q258. (Workflow Builder and Workflow API - Embedding workflow)** Daniel, a solutions architect at a commercial real-estate group, is connecting several line-of-business systems to Docusign APIs. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a custom app needs to display a workflow experience inside the app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which capability should be considered?

A. JWT admin consent only
B. Agreement type extraction only
C. Embedding or launching the workflow according to its configured start method
D. Envelope purge

**Answer:** C. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Option notes:**
- A. JWT admin consent only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- B. Agreement type extraction only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- C. Workflow integration depends on the configured start method and embedding/launch pattern.
- D. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.

**Q259. (App Center and Extension Apps - Connected Fields)** Elena, an implementation consultant, is reviewing a Docusign implementation for a partner-built customer portal. The relevant requirement is that an extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Option notes:**
- A. Agreement list search can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- B. Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- C. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- D. Go-live classification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q260. (API Authentication - Consent)** In a quick architecture review, the team wants the best answer without extra workflow context. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Option notes:**
- A. JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- B. A production account ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- C. A Connect listener URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.
- D. A new envelope template ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Individual or admin consent for the integration key and scopes: JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q261. (Docusign Connect - JSON SIM)** In a quick architecture review, the team wants the best answer without extra workflow context. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Option notes:**
- A. Workflow events rely on the JSON SIM event model.
- B. Legacy XML only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- C. CSV export format can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.
- D. PDF attachment only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to JSON SIM format: Workflow events rely on the JSON SIM event model.

**Q262. (eSignature API - Bulk send)** In a quick architecture review, the team wants the best answer without extra workflow context. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

**Option notes:**
- A. Bulk Send supports large batches of personalized envelopes.
- B. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- C. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- D. Organization Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.

**Q263. (Workflow Builder and Workflow API - Installed extensions)** Priya, a platform engineer at a legal operations team, is standardizing how agreements are prepared, sent, monitored, and stored. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, a workflow should call a third-party service through an extension app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must be true?

A. The Web Form must be public
B. The extension app must be installed and available for the workflow step
C. The envelope must be voided first
D. The app must use implicit grant

**Answer:** B. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Option notes:**
- A. The Web Form must be public can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- B. Workflow Builder can use installed extension applications in extension steps.
- C. The envelope must be voided first can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- D. The app must use implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.

**Q264. (App Center and Extension Apps - Data Verification)** In a quick architecture review, the team wants the best answer without extra workflow context. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

**Option notes:**
- A. Data Verification checks signer-entered data during the signing experience.
- B. Public Auth Code only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- D. Agreement Manager import can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.

**Q265. (API Authentication - Scopes)** Elena, an implementation consultant at a partner-built customer portal, is automating high-volume agreement work while keeping auditability intact. Security reviewers are focused on consent, least-privilege scopes, and whether the app can safely protect secrets. In the current design, an app only needs to send envelopes and read user account information. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Option notes:**
- A. Request every Docusign scope to avoid future changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- B. Omit scopes because Docusign infers them can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- C. Use account-level Connect settings as scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Request only the minimum scopes required for those operations: Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.
- D. Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q266. (eSignature API - Envelope create)** Sofia, a business systems analyst at a multinational HR operations team, is replacing a manual agreement process with a Docusign IAM integration. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, an integration needs to send an envelope for signature immediately. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- B. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to sent: Status sent sends the envelope; created saves it as a draft.
- D. Status sent sends the envelope; created saves it as a draft.

**Q267. (Workflow Builder and Workflow API - Workflow steps)** Luca, a developer on the IAM team at a sales contract automation team, is adding reusable agreement automation to an existing business application. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow must collect form data before sending a document for signature. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which step order best fits?

A. Collect Data with Web Forms, then Get Signatures
B. Get Signatures, then collect data
C. Archive first, then start
D. Void envelope, then collect data

**Answer:** A. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Option notes:**
- A. Workflow step order should match the business process.
- B. Get Signatures, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- C. Archive first, then start can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.
- D. Void envelope, then collect data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Get Signatures: Workflow step order should match the business process.

**Q268. (App Center and Extension Apps - Extension app role)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, a customer wants Docusign to call an external service during an agreement process. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Option notes:**
- A. A replacement for OAuth consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- B. Unlimited eSignature API calls can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- C. A mandatory PDF renderer can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A packaged way to connect external functionality into Docusign: Extension apps extend Docusign with external service actions and data.
- D. Extension apps extend Docusign with external service actions and data.

**Q269. (API Authentication - User info)** Amir, a workflow automation engineer at a regional healthcare provider, is moving a pilot integration from a developer account toward production. The team must choose an OAuth pattern before the integration key is approved for wider use. In the current design, after receiving an access token, the app must determine which base URI and account ID to use for API calls. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Option notes:**
- A. /oauth/token can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- B. /connect/events can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- C. The userinfo response includes account identifiers and base URI information needed for subsequent API calls.
- D. /restapi/v2.1/accounts can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to /oauth/userinfo: The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q270. (eSignature API - Draft envelope)** Noah, an API developer at a banking compliance unit, is connecting several line-of-business systems to Docusign APIs. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a developer wants to create an envelope but not send it yet. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Option notes:**
- A. voided can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- B. completed can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.
- C. The created status keeps an envelope in draft state.
- D. sent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to created: The created status keeps an envelope in draft state.

**Q271. (Workflow Builder and Workflow API - Identity step)** Sofia, a business systems analyst at a multinational HR operations team, is automating high-volume agreement work while keeping auditability intact. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a process must gather participant data and then verify identity. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which sequence is best?

A. Verify identity after archiving only
B. Get Signatures before collecting data
C. Connect retry before web form
D. Collect Data with Web Forms, then Verify Someone's Identity

**Answer:** D. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Option notes:**
- A. Verify identity after archiving only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- B. Get Signatures before collecting data can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- C. Connect retry before web form can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Collect Data with Web Forms, then Verify Someone's Identity: Collect required data before the identity verification step if the scenario requires it.
- D. Collect required data before the identity verification step if the scenario requires it.

**Q272. (App Center and Extension Apps - Public vs private)** Mateo, a DevOps engineer at a procurement shared-services group, is connecting several line-of-business systems to Docusign APIs. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an app is only for one organization's internal Docusign accounts. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Option notes:**
- A. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Public vs private, and the better fit is Private extension app.
- B. Recipient Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.
- C. Private apps are limited to selected accounts or the publisher's organization.
- D. Public App Center listing can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Private extension app: Private apps are limited to selected accounts or the publisher's organization.

**Q273. (API Authentication - PKCE)** Grace, a product owner at a university financial-aid office, is reducing support tickets caused by inconsistent envelope handling. The application will call Docusign APIs from several environments, so the authentication pattern must be defensible and repeatable. In the current design, a native app cannot store a client secret securely. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Option notes:**
- A. A template password can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- B. PKCE mitigates interception risk for public clients that cannot keep a client secret.
- C. An HMAC secret on each envelope can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.
- D. A Connect retry policy can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A PKCE code verifier and code challenge: PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q274. (eSignature API - Cancel envelope)** Elena, an implementation consultant at a partner-built customer portal, is standardizing how agreements are prepared, sent, monitored, and stored. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a sent envelope has a fatal error and no one should sign it. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Option notes:**
- A. created can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- B. Voiding cancels an in-process envelope and stops signing.
- C. deleted can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.
- D. purged can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to voided: Voiding cancels an in-process envelope and stops signing.

**Q275. (Workflow Builder and Workflow API - Extension step)** Noah, an API developer at a banking compliance unit, is moving a pilot integration from a developer account toward production. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, after signing, the completed document must be stored in an external file service. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow step type is appropriate?

A. Get Signatures step only
B. CORS configuration
C. Extension step using a file/archive extension app
D. Branching rule only

**Answer:** C. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Option notes:**
- A. Get Signatures step only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- B. CORS configuration can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.
- C. Extension steps call external services through installed extension apps.
- D. Branching rule only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Extension step using a file/archive extension app: Extension steps call external services through installed extension apps.

**Q276. (App Center and Extension Apps - Public App Center)** Maya, an integration lead at a public-sector records department, is standardizing how agreements are prepared, sent, monitored, and stored. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a partner wants customers broadly to discover and install an app. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Option notes:**
- A. Demo-only template can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- B. Public App Center distribution is for broad customer availability.
- C. Private app for one account only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.
- D. Envelope-level Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Public extension app published to the Docusign App Center: Public App Center distribution is for broad customer availability.

**Q277. (eSignature API - Idempotency)** Amir, a workflow automation engineer at a regional healthcare provider, is adding reusable agreement automation to an existing business application. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a network retry might submit the same create-envelope request twice. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Option notes:**
- A. Supplying a transactionId supports idempotent envelope creation.
- B. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- C. retryId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.
- D. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to transactionId: Supplying a transactionId supports idempotent envelope creation.

**Q278. (Workflow Builder and Workflow API - Branching)** Elena, an implementation consultant at a partner-built customer portal, is reducing support tickets caused by inconsistent envelope handling. Business owners want a repeatable workflow with approvals, conditions, and system calls that can evolve without rewriting the entire application. In the current design, a workflow should follow different paths based on a form response. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which workflow capability is used?

A. Brand destination URL
B. Branching or conditional rules
C. JWT consent
D. Envelope purge

**Answer:** B. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Option notes:**
- A. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- B. Branching rules route workflows based on conditions.
- C. JWT consent can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.
- D. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Branching or conditional rules: Branching rules route workflows based on conditions.

**Q279. (App Center and Extension Apps - Manifest)** Daniel, a solutions architect at a commercial real-estate group, is adding reusable agreement automation to an existing business application. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, an extension app action must call an external API endpoint. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Option notes:**
- A. Actions in the manifest describe calls to external endpoints.
- B. In an envelope email subject can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- C. In a recipient tab label can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.
- D. In the Safe Exam Browser can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to In an action definition in the extension app manifest: Actions in the manifest describe calls to external endpoints.

**Q280. (eSignature API - Template reference)** Grace, a product owner at a university financial-aid office, is automating high-volume agreement work while keeping auditability intact. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a request uses a server template already stored in Docusign. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Option notes:**
- A. clientUserId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- B. returnUrl can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- C. basePath can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to templateId: templateId references an existing template in an envelope request.
- D. templateId references an existing template in an envelope request.

**Q281. (Workflow Builder and Workflow API - Start method)** Amir, a workflow automation engineer at a regional healthcare provider, is building a self-service portal for internal teams and external customers. The automation team is combining Docusign workflow steps with external API calls and needs to choose the correct integration pattern. In the current design, a portal link should launch a workflow and pass values in the trigger URL. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method fits?

A. From a Link
B. Manually by someone in your organization only
C. From an envelope void event only
D. From a bulk send batch only

**Answer:** A. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Option notes:**
- A. A link start method can launch a workflow and pass URL values.
- B. Manually by someone in your organization only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- C. From an envelope void event only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.
- D. From a bulk send batch only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From a Link: A link start method can launch a workflow and pass URL values.

**Q282. (App Center and Extension Apps - Connections)** Priya, a platform engineer at a legal operations team, is automating high-volume agreement work while keeping auditability intact. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, an action must use external OAuth credentials. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Option notes:**
- A. publisher only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- B. brandColors can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- C. bulkCopies can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connections: The connections object defines authentication configuration used by actions.
- D. The connections object defines authentication configuration used by actions.

**Q283. (eSignature API - Composite templates)** Mateo, a DevOps engineer at a procurement shared-services group, is moving a pilot integration from a developer account toward production. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, a request must combine server templates, inline recipient data, and documents. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Option notes:**
- A. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- B. Connect 2.0 only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.
- C. Composite templates allow combining server templates, inline templates, and documents.
- D. Bulk send list only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Composite templates: Composite templates allow combining server templates, inline templates, and documents.

**Q284. (Workflow Builder and Workflow API - API trigger)** Grace, a product owner at a university financial-aid office, is replacing a manual agreement process with a Docusign IAM integration. A production workflow has to support branching, embedded experiences, and troubleshooting when a step does not complete as expected. In the current design, a backend service must programmatically trigger a workflow. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which start method/API pattern is relevant?

A. Remote signing email only
B. Brand resource file upload
C. Template reference ID only
D. From an API call with Workflow Builder API trigger requirements

**Answer:** D. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Option notes:**
- A. Remote signing email only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- B. Brand resource file upload can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- C. Template reference ID only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to From an API call with Workflow Builder API trigger requirements: API-triggered workflows use trigger requirements and workflow API calls.
- D. API-triggered workflows use trigger requirements and workflow API calls.

**Q285. (App Center and Extension Apps - connectionsReference)** Luca, a developer on the IAM team at a sales contract automation team, is moving a pilot integration from a developer account toward production. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, an action needs to use a named connection from the manifest. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Option notes:**
- A. transactionId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- B. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.
- C. connectionsReference ties an action to a connection definition.
- D. recipientId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to connectionsReference: connectionsReference ties an action to a connection definition.

**Q286. (eSignature API - Anchor tabs)** Maya, an integration lead at a public-sector records department, is reducing support tickets caused by inconsistent envelope handling. The business wants senders to stop preparing envelopes manually, but the recipient experience still has to match the existing process. In the current design, a document can vary in page length, but the signature should appear near a specific text string. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Option notes:**
- A. CORS origin settings can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- B. Anchor tabs place fields relative to document text.
- C. Fixed x/y coordinates only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.
- D. Branding resource files can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Anchor tagging with anchorString and offsets: Anchor tabs place fields relative to document text.

**Q287. (Workflow Builder and Workflow API - Runtime errors)** Mateo, a DevOps engineer, is reviewing a Docusign implementation for a procurement shared-services group. The relevant requirement is that a workflow trigger fails because required starting variables are missing. What should the developer inspect?

A. Connect HMAC secret only
B. Bulk send list status only
C. Workflow trigger requirements and variable mapping
D. Brand destination URLs

**Answer:** C. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Option notes:**
- A. Connect HMAC secret only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- B. Bulk send list status only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.
- C. Workflow trigger requirements define required input variables.
- D. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Workflow trigger requirements and variable mapping: Workflow trigger requirements define required input variables.

**Q288. (App Center and Extension Apps - API proxy)** Sofia, a business systems analyst at a multinational HR operations team, is reducing support tickets caused by inconsistent envelope handling. A partner team is packaging reusable capabilities for Docusign customers and must respect how Extension Apps are installed and invoked. In the current design, the third-party API format does not match what the extension app action needs. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Option notes:**
- A. Bulk send CSV can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- B. An API proxy can mediate between Docusign and the external service.
- C. Brand destination URL can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.
- D. Envelope void status can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to API proxy: An API proxy can mediate between Docusign and the external service.

**Q289. (eSignature API - Embedded signing)** Daniel, a solutions architect at a commercial real-estate group, is building a self-service portal for internal teams and external customers. Developers are translating a manual sending pattern into API calls and need to choose the correct envelope configuration. In the current design, a recipient must sign inside the host app rather than through an email link. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Option notes:**
- A. clientUserId identifies a captive/embedded recipient.
- B. emailNotification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- C. brandId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.
- D. listId can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to clientUserId: clientUserId identifies a captive/embedded recipient.

**Q290. (Workflow Builder and Workflow API - Embedding workflow)** Maya, an integration lead, is reviewing a Docusign implementation for a public-sector records department. The relevant requirement is that a custom app needs to display a workflow experience inside the app. Which capability should be considered?

A. Agreement type extraction only
B. Embedding or launching the workflow according to its configured start method
C. Envelope purge
D. JWT admin consent only

**Answer:** B. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Option notes:**
- A. Agreement type extraction only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- B. Workflow integration depends on the configured start method and embedding/launch pattern.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.
- D. JWT admin consent only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Embedding or launching the workflow according to its configured start method: Workflow integration depends on the configured start method and embedding/launch pattern.

**Q291. (App Center and Extension Apps - Firewall)** Noah, an API developer at a banking compliance unit, is building a self-service portal for internal teams and external customers. The app needs to expose a capability inside the Docusign IAM platform without forcing each customer to build custom middleware. In the current design, docusign must call a customer-hosted endpoint for an extension action. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Option notes:**
- A. The external endpoint must be reachable by Docusign.
- B. Disable all OAuth scopes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- C. Use only demo endpoints can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.
- D. Delete the app manifest can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Allow Docusign outbound requests through the endpoint firewall: The external endpoint must be reachable by Docusign.

**Q292. (eSignature API - Signing URL)** Priya, a platform engineer at a legal operations team, is replacing a manual agreement process with a Docusign IAM integration. The team is balancing automation, recipient routing, templates, and tab placement for a reusable send workflow. In the current design, an app has created an envelope for an embedded recipient. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Option notes:**
- A. A Connect JSON SIM event can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- B. A bulk send batch ID can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- C. A brand resource file can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to A recipient view URL from EnvelopeViews:createRecipient: Embedded signing requires requesting a short-lived recipient view URL.
- D. Embedded signing requires requesting a short-lived recipient view URL.

**Q293. (Workflow Builder and Workflow API - Installed extensions)** In a quick architecture review, the team wants the best answer without extra workflow context. What must be true?

A. The extension app must be installed and available for the workflow step
B. The envelope must be voided first
C. The app must use implicit grant
D. The Web Form must be public

**Answer:** A. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Option notes:**
- A. Workflow Builder can use installed extension applications in extension steps.
- B. The envelope must be voided first can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- C. The app must use implicit grant can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.
- D. The Web Form must be public can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The extension app must be installed and available for the workflow step: Workflow Builder can use installed extension applications in extension steps.

**Q294. (App Center and Extension Apps - Data IO)** Elena, an implementation consultant at a partner-built customer portal, is replacing a manual agreement process with a Docusign IAM integration. The team is reviewing manifest, connection, firewall, data exchange, and API proxy choices before publishing or deploying privately. In the current design, a workflow needs to read and write structured records in another system. The team wants the simplest Docusign-supported approach that satisfies the requirement and avoids unnecessary custom behavior. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Option notes:**
- A. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- B. Branding extension can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data IO extension app: Data IO extensions read/write structured data.
- C. Implicit Grant is not the preferred modern choice for these integrations. The scenario is testing Data IO, and the better fit is Data IO extension app.
- D. Data IO extensions read/write structured data.

**Q295. (eSignature API - Embedded signing timing)** Luca, a developer on the IAM team, is reviewing a Docusign implementation for a sales contract automation team. The relevant requirement is that an app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Option notes:**
- A. The account base URI disappears can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- B. Connect retries stop can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.
- C. Embedded signing URLs are short-lived and should be generated when the user is ready.
- D. The template ID changes can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to The short-lived URL may expire before use: Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q296. (App Center and Extension Apps - File IO)** Amir, a workflow automation engineer, is reviewing a Docusign implementation for a regional healthcare provider. The relevant requirement is that a workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Option notes:**
- A. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- B. CORS origin only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.
- C. File IO extensions handle document storage and retrieval use cases.
- D. Connected Fields only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to File IO or file archive extension app: File IO extensions handle document storage and retrieval use cases.

**Q297. (eSignature API - Embedded sending)** Sofia, a business systems analyst, is reviewing a Docusign implementation for a multinational HR operations team. The relevant requirement is that a sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Option notes:**
- A. Connect retry log can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- B. Embedded sending uses a sender view URL.
- C. BulkSend:createBulkSendList can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.
- D. Agreements:getAgreement can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to EnvelopeViews:createSender: Embedded sending uses a sender view URL.

**Q298. (App Center and Extension Apps - Connected Fields)** Grace, a product owner, is reviewing a Docusign implementation for a university financial-aid office. The relevant requirement is that an extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Option notes:**
- A. Agreement list search can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- B. Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- C. File archive only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.
- D. Go-live classification can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Connected Fields: Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q299. (eSignature API - Bulk send)** In a quick architecture review, the team wants the best answer without extra workflow context. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

**Option notes:**
- A. Bulk Send supports large batches of personalized envelopes.
- B. Recipient authentication only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- C. Brand destination URLs can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.
- D. Organization Connect only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Bulk Send: Bulk Send supports large batches of personalized envelopes.

**Q300. (App Center and Extension Apps - Data Verification)** In a quick architecture review, the team wants the best answer without extra workflow context. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

**Option notes:**
- A. Data Verification checks signer-entered data during the signing experience.
- B. Public Auth Code only can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- C. Envelope purge can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.
- D. Agreement Manager import can be valid in a different Docusign scenario, but it does not match the requirement in this question. The key clue points to Data Verification triggered during eSignature signing: Data Verification checks signer-entered data during the signing experience.

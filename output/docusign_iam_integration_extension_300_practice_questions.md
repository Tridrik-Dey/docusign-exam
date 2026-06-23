# Certified Docusign IAM Integration & Extension Developer - 300 Practice Questions

Original practice bank aligned to the 2026 prep guide, the supplied QA/explanation document style, and the self-paced course knowledge-check material in `study_material.md`.

Question distribution follows the exam guide weights:

- API Authentication: 39 questions
- Go Live Process: 33 questions
- Docusign Connect: 36 questions
- eSignature API: 48 questions
- eSignature Features and Web Forms: 33 questions
- Agreement Manager API: 18 questions
- Workflow Builder and Workflow API: 45 questions
- App Center and Extension Apps: 48 questions

## Questions

### API Authentication

**Q1. (OAuth flow selection)** A public-sector records process is working on this scenario: A server-side portal can store a client secret and each employee signs in interactively. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q2. (OAuth flow selection)** A real-estate transaction workflow is working on this scenario: A browser-only single-page application cannot protect a client secret but must authenticate each individual user. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q3. (JWT Grant)** A healthcare onboarding team is working on this scenario: A scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Q4. (Consent)** A university financial-aid portal is working on this scenario: A JWT integration fails because the user has never granted consent for the requested scopes. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q5. (Scopes)** A banking compliance application is working on this scenario: An app only needs to send envelopes and read user account information. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q6. (User info)** A procurement workflow is working on this scenario: After receiving an access token, the app must determine which base URI and account ID to use for API calls. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q7. (PKCE)** A legal operations integration is working on this scenario: A native app cannot store a client secret securely. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q8. (Bearer tokens)** A sales contract portal is working on this scenario: A REST API request is returning unauthorized even though the token endpoint returned an access token. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Q9. (OAuth flow selection)** An HR onboarding workflow is working on this scenario: A server-side portal can store a client secret and each employee signs in interactively. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q10. (OAuth flow selection)** A partner-built customer app is working on this scenario: A browser-only single-page application cannot protect a client secret but must authenticate each individual user. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q11. (JWT Grant)** A public-sector records process is working on this scenario: A scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Q12. (Consent)** A real-estate transaction workflow is working on this scenario: A JWT integration fails because the user has never granted consent for the requested scopes. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q13. (Scopes)** A healthcare onboarding team is working on this scenario: An app only needs to send envelopes and read user account information. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q14. (User info)** A university financial-aid portal is working on this scenario: After receiving an access token, the app must determine which base URI and account ID to use for API calls. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q15. (PKCE)** A banking compliance application is working on this scenario: A native app cannot store a client secret securely. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q16. (Bearer tokens)** A procurement workflow is working on this scenario: A REST API request is returning unauthorized even though the token endpoint returned an access token. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Q17. (OAuth flow selection)** A legal operations integration is working on this scenario: A server-side portal can store a client secret and each employee signs in interactively. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q18. (OAuth flow selection)** A sales contract portal is working on this scenario: A browser-only single-page application cannot protect a client secret but must authenticate each individual user. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q19. (JWT Grant)** An HR onboarding workflow is working on this scenario: A scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Q20. (Consent)** A partner-built customer app is working on this scenario: A JWT integration fails because the user has never granted consent for the requested scopes. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q21. (Scopes)** A public-sector records process is working on this scenario: An app only needs to send envelopes and read user account information. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q22. (User info)** A real-estate transaction workflow is working on this scenario: After receiving an access token, the app must determine which base URI and account ID to use for API calls. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q23. (PKCE)** A healthcare onboarding team is working on this scenario: A native app cannot store a client secret securely. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q24. (Bearer tokens)** A university financial-aid portal is working on this scenario: A REST API request is returning unauthorized even though the token endpoint returned an access token. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Q25. (OAuth flow selection)** A banking compliance application is working on this scenario: A server-side portal can store a client secret and each employee signs in interactively. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q26. (OAuth flow selection)** A procurement workflow is working on this scenario: A browser-only single-page application cannot protect a client secret but must authenticate each individual user. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q27. (JWT Grant)** A legal operations integration is working on this scenario: A scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Q28. (Consent)** A sales contract portal is working on this scenario: A JWT integration fails because the user has never granted consent for the requested scopes. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q29. (Scopes)** An HR onboarding workflow is working on this scenario: An app only needs to send envelopes and read user account information. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q30. (User info)** A partner-built customer app is working on this scenario: After receiving an access token, the app must determine which base URI and account ID to use for API calls. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q31. (PKCE)** A public-sector records process is working on this scenario: A native app cannot store a client secret securely. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

**Q32. (Bearer tokens)** A real-estate transaction workflow is working on this scenario: A REST API request is returning unauthorized even though the token endpoint returned an access token. Where should the access token be supplied?

A. In the Authorization header as a Bearer token
B. In the envelope email subject
C. In the Connect eventNotification object
D. In the templateId field

**Answer:** A. In the Authorization header as a Bearer token

**Explanation:** Docusign REST calls use Authorization: Bearer <access_token>.

**Q33. (OAuth flow selection)** A healthcare onboarding team is working on this scenario: A server-side portal can store a client secret and each employee signs in interactively. Which OAuth flow best fits this integration?

A. JSON Web Token Grant
B. Public Authorization Code Grant with PKCE
C. Implicit Grant
D. Confidential Authorization Code Grant

**Answer:** D. Confidential Authorization Code Grant

**Explanation:** Use Confidential Authorization Code Grant when a web server can protect a secret and users authenticate interactively.

**Q34. (OAuth flow selection)** A university financial-aid portal is working on this scenario: A browser-only single-page application cannot protect a client secret but must authenticate each individual user. Which flow should the developer choose?

A. JSON Web Token Grant
B. Implicit Grant
C. Public Authorization Code Grant with PKCE
D. Confidential Authorization Code Grant

**Answer:** C. Public Authorization Code Grant with PKCE

**Explanation:** Public Authorization Code Grant with PKCE is the recommended pattern for public clients such as SPAs or native apps.

**Q35. (JWT Grant)** A banking compliance application is working on this scenario: A scheduled service runs nightly using a dedicated system sender account and no person is present to sign in. Which authentication model is appropriate?

A. Implicit Grant
B. JSON Web Token Grant
C. Public Authorization Code Grant
D. Confidential Authorization Code Grant

**Answer:** B. JSON Web Token Grant

**Explanation:** JWT Grant supports non-interactive service integrations after consent has been granted.

**Q36. (Consent)** A procurement workflow is working on this scenario: A JWT integration fails because the user has never granted consent for the requested scopes. What must be obtained before token requests succeed?

A. Individual or admin consent for the integration key and scopes
B. A production account ID only
C. A Connect listener URL
D. A new envelope template ID

**Answer:** A. Individual or admin consent for the integration key and scopes

**Explanation:** JWT and other OAuth flows require consent for requested scopes before access tokens can be issued.

**Q37. (Scopes)** A legal operations integration is working on this scenario: An app only needs to send envelopes and read user account information. What should the developer do when requesting OAuth consent?

A. Request every Docusign scope to avoid future changes
B. Omit scopes because Docusign infers them
C. Use account-level Connect settings as scopes
D. Request only the minimum scopes required for those operations

**Answer:** D. Request only the minimum scopes required for those operations

**Explanation:** Least-privilege scope selection reduces risk and avoids unnecessary consent prompts.

**Q38. (User info)** A sales contract portal is working on this scenario: After receiving an access token, the app must determine which base URI and account ID to use for API calls. Which endpoint is used to retrieve that account context?

A. /oauth/token
B. /connect/events
C. /oauth/userinfo
D. /restapi/v2.1/accounts

**Answer:** C. /oauth/userinfo

**Explanation:** The userinfo response includes account identifiers and base URI information needed for subsequent API calls.

**Q39. (PKCE)** An HR onboarding workflow is working on this scenario: A native app cannot store a client secret securely. What protects the public authorization code exchange?

A. A template password
B. A PKCE code verifier and code challenge
C. An HMAC secret on each envelope
D. A Connect retry policy

**Answer:** B. A PKCE code verifier and code challenge

**Explanation:** PKCE mitigates interception risk for public clients that cannot keep a client secret.

### Go Live Process

**Q40. (Go-live setup)** A sales contract portal is working on this scenario: A developer promotes an integration key from demo to production. Which configuration commonly must be recreated in production?

A. Redirect URIs and secret keys
B. Completed demo envelopes
C. Envelope IDs
D. Connect event logs

**Answer:** A. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q41. (Integration classification)** An HR onboarding workflow is working on this scenario: A partner app will be distributed for many customers to install. Which go-live classification best reflects the use case?

A. Internal employee-only integration
B. One-time manual sending workflow
C. Template-only configuration
D. ISV or partner-distributed integration

**Answer:** D. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Q42. (Production endpoints)** A partner-built customer app is working on this scenario: After go-live, API calls still point to demo endpoints. What must be changed?

A. Use a Connect listener as the base URI
B. Replace all templates with web forms
C. Use production base URIs and production API endpoints
D. Keep demo endpoints and change only the email subject

**Answer:** C. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Q43. (Templates in production)** A public-sector records process is working on this scenario: An app uses a template reference model in demo. What is required for production?

A. Enable CORS only
B. Deploy or recreate the template in production and update the template ID
C. Reuse the demo template ID
D. Switch to JWT Grant

**Answer:** B. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Q44. (Post go-live)** A real-estate transaction workflow is working on this scenario: A promoted integration key uses Confidential Authorization Code Grant. What should be validated immediately after go-live?

A. Production redirect URIs, secrets, base URI, and consent
B. Recipient tab labels only
C. The user's browser zoom level
D. Template color branding only

**Answer:** A. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Q45. (API limits)** A healthcare onboarding team is working on this scenario: An integration repeatedly polls envelopes every few seconds for status. Which improvement best aligns with API usage guidelines?

A. Increase polling frequency
B. Create duplicate envelopes for retry
C. Move all status into email subject lines
D. Use Connect webhooks for event-driven status updates

**Answer:** D. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q46. (Troubleshooting)** A university financial-aid portal is working on this scenario: A production app fails after go-live with authentication errors, but worked in demo. What should be checked first?

A. Whether recipients use the same browser
B. Whether document tabs are locked
C. Production OAuth settings, redirect URI, consent, and account base URI
D. Whether demo envelopes are legally binding

**Answer:** C. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Q47. (Go-live setup)** A banking compliance application is working on this scenario: A developer promotes an integration key from demo to production. Which configuration commonly must be recreated in production?

A. Connect event logs
B. Redirect URIs and secret keys
C. Completed demo envelopes
D. Envelope IDs

**Answer:** B. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q48. (Integration classification)** A procurement workflow is working on this scenario: A partner app will be distributed for many customers to install. Which go-live classification best reflects the use case?

A. ISV or partner-distributed integration
B. Internal employee-only integration
C. One-time manual sending workflow
D. Template-only configuration

**Answer:** A. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Q49. (Production endpoints)** A legal operations integration is working on this scenario: After go-live, API calls still point to demo endpoints. What must be changed?

A. Keep demo endpoints and change only the email subject
B. Use a Connect listener as the base URI
C. Replace all templates with web forms
D. Use production base URIs and production API endpoints

**Answer:** D. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Q50. (Templates in production)** A sales contract portal is working on this scenario: An app uses a template reference model in demo. What is required for production?

A. Switch to JWT Grant
B. Enable CORS only
C. Deploy or recreate the template in production and update the template ID
D. Reuse the demo template ID

**Answer:** C. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Q51. (Post go-live)** An HR onboarding workflow is working on this scenario: A promoted integration key uses Confidential Authorization Code Grant. What should be validated immediately after go-live?

A. Template color branding only
B. Production redirect URIs, secrets, base URI, and consent
C. Recipient tab labels only
D. The user's browser zoom level

**Answer:** B. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Q52. (API limits)** A partner-built customer app is working on this scenario: An integration repeatedly polls envelopes every few seconds for status. Which improvement best aligns with API usage guidelines?

A. Use Connect webhooks for event-driven status updates
B. Increase polling frequency
C. Create duplicate envelopes for retry
D. Move all status into email subject lines

**Answer:** A. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q53. (Troubleshooting)** A public-sector records process is working on this scenario: A production app fails after go-live with authentication errors, but worked in demo. What should be checked first?

A. Whether demo envelopes are legally binding
B. Whether recipients use the same browser
C. Whether document tabs are locked
D. Production OAuth settings, redirect URI, consent, and account base URI

**Answer:** D. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Q54. (Go-live setup)** A real-estate transaction workflow is working on this scenario: A developer promotes an integration key from demo to production. Which configuration commonly must be recreated in production?

A. Envelope IDs
B. Connect event logs
C. Redirect URIs and secret keys
D. Completed demo envelopes

**Answer:** C. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q55. (Integration classification)** A healthcare onboarding team is working on this scenario: A partner app will be distributed for many customers to install. Which go-live classification best reflects the use case?

A. Template-only configuration
B. ISV or partner-distributed integration
C. Internal employee-only integration
D. One-time manual sending workflow

**Answer:** B. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Q56. (Production endpoints)** A university financial-aid portal is working on this scenario: After go-live, API calls still point to demo endpoints. What must be changed?

A. Use production base URIs and production API endpoints
B. Keep demo endpoints and change only the email subject
C. Use a Connect listener as the base URI
D. Replace all templates with web forms

**Answer:** A. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Q57. (Templates in production)** A banking compliance application is working on this scenario: An app uses a template reference model in demo. What is required for production?

A. Reuse the demo template ID
B. Switch to JWT Grant
C. Enable CORS only
D. Deploy or recreate the template in production and update the template ID

**Answer:** D. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Q58. (Post go-live)** A procurement workflow is working on this scenario: A promoted integration key uses Confidential Authorization Code Grant. What should be validated immediately after go-live?

A. The user's browser zoom level
B. Template color branding only
C. Production redirect URIs, secrets, base URI, and consent
D. Recipient tab labels only

**Answer:** C. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Q59. (API limits)** A legal operations integration is working on this scenario: An integration repeatedly polls envelopes every few seconds for status. Which improvement best aligns with API usage guidelines?

A. Move all status into email subject lines
B. Use Connect webhooks for event-driven status updates
C. Increase polling frequency
D. Create duplicate envelopes for retry

**Answer:** B. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q60. (Troubleshooting)** A sales contract portal is working on this scenario: A production app fails after go-live with authentication errors, but worked in demo. What should be checked first?

A. Production OAuth settings, redirect URI, consent, and account base URI
B. Whether demo envelopes are legally binding
C. Whether recipients use the same browser
D. Whether document tabs are locked

**Answer:** A. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Q61. (Go-live setup)** An HR onboarding workflow is working on this scenario: A developer promotes an integration key from demo to production. Which configuration commonly must be recreated in production?

A. Completed demo envelopes
B. Envelope IDs
C. Connect event logs
D. Redirect URIs and secret keys

**Answer:** D. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q62. (Integration classification)** A partner-built customer app is working on this scenario: A partner app will be distributed for many customers to install. Which go-live classification best reflects the use case?

A. One-time manual sending workflow
B. Template-only configuration
C. ISV or partner-distributed integration
D. Internal employee-only integration

**Answer:** C. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Q63. (Production endpoints)** A public-sector records process is working on this scenario: After go-live, API calls still point to demo endpoints. What must be changed?

A. Replace all templates with web forms
B. Use production base URIs and production API endpoints
C. Keep demo endpoints and change only the email subject
D. Use a Connect listener as the base URI

**Answer:** B. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Q64. (Templates in production)** A real-estate transaction workflow is working on this scenario: An app uses a template reference model in demo. What is required for production?

A. Deploy or recreate the template in production and update the template ID
B. Reuse the demo template ID
C. Switch to JWT Grant
D. Enable CORS only

**Answer:** A. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Q65. (Post go-live)** A healthcare onboarding team is working on this scenario: A promoted integration key uses Confidential Authorization Code Grant. What should be validated immediately after go-live?

A. Recipient tab labels only
B. The user's browser zoom level
C. Template color branding only
D. Production redirect URIs, secrets, base URI, and consent

**Answer:** D. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

**Q66. (API limits)** A university financial-aid portal is working on this scenario: An integration repeatedly polls envelopes every few seconds for status. Which improvement best aligns with API usage guidelines?

A. Create duplicate envelopes for retry
B. Move all status into email subject lines
C. Use Connect webhooks for event-driven status updates
D. Increase polling frequency

**Answer:** C. Use Connect webhooks for event-driven status updates

**Explanation:** Webhooks reduce unnecessary polling and help avoid resource-limit issues.

**Q67. (Troubleshooting)** A banking compliance application is working on this scenario: A production app fails after go-live with authentication errors, but worked in demo. What should be checked first?

A. Whether document tabs are locked
B. Production OAuth settings, redirect URI, consent, and account base URI
C. Whether demo envelopes are legally binding
D. Whether recipients use the same browser

**Answer:** B. Production OAuth settings, redirect URI, consent, and account base URI

**Explanation:** Common post-go-live issues are environment and OAuth configuration mismatches.

**Q68. (Go-live setup)** A procurement workflow is working on this scenario: A developer promotes an integration key from demo to production. Which configuration commonly must be recreated in production?

A. Redirect URIs and secret keys
B. Completed demo envelopes
C. Envelope IDs
D. Connect event logs

**Answer:** A. Redirect URIs and secret keys

**Explanation:** Security-sensitive settings such as secrets and redirect URIs are configured in the production environment.

**Q69. (Integration classification)** A legal operations integration is working on this scenario: A partner app will be distributed for many customers to install. Which go-live classification best reflects the use case?

A. Internal employee-only integration
B. One-time manual sending workflow
C. Template-only configuration
D. ISV or partner-distributed integration

**Answer:** D. ISV or partner-distributed integration

**Explanation:** Classification should match how the integration is used and distributed.

**Q70. (Production endpoints)** A sales contract portal is working on this scenario: After go-live, API calls still point to demo endpoints. What must be changed?

A. Use a Connect listener as the base URI
B. Replace all templates with web forms
C. Use production base URIs and production API endpoints
D. Keep demo endpoints and change only the email subject

**Answer:** C. Use production base URIs and production API endpoints

**Explanation:** Production integrations must call production endpoints and the correct account base URI.

**Q71. (Templates in production)** An HR onboarding workflow is working on this scenario: An app uses a template reference model in demo. What is required for production?

A. Enable CORS only
B. Deploy or recreate the template in production and update the template ID
C. Reuse the demo template ID
D. Switch to JWT Grant

**Answer:** B. Deploy or recreate the template in production and update the template ID

**Explanation:** Template IDs differ between environments; the production template must be referenced.

**Q72. (Post go-live)** A partner-built customer app is working on this scenario: A promoted integration key uses Confidential Authorization Code Grant. What should be validated immediately after go-live?

A. Production redirect URIs, secrets, base URI, and consent
B. Recipient tab labels only
C. The user's browser zoom level
D. Template color branding only

**Answer:** A. Production redirect URIs, secrets, base URI, and consent

**Explanation:** OAuth and endpoint settings often need production-specific validation.

### Docusign Connect

**Q73. (Envelope-level Connect)** An HR onboarding workflow is working on this scenario: A single high-value envelope needs a callback URL different from account-level settings. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Q74. (Connect vs polling)** A partner-built customer app is working on this scenario: A system must learn when recipients complete signing without excessive API calls. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Q75. (Configuration level)** A public-sector records process is working on this scenario: A company wants one webhook for events across all accounts in its Docusign organization. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Q76. (JSON SIM)** A real-estate transaction workflow is working on this scenario: A workflow event must be delivered to a custom listener. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Q77. (Security)** A healthcare onboarding team is working on this scenario: A listener must verify that incoming webhook messages really came from Docusign. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Q78. (Retries)** A university financial-aid portal is working on this scenario: A listener is temporarily unavailable when Docusign sends an event. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q79. (Troubleshooting)** A banking compliance application is working on this scenario: A listener receives duplicate webhook messages. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Q80. (Payload selection)** A procurement workflow is working on this scenario: A team wants smaller event payloads and will query details separately. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Q81. (Envelope-level Connect)** A legal operations integration is working on this scenario: A single high-value envelope needs a callback URL different from account-level settings. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Q82. (Connect vs polling)** A sales contract portal is working on this scenario: A system must learn when recipients complete signing without excessive API calls. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Q83. (Configuration level)** An HR onboarding workflow is working on this scenario: A company wants one webhook for events across all accounts in its Docusign organization. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Q84. (JSON SIM)** A partner-built customer app is working on this scenario: A workflow event must be delivered to a custom listener. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Q85. (Security)** A public-sector records process is working on this scenario: A listener must verify that incoming webhook messages really came from Docusign. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Q86. (Retries)** A real-estate transaction workflow is working on this scenario: A listener is temporarily unavailable when Docusign sends an event. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q87. (Troubleshooting)** A healthcare onboarding team is working on this scenario: A listener receives duplicate webhook messages. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Q88. (Payload selection)** A university financial-aid portal is working on this scenario: A team wants smaller event payloads and will query details separately. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Q89. (Envelope-level Connect)** A banking compliance application is working on this scenario: A single high-value envelope needs a callback URL different from account-level settings. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Q90. (Connect vs polling)** A procurement workflow is working on this scenario: A system must learn when recipients complete signing without excessive API calls. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Q91. (Configuration level)** A legal operations integration is working on this scenario: A company wants one webhook for events across all accounts in its Docusign organization. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Q92. (JSON SIM)** A sales contract portal is working on this scenario: A workflow event must be delivered to a custom listener. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Q93. (Security)** An HR onboarding workflow is working on this scenario: A listener must verify that incoming webhook messages really came from Docusign. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Q94. (Retries)** A partner-built customer app is working on this scenario: A listener is temporarily unavailable when Docusign sends an event. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q95. (Troubleshooting)** A public-sector records process is working on this scenario: A listener receives duplicate webhook messages. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Q96. (Payload selection)** A real-estate transaction workflow is working on this scenario: A team wants smaller event payloads and will query details separately. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Q97. (Envelope-level Connect)** A healthcare onboarding team is working on this scenario: A single high-value envelope needs a callback URL different from account-level settings. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Q98. (Connect vs polling)** A university financial-aid portal is working on this scenario: A system must learn when recipients complete signing without excessive API calls. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Q99. (Configuration level)** A banking compliance application is working on this scenario: A company wants one webhook for events across all accounts in its Docusign organization. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Q100. (JSON SIM)** A procurement workflow is working on this scenario: A workflow event must be delivered to a custom listener. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

**Q101. (Security)** A legal operations integration is working on this scenario: A listener must verify that incoming webhook messages really came from Docusign. Which control helps validate message authenticity?

A. Changing the envelope email subject
B. Using clientUserId on every signer
C. Adding a brand destination URL
D. HMAC validation or supported Connect authentication

**Answer:** D. HMAC validation or supported Connect authentication

**Explanation:** HMAC and authentication settings help secure Connect listeners.

**Q102. (Retries)** A sales contract portal is working on this scenario: A listener is temporarily unavailable when Docusign sends an event. What Connect behavior should the developer understand?

A. The integration key is revoked
B. The recipient must sign again
C. Docusign retries failed deliveries according to retry rules
D. The envelope is automatically voided

**Answer:** C. Docusign retries failed deliveries according to retry rules

**Explanation:** Connect has retry behavior for delivery failures; listeners should be idempotent.

**Q103. (Troubleshooting)** An HR onboarding workflow is working on this scenario: A listener receives duplicate webhook messages. What design practice should the integration use?

A. Use a different template ID
B. Idempotent processing based on event identifiers or envelope state
C. Treat every duplicate as a new envelope
D. Disable OAuth scopes

**Answer:** B. Idempotent processing based on event identifiers or envelope state

**Explanation:** Webhook systems should tolerate retries and duplicate delivery.

**Q104. (Payload selection)** A partner-built customer app is working on this scenario: A team wants smaller event payloads and will query details separately. Which Connect design choice is relevant?

A. Configure the event payload to include only needed data
B. Switch to implicit grant
C. Use recipient authentication instead
D. Create a bulk send list

**Answer:** A. Configure the event payload to include only needed data

**Explanation:** Connect payload options should match data minimization and processing needs.

**Q105. (Envelope-level Connect)** A public-sector records process is working on this scenario: A single high-value envelope needs a callback URL different from account-level settings. How should the webhook be configured?

A. Create a Web Form instance
B. Use Workflow Builder only
C. Set the envelope status to created
D. Include eventNotification in the envelope creation request

**Answer:** D. Include eventNotification in the envelope creation request

**Explanation:** The eventNotification object configures per-envelope Connect callbacks.

**Q106. (Connect vs polling)** A real-estate transaction workflow is working on this scenario: A system must learn when recipients complete signing without excessive API calls. Which design is preferred?

A. Wait for users to forward emails
B. Use a template reference model
C. Subscribe to Connect events
D. Poll EnvelopeRecipients:list every second

**Answer:** C. Subscribe to Connect events

**Explanation:** Connect pushes events and avoids high-volume polling.

**Q107. (Configuration level)** A healthcare onboarding team is working on this scenario: A company wants one webhook for events across all accounts in its Docusign organization. Which Connect level is most appropriate?

A. A Web Forms clientUserId
B. Organization-level Connect
C. Envelope-level Connect only
D. Recipient-only Connect in each template

**Answer:** B. Organization-level Connect

**Explanation:** Organization-level Connect centralizes events across accounts in the organization.

**Q108. (JSON SIM)** A university financial-aid portal is working on this scenario: A workflow event must be delivered to a custom listener. Which message format is required for workflow-related events?

A. JSON SIM format
B. Legacy XML only
C. CSV export format
D. PDF attachment only

**Answer:** A. JSON SIM format

**Explanation:** Workflow events rely on the JSON SIM event model.

### eSignature API

**Q109. (Envelope create)** A legal operations integration is working on this scenario: An integration needs to send an envelope for signature immediately. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Q110. (Draft envelope)** A sales contract portal is working on this scenario: A developer wants to create an envelope but not send it yet. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Q111. (Cancel envelope)** An HR onboarding workflow is working on this scenario: A sent envelope has a fatal error and no one should sign it. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Q112. (Idempotency)** A partner-built customer app is working on this scenario: A network retry might submit the same create-envelope request twice. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Q113. (Template reference)** A public-sector records process is working on this scenario: A request uses a server template already stored in Docusign. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Q114. (Composite templates)** A real-estate transaction workflow is working on this scenario: A request must combine server templates, inline recipient data, and documents. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Q115. (Anchor tabs)** A healthcare onboarding team is working on this scenario: A document can vary in page length, but the signature should appear near a specific text string. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Q116. (Embedded signing)** A university financial-aid portal is working on this scenario: A recipient must sign inside the host app rather than through an email link. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Q117. (Signing URL)** A banking compliance application is working on this scenario: An app has created an envelope for an embedded recipient. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Q118. (Embedded signing timing)** A procurement workflow is working on this scenario: An app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q119. (Embedded sending)** A legal operations integration is working on this scenario: A sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Q120. (Bulk send)** A sales contract portal is working on this scenario: A developer needs to send personalized copies of an envelope to many recipients. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

**Q121. (Envelope create)** An HR onboarding workflow is working on this scenario: An integration needs to send an envelope for signature immediately. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Q122. (Draft envelope)** A partner-built customer app is working on this scenario: A developer wants to create an envelope but not send it yet. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Q123. (Cancel envelope)** A public-sector records process is working on this scenario: A sent envelope has a fatal error and no one should sign it. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Q124. (Idempotency)** A real-estate transaction workflow is working on this scenario: A network retry might submit the same create-envelope request twice. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Q125. (Template reference)** A healthcare onboarding team is working on this scenario: A request uses a server template already stored in Docusign. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Q126. (Composite templates)** A university financial-aid portal is working on this scenario: A request must combine server templates, inline recipient data, and documents. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Q127. (Anchor tabs)** A banking compliance application is working on this scenario: A document can vary in page length, but the signature should appear near a specific text string. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Q128. (Embedded signing)** A procurement workflow is working on this scenario: A recipient must sign inside the host app rather than through an email link. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Q129. (Signing URL)** A legal operations integration is working on this scenario: An app has created an envelope for an embedded recipient. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Q130. (Embedded signing timing)** A sales contract portal is working on this scenario: An app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q131. (Embedded sending)** An HR onboarding workflow is working on this scenario: A sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Q132. (Bulk send)** A partner-built customer app is working on this scenario: A developer needs to send personalized copies of an envelope to many recipients. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

**Q133. (Envelope create)** A public-sector records process is working on this scenario: An integration needs to send an envelope for signature immediately. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Q134. (Draft envelope)** A real-estate transaction workflow is working on this scenario: A developer wants to create an envelope but not send it yet. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Q135. (Cancel envelope)** A healthcare onboarding team is working on this scenario: A sent envelope has a fatal error and no one should sign it. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Q136. (Idempotency)** A university financial-aid portal is working on this scenario: A network retry might submit the same create-envelope request twice. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Q137. (Template reference)** A banking compliance application is working on this scenario: A request uses a server template already stored in Docusign. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Q138. (Composite templates)** A procurement workflow is working on this scenario: A request must combine server templates, inline recipient data, and documents. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Q139. (Anchor tabs)** A legal operations integration is working on this scenario: A document can vary in page length, but the signature should appear near a specific text string. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Q140. (Embedded signing)** A sales contract portal is working on this scenario: A recipient must sign inside the host app rather than through an email link. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Q141. (Signing URL)** An HR onboarding workflow is working on this scenario: An app has created an envelope for an embedded recipient. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Q142. (Embedded signing timing)** A partner-built customer app is working on this scenario: An app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q143. (Embedded sending)** A public-sector records process is working on this scenario: A sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Q144. (Bulk send)** A real-estate transaction workflow is working on this scenario: A developer needs to send personalized copies of an envelope to many recipients. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

**Q145. (Envelope create)** A healthcare onboarding team is working on this scenario: An integration needs to send an envelope for signature immediately. Which envelope status should be used in the create request?

A. created
B. voided
C. deleted
D. sent

**Answer:** D. sent

**Explanation:** Status sent sends the envelope; created saves it as a draft.

**Q146. (Draft envelope)** A university financial-aid portal is working on this scenario: A developer wants to create an envelope but not send it yet. Which status is appropriate?

A. voided
B. completed
C. created
D. sent

**Answer:** C. created

**Explanation:** The created status keeps an envelope in draft state.

**Q147. (Cancel envelope)** A banking compliance application is working on this scenario: A sent envelope has a fatal error and no one should sign it. Which status should be set?

A. created
B. voided
C. deleted
D. purged

**Answer:** B. voided

**Explanation:** Voiding cancels an in-process envelope and stops signing.

**Q148. (Idempotency)** A procurement workflow is working on this scenario: A network retry might submit the same create-envelope request twice. Which value helps avoid duplicate envelopes?

A. transactionId
B. recipientId
C. retryId
D. brandId

**Answer:** A. transactionId

**Explanation:** Supplying a transactionId supports idempotent envelope creation.

**Q149. (Template reference)** A legal operations integration is working on this scenario: A request uses a server template already stored in Docusign. Which value identifies the template?

A. clientUserId
B. returnUrl
C. basePath
D. templateId

**Answer:** D. templateId

**Explanation:** templateId references an existing template in an envelope request.

**Q150. (Composite templates)** A sales contract portal is working on this scenario: A request must combine server templates, inline recipient data, and documents. Which model best supports that structure?

A. Brand destination URLs
B. Connect 2.0 only
C. Composite templates
D. Bulk send list only

**Answer:** C. Composite templates

**Explanation:** Composite templates allow combining server templates, inline templates, and documents.

**Q151. (Anchor tabs)** An HR onboarding workflow is working on this scenario: A document can vary in page length, but the signature should appear near a specific text string. Which tab placement method is best?

A. CORS origin settings
B. Anchor tagging with anchorString and offsets
C. Fixed x/y coordinates only
D. Branding resource files

**Answer:** B. Anchor tagging with anchorString and offsets

**Explanation:** Anchor tabs place fields relative to document text.

**Q152. (Embedded signing)** A partner-built customer app is working on this scenario: A recipient must sign inside the host app rather than through an email link. Which recipient property marks embedded signing?

A. clientUserId
B. emailNotification
C. brandId
D. listId

**Answer:** A. clientUserId

**Explanation:** clientUserId identifies a captive/embedded recipient.

**Q153. (Signing URL)** A public-sector records process is working on this scenario: An app has created an envelope for an embedded recipient. What must the app request before the recipient can sign in the host application?

A. A Connect JSON SIM event
B. A bulk send batch ID
C. A brand resource file
D. A recipient view URL from EnvelopeViews:createRecipient

**Answer:** D. A recipient view URL from EnvelopeViews:createRecipient

**Explanation:** Embedded signing requires requesting a short-lived recipient view URL.

**Q154. (Embedded signing timing)** A real-estate transaction workflow is working on this scenario: An app creates embedded signing URLs long before users are ready. What is the risk?

A. The account base URI disappears
B. Connect retries stop
C. The short-lived URL may expire before use
D. The template ID changes

**Answer:** C. The short-lived URL may expire before use

**Explanation:** Embedded signing URLs are short-lived and should be generated when the user is ready.

**Q155. (Embedded sending)** A healthcare onboarding team is working on this scenario: A sender must prepare or edit an envelope from inside a custom app. Which endpoint family is relevant?

A. Connect retry log
B. EnvelopeViews:createSender
C. BulkSend:createBulkSendList
D. Agreements:getAgreement

**Answer:** B. EnvelopeViews:createSender

**Explanation:** Embedded sending uses a sender view URL.

**Q156. (Bulk send)** A university financial-aid portal is working on this scenario: A developer needs to send personalized copies of an envelope to many recipients. Which feature is designed for that scenario?

A. Bulk Send
B. Recipient authentication only
C. Brand destination URLs
D. Organization Connect only

**Answer:** A. Bulk Send

**Explanation:** Bulk Send supports large batches of personalized envelopes.

### eSignature Features and Web Forms

**Q157. (Web Forms embedding)** A procurement workflow is working on this scenario: A custom website needs to render a Docusign Web Form instance inline. What client-side component is used with the instance URL?

A. EnvelopeViews:createRecipient
B. Connect JSON SIM
C. Workflow start link only
D. Docusign JS client SDK

**Answer:** D. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Q158. (Web Form correlation)** A legal operations integration is working on this scenario: An app creates one Web Form instance per customer record. Which value should be supplied to correlate back to the app?

A. brandId
B. envelopeId before creation
C. clientUserId
D. templateId

**Answer:** C. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Q159. (Identity verification)** A sales contract portal is working on this scenario: An envelope must require recipients to prove identity before signing. What must be included in the recipient configuration?

A. A template name only
B. An identity verification or recipient authentication configuration
C. A Connect retry policy
D. A workflow extension action

**Answer:** B. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Q160. (Recipient authentication)** An HR onboarding workflow is working on this scenario: A signer should receive a one-time code before accessing the envelope. Which feature category applies?

A. Recipient authentication
B. Bulk Send only
C. Agreement Manager extraction
D. App Center listing

**Answer:** A. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Q161. (Brand destination URLs)** A partner-built customer app is working on this scenario: Remote signers should be redirected to a custom page after finishing. Which branding feature is relevant?

A. Envelope transactionId
B. JWT consent URL
C. Bulk send list ID
D. Brand destination URLs

**Answer:** D. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Q162. (Connected Fields)** A public-sector records process is working on this scenario: A signer-provided value must be checked against an external data source during signing. Which feature supports this?

A. Envelope purge
B. Safe Exam Browser
C. Connected Fields or data verification
D. Agreement import only

**Answer:** C. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Q163. (ID Evidence)** A real-estate transaction workflow is working on this scenario: A system must retrieve retained data about a completed ID Verification event. Which API is relevant?

A. WorkflowInstanceManagement only
B. ID Evidence API
C. Web Forms API only
D. BulkSend API

**Answer:** B. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Q164. (Web Forms embedding)** A healthcare onboarding team is working on this scenario: A custom website needs to render a Docusign Web Form instance inline. What client-side component is used with the instance URL?

A. Docusign JS client SDK
B. EnvelopeViews:createRecipient
C. Connect JSON SIM
D. Workflow start link only

**Answer:** A. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Q165. (Web Form correlation)** A university financial-aid portal is working on this scenario: An app creates one Web Form instance per customer record. Which value should be supplied to correlate back to the app?

A. templateId
B. brandId
C. envelopeId before creation
D. clientUserId

**Answer:** D. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Q166. (Identity verification)** A banking compliance application is working on this scenario: An envelope must require recipients to prove identity before signing. What must be included in the recipient configuration?

A. A workflow extension action
B. A template name only
C. An identity verification or recipient authentication configuration
D. A Connect retry policy

**Answer:** C. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Q167. (Recipient authentication)** A procurement workflow is working on this scenario: A signer should receive a one-time code before accessing the envelope. Which feature category applies?

A. App Center listing
B. Recipient authentication
C. Bulk Send only
D. Agreement Manager extraction

**Answer:** B. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Q168. (Brand destination URLs)** A legal operations integration is working on this scenario: Remote signers should be redirected to a custom page after finishing. Which branding feature is relevant?

A. Brand destination URLs
B. Envelope transactionId
C. JWT consent URL
D. Bulk send list ID

**Answer:** A. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Q169. (Connected Fields)** A sales contract portal is working on this scenario: A signer-provided value must be checked against an external data source during signing. Which feature supports this?

A. Agreement import only
B. Envelope purge
C. Safe Exam Browser
D. Connected Fields or data verification

**Answer:** D. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Q170. (ID Evidence)** An HR onboarding workflow is working on this scenario: A system must retrieve retained data about a completed ID Verification event. Which API is relevant?

A. BulkSend API
B. WorkflowInstanceManagement only
C. ID Evidence API
D. Web Forms API only

**Answer:** C. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Q171. (Web Forms embedding)** A partner-built customer app is working on this scenario: A custom website needs to render a Docusign Web Form instance inline. What client-side component is used with the instance URL?

A. Workflow start link only
B. Docusign JS client SDK
C. EnvelopeViews:createRecipient
D. Connect JSON SIM

**Answer:** B. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Q172. (Web Form correlation)** A public-sector records process is working on this scenario: An app creates one Web Form instance per customer record. Which value should be supplied to correlate back to the app?

A. clientUserId
B. templateId
C. brandId
D. envelopeId before creation

**Answer:** A. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Q173. (Identity verification)** A real-estate transaction workflow is working on this scenario: An envelope must require recipients to prove identity before signing. What must be included in the recipient configuration?

A. A Connect retry policy
B. A workflow extension action
C. A template name only
D. An identity verification or recipient authentication configuration

**Answer:** D. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Q174. (Recipient authentication)** A healthcare onboarding team is working on this scenario: A signer should receive a one-time code before accessing the envelope. Which feature category applies?

A. Agreement Manager extraction
B. App Center listing
C. Recipient authentication
D. Bulk Send only

**Answer:** C. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Q175. (Brand destination URLs)** A university financial-aid portal is working on this scenario: Remote signers should be redirected to a custom page after finishing. Which branding feature is relevant?

A. Bulk send list ID
B. Brand destination URLs
C. Envelope transactionId
D. JWT consent URL

**Answer:** B. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Q176. (Connected Fields)** A banking compliance application is working on this scenario: A signer-provided value must be checked against an external data source during signing. Which feature supports this?

A. Connected Fields or data verification
B. Agreement import only
C. Envelope purge
D. Safe Exam Browser

**Answer:** A. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Q177. (ID Evidence)** A procurement workflow is working on this scenario: A system must retrieve retained data about a completed ID Verification event. Which API is relevant?

A. Web Forms API only
B. BulkSend API
C. WorkflowInstanceManagement only
D. ID Evidence API

**Answer:** D. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Q178. (Web Forms embedding)** A legal operations integration is working on this scenario: A custom website needs to render a Docusign Web Form instance inline. What client-side component is used with the instance URL?

A. Connect JSON SIM
B. Workflow start link only
C. Docusign JS client SDK
D. EnvelopeViews:createRecipient

**Answer:** C. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Q179. (Web Form correlation)** A sales contract portal is working on this scenario: An app creates one Web Form instance per customer record. Which value should be supplied to correlate back to the app?

A. envelopeId before creation
B. clientUserId
C. templateId
D. brandId

**Answer:** B. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Q180. (Identity verification)** An HR onboarding workflow is working on this scenario: An envelope must require recipients to prove identity before signing. What must be included in the recipient configuration?

A. An identity verification or recipient authentication configuration
B. A Connect retry policy
C. A workflow extension action
D. A template name only

**Answer:** A. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Q181. (Recipient authentication)** A partner-built customer app is working on this scenario: A signer should receive a one-time code before accessing the envelope. Which feature category applies?

A. Bulk Send only
B. Agreement Manager extraction
C. App Center listing
D. Recipient authentication

**Answer:** D. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Q182. (Brand destination URLs)** A public-sector records process is working on this scenario: Remote signers should be redirected to a custom page after finishing. Which branding feature is relevant?

A. JWT consent URL
B. Bulk send list ID
C. Brand destination URLs
D. Envelope transactionId

**Answer:** C. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

**Q183. (Connected Fields)** A real-estate transaction workflow is working on this scenario: A signer-provided value must be checked against an external data source during signing. Which feature supports this?

A. Safe Exam Browser
B. Connected Fields or data verification
C. Agreement import only
D. Envelope purge

**Answer:** B. Connected Fields or data verification

**Explanation:** Connected Fields and data verification support real-time validation scenarios.

**Q184. (ID Evidence)** A healthcare onboarding team is working on this scenario: A system must retrieve retained data about a completed ID Verification event. Which API is relevant?

A. ID Evidence API
B. Web Forms API only
C. BulkSend API
D. WorkflowInstanceManagement only

**Answer:** A. ID Evidence API

**Explanation:** The ID Evidence API retrieves retained evidence from ID verification events.

**Q185. (Web Forms embedding)** A university financial-aid portal is working on this scenario: A custom website needs to render a Docusign Web Form instance inline. What client-side component is used with the instance URL?

A. EnvelopeViews:createRecipient
B. Connect JSON SIM
C. Workflow start link only
D. Docusign JS client SDK

**Answer:** D. Docusign JS client SDK

**Explanation:** Docusign JS renders Web Form instances in the host page.

**Q186. (Web Form correlation)** A banking compliance application is working on this scenario: An app creates one Web Form instance per customer record. Which value should be supplied to correlate back to the app?

A. brandId
B. envelopeId before creation
C. clientUserId
D. templateId

**Answer:** C. clientUserId

**Explanation:** clientUserId can map a form instance to an external record.

**Q187. (Identity verification)** A procurement workflow is working on this scenario: An envelope must require recipients to prove identity before signing. What must be included in the recipient configuration?

A. A template name only
B. An identity verification or recipient authentication configuration
C. A Connect retry policy
D. A workflow extension action

**Answer:** B. An identity verification or recipient authentication configuration

**Explanation:** Recipient authentication or ID verification settings enforce identity checks.

**Q188. (Recipient authentication)** A legal operations integration is working on this scenario: A signer should receive a one-time code before accessing the envelope. Which feature category applies?

A. Recipient authentication
B. Bulk Send only
C. Agreement Manager extraction
D. App Center listing

**Answer:** A. Recipient authentication

**Explanation:** Recipient authentication controls access to signing.

**Q189. (Brand destination URLs)** A sales contract portal is working on this scenario: Remote signers should be redirected to a custom page after finishing. Which branding feature is relevant?

A. Envelope transactionId
B. JWT consent URL
C. Bulk send list ID
D. Brand destination URLs

**Answer:** D. Brand destination URLs

**Explanation:** Brand destination URLs control post-signing redirect destinations for remote signing.

### Agreement Manager API

**Q190. (Agreement data)** A university financial-aid portal is working on this scenario: A custom app needs structured extracted data for a specific agreement. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q191. (Agreement list)** A banking compliance application is working on this scenario: An app needs to find agreements matching criteria before retrieving details. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q192. (Legacy import)** A procurement workflow is working on this scenario: A company wants to bring existing contracts into Agreement Manager. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q193. (Agreement documents)** A legal operations integration is working on this scenario: A downstream system needs a copy of an agreement document. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q194. (Agreement data)** A sales contract portal is working on this scenario: A custom app needs structured extracted data for a specific agreement. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q195. (Agreement list)** An HR onboarding workflow is working on this scenario: An app needs to find agreements matching criteria before retrieving details. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q196. (Legacy import)** A partner-built customer app is working on this scenario: A company wants to bring existing contracts into Agreement Manager. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q197. (Agreement documents)** A public-sector records process is working on this scenario: A downstream system needs a copy of an agreement document. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q198. (Agreement data)** A real-estate transaction workflow is working on this scenario: A custom app needs structured extracted data for a specific agreement. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q199. (Agreement list)** A healthcare onboarding team is working on this scenario: An app needs to find agreements matching criteria before retrieving details. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q200. (Legacy import)** A university financial-aid portal is working on this scenario: A company wants to bring existing contracts into Agreement Manager. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q201. (Agreement documents)** A banking compliance application is working on this scenario: A downstream system needs a copy of an agreement document. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q202. (Agreement data)** A procurement workflow is working on this scenario: A custom app needs structured extracted data for a specific agreement. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q203. (Agreement list)** A legal operations integration is working on this scenario: An app needs to find agreements matching criteria before retrieving details. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

**Q204. (Legacy import)** A sales contract portal is working on this scenario: A company wants to bring existing contracts into Agreement Manager. Which capability matters?

A. Agreement upload or bulk import using the Agreement Manager API
B. Recipient view URLs
C. Implicit Grant
D. Envelope-level Connect only

**Answer:** A. Agreement upload or bulk import using the Agreement Manager API

**Explanation:** Agreement Manager supports bringing legacy agreement content and metadata into the repository.

**Q205. (Agreement documents)** An HR onboarding workflow is working on this scenario: A downstream system needs a copy of an agreement document. What should the integration plan include?

A. A Web Forms client SDK only
B. A Connect listener with no API calls
C. A bulk send CSV
D. Document download using Agreement Manager capabilities

**Answer:** D. Document download using Agreement Manager capabilities

**Explanation:** Agreement Manager API scenarios include retrieving agreement documents and metadata.

**Q206. (Agreement data)** A partner-built customer app is working on this scenario: A custom app needs structured extracted data for a specific agreement. Which operation is most relevant?

A. Workflow trigger requirements
B. BulkSend:createBulkSendList
C. Agreements:getAgreement
D. Envelopes:create

**Answer:** C. Agreements:getAgreement

**Explanation:** Agreements:getAgreement retrieves agreement data for a specific agreement.

**Q207. (Agreement list)** A public-sector records process is working on this scenario: An app needs to find agreements matching criteria before retrieving details. Which API pattern is relevant?

A. Configure CORS origins
B. List or search agreements, then retrieve the target agreement
C. Create an envelope with status voided
D. Use only brand destination URLs

**Answer:** B. List or search agreements, then retrieve the target agreement

**Explanation:** Agreement Manager integrations commonly list/search then retrieve detailed agreement data.

### Workflow Builder and Workflow API

**Q208. (Workflow steps)** A procurement workflow is working on this scenario: A workflow must collect form data before sending a document for signature. Which step order best fits?

A. Collect Data with Web Forms, then Get Signatures
B. Get Signatures, then collect data
C. Archive first, then start
D. Void envelope, then collect data

**Answer:** A. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Q209. (Identity step)** A legal operations integration is working on this scenario: A process must gather participant data and then verify identity. Which sequence is best?

A. Verify identity after archiving only
B. Get Signatures before collecting data
C. Connect retry before web form
D. Collect Data with Web Forms, then Verify Someone's Identity

**Answer:** D. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Q210. (Extension step)** A sales contract portal is working on this scenario: After signing, the completed document must be stored in an external file service. Which workflow step type is appropriate?

A. Get Signatures step only
B. CORS configuration
C. Extension step using a file/archive extension app
D. Branching rule only

**Answer:** C. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Q211. (Branching)** An HR onboarding workflow is working on this scenario: A workflow should follow different paths based on a form response. Which workflow capability is used?

A. Brand destination URL
B. Branching or conditional rules
C. JWT consent
D. Envelope purge

**Answer:** B. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Q212. (Start method)** A partner-built customer app is working on this scenario: A portal link should launch a workflow and pass values in the trigger URL. Which start method fits?

A. From a Link
B. Manually by someone in your organization only
C. From an envelope void event only
D. From a bulk send batch only

**Answer:** A. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Q213. (API trigger)** A public-sector records process is working on this scenario: A backend service must programmatically trigger a workflow. Which start method/API pattern is relevant?

A. Remote signing email only
B. Brand resource file upload
C. Template reference ID only
D. From an API call with Workflow Builder API trigger requirements

**Answer:** D. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Q214. (Runtime errors)** A real-estate transaction workflow is working on this scenario: A workflow trigger fails because required starting variables are missing. What should the developer inspect?

A. Connect HMAC secret only
B. Bulk send list status only
C. Workflow trigger requirements and variable mapping
D. Brand destination URLs

**Answer:** C. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Q215. (Embedding workflow)** A healthcare onboarding team is working on this scenario: A custom app needs to display a workflow experience inside the app. Which capability should be considered?

A. Agreement type extraction only
B. Embedding or launching the workflow according to its configured start method
C. Envelope purge
D. JWT admin consent only

**Answer:** B. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Q216. (Installed extensions)** A university financial-aid portal is working on this scenario: A workflow should call a third-party service through an extension app. What must be true?

A. The extension app must be installed and available for the workflow step
B. The envelope must be voided first
C. The app must use implicit grant
D. The Web Form must be public

**Answer:** A. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Q217. (Workflow steps)** A banking compliance application is working on this scenario: A workflow must collect form data before sending a document for signature. Which step order best fits?

A. Get Signatures, then collect data
B. Archive first, then start
C. Void envelope, then collect data
D. Collect Data with Web Forms, then Get Signatures

**Answer:** D. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Q218. (Identity step)** A procurement workflow is working on this scenario: A process must gather participant data and then verify identity. Which sequence is best?

A. Get Signatures before collecting data
B. Connect retry before web form
C. Collect Data with Web Forms, then Verify Someone's Identity
D. Verify identity after archiving only

**Answer:** C. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Q219. (Extension step)** A legal operations integration is working on this scenario: After signing, the completed document must be stored in an external file service. Which workflow step type is appropriate?

A. CORS configuration
B. Extension step using a file/archive extension app
C. Branching rule only
D. Get Signatures step only

**Answer:** B. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Q220. (Branching)** A sales contract portal is working on this scenario: A workflow should follow different paths based on a form response. Which workflow capability is used?

A. Branching or conditional rules
B. JWT consent
C. Envelope purge
D. Brand destination URL

**Answer:** A. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Q221. (Start method)** An HR onboarding workflow is working on this scenario: A portal link should launch a workflow and pass values in the trigger URL. Which start method fits?

A. Manually by someone in your organization only
B. From an envelope void event only
C. From a bulk send batch only
D. From a Link

**Answer:** D. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Q222. (API trigger)** A partner-built customer app is working on this scenario: A backend service must programmatically trigger a workflow. Which start method/API pattern is relevant?

A. Brand resource file upload
B. Template reference ID only
C. From an API call with Workflow Builder API trigger requirements
D. Remote signing email only

**Answer:** C. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Q223. (Runtime errors)** A public-sector records process is working on this scenario: A workflow trigger fails because required starting variables are missing. What should the developer inspect?

A. Bulk send list status only
B. Workflow trigger requirements and variable mapping
C. Brand destination URLs
D. Connect HMAC secret only

**Answer:** B. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Q224. (Embedding workflow)** A real-estate transaction workflow is working on this scenario: A custom app needs to display a workflow experience inside the app. Which capability should be considered?

A. Embedding or launching the workflow according to its configured start method
B. Envelope purge
C. JWT admin consent only
D. Agreement type extraction only

**Answer:** A. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Q225. (Installed extensions)** A healthcare onboarding team is working on this scenario: A workflow should call a third-party service through an extension app. What must be true?

A. The envelope must be voided first
B. The app must use implicit grant
C. The Web Form must be public
D. The extension app must be installed and available for the workflow step

**Answer:** D. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Q226. (Workflow steps)** A university financial-aid portal is working on this scenario: A workflow must collect form data before sending a document for signature. Which step order best fits?

A. Archive first, then start
B. Void envelope, then collect data
C. Collect Data with Web Forms, then Get Signatures
D. Get Signatures, then collect data

**Answer:** C. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Q227. (Identity step)** A banking compliance application is working on this scenario: A process must gather participant data and then verify identity. Which sequence is best?

A. Connect retry before web form
B. Collect Data with Web Forms, then Verify Someone's Identity
C. Verify identity after archiving only
D. Get Signatures before collecting data

**Answer:** B. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Q228. (Extension step)** A procurement workflow is working on this scenario: After signing, the completed document must be stored in an external file service. Which workflow step type is appropriate?

A. Extension step using a file/archive extension app
B. Branching rule only
C. Get Signatures step only
D. CORS configuration

**Answer:** A. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Q229. (Branching)** A legal operations integration is working on this scenario: A workflow should follow different paths based on a form response. Which workflow capability is used?

A. JWT consent
B. Envelope purge
C. Brand destination URL
D. Branching or conditional rules

**Answer:** D. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Q230. (Start method)** A sales contract portal is working on this scenario: A portal link should launch a workflow and pass values in the trigger URL. Which start method fits?

A. From an envelope void event only
B. From a bulk send batch only
C. From a Link
D. Manually by someone in your organization only

**Answer:** C. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Q231. (API trigger)** An HR onboarding workflow is working on this scenario: A backend service must programmatically trigger a workflow. Which start method/API pattern is relevant?

A. Template reference ID only
B. From an API call with Workflow Builder API trigger requirements
C. Remote signing email only
D. Brand resource file upload

**Answer:** B. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Q232. (Runtime errors)** A partner-built customer app is working on this scenario: A workflow trigger fails because required starting variables are missing. What should the developer inspect?

A. Workflow trigger requirements and variable mapping
B. Brand destination URLs
C. Connect HMAC secret only
D. Bulk send list status only

**Answer:** A. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Q233. (Embedding workflow)** A public-sector records process is working on this scenario: A custom app needs to display a workflow experience inside the app. Which capability should be considered?

A. Envelope purge
B. JWT admin consent only
C. Agreement type extraction only
D. Embedding or launching the workflow according to its configured start method

**Answer:** D. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Q234. (Installed extensions)** A real-estate transaction workflow is working on this scenario: A workflow should call a third-party service through an extension app. What must be true?

A. The app must use implicit grant
B. The Web Form must be public
C. The extension app must be installed and available for the workflow step
D. The envelope must be voided first

**Answer:** C. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Q235. (Workflow steps)** A healthcare onboarding team is working on this scenario: A workflow must collect form data before sending a document for signature. Which step order best fits?

A. Void envelope, then collect data
B. Collect Data with Web Forms, then Get Signatures
C. Get Signatures, then collect data
D. Archive first, then start

**Answer:** B. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Q236. (Identity step)** A university financial-aid portal is working on this scenario: A process must gather participant data and then verify identity. Which sequence is best?

A. Collect Data with Web Forms, then Verify Someone's Identity
B. Verify identity after archiving only
C. Get Signatures before collecting data
D. Connect retry before web form

**Answer:** A. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Q237. (Extension step)** A banking compliance application is working on this scenario: After signing, the completed document must be stored in an external file service. Which workflow step type is appropriate?

A. Branching rule only
B. Get Signatures step only
C. CORS configuration
D. Extension step using a file/archive extension app

**Answer:** D. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Q238. (Branching)** A procurement workflow is working on this scenario: A workflow should follow different paths based on a form response. Which workflow capability is used?

A. Envelope purge
B. Brand destination URL
C. Branching or conditional rules
D. JWT consent

**Answer:** C. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Q239. (Start method)** A legal operations integration is working on this scenario: A portal link should launch a workflow and pass values in the trigger URL. Which start method fits?

A. From a bulk send batch only
B. From a Link
C. Manually by someone in your organization only
D. From an envelope void event only

**Answer:** B. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Q240. (API trigger)** A sales contract portal is working on this scenario: A backend service must programmatically trigger a workflow. Which start method/API pattern is relevant?

A. From an API call with Workflow Builder API trigger requirements
B. Remote signing email only
C. Brand resource file upload
D. Template reference ID only

**Answer:** A. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Q241. (Runtime errors)** An HR onboarding workflow is working on this scenario: A workflow trigger fails because required starting variables are missing. What should the developer inspect?

A. Brand destination URLs
B. Connect HMAC secret only
C. Bulk send list status only
D. Workflow trigger requirements and variable mapping

**Answer:** D. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Q242. (Embedding workflow)** A partner-built customer app is working on this scenario: A custom app needs to display a workflow experience inside the app. Which capability should be considered?

A. JWT admin consent only
B. Agreement type extraction only
C. Embedding or launching the workflow according to its configured start method
D. Envelope purge

**Answer:** C. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Q243. (Installed extensions)** A public-sector records process is working on this scenario: A workflow should call a third-party service through an extension app. What must be true?

A. The Web Form must be public
B. The extension app must be installed and available for the workflow step
C. The envelope must be voided first
D. The app must use implicit grant

**Answer:** B. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

**Q244. (Workflow steps)** A real-estate transaction workflow is working on this scenario: A workflow must collect form data before sending a document for signature. Which step order best fits?

A. Collect Data with Web Forms, then Get Signatures
B. Get Signatures, then collect data
C. Archive first, then start
D. Void envelope, then collect data

**Answer:** A. Collect Data with Web Forms, then Get Signatures

**Explanation:** Workflow step order should match the business process.

**Q245. (Identity step)** A healthcare onboarding team is working on this scenario: A process must gather participant data and then verify identity. Which sequence is best?

A. Verify identity after archiving only
B. Get Signatures before collecting data
C. Connect retry before web form
D. Collect Data with Web Forms, then Verify Someone's Identity

**Answer:** D. Collect Data with Web Forms, then Verify Someone's Identity

**Explanation:** Collect required data before the identity verification step if the scenario requires it.

**Q246. (Extension step)** A university financial-aid portal is working on this scenario: After signing, the completed document must be stored in an external file service. Which workflow step type is appropriate?

A. Get Signatures step only
B. CORS configuration
C. Extension step using a file/archive extension app
D. Branching rule only

**Answer:** C. Extension step using a file/archive extension app

**Explanation:** Extension steps call external services through installed extension apps.

**Q247. (Branching)** A banking compliance application is working on this scenario: A workflow should follow different paths based on a form response. Which workflow capability is used?

A. Brand destination URL
B. Branching or conditional rules
C. JWT consent
D. Envelope purge

**Answer:** B. Branching or conditional rules

**Explanation:** Branching rules route workflows based on conditions.

**Q248. (Start method)** A procurement workflow is working on this scenario: A portal link should launch a workflow and pass values in the trigger URL. Which start method fits?

A. From a Link
B. Manually by someone in your organization only
C. From an envelope void event only
D. From a bulk send batch only

**Answer:** A. From a Link

**Explanation:** A link start method can launch a workflow and pass URL values.

**Q249. (API trigger)** A legal operations integration is working on this scenario: A backend service must programmatically trigger a workflow. Which start method/API pattern is relevant?

A. Remote signing email only
B. Brand resource file upload
C. Template reference ID only
D. From an API call with Workflow Builder API trigger requirements

**Answer:** D. From an API call with Workflow Builder API trigger requirements

**Explanation:** API-triggered workflows use trigger requirements and workflow API calls.

**Q250. (Runtime errors)** A sales contract portal is working on this scenario: A workflow trigger fails because required starting variables are missing. What should the developer inspect?

A. Connect HMAC secret only
B. Bulk send list status only
C. Workflow trigger requirements and variable mapping
D. Brand destination URLs

**Answer:** C. Workflow trigger requirements and variable mapping

**Explanation:** Workflow trigger requirements define required input variables.

**Q251. (Embedding workflow)** An HR onboarding workflow is working on this scenario: A custom app needs to display a workflow experience inside the app. Which capability should be considered?

A. Agreement type extraction only
B. Embedding or launching the workflow according to its configured start method
C. Envelope purge
D. JWT admin consent only

**Answer:** B. Embedding or launching the workflow according to its configured start method

**Explanation:** Workflow integration depends on the configured start method and embedding/launch pattern.

**Q252. (Installed extensions)** A partner-built customer app is working on this scenario: A workflow should call a third-party service through an extension app. What must be true?

A. The extension app must be installed and available for the workflow step
B. The envelope must be voided first
C. The app must use implicit grant
D. The Web Form must be public

**Answer:** A. The extension app must be installed and available for the workflow step

**Explanation:** Workflow Builder can use installed extension applications in extension steps.

### App Center and Extension Apps

**Q253. (Extension app role)** A real-estate transaction workflow is working on this scenario: A customer wants Docusign to call an external service during an agreement process. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Q254. (Public vs private)** A healthcare onboarding team is working on this scenario: An app is only for one organization's internal Docusign accounts. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Q255. (Public App Center)** A university financial-aid portal is working on this scenario: A partner wants customers broadly to discover and install an app. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Q256. (Manifest)** A banking compliance application is working on this scenario: An extension app action must call an external API endpoint. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Q257. (Connections)** A procurement workflow is working on this scenario: An action must use external OAuth credentials. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Q258. (connectionsReference)** A legal operations integration is working on this scenario: An action needs to use a named connection from the manifest. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Q259. (API proxy)** A sales contract portal is working on this scenario: The third-party API format does not match what the extension app action needs. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Q260. (Firewall)** An HR onboarding workflow is working on this scenario: Docusign must call a customer-hosted endpoint for an extension action. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Q261. (Data IO)** A partner-built customer app is working on this scenario: A workflow needs to read and write structured records in another system. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Q262. (File IO)** A public-sector records process is working on this scenario: A workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Q263. (Connected Fields)** A real-estate transaction workflow is working on this scenario: An extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q264. (Data Verification)** A healthcare onboarding team is working on this scenario: A signer enters a bank account value that must be validated at signing. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

**Q265. (Extension app role)** A university financial-aid portal is working on this scenario: A customer wants Docusign to call an external service during an agreement process. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Q266. (Public vs private)** A banking compliance application is working on this scenario: An app is only for one organization's internal Docusign accounts. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Q267. (Public App Center)** A procurement workflow is working on this scenario: A partner wants customers broadly to discover and install an app. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Q268. (Manifest)** A legal operations integration is working on this scenario: An extension app action must call an external API endpoint. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Q269. (Connections)** A sales contract portal is working on this scenario: An action must use external OAuth credentials. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Q270. (connectionsReference)** An HR onboarding workflow is working on this scenario: An action needs to use a named connection from the manifest. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Q271. (API proxy)** A partner-built customer app is working on this scenario: The third-party API format does not match what the extension app action needs. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Q272. (Firewall)** A public-sector records process is working on this scenario: Docusign must call a customer-hosted endpoint for an extension action. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Q273. (Data IO)** A real-estate transaction workflow is working on this scenario: A workflow needs to read and write structured records in another system. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Q274. (File IO)** A healthcare onboarding team is working on this scenario: A workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Q275. (Connected Fields)** A university financial-aid portal is working on this scenario: An extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q276. (Data Verification)** A banking compliance application is working on this scenario: A signer enters a bank account value that must be validated at signing. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

**Q277. (Extension app role)** A procurement workflow is working on this scenario: A customer wants Docusign to call an external service during an agreement process. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Q278. (Public vs private)** A legal operations integration is working on this scenario: An app is only for one organization's internal Docusign accounts. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Q279. (Public App Center)** A sales contract portal is working on this scenario: A partner wants customers broadly to discover and install an app. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Q280. (Manifest)** An HR onboarding workflow is working on this scenario: An extension app action must call an external API endpoint. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Q281. (Connections)** A partner-built customer app is working on this scenario: An action must use external OAuth credentials. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Q282. (connectionsReference)** A public-sector records process is working on this scenario: An action needs to use a named connection from the manifest. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Q283. (API proxy)** A real-estate transaction workflow is working on this scenario: The third-party API format does not match what the extension app action needs. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Q284. (Firewall)** A healthcare onboarding team is working on this scenario: Docusign must call a customer-hosted endpoint for an extension action. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Q285. (Data IO)** A university financial-aid portal is working on this scenario: A workflow needs to read and write structured records in another system. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Q286. (File IO)** A banking compliance application is working on this scenario: A workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Q287. (Connected Fields)** A procurement workflow is working on this scenario: An extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q288. (Data Verification)** A legal operations integration is working on this scenario: A signer enters a bank account value that must be validated at signing. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

**Q289. (Extension app role)** A sales contract portal is working on this scenario: A customer wants Docusign to call an external service during an agreement process. What does an extension app provide?

A. A replacement for OAuth consent
B. Unlimited eSignature API calls
C. A mandatory PDF renderer
D. A packaged way to connect external functionality into Docusign

**Answer:** D. A packaged way to connect external functionality into Docusign

**Explanation:** Extension apps extend Docusign with external service actions and data.

**Q290. (Public vs private)** An HR onboarding workflow is working on this scenario: An app is only for one organization's internal Docusign accounts. Which distribution is most appropriate?

A. Implicit Grant application
B. Recipient Connect only
C. Private extension app
D. Public App Center listing

**Answer:** C. Private extension app

**Explanation:** Private apps are limited to selected accounts or the publisher's organization.

**Q291. (Public App Center)** A partner-built customer app is working on this scenario: A partner wants customers broadly to discover and install an app. Which distribution goal applies?

A. Demo-only template
B. Public extension app published to the Docusign App Center
C. Private app for one account only
D. Envelope-level Connect only

**Answer:** B. Public extension app published to the Docusign App Center

**Explanation:** Public App Center distribution is for broad customer availability.

**Q292. (Manifest)** A public-sector records process is working on this scenario: An extension app action must call an external API endpoint. Where is that endpoint represented?

A. In an action definition in the extension app manifest
B. In an envelope email subject
C. In a recipient tab label
D. In the Safe Exam Browser

**Answer:** A. In an action definition in the extension app manifest

**Explanation:** Actions in the manifest describe calls to external endpoints.

**Q293. (Connections)** A real-estate transaction workflow is working on this scenario: An action must use external OAuth credentials. Which manifest object defines reusable auth details?

A. publisher only
B. brandColors
C. bulkCopies
D. connections

**Answer:** D. connections

**Explanation:** The connections object defines authentication configuration used by actions.

**Q294. (connectionsReference)** A healthcare onboarding team is working on this scenario: An action needs to use a named connection from the manifest. What links the action to that authentication configuration?

A. transactionId
B. brandId
C. connectionsReference
D. recipientId

**Answer:** C. connectionsReference

**Explanation:** connectionsReference ties an action to a connection definition.

**Q295. (API proxy)** A university financial-aid portal is working on this scenario: The third-party API format does not match what the extension app action needs. What architecture component can transform requests and responses?

A. Bulk send CSV
B. API proxy
C. Brand destination URL
D. Envelope void status

**Answer:** B. API proxy

**Explanation:** An API proxy can mediate between Docusign and the external service.

**Q296. (Firewall)** A banking compliance application is working on this scenario: Docusign must call a customer-hosted endpoint for an extension action. What network consideration is important?

A. Allow Docusign outbound requests through the endpoint firewall
B. Disable all OAuth scopes
C. Use only demo endpoints
D. Delete the app manifest

**Answer:** A. Allow Docusign outbound requests through the endpoint firewall

**Explanation:** The external endpoint must be reachable by Docusign.

**Q297. (Data IO)** A procurement workflow is working on this scenario: A workflow needs to read and write structured records in another system. Which extension type fits?

A. File archive only
B. Branding extension
C. Implicit Grant
D. Data IO extension app

**Answer:** D. Data IO extension app

**Explanation:** Data IO extensions read/write structured data.

**Q298. (File IO)** A legal operations integration is working on this scenario: A workflow needs to archive completed documents to an external repository. Which extension type fits?

A. Recipient authentication only
B. CORS origin only
C. File IO or file archive extension app
D. Connected Fields only

**Answer:** C. File IO or file archive extension app

**Explanation:** File IO extensions handle document storage and retrieval use cases.

**Q299. (Connected Fields)** A sales contract portal is working on this scenario: An extension needs to validate field data while a sender adds fields or a signer signs. Which extension category applies?

A. Agreement list search
B. Connected Fields
C. File archive only
D. Go-live classification

**Answer:** B. Connected Fields

**Explanation:** Connected Fields extensions integrate data validation into eSignature field/signing experiences.

**Q300. (Data Verification)** An HR onboarding workflow is working on this scenario: A signer enters a bank account value that must be validated at signing. Which extension pattern fits?

A. Data Verification triggered during eSignature signing
B. Public Auth Code only
C. Envelope purge
D. Agreement Manager import

**Answer:** A. Data Verification triggered during eSignature signing

**Explanation:** Data Verification checks signer-entered data during the signing experience.

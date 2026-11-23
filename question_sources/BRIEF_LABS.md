# Brief: write three hands-on lab guides for the Docusign IAM exam retake

The learner failed the Certified Docusign IAM Integration & Extension Developer exam (60%) with the weakest scores in
eSignature API (46%), Docusign Connect (48%), Go Live (58%) and eSignature Features & Web Forms (37%). The exam uses
business scenarios whose answers are design choices, so the learner will now BUILD small things against a Docusign
developer (demo) account to make the API behaviour concrete. Each weekday has a 15-20 min lab slot plus a longer
Saturday lab.

Write the content of three lab guides:
1. `esignature` - "Lab 1-2: eSignature API" (weeks 1-2): one envelope three ways (documents, templateId + templateRoles,
   compositeTemplates with sequence), status created vs sent, embedded signing (clientUserId, EnvelopeViews:createRecipient,
   returnUrl event values, 5-minute single-use URL), embedded sending (draft + EnvelopeViews:createSender), void vs lock,
   correct/resend, bulk send end to end (list -> envelope with placeholder -> test -> send -> batch status), focused vs
   classic view, request URL anatomy (base_uri from /oauth/userinfo, /restapi/v2.1/accounts/{accountId}/...).
2. `connect_golive` - "Lab 3: Docusign Connect + Go Live" (week 3): a listener (webhook.site for zero-code, or ngrok +
   a tiny Node/Express handler), envelope-level eventNotification on one envelope, an account-level custom configuration
   (eSignature Admin and ConnectConfigurations API, allowEnvelopePublish), JSON SIM vs legacy XML, HMAC set-up and
   verification over the RAW body (X-DocuSign-Signature-1), what happens when the listener returns non-2xx (retries,
   failure log, republish), idempotent processing; Go Live: Apps and Keys walkthrough, the four integration-key
   classifications, Start Go live steps, request logging (50 logs), API Dashboard, API Usage Center efficiency score,
   rate limits (3,000/hour per account, burst 500/30 s, polling at most once per envelope per 15 min), what changes in
   production (auth host, base_uri, secrets/RSA keys/redirect URIs, template IDs).
3. `features_webforms` - "Lab 4: eSignature Features & Web Forms" (week 4): recipient authentication (access code,
   phone/SMS, KBA US only, IDV via identityVerification.workflowId from IdentityVerifications:list; note IDV may need
   enabling in demo), authenticationMethod only records, branding (brand + brandId), web forms (standalone vs
   template-based, Configurations:getForm field names, createInstance embedded with clientUserId + Docusign JS vs remote
   with sendOption + recipients[].roleName, formValues prefill, Instances:getInstance status/envelopes), Connected Fields
   send flow (TabInfo:GetConnectedFieldsTabGroups -> extensionData -> Envelopes:create), ID Evidence API.

## Fact sources (verify; never invent endpoints, parameters or limits)
- `d:/Docusign exam/study_sections_content.py`, `d:/Docusign exam/gap_fill/exam_gap_notes.md`,
  `d:/Docusign exam/study_material.md` (official course text, includes hands-on activities - grep it)
- `d:/Docusign exam/docusign-node-quickstart/` (a Node quickstart already in the project; reference its relevant
  examples by file name where useful, but NEVER copy or print any key, secret, account ID or user ID found there)
- Deferred tool `mcp__docusign__searchDocusignDocs` (load with ToolSearch `select:mcp__docusign__searchDocusignDocs`,
  mcpClientModel "unknown") for endpoint paths, request bodies and Postman/API Explorer usage.
Prefer tools that need little code: the API Request Builder / API Explorer, the Docusign Postman collections,
webhook.site. Use placeholders like {accountId}, {base_uri}, {envelopeId}, {integrationKey}.

## Output
Write `d:/Docusign exam/tmp/papers/labs.json` with a Python script (json.dump, ensure_ascii=False, indent=2), re-load
to verify. Do not edit other files. Shape:
{"esignature": LAB, "connect_golive": LAB, "features_webforms": LAB} where LAB =
{"title": "...", "weeks": "...", "goal": "2-3 sentences", "setup": ["step", ...],
 "exercises": [ {"title": "...", "minutes": 15-60, "steps": ["imperative step", ...],
                 "api": "the key call(s): METHOD /path plus the minimal JSON body as plain text (may be multi-line)",
                 "observe": ["what to look at / what you should see", ...],
                 "examTraps": ["the exam trap this exercise teaches, one line each", ...]} , ... ] (7-10 exercises),
 "cleanup": ["..."], "takeaways": ["one-line design rule", ...] (6-10)}
Exercises should be small enough for one 15-20 minute weekday slot, except one or two marked as Saturday labs (45-60
min). Plain text only, no markdown. Reply in 3 lines when done (exercise counts, anything unverified).

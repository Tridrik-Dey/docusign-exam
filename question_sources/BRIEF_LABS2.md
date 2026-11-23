# Brief: more hands-on lab guides (strong sections + embedding)

Read `d:/Docusign exam/tmp/papers/BRIEF_LABS.md` first: same purpose, same fact sources, same safety rules (developer
/demo account only, placeholders such as {accountId}, never copy keys/IDs from the quickstart) and the SAME LAB JSON
shape. Context: the learner already scored 70-80% on API Authentication, Agreement Manager and App Center & Extension
Apps (Workflow 65%). These labs are SHORT: they run in 10-15 minute "keep-alive" slots, so 5-7 exercises of 10-15
minutes each (one optional 30-45 min exercise allowed). Focus on what the exam turns into scenarios, not basics.

The plan's app runs locally at http://127.0.0.1:5173 and now has an "Embedding lab" page: the learner pastes a URL
returned by an API call (recipient view / sender view / web form instance formUrl + instanceToken / workflow instance
URL), enters the integration key, and the page shows it three ways: (1) full-page redirect (opens a new tab),
(2) a plain <iframe>, (3) Docusign JS (bundle.js from https://js-d.docusign.com in demo: loadDocuSign(integrationKey),
then signing({url, displayFormat:'focused'}).mount(...) or webforms({url, options:{instanceToken}}).mount(...)), with an
event log of the Docusign JS events (e.g. sessionEnd). The page shows the origin to add to frameAncestors /
messageOrigins: http://127.0.0.1:5173.

Write these guides (keys of the output object):
- `auth` - "Lab 4: API Authentication": JWT (consent URL with signature impersonation, building the assertion, token,
  /oauth/userinfo), Confidential Auth Code vs Public Auth Code + PKCE (code_verifier/code_challenge S256), state, refresh
  tokens and the extended scope, admin consent vs individual consent (as reading/inspection where a lab is not practical).
- `workflow` - "Lab 5: Workflow Builder & Workflow API": build and publish a small workflow (web form -> signature),
  start methods (manual, from a link, from an API call), aow_manage, GetWorkflowsList / GetWorkflowTriggerRequirements /
  TriggerWorkflow, getWorkflowInstance(s), cancel vs pauseNewWorkflowInstances / resume, embedding the instance URL
  (redirect vs iframe; documented restrictions when embedded), consentUrl on publish.
- `extension_apps` - "Lab 6: App Center & Extension Apps": Developer Console registration (form vs manifest), a sample
  connected-fields or Data IO reference app run locally behind ngrok, connections / extensions / actions in the manifest,
  console connection + extension tests, functional test, private vs public distribution, what review checks.
- `agreement_manager` - "Lab 7: Agreement Manager API": GetAgreementsList with filters and paging, GetAgreement for one
  ID, CreateAgreementSummary (POST .../ai/actions/summarize), base path and scope, mapping extracted provisions to an
  external system, review of AI-extracted values. Only these four operations exist (plus DeleteAgreement); there is no
  getAgreementSummary.
- `embedding` - "Lab 8: Embedding - redirect vs iframe vs Docusign JS" (uses the app's Embedding lab page): embedded
  signing classic vs focused view (clientUserId, createRecipient returnUrl, frameAncestors + messageOrigins; what breaks
  when the origin is missing; which features force classic view), embedded sending (createSender on a draft), a web
  form instance (embedded vs remote), a workflow instance URL; returnUrl events vs Docusign JS sessionEnd; URL lifetime
  (5 minutes, single use); "never trust the browser: confirm with Connect". Say what to OBSERVE, but where the exact
  browser behaviour of a plain iframe is not documented, phrase it as "observe whether..." rather than asserting it.

Output: `d:/Docusign exam/tmp/papers/labs2_<part>.json` (part given in your prompt) containing only your keys, written
with a Python script (json.dump, ensure_ascii=False, indent=2) and re-loaded to verify. Do not edit other files.
Reply in 3 lines: exercise counts per guide and anything unverified.

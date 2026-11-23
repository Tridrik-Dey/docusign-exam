# Review cd1 (cd_auth, cd_golive, cd_connect, cd_esig)

cd_golive.json#4 C Reducing calls per envelope under the hourly limit: trap A ("raise the hourly limit in the API Usage Center") was factually defensible, since Update Hourly Limit exists when the plan allows it and the apps are efficient -> added a stem clause saying the plan lacks hourly limit management, reworded A to name Update Hourly Limit, updated A explanation, whyNotOthers, decode and answerText.
cd_connect.json#0 C Recipient Connect for received envelopes: trap B said "legacy XML aggregate", which gives it away, and the course says org-level Connect covers received envelopes -> removed "legacy" and added a stem clue that the listener accepts only JSON. B now fails only because org-level Connect supports only JSON SIM (confirmed in the Developer Center docs). Updated B explanation, whyNotOthers and decode.
cd_esig.json#6 C Correcting a recipient email: trap C used "always", an absolute that gives it away -> reworded C to "relying on Docusign to notify the client at the new address". Updated the C explanation.
cd_esig.json#8 C Request URL base URI per account: the wrong options were easy to rule out (D had "exactly one" and "never changes") -> D is now a near miss that calls userinfo but takes the first listed account. Added a stem clue that users also belong to other companies' accounts, and set trapOption to D. Updated the D and B explanations, whyNotOthers and decode.

Checked facts (no change needed): auth#6 (live tokens survive revocation), golive#1 (Declined = manual review), golive#3 (the 20-call rule is gone), golive#11 (overlapping listStatusChanges windows are recommended, not a factor), connect#10 (Basic auth cannot be used with config OAuth, at org level or in envelope-level Connect), esig#14 (focused view does not support payment tabs).

Reviewed: 64 (auth 16, golive 14, connect 14, esig 20) / changed: 4 / unsure: 0

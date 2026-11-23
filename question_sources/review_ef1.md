# Review ef1 (ef_auth.json, ef_golive.json, ef_apps.json)

ef_auth.json#10 F JWT Grant sequence: trap B and option A each had two errors (B: no userinfo + hourly refresh token; A: consent order + refresh), so both were easy to eliminate -> rewrote A and B to differ from key D by exactly one detail (A: consent after the token request; B: renews with a refresh token instead of a new JWT); updated optionExplanations, whyNotOthers and decode clues.

All other questions reviewed and left unchanged: traps already differ from the key by one detail tied to a stem clue, select-two items already have a convincing third candidate, option lengths are even.

Notes (not changed, facts not verifiable from local sources): ef_auth#7 (max 5 RSA key pairs per key), ef_golive#29 (100 integration keys per account), ef_apps#24 (30-character app name). ef_golive#0 trap D (exactly 15-minute polling) is compliant with the stated 15-minute rule; it stays wrong only on the "design for 20 minutes / use Connect" guidance.

Count: reviewed 84 (auth 24, golive 34, apps 26) / changed 1 / unsure 4 (facts listed above, unchanged)

# Brief: add a "decode" step to the long scenario questions of Papers A and B

The learner failed the Docusign IAM Integration & Extension Developer exam mainly because they struggled to decode
long business scenarios written with varied wording and jargon. We are building a **decode drill**: the learner reads
the scenario WITHOUT the answer options, first answers "what does this scenario really need?", then sees the real
options.

Input: `d:/Docusign exam/quiz-app/src/papers.json` (Papers A and B). Process ONLY the questions with
`"length": "long"` and the `paper` value given in your prompt.

For each such question write:
{"id": <question id>,
 "decode": {
   "prompt": "What does this scenario really require?" (or a sharper variant, e.g. "Which requirement decides the design here?"),
   "options": [{"id": "A", "text": "..."}, {"id": "B", ...}, {"id": "C", ...}, {"id": "D", ...}],
   "correct": "B",
   "explanation": "1-2 sentences linking the stem's wording to the requirement",
   "clues": ["business phrase from the stem -> what it means in Docusign terms", "..."] (2-4 items),
   "needs": "one line, the requirement in Docusign terms"}}

Rules:
- Decode options are REQUIREMENTS, not solutions, e.g. "Authenticate with no user present, from a server that can
  hold a private key" vs "Let each signed-in user authorize the app in a browser". They must not simply repeat the
  answer options of the question, and must not give away the final answer letter.
- Exactly one decode option is correct; the others are realistic misreadings of the scenario (e.g. focusing on a red
  herring, the wrong actor, the wrong level).
- Base everything strictly on the question's stem, keyed answer and explanation. Plain text only.
- Spread decode correct letters evenly across A-D.

Write the array with a Python script (`json.dump(..., ensure_ascii=False, indent=2)`) to
`d:/Docusign exam/tmp/papers/decode_<paper>.json`, re-load to verify. Do not edit other files. Reply in 2 lines.

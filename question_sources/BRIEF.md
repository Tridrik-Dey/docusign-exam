# Brief: write HARD exam-style questions for two mock papers (Paper A and Paper B)

Exam: **Certified Docusign IAM Integration & Extension Developer** (real exam: 60 questions, 150 min, 70% pass,
some multiple-answer). The learner sits it on 22 Nov 2026 and will take these papers on 21 Nov.
**Factual accuracy beats everything.** A wrong key is worse than an easy question.

## Your assignment
You write questions for ONE exam section (given in your prompt): `A_COUNT` questions for Paper A and `B_COUNT` for Paper B.
Paper A and Paper B must not share questions or scenarios (different stories, different tested points where possible).

## Source of concepts (the user's rule)
`d:/Docusign exam/tmp/papers/dsu47.json` holds 47 real Docusign University practice questions with their options.
Every question you write must be built around concepts that appear in the **options** (correct or wrong) of those 47
questions (e.g. Docusign JS, EnvelopeViews:createRecipient, JWT consent, Connected Fields, File IO, Concerto, Focused
view, frameAncestors, eventNotification, HMAC, etc.). Read the whole file first and list the option concepts relevant
to your section. Do not test topics that appear nowhere in those options. Your questions must be **harder** than the
47 originals and must not copy their stems.

## Fact sources (verify before you key an answer; do not invent API names, values or limits)
- `d:/Docusign exam/study_sections_content.py` (curated must-know facts per section, verified)
- `d:/Docusign exam/gap_fill/exam_gap_notes.md` (verified Developer Center notes)
- `d:/Docusign exam/study_material.md` (official Docusign University course text, grep it)
- `d:/Docusign exam/tmp/papers/dsu47.json` explanations
- Optional: deferred tool `mcp__docusign__searchDocusignDocs` (load with ToolSearch `select:mcp__docusign__searchDocusignDocs`,
  pass mcpClientModel "unknown") to check a doubtful fact against the public Developer Center.
If you cannot verify a detail, do not build a question on it.

## Difficulty rules
1. **Length mix 7:3**: about 70% `"length": "long"` = a scenario of 70-130 words (named company/developer, systems,
   constraints, one or two red herrings, and the deciding clue buried in the middle), and 30% `"length": "short"` = a
   direct 1-2 sentence question.
2. **Confusing options**: 4 options (5 for some multi-answer). Every wrong option is a near-miss from the same product
   area that is wrong for ONE specific reason (wrong level, wrong flow, wrong endpoint, wrong lifetime, enforces vs
   records, all vs new-only, draft vs sent, etc.). No silly or obviously unrelated distractors. Options similar in
   length and style so length does not give the key away.
3. **Exactly one defensible key** (or exactly the keyed set). Re-read each question as a skeptical examiner: if a
   second option could be argued correct, tighten the stem.
4. **Multiple-answer**: about 20% of your questions, stem ends with "(Select two)" or "(Select three)".
5. Spread the correct letters evenly across A-D (do not favour one letter).

## Output
Write `d:/Docusign exam/tmp/papers/out_<slug>.json` (slug given in your prompt): a JSON array, written with a Python
script using `json.dump(..., ensure_ascii=False, indent=2)` and re-loaded to verify it parses. Do not edit other files.
Each object:
{"paper": "A", "length": "long", "domain": "<exact section name given>", "topic": "<short topic>",
 "stem": "...", "options": [{"id": "A", "text": "..."}, ...],
 "correct": "C"  (or "A,D" for multi), "correctAnswers": ["A","D"] (multi only),
 "answerText": "<text of correct option(s), joined with '; '>",
 "explanation": "1-3 sentences: why the key is right, quoting the deciding clue",
 "whyNotOthers": "2-4 sentences: 'C is right because ... The trap is B: ... but ... A and D fail because ...'",
 "optionExplanations": {"A": "...", "B": "...", ...}  (one specific reason per option; correct ones start with "Correct."),
 "trapOption": "B" (most tempting wrong option),
 "importance": "HIGH" | "MEDIUM" | "LOW" (HIGH = tests a HIGH objective / classic trap / exact fact),
 "basedOn": [3, 17]  (numbers `n` of the dsu47 questions whose options inspired it)}
Plain text only (no markdown, HTML, backticks).

When done, reply in at most 8 lines: counts per paper, long/short counts, multi-answer count, correct-letter
distribution, and any fact you were unsure about.

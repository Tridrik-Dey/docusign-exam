# Brief: write REAL-EXAM-STYLE questions for mock Papers C and D

Exam: **Certified Docusign IAM Integration & Extension Developer** (60 questions, 150 min, 70% to pass).
The learner failed the first attempt (60%) and will use Papers C and D in the final week before the retake.
**Factual accuracy beats everything.** A wrong key is worse than an easy question.

## What the real exam felt like (from the candidate; match this exactly)
- Difficulty like our hard Papers A and B (`d:/Docusign exam/quiz-app/src/papers.json`), not the easy bank.
- **Single-answer**: at least TWO options are very close (both sound right; they differ by one detail such as level,
  flow, who acts, timing, enforce vs record, draft vs sent). Exactly one is correct.
- **Multiple-answer**: ALWAYS "(Select two)", NEVER select three. Give 5 options where THREE look right and one of
  those three fails on one detail.
- Mixed question length: about 65% long business scenarios (80-140 words), 35% short (1-2 sentences).
- Mixed type: about 60% **design choice** (which approach / flow / configuration / sequence fits best) and 40% **fact**.
- Mixed option length: design-choice questions have LONG options (a full approach with its reason, 15-35 words, e.g.
  "Configure Connect at the account level with HMAC enabled so that every envelope sent by the account's users is
  reported without code changes"); fact questions have SHORT options (a term, value or endpoint).
- **Business language and jargon**: write scenarios the way a business analyst would, NOT in Docusign terms. Use varied
  vocabulary for the same idea (e.g. "headless nightly job", "unattended back-office process", "no human at the
  keyboard"; "system of record", "line-of-business app", "ERP"; "counterparty", "customer", "applicant";
  "tenant", "subsidiary", "business unit"; "kiosk", "tablet in the branch", "field rep's phone"; "audit trail",
  "compliance team", "tamper-proof"). The candidate must translate the business need into the Docusign choice.
  Include one or two realistic red herrings (details that do not change the answer).

## Your assignment
One exam section (given in your prompt): `C_COUNT` questions for Paper C and `D_COUNT` for Paper D.
Cover the section's official objectives broadly (see `d:/Docusign exam/tmp/dsu_check/prep_guide_2026.txt` and the
objectives in `d:/Docusign exam/study_sections_content.py`). Papers C and D must not share scenarios with each other
or with Papers A and B in papers.json (read the questions of your section there first and avoid repeating them).

## Fact sources (verify before you key an answer; never invent API names, values or limits)
- `d:/Docusign exam/study_sections_content.py` (curated verified facts per section)
- `d:/Docusign exam/gap_fill/exam_gap_notes.md`, `d:/Docusign exam/study_material.md` (official course text, grep it)
- `d:/Docusign exam/tmp/papers/dsu47.json` (47 Docusign University questions with explanations)
- Deferred tool `mcp__docusign__searchDocusignDocs` (load with ToolSearch `select:mcp__docusign__searchDocusignDocs`,
  pass mcpClientModel "unknown") to verify doubtful facts against the public Developer Center.
If you cannot verify a detail, do not build a question on it.

## Quality rules
1. Exactly one defensible key (or exactly the two keyed options). Re-read as a skeptical examiner; tighten the stem
   (add the deciding clue) if a close option could also be argued correct. The clue must be in the stem, possibly
   phrased in business language.
2. No silly distractors. Options similar in length and style within a question so length gives nothing away.
3. Spread correct letters evenly across A-E (do not favour one letter; avoid making the longest option the key).

## Output
Write `d:/Docusign exam/tmp/papers/cd_<slug>.json` (slug in your prompt) with a Python script
(`json.dump(..., ensure_ascii=False, indent=2)`), re-load it to verify. Do not edit other files. Each object:
{"paper": "C", "length": "long"|"short", "style": "design"|"fact", "domain": "<exact section name given>",
 "topic": "<short topic>", "stem": "...", "options": [{"id": "A", "text": "..."}, ...],
 "correct": "C" (or "A,D"), "correctAnswers": ["A","D"] (multi only),
 "answerText": "<text of correct option(s) joined with '; '>",
 "explanation": "1-3 sentences: why the key is right, quoting the deciding clue",
 "whyNotOthers": "2-4 sentences: 'C is right because ... The trap is B: ... but ... A and D fail because ...'",
 "optionExplanations": {"A": "...", ...} (one specific reason per option; correct ones start with "Correct."),
 "trapOption": "B", "importance": "HIGH"|"MEDIUM"|"LOW",
 "decode": {"needs": "one line: what the scenario really requires in Docusign terms",
            "clues": ["business phrase -> what it means", "..."]}  (2-4 clues; required for long questions, optional for short),
 "concept": {"title": "max 6 words", "line": "max 25 words: the general rule tested, no story details"}}
Plain text only (no markdown, HTML, backticks).

Reply in at most 8 lines: counts per paper, long/short, design/fact, multi-answer count, letter distribution, and any
fact you were unsure about.

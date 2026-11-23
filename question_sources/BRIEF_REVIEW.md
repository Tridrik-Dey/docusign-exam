# Brief: quality review - make the close options genuinely close

The learner failed the Docusign IAM Integration & Extension Developer exam (60%) and described the real exam:
- **single-answer** questions have at least TWO options so close that choosing is hard (same product area, both sound
  right, they differ by ONE detail: level, flow, actor, timing, draft vs sent, enforce vs record, new vs running, etc.);
- **select-two** questions have 5 options where THREE look right; one of those three fails on one detail;
- long business scenarios in varied jargon; design-choice options are long sentences ("Use X at Y level so that Z").

Our questions were written to this brief, but nobody has checked each one. Your job: review every question in your
files and sharpen the ones that are too easy to answer by elimination.

## Files
Edit ONLY the files named in your prompt (in `d:/Docusign exam/tmp/papers/`). Each is a JSON array of question
objects. Load with Python, modify in memory, write back with `json.dump(..., ensure_ascii=False, indent=2)`, re-load
to verify. Do not touch any other file.

## For each question, check
1. **Single-answer**: is the `trapOption` a real near-miss? A well-prepared candidate should need the deciding clue in
   the stem to reject it. If the trap (or every wrong option) can be ruled out without reading the scenario carefully,
   rewrite the trap so it differs from the key by exactly one detail, and make at least one more wrong option plausible.
2. **Select two**: do exactly THREE options look right at first glance? If only the two keys look right, rewrite one
   wrong option into a convincing third candidate that fails on one stated constraint.
3. **Exactly one defensible key** (or exactly the two keys) after your edit. Re-read as a skeptical examiner. If your
   sharper distractor could be argued correct, make the stem's deciding clue explicit (you may add one short clause to
   the stem) or choose a different detail. Never make a wrong option factually defensible.
4. **Give-aways**: options of very different length or style, absolute words only in wrong options ("always",
   "never"), the key repeating stem words verbatim, the key being the only long option. Even them out.
5. **Facts**: do not introduce new technical claims you cannot verify. Sources: `d:/Docusign exam/study_sections_content.py`,
   `gap_fill/exam_gap_notes.md`, `study_material.md` (official course text), and the deferred tool
   `mcp__docusign__searchDocusignDocs` (load with ToolSearch `select:mcp__docusign__searchDocusignDocs`, mcpClientModel
   "unknown"). Known corrections: Data IO has no UpdateRecord; do not depend on whether account-level Connect covers
   envelopes users receive (course and docs disagree); the Agreement Manager API has exactly GetAgreementsList,
   GetAgreement, DeleteAgreement, CreateAgreementSummary.

## Rules
- NEVER change: `paper`, `domain`, `length`, `style`, the option ids, which letters are correct (`correct`,
  `correctAnswers`), or the order of questions in the file. You may reword the correct option(s) slightly only to even
  out length/style without changing meaning.
- If you change any option text or the stem, update `optionExplanations` (every option; correct ones start with
  "Correct."), `whyNotOthers` (name the trap and why it fails), `explanation` if needed, `answerText` (text of the
  correct option(s) joined with "; "), `trapOption` (must be a wrong option), and `decode` / `concept` if affected.
- Plain text only. Keep design options 15-35 words, fact options short.
- Leave good questions unchanged. Do not rewrite for the sake of it.

## Report
Write `d:/Docusign exam/tmp/papers/review_<slug>.md`: one line per question you changed ("<file>#<index> <paper>
<topic>: what was weak -> what you changed") and a final count (reviewed / changed / unsure). Reply in at most 6 lines:
counts per file and anything you were unsure about.

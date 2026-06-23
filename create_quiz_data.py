from __future__ import annotations

import json
import re
from pathlib import Path


SOURCE = Path("output/docusign_iam_integration_extension_300_practice_questions.md")
DEST = Path("quiz-app/src/questions.json")


def parse_questions(text: str) -> list[dict]:
    question_re = re.compile(
        r"(?ms)^\*\*Q(?P<number>\d+)\. \((?P<topic>[^)]+)\)\*\* (?P<stem>.*?)\n\n"
        r"A\. (?P<A>.*?)\n"
        r"B\. (?P<B>.*?)\n"
        r"C\. (?P<C>.*?)\n"
        r"D\. (?P<D>.*?)\n\n"
        r"\*\*Answer:\*\* (?P<answer>[A-D])\. (?P<answer_text>.*?)\n\n"
        r"\*\*Explanation:\*\* (?P<explanation>.*?)(?=\n\n\*\*Q|\n\n### |\Z)"
    )
    domain = None
    questions = []
    lines = text.splitlines()
    domain_by_pos = {}
    for match in re.finditer(r"(?m)^### (.+)$", text):
        domain_by_pos[match.start()] = match.group(1).strip()

    domains = sorted(domain_by_pos.items())
    for match in question_re.finditer(text):
        for pos, name in domains:
            if pos < match.start():
                domain = name
            else:
                break
        options = [
            {"id": "A", "text": match.group("A").strip()},
            {"id": "B", "text": match.group("B").strip()},
            {"id": "C", "text": match.group("C").strip()},
            {"id": "D", "text": match.group("D").strip()},
        ]
        correct = match.group("answer").strip()
        answer_text = match.group("answer_text").strip()
        explanation = re.sub(r"\s+", " ", match.group("explanation").strip())
        questions.append(
            {
                "id": int(match.group("number")),
                "domain": domain,
                "topic": match.group("topic").strip(),
                "stem": re.sub(r"\s+", " ", match.group("stem").strip()),
                "options": options,
                "correct": correct,
                "answerText": answer_text,
                "explanation": explanation,
                "optionExplanations": build_option_explanations(options, correct, answer_text, explanation),
            }
        )
    return questions


def build_option_explanations(options: list[dict], correct: str, answer_text: str, explanation: str) -> dict[str, str]:
    output = {}
    for option in options:
        if option["id"] == correct:
            output[option["id"]] = explanation
        else:
            output[option["id"]] = (
                f"This choice is not the best answer for this scenario. The scenario points to "
                f"{answer_text}, while '{option['text']}' addresses a different Docusign feature, "
                "configuration, or integration pattern."
            )
    return output


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    questions = parse_questions(text)
    if len(questions) != 300:
        raise RuntimeError(f"Expected 300 questions, found {len(questions)}")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(questions, indent=2), encoding="utf-8")
    print(f"Wrote {len(questions)} questions to {DEST}")


if __name__ == "__main__":
    main()

"""Merge the hard Paper A / Paper B questions (tmp/papers/out_*.json), validate them, and publish.

Writes: quiz-app/src/papers.json             (used by the Mock exam screen: Start Paper A / B)
        output/pdf/docusign_hard_papers_A_B.pdf  (both papers; questions first, answer key with explanations after)
Usage:  python build_hard_papers.py            validate + write
        python build_hard_papers.py --check    validate only
"""
import collections
import html
import json
import random
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

import build_question_bank_pdf as qb  # registers Arial and holds the shared styles

ROOT = Path(__file__).parent
SRC = ROOT / "question_sources"
OUT_JSON = ROOT / "quiz-app" / "src" / "papers.json"
OUT_PDF = ROOT / "output" / "pdf" / "docusign_hard_papers_A_B.pdf"
DOMAINS = [d for d, _ in qb.ORDER]
TEMPLATED = re.compile(r"can be valid in a different Docusign scenario|is a different Docusign concept", re.I)
MARKUP = re.compile(r"</?(b|i|u|br|p|div|span|strong|em)[^>]*>|\*\*|`")


def corr(q):
    return q["correctAnswers"] if q.get("correctAnswers") else [c.strip() for c in q["correct"].split(",")]


def validate(q, tag):
    p = []
    ids = [o["id"] for o in q.get("options", [])]
    c = corr(q)
    if q.get("paper") not in ("A", "B", "C", "D", "E", "F", "T"): p.append("paper")
    if q.get("domain") not in DOMAINS: p.append(f"domain {q.get('domain')}")
    if q.get("length") not in ("long", "short"): p.append("length")
    if len(ids) < 4 or ids != [chr(65 + i) for i in range(len(ids))]: p.append(f"option ids {ids}")
    if not set(c) <= set(ids): p.append("correct not in options")
    if sorted(x.strip() for x in q.get("correct", "").split(",")) != sorted(c): p.append("correct/correctAnswers mismatch")
    if len(c) > 1 and not re.search(r"select (two|three|2|3)", q["stem"], re.I): p.append("multi without Select N")
    if len(c) == 1 and re.search(r"\(select (two|three)", q["stem"], re.I): p.append("Select N on single answer")
    if q.get("trapOption") not in ids or q.get("trapOption") in c: p.append("trapOption")
    if q.get("importance") not in ("HIGH", "MEDIUM", "LOW"): p.append("importance")
    if sorted(q.get("optionExplanations") or {}) != sorted(ids): p.append("optionExplanations keys")
    if len((q.get("whyNotOthers") or "")) < 40: p.append("whyNotOthers")
    texts = [q["stem"], q.get("explanation", ""), q.get("whyNotOthers", "")] + list((q.get("optionExplanations") or {}).values()) + [o["text"] for o in q["options"]]
    if any(TEMPLATED.search(t) or MARKUP.search(t) for t in texts): p.append("templated/markup")
    return [f"{tag}: {x}" for x in p]


def load(pattern, strict):
    allq, problems = [], []
    for f in sorted(SRC.glob(pattern)):
        data = json.loads(f.read_text(encoding="utf-8"))
        for i, q in enumerate(data):
            tag = f"{f.stem}#{i}"
            problems += validate(q, tag)
            if strict:  # real-exam style (Papers C/D): select-2 only, 5 options on multi, decode + concept
                c = corr(q)
                if len(c) > 2: problems.append(f"{tag}: more than two answers")
                if len(c) == 2 and len(q["options"]) != 5: problems.append(f"{tag}: select-2 needs 5 options")
                if q.get("length") == "long" and not (q.get("decode") or {}).get("needs"): problems.append(f"{tag}: decode missing")
                if not (q.get("concept") or {}).get("line"): problems.append(f"{tag}: concept missing")
            allq.append(q)
    stems = collections.Counter(q["stem"].strip().lower() for q in allq)
    problems += [f"duplicate stem: {s[:60]}" for s, n in stems.items() if n > 1]
    return allq, problems


def order_paper(qs, seed):
    """Shuffle questions in a fixed (seeded) order, mixing sections like the real exam."""
    rng = random.Random(seed)
    qs = qs[:]
    rng.shuffle(qs)
    return qs


def stats(qs, ids=("A", "B")):
    lines = []
    for p in ids:
        ps = [q for q in qs if q["paper"] == p]
        lc = collections.Counter(q["length"] for q in ps)
        multi = sum(1 for q in ps if len(corr(q)) > 1)
        letters = collections.Counter(corr(q)[0] for q in ps if len(corr(q)) == 1)
        dom = collections.Counter(q["domain"] for q in ps)
        lines.append(f"Paper {p}: {len(ps)} q | long {lc['long']} short {lc['short']} | multi {multi} | "
                     f"letters {dict(sorted(letters.items()))} | " + ", ".join(f"{d.split()[0]} {dom[d]}" for d in DOMAINS))
    return lines


def pdf(papers, out_pdf, title, intro):
    ST = qb.ST
    story = [Paragraph(title, ST["title"]),
             Paragraph(intro, ST["sub"]),
             Paragraph("Take each paper like the real exam: 60 questions, 150 minutes, 70% to pass. Answers and explanations are at the end of each paper. "
                       "Importance tags: MUST KNOW (red), IMPORTANT (amber), BACKGROUND (blue). [TRAP] = the most tempting wrong option.", ST["sub"])]
    for pid, qs in papers.items():
        story += [PageBreak(), Paragraph(f"Paper {pid}: questions ({len(qs)})", ST["h1"])]
        for n, q in enumerate(qs, 1):
            c = corr(q)
            head = f"Q{n}" + (f" &middot; <font color='#d92d20'>MULTIPLE ANSWER - select {len(c)}</font>" if len(c) > 1 else "")
            block = [Paragraph(head, ST["qhead"]), Paragraph(qb.esc(q["stem"]), ST["stem"])]
            block += [Paragraph(f"<b>{o['id']}.</b> {qb.esc(o['text'])}", ST["opt"]) for o in q["options"]]
            story += [KeepTogether(block), Spacer(1, 8)]
        story += [PageBreak(), Paragraph(f"Paper {pid}: answer key and explanations", ST["h1"])]
        key = [[f"Q{n}", ", ".join(corr(q))] for n, q in enumerate(qs, 1)]
        cols = 6
        per = (len(key) + cols - 1) // cols
        rows = []
        for i in range(per):
            row = []
            for j in range(cols):
                k = i + j * per
                row += key[k] if k < len(key) else ["", ""]
            rows.append(row)
        t = Table(rows, colWidths=[13 * mm, 15 * mm] * cols)
        t.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), qb.FONT), ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                               ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#d0d5dd"))]))
        story += [t, Spacer(1, 10)]
        for n, q in enumerate(qs, 1):
            story += qb.question_block(n, q)
            dec = q.get("decode") or {}
            if dec.get("needs"):
                clues = "; ".join(dec.get("clues") or [])
                story.insert(len(story) - 1, Paragraph(f"<b>Decode:</b> {qb.esc(dec['needs'])}" + (f" <i>Clues: {qb.esc(clues)}</i>" if clues else ""), ST["exp"]))
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    def page(c, doc):
        c.saveState(); c.setFont(qb.FONT, 7.5); c.setFillColor(qb.MUTED)
        c.drawString(15 * mm, 9 * mm, f"Docusign IAM Integration & Extension Developer - {title}")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    SimpleDocTemplate(str(out_pdf), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=14 * mm, bottomMargin=15 * mm,
                      title=title).build(story, onFirstPage=page, onLaterPages=page)


SEEDS = {"A": 2211, "B": 2212, "C": 2213, "D": 2214, "E": 2215, "F": 2216, "T": 2217}  # fixed order: A/B ids must not change

SETS = [
    {"ids": ("A", "B"), "pattern": "out_*.json", "strict": False, "base": {"A": 10001, "B": 20001},
     "pdf": ROOT / "output" / "pdf" / "docusign_hard_papers_A_B.pdf", "title": "Hard Practice Papers A and B",
     "intro": "Certified Docusign IAM Integration &amp; Extension Developer &middot; built only from the concepts in the options of the "
              "47 Docusign University practice questions, made harder: long scenarios (about 70%), near-miss options, multiple-answer items."},
    {"ids": ("C", "D"), "pattern": "cd_*.json", "strict": True, "base": {"C": 30001, "D": 40001},
     "pdf": ROOT / "output" / "pdf" / "docusign_hard_papers_C_D.pdf", "title": "Real-Exam-Style Papers C and D",
     "intro": "Certified Docusign IAM Integration &amp; Extension Developer &middot; written to match the real exam as the candidate experienced it: "
              "business scenarios in varied wording, two very close options on single-answer questions, select-two questions where three "
              "options look right, design-choice and fact questions, long and short options. Each long question has a Decode line."},
    {"ids": ("E", "F", "T"), "pdf_ids": ("E", "F"), "pattern": "ef_*.json", "strict": True, "base": {"E": 50001, "F": 60001, "T": 70001},
     "pdf": ROOT / "output" / "pdf" / "docusign_hard_papers_E_F.pdf", "title": "Checkpoint Papers E and F",
     "intro": "Certified Docusign IAM Integration &amp; Extension Developer &middot; real-exam-style checkpoint papers for the 45-day plan "
              "(Paper E at the end of week 3, Paper F in week 6). Same style as Papers C and D. The topic-test bank is not printed here."},
]


def main():
    final, all_problems = [], 0
    for st in SETS:
        qs, problems = load(st["pattern"], st["strict"])
        if not qs:
            print(f"papers {st['ids']}: no source files yet")
            continue
        print(f"papers {st['ids']}: {len(qs)} questions, {len(problems)} problems")
        for p in problems[:40]:
            print("  ", p)
        for line in stats(qs, st["ids"]):
            print(line)
        all_problems += len(problems)
        if problems or "--check" in sys.argv:
            continue
        papers = {}
        for pid in st["ids"]:
            ordered = order_paper([q for q in qs if q["paper"] == pid], SEEDS[pid])
            for i, q in enumerate(ordered):
                q["id"] = st["base"][pid] + i
                q["answerText"] = "; ".join(next(o["text"] for o in q["options"] if o["id"] == c) for c in corr(q))
            concepts_file = SRC / "concepts.json"  # one-line concepts for Papers A/B (C-F/T carry their own)
            if concepts_file.exists():
                cmap = json.loads(concepts_file.read_text(encoding="utf-8"))
                for q in ordered:
                    if not q.get("concept") and str(q["id"]) in cmap:
                        q["concept"] = cmap[str(q["id"])]
            dec_file = SRC / f"decode_{pid}.json"
            if dec_file.exists():  # decode-drill steps for Papers A/B, keyed by question id
                dec = {d["id"]: d["decode"] for d in json.loads(dec_file.read_text(encoding="utf-8"))}
                for q in ordered:
                    if q["id"] in dec:
                        q["decode"] = dec[q["id"]]
            papers[pid] = ordered
            final += ordered
        pdf({k: v for k, v in papers.items() if k in st.get("pdf_ids", st["ids"])}, st["pdf"], st["title"], st["intro"])
        print("wrote", st["pdf"])
    if "--check" in sys.argv or all_problems:
        print("papers.json NOT written" + (f": {all_problems} problems" if all_problems else " (check only)"))
        return
    OUT_JSON.write_text(json.dumps(final, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", OUT_JSON, len(final), "questions")


if __name__ == "__main__":
    main()

"""Concise concept sheets for hard Paper A and Paper B: one line per question (same Q numbers as the paper),
grouped by exam section and colour-coded by importance.

Input:  quiz-app/src/papers.json, tmp/papers/concepts.json ({id: {title, line}})
Output: output/pdf/paper_<X>_concepts.pdf for every paper in papers.json (A-D)
"""
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import CondPageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

import build_question_bank_pdf as qb  # fonts + styles
from build_confusion_cheat_sheet_pdf import ST, NAVY, GRID

ROOT = Path(__file__).parent
PAPERS = json.loads((ROOT / "quiz-app" / "src" / "papers.json").read_text(encoding="utf-8"))
CONCEPTS = json.loads((ROOT / "question_sources" / "concepts.json").read_text(encoding="utf-8"))
LEVEL = {"HIGH": ("#d92d20", "#fef3f2"), "MEDIUM": ("#f79009", "#fffaeb"), "LOW": ("#84adff", "#eff4ff")}


def corr(q):
    return q["correctAnswers"] if q.get("correctAnswers") else [c.strip() for c in q["correct"].split(",")]


def build(pid):
    qs = [q for q in PAPERS if q["paper"] == pid]
    num = {q["id"]: n for n, q in enumerate(qs, 1)}
    out = ROOT / "output" / "pdf" / f"paper_{pid}_concepts.pdf"
    story = [Paragraph(f"Paper {pid}: Concepts Tested", ST["title"]),
             Paragraph(f"One line per question (Q numbers match Paper {pid}), grouped by exam section. "
                       "<font color='#d92d20'><b>red = must know</b></font>, <font color='#b54708'><b>amber = important</b></font>, "
                       "<font color='#2e90fa'><b>blue = background</b></font>. Answer letter in brackets. "
                       f"Full explanations: docusign_hard_papers_{ {'A': 'A_B', 'B': 'A_B', 'C': 'C_D', 'D': 'C_D'}.get(pid, 'E_F') }.pdf.", ST["sub"])]
    for dom, w in qb.ORDER:
        items = sorted((q for q in qs if q["domain"] == dom), key=lambda q: num[q["id"]])
        if not items:
            continue
        head = Table([[Paragraph(f"{qb.esc(dom)} ({w}%) &middot; {len(items)} questions", ST["h2"])]], colWidths=[180 * mm])
        head.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
        rows, style = [], [("GRID", (0, 0), (-1, -1), 0.4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
        for i, q in enumerate(items):
            c = q.get("concept") or CONCEPTS.get(str(q["id"]), {"title": q["topic"], "line": q["explanation"]})
            stripe, bg = LEVEL.get(q.get("importance"), LEVEL["MEDIUM"])
            rows.append([Paragraph(f"<b>Q{num[q['id']]}</b> [{', '.join(corr(q))}]", ST["cell"]),
                         Paragraph(f"<b>{qb.esc(c['title'])}</b>", ST["cell"]),
                         Paragraph(qb.esc(c["line"]), ST["cell"])])
            style += [("BACKGROUND", (0, i), (-1, i), colors.HexColor(bg)), ("LINEBEFORE", (0, i), (0, i), 3, colors.HexColor(stripe))]
        t = Table(rows, colWidths=[17 * mm, 45 * mm, 118 * mm])
        t.setStyle(TableStyle(style))
        story += [CondPageBreak(30 * mm), head, t, Spacer(1, 5)]

    def page(c, doc):
        c.saveState(); c.setFont(qb.FONT, 7.5); c.setFillColor(qb.MUTED)
        c.drawString(15 * mm, 9 * mm, f"Docusign IAM Integration & Extension Developer - Paper {pid} concepts")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=12 * mm, bottomMargin=14 * mm,
                      title=f"Paper {pid} concepts").build(story, onFirstPage=page, onLaterPages=page)
    print(out)


if __name__ == "__main__":
    missing = [q["id"] for q in PAPERS if str(q["id"]) not in CONCEPTS and not q.get("concept")]
    print("missing concept lines:", missing or "none")
    for pid in sorted({q["paper"] for q in PAPERS} - {"T"}):  # T = topic-test bank, never printed
        build(pid)

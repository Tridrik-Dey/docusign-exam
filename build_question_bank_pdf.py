"""Build the full practice question bank PDF from quiz-app/src/questions.json.

Questions are grouped by official exam section (in exam order). Each question shows the
options, then a green answer box, the explanation, and why each option is right or wrong.
Multiple-answer questions are flagged like the real exam ("Select N").
Output: output/pdf/docusign_iam_practice_question_bank.pdf (all sections)
        output/pdf/sections/NN_<section>_questions.pdf (one per section)
"""
import collections
import html
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).parent
QUESTIONS = ROOT / "quiz-app" / "src" / "questions.json"
OUT = ROOT / "output" / "pdf" / "docusign_iam_practice_question_bank.pdf"

FONT, BOLD = "Helvetica", "Helvetica-Bold"
try:
    pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Italic", "C:/Windows/Fonts/ariali.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-BoldItalic", "C:/Windows/Fonts/arialbi.ttf"))
    pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-BoldItalic")
    FONT, BOLD = "Arial", "Arial-Bold"
except Exception:
    pass

ORDER = [("API Authentication", 13), ("Go Live Process", 11), ("Docusign Connect", 12), ("eSignature API", 16),
         ("eSignature Features and Web Forms", 11), ("Agreement Manager API", 6),
         ("Workflow Builder and Workflow API", 15), ("App Center and Extension Apps", 16)]
NAVY, INK, MUTED = colors.HexColor("#0b2545"), colors.HexColor("#1d2939"), colors.HexColor("#667085")
GREEN_BG, GREEN = colors.HexColor("#ecfdf3"), colors.HexColor("#039855")
RED = colors.HexColor("#d92d20")

ST = {
    "title": ParagraphStyle("t", fontName=BOLD, fontSize=22, leading=27, textColor=NAVY, spaceAfter=6),
    "sub": ParagraphStyle("s", fontName=FONT, fontSize=10, leading=14, textColor=MUTED, spaceAfter=8),
    "h1": ParagraphStyle("h1", fontName=BOLD, fontSize=16, leading=20, textColor=NAVY, spaceAfter=8),
    "qhead": ParagraphStyle("qh", fontName=BOLD, fontSize=8, leading=10, textColor=MUTED),
    "stem": ParagraphStyle("st", fontName=BOLD, fontSize=9.6, leading=12.8, textColor=INK, spaceAfter=3),
    "opt": ParagraphStyle("o", fontName=FONT, fontSize=9.2, leading=12, textColor=INK, leftIndent=10),
    "ans": ParagraphStyle("a", fontName=BOLD, fontSize=9, leading=12, textColor=GREEN),
    "exp": ParagraphStyle("e", fontName=FONT, fontSize=8.6, leading=11.4, textColor=INK),
    "note": ParagraphStyle("n", fontName=FONT, fontSize=7.9, leading=10.2, textColor=colors.HexColor("#344054"), leftIndent=6),
}


IMP = {"HIGH": ("MUST KNOW", "#d92d20"), "MEDIUM": ("IMPORTANT", "#f79009"), "LOW": ("BACKGROUND", "#84adff")}


def esc(t):
    return html.escape(str(t), quote=False).replace("\u2192", "->").replace("\ufffd", "-")


def question_block(n, q):
    correct = q.get("correctAnswers") or [c.strip() for c in q["correct"].split(",")]
    multi = len(correct) > 1
    flow = []
    imp = IMP.get(q.get("importance"))
    head = (f"<font backColor='{imp[1]}' color='#ffffff'><b>&nbsp;{imp[0]}&nbsp;</b></font> &nbsp;" if imp else "") + f"Q{n} &middot; {esc(q['topic'])}"
    if multi:
        head += f" &middot; <font color='#d92d20'>MULTIPLE ANSWER - select {len(correct)}</font>"
    flow.append(Paragraph(head, ST["qhead"]))
    flow.append(Paragraph(esc(q["stem"]), ST["stem"]))
    for o in q["options"]:
        flow.append(Paragraph(f"<b>{o['id']}.</b> {esc(o['text'])}", ST["opt"]))
    opt_text = {o["id"]: o["text"] for o in q["options"]}
    box = [Paragraph(f"Answer: {', '.join(correct)} &nbsp;&mdash;&nbsp; " + esc(" | ".join(opt_text.get(c, '').rstrip('.') for c in correct)), ST["ans"]),
           Paragraph(esc(q.get("explanation", "")), ST["exp"])]
    if q.get("whyNotOthers"):
        box.append(Paragraph("<b>Why this answer and not the others:</b> " + esc(q["whyNotOthers"]), ST["exp"]))
    notes = q.get("optionExplanations") or {}
    for oid in [o["id"] for o in q["options"]]:
        if oid in notes:
            mark = "<font color='#039855'><b>[RIGHT]</b></font>" if oid in correct else "<font color='#d92d20'><b>[WRONG]</b></font>"
            trap = " <font color='#b54708'><b>[TRAP]</b></font>" if q.get("trapOption") == oid else ""
            box.append(Paragraph(f"{mark}{trap} <b>{oid}.</b> {esc(notes[oid])}", ST["note"]))
    t = Table([[b] for b in box], colWidths=[None])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GREEN_BG), ("LINEBEFORE", (0, 0), (0, -1), 3, GREEN),
                           ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
    flow.append(Spacer(1, 3))
    return [KeepTogether(flow + [t]), Spacer(1, 9)]


def main():
    qs = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    by = collections.defaultdict(list)
    for q in qs:
        by[q["domain"]].append(q)
    multi = sum(1 for q in qs if "," in q["correct"])
    story = [Paragraph("Certified Docusign IAM Integration &amp; Extension Developer", ST["title"]),
             Paragraph(f"Practice question bank &middot; <b>{len(qs)} questions</b> ({multi} multiple-answer) &middot; "
                       "grouped by official exam section (Prep Guide v. 2026)", ST["sub"]),
             Paragraph("Real exam: 60 questions, 150 minutes, 70% to pass, some questions have more than one correct answer. "
                       "Cover the green box, answer, then check. Red \"MULTIPLE ANSWER\" tags mark select-N questions. "
                       "Importance tags: MUST KNOW (red), IMPORTANT (amber), BACKGROUND (blue). [TRAP] marks the most tempting wrong option.", ST["sub"])]
    rows = [["Section", "Exam weight", "Questions here"]] + [[d, f"{w}%", str(len(by.get(d, [])))] for d, w in ORDER]
    t = Table(rows, colWidths=[95 * mm, 30 * mm, 35 * mm])
    t.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), FONT), ("FONTNAME", (0, 0), (-1, 0), BOLD),
                           ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                           ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d0d5dd")), ("FONTSIZE", (0, 0), (-1, -1), 9)]))
    story += [t]
    n = 1
    for i, (dom, w) in enumerate(ORDER, 1):
        story += [PageBreak(), Paragraph(f"Section {i}: {esc(dom)} ({w}%)", ST["h1"])]
        for q in by.get(dom, []):
            story += question_block(n, q)
            n += 1
    extra = [d for d in by if d not in dict(ORDER)]
    for dom in extra:
        story += [PageBreak(), Paragraph(esc(dom), ST["h1"])]
        for q in by[dom]:
            story += question_block(n, q)
            n += 1

    def page(c, doc):
        c.saveState(); c.setFont(FONT, 7.5); c.setFillColor(MUTED)
        c.drawString(15 * mm, 9 * mm, "Docusign IAM Integration & Extension Developer - practice question bank")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=14 * mm, bottomMargin=15 * mm,
                      title="Docusign IAM practice question bank").build(story, onFirstPage=page, onLaterPages=page)
    print(OUT, n - 1, "questions")

    # ---- one question PDF per section, saved next to that section's study PDF ----
    from study_sections_content import SECTIONS
    sec_dir = ROOT / "output" / "pdf" / "sections"
    sec_dir.mkdir(parents=True, exist_ok=True)
    for i, (dom, w) in enumerate(ORDER, 1):
        sec = next(s for s in SECTIONS if s["num"] == i)
        items = by.get(dom, [])
        m = sum(1 for q in items if "," in q["correct"])
        s_story = [Paragraph(f"Section {i}: {esc(dom)} - Practice Questions", ST["title"]),
                   Paragraph(f"Exam weight <b>{w}%</b> (about {round(60 * w / 100)} of 60 exam questions) &middot; "
                             f"<b>{len(items)} questions</b> here ({m} multiple-answer)", ST["sub"]),
                   Paragraph("Cover the green box, answer, then check. Red \"MULTIPLE ANSWER\" tags mark select-N questions. "
                             "Importance tags: MUST KNOW (red), IMPORTANT (amber), BACKGROUND (blue). [TRAP] marks the most tempting wrong option. "
                             f"Study guide for this section: {sec['slug']}.pdf", ST["sub"]), Spacer(1, 6)]
        for k, q in enumerate(items, 1):
            s_story += question_block(k, q)

        def s_page(c, doc, label=f"Section {i}: {dom} ({w}%) - practice questions"):
            c.saveState(); c.setFont(FONT, 7.5); c.setFillColor(MUTED)
            c.drawString(15 * mm, 9 * mm, f"Docusign IAM Integration & Extension Developer - {label}")
            c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

        out = sec_dir / f"{sec['slug']}_questions.pdf"
        SimpleDocTemplate(str(out), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=14 * mm,
                          bottomMargin=15 * mm, title=f"Section {i} - {dom} - practice questions").build(
            s_story, onFirstPage=s_page, onLaterPages=s_page)
        print(out, len(items), "questions")


if __name__ == "__main__":
    main()

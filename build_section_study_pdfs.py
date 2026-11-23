"""Build one color-coded study PDF per official exam section.

Inputs:
  study_sections_content.py   curated objectives / must-know / important facts
  study_material.md           course text (deduplicated and auto-highlighted)
                              plus the "Exam Gap Topics" notes at the end
  quiz-app/src/questions.json practice question counts per section

Output: output/pdf/sections/NN_<section>.pdf

Color legend:
  RED    MUST KNOW   - official objective / frequently tested fact / exam trap
  AMBER  IMPORTANT   - supporting detail you should recognize
  BLUE   BACKGROUND  - context, lab steps, product overview
"""
import collections
import html
import json
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table,
                                TableStyle)

from study_sections_content import SECTIONS

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "output" / "pdf" / "sections"
STUDY = ROOT / "study_material.md"
QUESTIONS = ROOT / "quiz-app" / "src" / "questions.json"

# ---------- fonts ----------
FONT, BOLD, ITALIC, MONO = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Courier"
try:
    pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Italic", "C:/Windows/Fonts/ariali.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-BoldItalic", "C:/Windows/Fonts/arialbi.ttf"))
    pdfmetrics.registerFont(TTFont("Consolas", "C:/Windows/Fonts/consola.ttf"))
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-BoldItalic")
    FONT, BOLD, ITALIC, MONO = "Arial", "Arial-Bold", "Arial-Italic", "Consolas"
except Exception:
    pass

# ---------- palette ----------
LEVELS = {
    "HIGH": dict(label="MUST KNOW", fg=colors.HexColor("#b42318"), bg=colors.HexColor("#fef3f2"), bar=colors.HexColor("#d92d20")),
    "MEDIUM": dict(label="IMPORTANT", fg=colors.HexColor("#b54708"), bg=colors.HexColor("#fffaeb"), bar=colors.HexColor("#f79009")),
    "LOW": dict(label="BACKGROUND", fg=colors.HexColor("#175cd3"), bg=colors.HexColor("#f5f8ff"), bar=colors.HexColor("#84adff")),
}
NAVY = colors.HexColor("#0b2545")
INK = colors.HexColor("#1d2939")
MUTED = colors.HexColor("#667085")

ST = {
    "title": ParagraphStyle("t", fontName=BOLD, fontSize=21, leading=25, textColor=NAVY, spaceAfter=4),
    "sub": ParagraphStyle("s", fontName=FONT, fontSize=10, leading=13, textColor=MUTED, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=14, leading=18, textColor=NAVY, spaceBefore=12, spaceAfter=6),
    "h3": ParagraphStyle("h3", fontName=BOLD, fontSize=11, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4),
    "body": ParagraphStyle("b", fontName=FONT, fontSize=9.2, leading=12.4, textColor=INK, alignment=TA_LEFT),
    "small": ParagraphStyle("sm", fontName=FONT, fontSize=8.2, leading=10.6, textColor=INK),
    "q": ParagraphStyle("q", fontName=BOLD, fontSize=9.2, leading=12.4, textColor=NAVY),
    "tag": ParagraphStyle("tag", fontName=BOLD, fontSize=7, leading=9, textColor=colors.white),
}

SIGNAL = re.compile(r"\b(must|only|cannot|can't|required|requires|not supported|not available|expire[sd]?|limit|"
                    r"recommend(ed|s)?|best practice|important|never|always|instead|do not|don't|valid for|"
                    r"maximum|minimum|no longer|default)\b", re.I)
LAB = re.compile(r"^(click|select|open|copy|paste|navigate|in postman|in the postman|go to|return to|replace|"
                 r"download|log in|verify that|examine|save|enter|scroll|choose|create a new|if you)\b", re.I)
CODEISH = re.compile(r"([a-z]+[A-Z][a-zA-Z]+|/oauth/|/restapi|/v1/|_[a-z]+_|\{\w+\})")


def esc(text):
    text = html.escape(text, quote=False)
    return text.replace("\u2192", "->").replace("\u200b", "")


def classify(line, keywords):
    low = line.lower()
    kw = sum(1 for k in keywords if k in low)
    sig = bool(SIGNAL.search(line))
    if LAB.match(line.strip()) and not sig:
        return "LOW"
    if line.startswith("Objective:") or line.startswith("Welcome to"):
        return "LOW"
    if sig and kw >= 1:
        return "HIGH"
    if kw >= 2 or sig or CODEISH.search(line):
        return "MEDIUM"
    return "LOW"


def bar_block(content, level, style=None, tag=True):
    """A paragraph with a colored left bar + tinted background."""
    lv = LEVELS[level]
    style = style or ST["body"]
    cells = []
    para = Paragraph(content, style)
    if tag:
        tag_tbl = Table([[Paragraph(lv["label"], ST["tag"])]], colWidths=[18 * mm])
        tag_tbl.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), lv["bar"]),
                                     ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                                     ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
        cells = [[tag_tbl, para]]
        widths = [20 * mm, None]
    else:
        cells = [[para]]
        widths = [None]
    t = Table(cells, colWidths=widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), lv["bg"]),
        ("LINEBEFORE", (0, 0), (0, -1), 3, lv["bar"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def legend():
    rows = [[Paragraph(f"<font color='white'><b>{LEVELS[k]['label']}</b></font>", ST["small"]), Paragraph(desc, ST["small"])]
            for k, desc in [("HIGH", "Official objective / frequently tested fact / exam trap. Learn these first."),
                            ("MEDIUM", "Supporting detail you should recognize in a scenario."),
                            ("LOW", "Context, lab steps, product overview. Skim.")]]
    t = Table(rows, colWidths=[26 * mm, None])
    style = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#d0d5dd")),
             ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for i, k in enumerate(["HIGH", "MEDIUM", "LOW"]):
        style += [("BACKGROUND", (0, i), (0, i), LEVELS[k]["bar"]), ("BACKGROUND", (1, i), (1, i), LEVELS[k]["bg"])]
    t.setStyle(TableStyle(style))
    return t


# ---------- source extraction ----------
def load_study():
    return STUDY.read_text(encoding="utf-8").split("\n")


def course_lines(L, course_patterns):
    """Deduplicated, nav-free lines from the matching ### course blocks."""
    heads = [(i, l[4:]) for i, l in enumerate(L) if l.startswith("### ")]
    gap = next(i for i, l in enumerate(L) if l.startswith("## Exam Gap Topics"))
    counts = collections.Counter(l.strip() for l in L)
    out, seen = [], set()
    for k, (i, h) in enumerate(heads):
        if i >= gap or not any(p in h for p in course_patterns):
            continue
        j = heads[k + 1][0] if k + 1 < len(heads) else gap
        j = min(j, gap, next((x for x in range(i + 1, j) if L[x].startswith("## ")), j))
        lines = []
        for l in L[i + 1:j]:
            s = l.strip()
            if not s or s in seen or s.startswith("_UI-only"):
                continue
            if re.match(r"^Lesson \d+ - ", s) or s.startswith("Source: "):
                continue
            if len(s) < 70 and counts[s] >= 3:
                continue
            if re.fullmatch(r"[\d.]+ ?[KM]?B", s) or s.startswith("Please provide feedback"):
                continue
            if len(s) <= 30 and s.upper() == s and not any(ch.isdigit() for ch in s):  # UI tab labels like CURL, DOCUMENTS
                continue
            seen.add(s)
            lines.append(s)
        out.append((re.sub(r"\s+\d+ min$", "", h), lines))
    return out


def gap_block(L, heading_prefix):
    """Markdown chunks from 'Exam Gap Topics' whose ### heading starts with heading_prefix."""
    if not heading_prefix:
        return []
    gap = next(i for i, l in enumerate(L) if l.startswith("## Exam Gap Topics"))
    blocks, cur = [], None
    for l in L[gap + 1:]:
        if l.startswith("### "):
            cur = [l[4:], []] if l.startswith(heading_prefix) else None
            if cur:
                blocks.append(cur)
        elif cur is not None:
            cur[1].append(l)
    return blocks


def md_inline(text):
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", rf"<font face='{MONO}'>\1</font>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", text)
    return text


def render_markdown(lines):
    """Very small markdown renderer: bullets + pipe tables + paragraphs. All rendered as MUST KNOW."""
    flow, table_rows = [], []

    def flush_table():
        if not table_rows:
            return
        data = []
        for r in table_rows:
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            data.append([Paragraph(md_inline(c), ST["small"]) for c in cells])
        if data:
            n = max(len(r) for r in data)
            data = [r + [Paragraph("", ST["small"])] * (n - len(r)) for r in data]
            t = Table(data, repeatRows=1)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), LEVELS["HIGH"]["bar"]), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 1), (-1, -1), LEVELS["HIGH"]["bg"]),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#fda29b")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
            for c in range(n):
                data[0][c].style = ParagraphStyle("th", parent=ST["small"], fontName=BOLD, textColor=colors.white)
            flow.append(t)
            flow.append(Spacer(1, 4))
        table_rows.clear()

    for l in lines:
        s = l.rstrip()
        if s.strip().startswith("|"):
            if re.fullmatch(r"\|[\s:|-]+\|?", s.strip()):
                continue
            table_rows.append(s)
            continue
        flush_table()
        if not s.strip():
            continue
        if s.lstrip().startswith("- "):
            indent = len(s) - len(s.lstrip())
            text = md_inline(s.lstrip()[2:])
            flow.append(bar_block(("&nbsp;&nbsp;&nbsp;&nbsp;" if indent else "") + "&bull; " + text, "HIGH", tag=False))
        else:
            flow.append(bar_block(md_inline(s), "HIGH", tag=False))
        flow.append(Spacer(1, 1.5))
    flush_table()
    return flow


def domain_counts():
    qs = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    by = collections.Counter(q["domain"] for q in qs)
    multi = collections.Counter(q["domain"] for q in qs if "," in q["correct"])
    return by, multi


DOMAIN_NAME = {1: "API Authentication", 2: "Go Live Process", 3: "Docusign Connect", 4: "eSignature API",
               5: "eSignature Features and Web Forms", 6: "Agreement Manager API",
               7: "Workflow Builder and Workflow API", 8: "App Center and Extension Apps"}


# ---------- build ----------
def build(sec, L, counts, multi):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{sec['slug']}.pdf"
    story = []
    story.append(Paragraph(f"Section {sec['num']}: {esc(sec['title'])}", ST["title"]))
    dn = DOMAIN_NAME[sec["num"]]
    story.append(Paragraph(
        f"Certified Docusign IAM Integration &amp; Extension Developer &middot; exam weight <b>{sec['weight']}%</b> "
        f"(about {round(60 * sec['weight'] / 100)} of 60 questions) &middot; practice questions in the quiz app: "
        f"<b>{counts.get(dn, 0)}</b> ({multi.get(dn, 0)} multiple-answer)", ST["sub"]))
    story.append(legend())

    story.append(Paragraph("1. Official exam objectives (Prep Guide v. 2026)", ST["h2"]))
    for lvl, obj in sec["objectives"]:
        story.append(bar_block(esc(obj), lvl))
        story.append(Spacer(1, 2))

    story.append(Paragraph("2. Must-know facts", ST["h2"]))
    for item in sec["must_know"]:
        story.append(bar_block(item, "HIGH"))
        story.append(Spacer(1, 2))

    story.append(Paragraph("3. Important details", ST["h2"]))
    for item in sec["important"]:
        story.append(bar_block(item, "MEDIUM"))
        story.append(Spacer(1, 2))

    gaps = gap_block(L, sec["gap_heading"])
    if gaps:
        story.append(Paragraph("4. Exam gap topics (from Docusign Developer Center)", ST["h2"]))
        for title, lines in gaps:
            story.append(Paragraph(esc(title.split(" - ", 1)[-1]), ST["h3"]))
            story += render_markdown(lines)

    story.append(PageBreak())
    n = 5 if gaps else 4
    story.append(Paragraph(f"{n}. Course notes (Docusign University, auto-highlighted)", ST["h2"]))
    story.append(Paragraph("Deduplicated text of the official self-paced course(s). Each line is colored by how closely it "
                           "matches this section's objectives and exam-signal words (must, only, cannot, required, expires, ...). "
                           "Knowledge-check questions are shown in bold.", ST["sub"]))
    for course, lines in course_lines(L, sec["courses"]):
        story.append(Paragraph(esc(course), ST["h3"]))
        for s in lines:
            if s.endswith("?"):
                story.append(Paragraph("Q: " + esc(s), ST["q"]))
                continue
            lvl = classify(s, sec["keywords"])
            story.append(bar_block(esc(s), lvl, style=ST["small"], tag=False))
            story.append(Spacer(1, 1))

    def page(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONT, 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(15 * mm, 9 * mm, f"Docusign IAM Integration & Extension Developer - Section {sec['num']}: {sec['title']} ({sec['weight']}%)")
        canvas.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}")
        canvas.setFillColor(LEVELS["HIGH"]["bar"]); canvas.rect(15 * mm, A4[1] - 8 * mm, 25 * mm, 1.6 * mm, fill=1, stroke=0)
        canvas.setFillColor(LEVELS["MEDIUM"]["bar"]); canvas.rect(40 * mm, A4[1] - 8 * mm, 25 * mm, 1.6 * mm, fill=1, stroke=0)
        canvas.setFillColor(LEVELS["LOW"]["bar"]); canvas.rect(65 * mm, A4[1] - 8 * mm, 25 * mm, 1.6 * mm, fill=1, stroke=0)
        canvas.restoreState()

    doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=14 * mm,
                            bottomMargin=15 * mm, title=f"Section {sec['num']} - {sec['title']}",
                            author="Docusign exam study material")
    doc.build(story, onFirstPage=page, onLaterPages=page)
    return out


def main():
    L = load_study()
    counts, multi = domain_counts()
    for sec in SECTIONS:
        out = build(sec, L, counts, multi)
        print(out)


if __name__ == "__main__":
    main()

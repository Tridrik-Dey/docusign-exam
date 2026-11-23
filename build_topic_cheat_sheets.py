"""One cheat sheet per exam section (8 PDFs): must-know facts, key numbers, confusing pairs, business wording ->
Docusign choice, and the most important rules tested in the practice papers for that section.

Output: output/pdf/cheatsheets/NN_<section>_cheat_sheet.pdf
Sources: study_sections_content.py, build_confusion_cheat_sheet_pdf.py (NUMBERS, PAIRS),
         build_scenario_decoder_pdf.py (PHRASES), quiz-app/src/papers.json + question_sources/concepts.json (concept lines)
"""
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import CondPageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from build_confusion_cheat_sheet_pdf import FONT, GRID, MUTED, NAVY, NUMBERS, PAIRS, ST, tint
from build_scenario_decoder_pdf import PHRASES
from study_sections_content import SECTIONS

ROOT = Path(__file__).parent
OUT = ROOT / "output" / "pdf" / "cheatsheets"
PAPERS = json.loads((ROOT / "quiz-app" / "src" / "papers.json").read_text(encoding="utf-8"))
CONCEPTS = json.loads((ROOT / "question_sources" / "concepts.json").read_text(encoding="utf-8"))

DOMAIN = {1: "API Authentication", 2: "Go Live Process", 3: "Docusign Connect", 4: "eSignature API",
          5: "eSignature Features and Web Forms", 6: "Agreement Manager API", 7: "Workflow Builder and Workflow API",
          8: "App Center and Extension Apps"}
# which rows of the numbers table belong to which section
NUM_FOR = {
    1: ["Authorization code lifetime", "Auth Code Grant access token", "JWT Grant access token", "Refresh token", "extended"],
    2: ["API hourly limit", "Burst limit", "Polling", "20 API calls before Go-Live", "Go-Live manual review", "API request logging", "API Dashboard"],
    3: ["Polling"],
    4: ["Embedded signing URL", "Composite templates"],
    5: ["Recipient access code", "Web form clientUserId", "Geography limits"],
    8: ["Geography limits"],
}
LEVEL = {"HIGH": ("#d92d20", "#fef3f2"), "MEDIUM": ("#f79009", "#fffaeb"), "LOW": ("#84adff", "#eff4ff")}


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def head(text):
    t = Table([[Paragraph(text, ST["h2"])]], colWidths=[180 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return [CondPageBreak(30 * mm), Spacer(1, 4), t]


def table(rows, widths, levels=None, header=None):
    data, style = [], [("GRID", (0, 0), (-1, -1), 0.4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    off = 0
    if header:
        data.append([Paragraph(h, ST["hcell"]) for h in header])
        style.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#475467")))
        off = 1
    for i, r in enumerate(rows):
        data.append([Paragraph(c, ST["cell"]) for c in r])
        if levels:
            stripe, bg = levels[i]
            style += [("BACKGROUND", (0, i + off), (-1, i + off), colors.HexColor(bg) if isinstance(bg, str) else bg),
                      ("LINEBEFORE", (0, i + off), (0, i + off), 3, colors.HexColor(stripe) if isinstance(stripe, str) else stripe)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle(style))
    return t


def concept_lines(domain, limit=16):
    seen, out = set(), []
    qs = sorted((q for q in PAPERS if q["domain"] == domain), key=lambda q: {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(q.get("importance"), 1))
    for q in qs:
        c = q.get("concept") or CONCEPTS.get(str(q["id"]))
        if not c:
            continue
        key = c["title"].lower().strip()
        if key in seen:
            continue
        seen.add(key)
        out.append((q.get("importance", "MEDIUM"), c["title"], c["line"]))
        if len(out) >= limit:
            break
    return out


def build(sec):
    n = sec["num"]
    domain = DOMAIN[n]
    story = [Paragraph(f"Cheat Sheet {n}: {esc(sec['title'])}", ST["title"]),
             Paragraph(f"Exam weight <b>{sec['weight']}%</b> (about {round(60 * sec['weight'] / 100)} of 60 questions) &middot; "
                       "<font color='#d92d20'><b>red = must know</b></font>, <font color='#b54708'><b>amber = important</b></font>. "
                       f"Full guide: sections/{sec['slug']}.pdf", ST["sub"])]

    story += head("1. Must-know facts")
    story.append(table([[f] for f in sec["must_know"]], [180 * mm], [("#d92d20", "#fef3f2")] * len(sec["must_know"])))

    nums = [r for r in NUMBERS if any(r[1].startswith(k) or k in r[1] for k in NUM_FOR.get(n, []))]
    if nums:
        story += head("2. Numbers and exact facts")
        story.append(table([[f"<b>{f}</b>", v, f"<i>{c}</i>"] for _, f, v, c in nums], [45 * mm, 90 * mm, 45 * mm],
                           [tint(l) for l, *_ in nums], ["Fact", "Value", "Do not confuse with"]))

    pairs = next((items for title, items in PAIRS if title.split(". ", 1)[1].startswith(sec["title"].split(" (")[0][:12])), [])
    if pairs:
        story += head("3. Confusing pairs: the clue that decides")
        story.append(table([[f"<b>{p}</b>", c] for _, p, c in pairs], [52 * mm, 128 * mm], [tint(l) for l, *_ in pairs]))

    phrases = next((items for title, items in PHRASES if title == domain), [])
    if phrases:
        story += head("4. Business wording -> what it means -> the Docusign choice")
        story.append(table([[f"<i>\"{s}\"</i>", f"<b>{m}</b>", c] for _, s, m, c in phrases], [70 * mm, 32 * mm, 78 * mm],
                           [tint(l) for l, *_ in phrases], ["The exam says...", "It means", "So choose"]))

    lines = concept_lines(domain)
    if lines:
        story += head("5. Rules tested in your practice papers")
        story.append(table([[f"<b>{esc(t)}</b>", esc(l)] for _, t, l in lines], [52 * mm, 128 * mm],
                           [LEVEL.get(i, LEVEL["MEDIUM"]) for i, *_ in lines]))

    if sec.get("important"):
        story += head("6. Also important")
        story.append(table([[f] for f in sec["important"]], [180 * mm], [("#f79009", "#fffaeb")] * len(sec["important"])))

    def page(c, doc):
        c.saveState(); c.setFont(FONT, 7.5); c.setFillColor(MUTED)
        c.drawString(15 * mm, 9 * mm, f"Docusign IAM exam - cheat sheet {n}: {sec['title']}")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{sec['slug']}_cheat_sheet.pdf"
    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=12 * mm, bottomMargin=14 * mm,
                      title=f"Cheat sheet {n} - {sec['title']}").build(story, onFirstPage=page, onLaterPages=page)
    print(out.name, "| pairs", len(pairs), "| phrases", len(phrases), "| numbers", len(nums), "| paper rules", len(lines))


def export_facts():
    """Plain-text cheat-sheet facts per section for the app's dynamic 'Memorize today' (used when mistakes are few)."""
    import re
    strip = lambda t: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").strip()
    out = {}
    for sec in SECTIONS:
        n = sec["num"]
        items = [strip(f) for f in sec["must_know"]]
        pairs = next((it for title, it in PAIRS if title.split(". ", 1)[1].startswith(sec["title"].split(" (")[0][:12])), [])
        items += [f"{strip(p)}: {strip(c)}" for lvl, p, c in pairs if lvl == "H"]
        out[DOMAIN[n]] = items
    path = ROOT / "quiz-app" / "src" / "facts.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", path, {k: len(v) for k, v in out.items()})


if __name__ == "__main__":
    for s in SECTIONS:
        build(s)
    export_facts()

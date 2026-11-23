"""Hands-on lab guides for the 45-day plan (weak sections: eSignature API, Connect + Go Live, Features & Web Forms).

Input:  tmp/papers/labs.json  ({"esignature": LAB, "connect_golive": LAB, "features_webforms": LAB})
Output: output/pdf/labs/lab_1_esignature_api.pdf, lab_2_connect_golive.pdf, lab_3_features_webforms.pdf
        quiz-app/src/labs.json (exercise titles + minutes, used by the plan to name each day's lab slot)
"""
import json
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle

from build_confusion_cheat_sheet_pdf import BOLD, FONT, GRID, MUTED, NAVY, ST

ROOT = Path(__file__).parent
SRC = ROOT / "question_sources" / "labs.json"
OUT_DIR = ROOT / "output" / "pdf" / "labs"
APP_JSON = ROOT / "quiz-app" / "src" / "labs.json"
FILES = {"esignature": "lab_1_esignature_api.pdf", "connect_golive": "lab_2_connect_golive.pdf", "features_webforms": "lab_3_features_webforms.pdf",
         "auth": "lab_4_api_authentication.pdf", "workflow": "lab_5_workflow.pdf", "extension_apps": "lab_6_extension_apps.pdf",
         "agreement_manager": "lab_7_agreement_manager.pdf"}  # embedding is part of labs 1, 3 and 5
EXTRA = sorted((ROOT / "question_sources").glob("labs2_*.json"))  # labs 4-8 (strong sections + embedding)

S = {
    "body": ParagraphStyle("b", fontName=FONT, fontSize=9, leading=12.2, textColor=colors.HexColor("#1d2939")),
    "step": ParagraphStyle("s", fontName=FONT, fontSize=9, leading=12.2, leftIndent=12, bulletIndent=2, spaceAfter=1.5),
    "h": ParagraphStyle("h", fontName=BOLD, fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=3),
    "lbl": ParagraphStyle("l", fontName=BOLD, fontSize=8.6, leading=11, textColor=colors.HexColor("#475467"), spaceBefore=3),
    "code": ParagraphStyle("c", fontName="Courier", fontSize=7.6, leading=9.4, textColor=colors.HexColor("#101828")),
    "trap": ParagraphStyle("t", fontName=FONT, fontSize=8.8, leading=11.6, leftIndent=12, bulletIndent=2, textColor=colors.HexColor("#912018")),
}


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bullets(items, style="step", char="•"):
    return [Paragraph(esc(x), S[style], bulletText=char) for x in items or []]


def box(flow, bg, line):
    t = Table([[f] for f in flow], colWidths=[180 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg)), ("LINEBEFORE", (0, 0), (0, -1), 3, colors.HexColor(line)),
                           ("LEFTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
    return t


def build(key, lab, n):
    story = [Paragraph(esc(lab["title"]), ST["title"]),
             Paragraph(f"45-day plan &middot; {esc(lab.get('weeks', ''))} &middot; use a Docusign <b>developer (demo)</b> account only. "
                       "Never commit secrets, RSA keys, account IDs or tokens to git.", ST["sub"]),
             Paragraph(esc(lab.get("goal", "")), S["body"]), Paragraph("Setup", S["h"])]
    story += bullets(lab.get("setup"), char="-")
    for i, ex in enumerate(lab.get("exercises", []), 1):
        sat = (ex.get("minutes") or 15) >= 45
        head = f"Exercise {i}: {esc(re.sub(r'^\d+\.\s*', '', ex['title']))} &middot; {ex.get('minutes', 15)} min" + (" &middot; <font color='#b54708'>Saturday lab</font>" if sat else "")
        block = [Paragraph(head, S["h"])]
        block += bullets(ex.get("steps"))
        if ex.get("api"):
            block += [Paragraph("API", S["lbl"]), box([Preformatted(ex["api"], S["code"], maxLineLength=110)], "#f2f4f7", "#98a2b3")]
        if ex.get("observe"):
            block += [Paragraph("What to observe", S["lbl"])] + bullets(ex["observe"])
        if ex.get("examTraps"):
            block += [Spacer(1, 2), box([Paragraph("<b>Exam traps this teaches</b>", S["body"])] + bullets(ex["examTraps"], "trap"), "#fef3f2", "#d92d20")]
        story += [KeepTogether(block[:4]), *block[4:], Spacer(1, 4)]
    if lab.get("cleanup"):
        story += [Paragraph("Clean-up", S["h"])] + bullets(lab["cleanup"], char="-")
    if lab.get("takeaways"):
        story += [Paragraph("Design rules to remember", S["h"]), box(bullets(lab["takeaways"]), "#ecfdf3", "#039855")]

    def page(c, doc):
        c.saveState(); c.setFont(FONT, 7.5); c.setFillColor(MUTED)
        c.drawString(15 * mm, 9 * mm, f"Docusign IAM exam - lab guide {n}")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    out = OUT_DIR / FILES[key]
    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=12 * mm, bottomMargin=14 * mm,
                      title=lab["title"]).build(story, onFirstPage=page, onLaterPages=page)
    print(out, len(lab.get("exercises", [])), "exercises")


def main():
    labs = json.loads(SRC.read_text(encoding="utf-8"))
    for f in EXTRA:
        labs.update(json.loads(f.read_text(encoding="utf-8")))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for n, key in enumerate(FILES, 1):
        if key in labs:
            build(key, labs[key], n)
        else:
            print("missing lab:", key)
    summary = {k: {"title": v["title"], "exercises": [{"title": e["title"], "minutes": e.get("minutes", 15), "tryIt": bool(e.get("tryIt"))} for e in v.get("exercises", [])]}
               for k, v in labs.items() if k in FILES}
    APP_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", APP_JSON)


if __name__ == "__main__":
    main()

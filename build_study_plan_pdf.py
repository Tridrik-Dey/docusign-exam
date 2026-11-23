"""Build the dated study plan PDF (exam Sunday 22 Nov 2026) (recommended order: quick wins -> highest-risk -> broad -> small).
Output: output/pdf/00_study_plan_exam_22_nov.pdf
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import CondPageBreak, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).parent
OUT = ROOT / "output" / "pdf" / "00_study_plan_exam_22_nov.pdf"

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

NAVY, INK, MUTED = colors.HexColor("#0b2545"), colors.HexColor("#1d2939"), colors.HexColor("#667085")
PHASE_COLORS = {
    1: (colors.HexColor("#039855"), colors.HexColor("#ecfdf3")),
    2: (colors.HexColor("#d92d20"), colors.HexColor("#fef3f2")),
    3: (colors.HexColor("#f79009"), colors.HexColor("#fffaeb")),
    4: (colors.HexColor("#175cd3"), colors.HexColor("#eff4ff")),
}
ST = {
    "title": ParagraphStyle("t", fontName=BOLD, fontSize=22, leading=27, textColor=NAVY, spaceAfter=4),
    "sub": ParagraphStyle("s", fontName=FONT, fontSize=10, leading=14, textColor=MUTED, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=14, leading=18, textColor=NAVY, spaceBefore=10, spaceAfter=6),
    "day": ParagraphStyle("d", fontName=BOLD, fontSize=11, leading=14, textColor=colors.white),
    "body": ParagraphStyle("b", fontName=FONT, fontSize=9.2, leading=12.6, textColor=INK),
    "small": ParagraphStyle("sm", fontName=FONT, fontSize=8.4, leading=11, textColor=INK),
}
SEC = "output/pdf/sections/"

PHASES = [
    (1, "Mon-Tue: Quick wins + start the highest-risk section", "Authentication, Connect and Go-Live are small and fact-heavy (36% of the exam). Bank them fast, then start App Center."),
    (2, "Wed: Highest risk", "App Center and Workflow (31%) have the most conceptual and multiple-answer questions."),
    (3, "Thu-Fri: Broad and gap topics", "eSignature API, then Features, Web Forms and Agreement Manager (33%)."),
    (4, "Sat-Sun: Simulation, then exam", "Simulate the exam, rest, sit the exam."),
]

DAYS = [
    ("Mon 16 Nov", 1, "Baseline mock + API Authentication (13%) + Connect (12%)", [
        "Quiz app: <b>Mock exam</b> (60 Q, 150 min) as a baseline. Do not study first. Write down your 3 weakest sections.",
        f"Read the red and amber boxes in <b>{SEC}01_api_authentication.pdf</b>, then do <b>01_api_authentication_questions.pdf</b> (48 Q).",
        f"Read the red and amber boxes in <b>{SEC}03_docusign_connect.pdf</b>, then do <b>03_docusign_connect_questions.pdf</b> (41 Q).",
        "Memorize: code 120 s, access token 8 h, refresh 30 d (confidential) / 24 h (public), JWT 1 h with no refresh; PKCE; consent types and revoke rules; Connect levels; JSON SIM; HMAC / mTLS; retries.",
    ]),
    ("Tue 17 Nov", 1, "Go Live (11%) + App Center & Extension Apps (16%) part 1", [
        f"Read <b>{SEC}02_go_live_process.pdf</b> (4 pages) and do its 44 questions.",
        "Memorize: no 20-call rule, Start Go live, 48 h manual review, 3,000/hour, 500 per 30 s burst, 15-minute polling rule, API Usage Center and efficiency factors.",
        f"Read <b>{SEC}08_app_center_extension_apps.pdf</b> sections 1 to 4 and <b>output/pdf/docusign_extension_apps_exam_guide.pdf</b>.",
        "Do the first half of <b>08_app_center_extension_apps_questions.pdf</b> (about 36 of 73 Q).",
    ]),
    ("Wed 18 Nov", 2, "App Center part 2 + Workflow Builder & Workflow API (15%)", [
        "Finish the section 8 questions. Then quiz app <b>Review incorrect</b> for App Center.",
        "Memorize: extension -> extension point table, public vs private, manifest parts, register -> test -> review -> publish, Concerto data model, connected fields flow.",
        f"Read <b>{SEC}07_workflow_builder_and_api.pdf</b> and do <b>07_workflow_builder_and_api_questions.pdf</b> (54 Q).",
        "Memorize: start methods; trigger flow (aow_manage -> trigger requirements -> trigger); getWorkflowInstance, cancel (one instance), pause/resume (new instances only).",
    ]),
    ("Thu 19 Nov", 3, "eSignature API (16%)", [
        f"Read the red and amber boxes in <b>{SEC}04_esignature_api.pdf</b> (skip the blue course notes).",
        "Focus: 3 envelope models, composite templates (sequence, one document per object), created vs sent, embedded signing (clientUserId, createRecipient, 5-minute URL, focused vs classic view), embedded sending, bulk send, void vs lock, CORS.",
        "Do <b>04_esignature_api_questions.pdf</b> (58 Q). Then Review incorrect.",
        "If time allows: the free <b>Docusign Integration Developer Pro</b> exam.",
    ]),
    ("Fri 20 Nov", 3, "Features & Web Forms (11%) + Agreement Manager (6%) + Mock #2", [
        f"Read <b>{SEC}05_esignature_features_web_forms.pdf</b> (gap topics: IDV, auth methods, EU SBS, web forms with or without an envelope) and do its 49 questions.",
        f"Read <b>{SEC}06_agreement_manager_api.pdf</b> sections 1 to 4 only and do its 23 questions.",
        "Evening: quiz app <b>Mock exam #2</b>. Target 75% or higher. Note the 2 weakest sections.",
    ]),
    ("Sat 21 Nov", 4, "Simulation + final review (keep it light)", [
        "Morning: Docusign University official <b>Practice Exam</b> (Certification Prep Toolkit).",
        "Fix the weakest sections from Mock #2 and the practice exam: re-read their red boxes and do Review incorrect.",
        "Afternoon: quiz app <b>Mock exam #3</b>. Target 85% or higher.",
        "Logistics: Certiverse <b>system check</b>, install <b>Safe Exam Browser</b> (admin rights needed on work laptops), check your photo ID name matches your registration. Prepare a quiet room with 1 monitor and no headphones.",
        "Stop studying by evening and sleep well.",
    ]),
    ("Sun 22 Nov", 4, "EXAM DAY", [
        "30 minutes before: skim only the red <b>Must-know facts</b> boxes (section 2 of each study PDF). Nothing new.",
        "Join early with your ID ready; close other apps; disable pop-up and ad blockers.",
        "During the exam: answer every question (no penalty for guessing); on multiple-answer questions judge each option on its own and pick exactly the number asked; flag and return; 150 minutes is about 2.5 min per question.",
    ]),
]


def day_card(label, phase, title, tasks):
    fg, bg = PHASE_COLORS[phase]
    head = Table([[Paragraph(label, ST["day"]), Paragraph(title, ST["day"])]], colWidths=[26 * mm, None])
    head.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), fg), ("LEFTPADDING", (0, 0), (-1, -1), 6),
                              ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    rows = [[Paragraph("[ ]", ST["body"]), Paragraph(t, ST["body"])] for t in tasks]
    body = Table(rows, colWidths=[8 * mm, None])
    body.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5), ("LINEBEFORE", (0, 0), (0, -1), 3, fg)]))
    return KeepTogether([head, body, Spacer(1, 7)])


def main():
    story = [Paragraph("Study Plan: Exam on Sunday 22 November 2026", ST["title"]),
             Paragraph("Certified Docusign IAM Integration &amp; Extension Developer &middot; 60 questions &middot; 150 minutes &middot; "
                       "70% to pass (42/60) &middot; some questions have more than one correct answer", ST["sub"])]

    rank = [["Rank", "Section", "Weight", "~Q of 60", "Study on"],
            ["1", "eSignature API", "16%", "10", "Thu 19"], ["1", "App Center & Extension Apps", "16%", "10", "Tue 17 - Wed 18"],
            ["3", "Workflow Builder & Workflow API", "15%", "9", "Wed 18"], ["4", "API Authentication", "13%", "8", "Mon 16"],
            ["5", "Docusign Connect", "12%", "7", "Mon 16"], ["6", "Go Live Process", "11%", "7", "Tue 17"],
            ["6", "eSignature Features & Web Forms", "11%", "7", "Fri 20"], ["8", "Agreement Manager API", "6%", "3-4", "Fri 20"]]
    rank_phase = [None, 3, 2, 2, 1, 1, 1, 3, 3]
    t = Table(rank, colWidths=[14 * mm, 66 * mm, 18 * mm, 20 * mm, 38 * mm])
    style = [("FONTNAME", (0, 0), (-1, -1), FONT), ("FONTNAME", (0, 0), (-1, 0), BOLD), ("FONTSIZE", (0, 0), (-1, -1), 9),
             ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
             ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d0d5dd"))]
    for r in range(1, len(rank)):
        fg, bg = PHASE_COLORS[rank_phase[r]]
        style += [("BACKGROUND", (0, r), (-1, r), bg), ("TEXTCOLOR", (4, r), (4, r), fg), ("FONTNAME", (4, r), (4, r), BOLD)]
    t.setStyle(TableStyle(style))
    story += [Paragraph("Exam importance and study order", ST["h2"]), t, Spacer(1, 8)]

    story.append(Paragraph("Daily method (every study day)", ST["h2"]))
    for line in ["1. Read only the <b>red (MUST KNOW)</b> and <b>amber (IMPORTANT)</b> boxes of the section study PDF. Skim the blue course notes only to look things up.",
                 "2. Answer that section's questions <b>without looking</b> at the green answer box (PDF), or filter the quiz app to the section.",
                 "3. Quiz app <b>Review incorrect</b>: redo misses, read the [WRONG] notes, and re-read the red box behind each miss.",
                 "4. Time-box each section: if a section is at 85% or higher, move on. Target <b>85% or higher</b> per section. The real exam is harder than the practice bank, so a margin above 70% matters.",
                 "5. Multiple-answer questions: decide each option true/false on its own, then pick exactly the number asked."]:
        story.append(Paragraph(line, ST["body"]))

    for ph, title, desc in PHASES:
        cards = [day_card(num, p, dtitle, tasks) for num, p, dtitle, tasks in DAYS if p == ph]
        story += [CondPageBreak(50 * mm), Paragraph(title, ST["h2"]), Paragraph(desc, ST["sub"])] + cards

    story.append(Paragraph("Score tracker", ST["h2"]))
    tr = [["", "Date", "Score", "Weakest 2 sections", "Action"]] + [[f"Mock #{i}", "", "", "", ""] for i in range(1, 4)] + \
         [["Official practice", "", "", "", ""], ["Integration Pro", "", "", "", ""], ["Extension Pro", "", "", "", ""]]
    t2 = Table(tr, colWidths=[30 * mm, 25 * mm, 20 * mm, 55 * mm, 50 * mm], rowHeights=[16] + [20] * (len(tr) - 1))
    t2.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), FONT), ("FONTNAME", (0, 0), (-1, 0), BOLD), ("FONTSIZE", (0, 0), (-1, -1), 9),
                            ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#98a2b3")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    story.append(t2)

    def page(c, doc):
        c.saveState(); c.setFont(FONT, 7.5); c.setFillColor(MUTED)
        c.drawString(15 * mm, 9 * mm, "Docusign IAM Integration & Extension Developer - study plan (exam Sun 22 Nov 2026)")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=14 * mm,
                      bottomMargin=15 * mm, title="Study Plan - exam 22 Nov 2026").build(story, onFirstPage=page, onLaterPages=page)
    print(OUT)


if __name__ == "__main__":
    main()

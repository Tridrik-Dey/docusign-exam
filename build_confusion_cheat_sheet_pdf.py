"""Short last-day cheat sheet: only the must-know numbers, the easily confused pairs, and the trap patterns.

Output: output/pdf/00_confusion_cheat_sheet.pdf
Facts come from study_sections_content.py (verified against the course and Developer Center).
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import CondPageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).parent
OUT = ROOT / "output" / "pdf" / "00_confusion_cheat_sheet.pdf"

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
RED, RED_BG = colors.HexColor("#d92d20"), colors.HexColor("#fef3f2")
AMB, AMB_BG = colors.HexColor("#f79009"), colors.HexColor("#fffaeb")
GRID = colors.HexColor("#d0d5dd")

ST = {
    "title": ParagraphStyle("t", fontName=BOLD, fontSize=18, leading=22, textColor=NAVY, spaceAfter=3),
    "sub": ParagraphStyle("s", fontName=FONT, fontSize=8.6, leading=11.5, textColor=MUTED, spaceAfter=5),
    "h1": ParagraphStyle("h1", fontName=BOLD, fontSize=12.5, leading=16, textColor=NAVY, spaceBefore=7, spaceAfter=4),
    "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=9.6, leading=12, textColor=colors.white),
    "cell": ParagraphStyle("c", fontName=FONT, fontSize=7.9, leading=9.9, textColor=INK),
    "hcell": ParagraphStyle("hc", fontName=BOLD, fontSize=7.9, leading=9.9, textColor=colors.white),
    "trap": ParagraphStyle("tr", fontName=FONT, fontSize=8.2, leading=10.6, textColor=INK, leftIndent=8, bulletIndent=0, spaceAfter=2),
}
C = "<font face='Courier'>"
E = "</font>"

# ---------------------------------------------------------------- 1. numbers
# (level, fact, value, what it gets confused with)
NUMBERS = [
    ("H", "Exam format", "60 questions, 150 min, pass 70%; some are multiple-answer (pick exactly N)", ""),
    ("H", "Authorization code lifetime", "<b>120 seconds</b>", "not 5 min (that is the signing URL)"),
    ("H", "Auth Code Grant access token", "<b>8 hours</b>", "JWT token is 1 hour"),
    ("H", "JWT Grant access token", "<b>1 hour, NO refresh token</b> (build a new JWT); JWT exp max 1 h after iat", "Auth Code is 8 h + refresh token"),
    ("H", "Refresh token", "<b>30 days</b> Confidential / <b>24 hours</b> Public (PKCE)", "JWT has none"),
    ("H", f"{C}extended{E} scope", "refresh token lasts 30 days from the <b>last refresh</b> (rolling); Auth Code only", "without it: 30 days from first issue"),
    ("H", "Embedded signing URL", "<b>5 minutes</b>, single use; request it only when the signer is ready", "auth code is 120 s"),
    ("H", "API hourly limit", "<b>3,000 calls / hour per ACCOUNT</b>, shared by all apps, resets on the hour; excess calls blocked", "NOT per app, NOT per user"),
    ("H", "Burst limit", "<b>500 calls / 30 s</b> production; 200 demo", "hourly limit is 3,000"),
    ("H", "Polling", "max <b>1 status GET per envelope every 15 minutes</b>; use Connect instead", ""),
    ("H", "Connect reply window", "waits up to <b>100 s</b> for HTTP 200; aim for under <b>5 s</b>", "5 s is guidance, not the cut-off"),
    ("H", "Connect retry schedule", "5, 10, 20, 40 min, 1 h, 2 h, 1 day, then <b>daily for 15 days</b>", "after 15 days: republish by hand"),
    ("H", "20 API calls before Go-Live", "<b>No longer required</b>; start Go-Live right after creating the key", "old course material"),
    ("H", "Go-Live manual review", "up to <b>48 hours</b>; <i>Review Expired</i> if not promoted within <b>90 days</b>", ""),
    ("M", "API request logging", "off by default, keeps <b>50 logs</b> (My Preferences), any user", "API Dashboard = 90-day view"),
    ("M", "API Dashboard", "failed requests, <b>90-day</b> timeline (Admin > Apps and Keys)", "Usage Center = efficiency score"),
    ("M", "Web form clientUserId", "required for embedded instance, max <b>100 characters</b>", ""),
    ("M", "Composite templates", "<b>one document</b> per composite object; every server/inline template needs a <b>sequence</b>", ""),
    ("H", "Recipient access code", "set per recipient in the API (<b>accessCode</b> on the signer); max <b>50</b> chars; <b>you</b> share it; no fee", "phone, KBA, IDV cost per use"),
    ("M", "Geography limits", "KBA = <b>US only</b>; bank account OWNER verification = <b>US ABA only</b>", ""),
    ("M", "Exam weights", "App Center 16, eSignature API 16, Workflow 15, Auth 13, Connect 12, Go-Live 11, Features 11, Agreement Manager 6 (%)", ""),
]

# ---------------------------------------------------------------- 2. confusing pairs
# section -> list of (level, "A vs B", "the clue that decides")
PAIRS = [
    ("1. API Authentication (13%)", [
        ("H", "Confidential Auth Code  vs  Public Auth Code + PKCE",
         "Can the app keep a secret? <b>Server-side web app = Confidential</b> (Basic base64(key:secret)). <b>SPA / mobile / desktop = Public + PKCE</b> (no secret, sends code_verifier)."),
        ("H", "Auth Code Grant  vs  JWT Grant",
         "Is a <b>user present</b> to log in? Yes = Auth Code. <b>No user / backend service / scheduled job = JWT</b> (impersonates a user, RSA key)."),
        ("H", "Implicit Grant  vs  Public Auth Code + PKCE", "Implicit is legacy and not recommended. For a browser or mobile app the answer is <b>PKCE</b>."),
        ("H", f"Consent scope  vs  JWT payload scope",
         f"JWT needs consent once with {C}signature impersonation{E}. Afterwards the JWT payload asks only for API scopes (e.g. {C}signature{E})."),
        ("H", "Individual consent  vs  admin consent",
         f"Admin consent needs <b>Access Management + a claimed domain</b>. Internal app: Docusign Admin > Connected Apps. External app: {C}openid + admin_consent_scope{E}. Always keep individual consent as fallback."),
        ("H", "Revoking consent: refresh token  vs  access token",
         "Refresh tokens stop working at once; <b>access tokens already issued keep working until they expire</b>."),
        ("H", "Auth host  vs  API base URI",
         f"Tokens come from {C}account-d{E} (demo) / {C}account{E} (prod). API calls go to <b>base_uri from /oauth/userinfo</b> (account with is_default=true)."),
        ("H", "API call sent to account-d  vs  to base_uri",
         f"{C}account-d/restapi/...{E} returns <b>200 but an HTML login page</b>: 200 is not success. API calls go to <b>base_uri</b>."),
        ("H", "PARTNER_AUTHENTICATION_FAILED (\"Invalid account specified for user\")",
         "Wrong <b>account_id</b> (or <b>sub</b> used in its place), or demo and production mixed. The key itself is usually fine."),
        ("M", "ID token  vs  access token", "ID token (openid) identifies the user; it is <b>never</b> used to call APIs. Its coid claim lists orgs that gave admin consent."),
        ("M", "JWT claims", "iss = integration key, sub = user GUID, aud = account-d.docusign.com (no https), alg RS256. Do not swap iss and sub."),
    ]),
    ("2. Go Live Process (11%)", [
        ("H", "Integration key classifications",
         "<b>Private custom integration</b> = your/your customers' own employees. <b>Third-party integration key</b> = a partner app needs YOUR key. "
         "<b>Public integration</b> = sold to many customers (Partner Program). <b>Embedded integration</b> = customers use YOUR Docusign account (ISV Embed)."),
        ("H", "Go-Live error: no accounts listed", "The <b>integration type does not match the account type</b> you logged into. It is not a permission or 20-calls problem."),
        ("H", "Who submits Go-Live", "Must log in to the <b>production</b> account and be an <b>admin</b> of it."),
        ("H", "API Usage Center  vs  API Dashboard  vs  request logging",
         "Usage Center = <b>efficiency score</b> + raise the hourly limit; charts go back <b>30 days</b> max. Dashboard = timeline up to <b>90 days</b>, call log filtered by "
         "<b>response code</b>. Request logging = <b>50 raw logs</b> for one user."),
        ("H", "Update Hourly Limit  vs  Improve App Efficiency window",
         "The window means: <b>fix the listed apps first</b>, then the button works. Scores start improving after <b>48 h</b>, fully after <b>8 days</b> (not hourly)."),
        ("H", "Big batch job inside the shared limit",
         "Limit is per <b>account</b>: a new integration key adds nothing. Read <b>X-RateLimit-Remaining / -Reset</b>, pause until the reset, ramp up slowly, no tight retry loops."),
        ("H", "Hourly limit  vs  burst limit", "3,000/hour per account (resets on the hour)  vs  500 per 30 seconds. Error names: Hourly_... / Burst_..._Limit_Exceeded."),
        ("M", "Status names", "Course: <i>App is live / Pending approval</i>. Developer Center: <i>Under Review -> Review Passed -> Live</i>, <i>Declined</i>, <i>Review Expired</i>. Both may appear."),
        ("M", "After Go-Live", "Switch to <b>production</b> auth host + base URI, re-create secrets / RSA keys / redirect URIs, update template IDs (they differ)."),
    ]),
    ("3. Docusign Connect (12%)", [
        ("H", "Org  vs  Account  vs  Envelope level",
         "<b>Org</b> = all or <b>selected</b> accounts, one config in Org Admin, <b>JSON SIM only</b>. <b>Account</b> = one account, eSignature Admin or ConnectConfigurations API. "
         f"<b>Envelope</b> = {C}eventNotification{E} on Envelopes:create, <b>API only</b>: misses envelopes sent from the <b>web app</b> or a partner system (Workday...)."),
        ("H", "Connect  vs  polling", "Connect messages <b>do not count against API limits</b> and arrive only on change. Polling: 1 per envelope per 15 min."),
        ("H", "JSON SIM  vs  legacy XML / aggregate",
         "JSON SIM = <b>one message per event</b>, recommended, all levels. <b>Aggregate</b> (JSON or XML, legacy) = related events in <b>one message</b> "
         "(recipient-completed + envelope-completed); account / envelope level only, <b>never org</b>."),
        ("H", "HMAC  vs  Basic  vs  mutual TLS  vs  OAuth",
         "HMAC (SHA-256, X-DocuSign-Signature-1) proves the <b>payload came from Docusign and was not changed</b>. Basic = username/password. mTLS = certificates at the transport layer. "
         "OAuth for Connect = token. Org-level Connect does not offer Basic auth."),
        ("H", "Include HMAC  vs  Require Acknowledgement",
         "<b>HMAC = security</b>: proves the message is from Docusign and unchanged. <b>Require Acknowledgement = reliable delivery</b>: listener must return 2xx "
         "fast, else Connect retries (5, 10, 20, 40 min, 1 h, 2 h, 1 day, then daily for 15 days). Account config API: <b>includeHMAC</b> / <b>requiresAcknowledgement</b>."),
        ("H", "Retries", "Any <b>non-2xx or timeout</b> = failure, retried. Return <b>200 fast</b>, process later (queue), make processing <b>idempotent</b>."),
        ("H", "Require Acknowledgement on  vs  off (account level)",
         "<b>On</b>: failures retried automatically. <b>Off</b>: no retry, a lost event needs a <b>manual republish</b>. <b>Org level always retries.</b>"),
        ("H", "Retry  vs  historical republish (API)",
         "<b>Logged failures</b>: GET .../connect/failures, then PUT .../connect/envelopes/retry_queue (envelopeIds). "
         "<b>Any envelopes, nothing logged</b>: POST .../connect/envelopes/publish/historical (ad hoc config, <b>JSON only</b>, Bulk Actions Log)."),
        ("M", "Republish in the web app",
         "Admin > Connect > <b>Failures > Actions > Republish</b> (failed events), or the <b>Publish</b> tab: filter, tick, Publish (or <b>CSV</b> for bulk)."),
        ("M", "Connected Fields result event", "Arrives as the <b>extension-executed</b> event, JSON SIM only."),
    ]),
    ("4. eSignature API (16%)", [
        ("H", "templateId + templateRoles  vs  compositeTemplates",
         "One template = templateRoles. <b>Combine several templates or templates + extra documents = composite templates</b>."),
        ("H", "status created  vs  sent", "<b>created = draft</b> (needed for embedded sending and doc generation). <b>sent = send now</b>."),
        ("H", "createRecipient  vs  createSender",
         "createRecipient = <b>embedded SIGNING</b> URL (signer has clientUserId, status sent). createSender = <b>embedded SENDING</b> (user tags and sends a <b>draft</b> inside your app)."),
        ("H", "clientUserId set  vs  not set", "With clientUserId the signer is <b>embedded</b> and gets <b>no email</b>. Values in createRecipient must match exactly (email, userName, clientUserId)."),
        ("H", "Focused view  vs  classic view",
         "Focused = recommended, needs <b>frameAncestors + messageOrigins</b> and Docusign JS. <b>Classic</b> needed for payments, ID verification, some SBS, 21 CFR Part 11."),
        ("H", "returnUrl event  vs  Connect", "returnUrl's ?event=signing_complete is a hint only; <b>confirm the status with Connect</b> (or a GET)."),
        ("H", "Void  vs  lock", "<b>Void = permanent</b> (status voided + voidedReason). <b>Lock = temporary</b> while you edit."),
        ("M", "Bulk send  vs  many Envelopes:create calls",
         "Same envelope to many recipients, each getting their own copy = <b>bulk send</b> (list -> envelope with placeholder -> test -> send batch)."),
        ("M", "CORS  vs  back-end proxy", "Single-page app calling the API from the browser = enable <b>CORS</b> origins in Apps and Keys; otherwise call through your back end."),
    ]),
    ("5. eSignature Features & Web Forms (11%)", [
        ("H", "Access code  vs  phone  vs  KBA  vs  IDV",
         "Access code = lightest, free, shared out of band. Phone = call/SMS. <b>KBA = US only</b>. IDV = government photo ID / eID, strongest. Phone, KBA, IDV cost per use."),
        ("H", "identityVerification.workflowId  vs  authenticationMethod",
         f"{C}identityVerification.workflowId{E} (from IdentityVerifications:list) <b>enforces</b> IDV/phone. "
         f"{C}authenticationMethod{E} on createRecipient only <b>records</b> how your app logged the user in."),
        ("H", "Template-based  vs  standalone web form", "Template-based = <b>an envelope is created</b> after submit. Standalone = <b>no envelope</b>, data only."),
        ("H", "Embedded  vs  remote web form instance",
         "Embedded = createInstance with <b>clientUserId</b>, show with Docusign JS. Remote = <b>sendOption + recipients[] with roleName</b>, user gets an email."),
        ("H", "Connected Fields  vs  Data Verification",
         "Connected Fields = signer fields bound to <b>your own data model</b> (Concerto types) and verified against your system. "
         "Data Verification = <b>standard checks</b> (bank account, SSN, email, phone, address, FEIN)."),
        ("H", "Web form prefill: Docusign JS prefillValues  vs  createInstance formValues  vs  default",
         "Priority: <b>Docusign JS prefillValues</b> (browser) &gt; <b>formValues in createInstance</b> &gt; the configuration default. "
         "Exception: <b>read-only fields</b> keep the createInstance value. Users see stale data? Check the front end's prefillValues first."),
        ("H", "Web form: sign in the same page  vs  signing email",
         "In-session signing right after submit needs an <b>embedded</b> instance (createInstance with <b>clientUserId</b>, no sendOption/recipients) and the submitter must be the "
         "<b>signer role</b> in the linked template. <b>useFocusedViewForSigning</b> only switches focused vs classic look; it never causes an email. "
         "An email instead points to a remote instance or the configuration setting <b>Initiate signing session from email</b> (which also disables focused view)."),
        ("M", "Prefill  vs  read results", "Prefill with <b>formValues</b>; read with <b>Instances:getInstance</b> (status, formValues, envelopes[])."),
        ("M", "IDV setup  vs  ID Evidence API", "IDV config makes the signer verify; <b>ID Evidence API</b> retrieves the evidence (ID images, events) afterwards."),
        ("M", "EU AES / QES", "Use IDV configs labelled EU AES / EU QES or recipientSignatureProviders. SBS disables Markup, Notary, field add/delete after first signature."),
    ]),
    ("6. Agreement Manager API (6%)", [
        ("H", "GetAgreementsList  vs  GetAgreement",
         "ID <b>unknown</b> / search / filter = <b>GetAgreementsList</b>. ID <b>known</b>, need parties + provisions = <b>GetAgreement</b>."),
        ("H", "GetAgreement  vs  CreateAgreementSummary",
         f"Structured fields = GetAgreement. AI prose summary = <b>CreateAgreementSummary</b> ({C}POST .../ai/actions/summarize{E}). "
         "<b>There is no getAgreementSummary.</b> Only 4 operations: list, get, delete, createSummary."),
        ("H", "Agreement data  vs  envelope data",
         "Imported legacy agreements <b>have no envelope</b>, so Connect / Envelopes calls miss them. Extracted data is not the PDF file."),
        ("M", "RAG", "Pull agreement data via API, index keyed by <b>agreementId</b>, cite the source agreement."),
    ]),
    ("7. Workflow Builder & Workflow API (15%)", [
        ("H", "Start: manually  vs  from a link  vs  from an API call",
         "Staff run it in Docusign = <b>manually</b>. Public self-service intake on a website/email = <b>from a link</b>. Your app starts it = <b>from an API call</b>."),
        ("H", "GetWorkflowTriggerRequirements  vs  TriggerWorkflow",
         f"First get the trigger URL + input schema (<b>Requirements</b>), then <b>TriggerWorkflow</b> with the inputs. Scope = <b>{C}aow_manage{E}</b>, not signature."),
        ("H", "cancel  vs  pause / resume",
         "<b>cancelWorkflowInstance stops ONE running instance</b>. pauseNewWorkflowInstances / resume affect <b>only NEW instances</b>; running ones continue."),
        ("H", "Instance status", "getWorkflowInstance = one instance's status. getWorkflowInstancesList = all instances."),
        ("H", "Step names", "<b>Send Documents for Signature</b> (older: Get Signatures), Collect Data with Web Forms, Prepare eSignature Template, Identity Verification."),
        ("M", "Prepare eSignature Template  vs  document generation", "Same template every time = Prepare eSignature Template. Content varies per run = document generation."),
        ("M", "Publish error with consentUrl", "Grant consent at the consentUrl, then publish again. <b>Connected fields are not supported in Maestro.</b>"),
    ]),
    ("8. App Center & Extension Apps (16%)", [
        ("H", "Extension -> extension point",
         "<b>Connected Fields + Data Verification -> eSignature</b> (Add Fields / signing; email & phone verification also in Web Forms). <b>Data IO + File output -> Maestro workflows</b>."),
        ("H", "Data IO  vs  File output  vs  Connected Fields  vs  Data Verification",
         "Data IO = <b>read/write records</b> in a system of record (workflow). File output = <b>send the finished file</b> to storage. "
         "Connected Fields = signer fields from your data. Data Verification = check a value (bank, SSN...)."),
        ("H", "Public  vs  private distribution",
         "Public = any App Center customer can install. <b>Private = only listed production accounts</b> (internal DB, org-only data)."),
        ("H", "Developer Console  vs  App Center",
         "<b>Register, test, submit</b> in the Developer Console (form or JSON manifest). <b>Install / list</b> in the App Center."),
        ("H", "Lifecycle", "Register -> console tests -> functional tests -> submit for review -> publish. Statuses: Draft, In Review, Approved, Rejected, Live, Discontinued."),
        ("M", "connectionsReference  vs  actionReferences",
         "In the manifest, an <b>extension</b> lists its actions in <b>actionReferences</b>; an <b>action</b> names its connection in <b>connectionsReference</b>."),
        ("M", "File output  vs  file archive", "File output (cloud storage) = new apps. File archive = legacy."),
        ("M", "Firewall allow-list  vs  API proxy", "Docusign must reach your HTTPS endpoint. An <b>API proxy</b> also translates Docusign's format to your existing API."),
    ]),
]

# ---------------------------------------------------------------- 3. trap patterns
TRAPS = [
    "<b>Fake method names.</b> e.g. getAgreementSummary does not exist. If a method is not in your notes, be suspicious of it.",
    "<b>Swapped numbers.</b> 120 s (auth code) vs 5 min (signing URL); 8 h (Auth Code) vs 1 h (JWT); 3,000/hour vs 500/30 s.",
    "<b>Right feature, wrong level.</b> Account-level Connect when the scenario says all accounts in the org; envelope-level when the sender uses the web app.",
    "<b>\"Records\" vs \"enforces\".</b> authenticationMethod only records; identityVerification enforces.",
    "<b>\"All\" vs \"new only\".</b> Pausing a workflow does not stop instances already running; cancel does.",
    "<b>Trusting the browser.</b> returnUrl events are hints; Connect gives the real status.",
    "<b>Envelope-only thinking.</b> Imported agreements have no envelope; use Agreement Manager calls.",
    "<b>Old rules.</b> The 20-API-call Go-Live test is gone; Implicit Grant is not recommended.",
    "<b>Wrong scope.</b> Workflow API = aow_manage; JWT consent = signature impersonation.",
    "<b>Multiple-answer questions.</b> Judge each option on its own and pick exactly the number asked.",
]


def tint(level):
    return (RED, RED_BG) if level == "H" else (AMB, AMB_BG)


def numbers_table():
    rows = [[Paragraph("Fact", ST["hcell"]), Paragraph("Value", ST["hcell"]), Paragraph("Do not confuse with", ST["hcell"])]]
    style = [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("GRID", (0, 0), (-1, -1), 0.4, GRID),
             ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    for i, (lvl, fact, val, conf) in enumerate(NUMBERS, 1):
        stripe, bg = tint(lvl)
        rows.append([Paragraph(f"<b>{fact}</b>", ST["cell"]), Paragraph(val, ST["cell"]), Paragraph(f"<i>{conf}</i>", ST["cell"])])
        style += [("BACKGROUND", (0, i), (-1, i), bg), ("LINEBEFORE", (0, i), (0, i), 3, stripe)]
    t = Table(rows, colWidths=[45 * mm, 90 * mm, 45 * mm], repeatRows=1)
    t.setStyle(TableStyle(style))
    return t


def pairs_table(section, items):
    head = Table([[Paragraph(section, ST["h2"])]], colWidths=[180 * mm])
    head.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    rows, style = [], [("GRID", (0, 0), (-1, -1), 0.4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    for i, (lvl, pair, clue) in enumerate(items):
        stripe, bg = tint(lvl)
        rows.append([Paragraph(f"<b>{pair}</b>", ST["cell"]), Paragraph(clue, ST["cell"])])
        style += [("BACKGROUND", (0, i), (-1, i), bg), ("LINEBEFORE", (0, i), (0, i), 3, stripe)]
    t = Table(rows, colWidths=[52 * mm, 128 * mm])
    t.setStyle(TableStyle(style))
    return [CondPageBreak(40 * mm), head, t, Spacer(1, 5)]


def main():
    story = [
        Paragraph("Exam Cheat Sheet: Numbers, Confusing Pairs, Traps", ST["title"]),
        Paragraph("Certified Docusign IAM Integration &amp; Extension Developer &middot; exam Sun 22 Nov 2026 &middot; "
                  "<font color='#d92d20'><b>red = must know</b></font>, <font color='#b54708'><b>amber = important</b></font>. "
                  "Only what gets confused; read the section guides for explanations.", ST["sub"]),
        Paragraph("1. Numbers and exact facts", ST["h1"]),
        numbers_table(),
        Paragraph("2. Confusing pairs: the clue that decides", ST["h1"]),
    ]
    for section, items in PAIRS:
        story += pairs_table(section, items)
    story += [CondPageBreak(60 * mm), Paragraph("3. Trap patterns: do not fall for these", ST["h1"])]
    story += [Paragraph(t, ST["trap"], bulletText="\u2022") for t in TRAPS]

    def page(c, doc):
        c.saveState(); c.setFont(FONT, 7.5); c.setFillColor(MUTED)
        c.drawString(15 * mm, 9 * mm, "Docusign IAM Integration & Extension Developer - confusion cheat sheet")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=12 * mm, bottomMargin=14 * mm,
                      title="Docusign IAM exam cheat sheet").build(story, onFirstPage=page, onLaterPages=page)
    print(OUT)


if __name__ == "__main__":
    main()

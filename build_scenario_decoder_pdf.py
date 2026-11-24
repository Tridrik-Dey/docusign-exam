"""Scenario Decoder: translate exam business language into Docusign requirements and choices.

Built after attempt 1 (22 Nov 2026): the candidate knew most facts but struggled to decode long business scenarios
written with varied wording and jargon. Output: output/pdf/00_scenario_decoder.pdf
Facts come from study_sections_content.py (verified against the course and the Developer Center).
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import CondPageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from build_confusion_cheat_sheet_pdf import AMB, AMB_BG, BOLD, FONT, GRID, MUTED, NAVY, RED, RED_BG, ST

ROOT = Path(__file__).parent
OUT = ROOT / "output" / "pdf" / "00_scenario_decoder.pdf"

CHECKLIST = [
    ("Who acts?", "A signer, a sender, an admin, a developer, or a system with nobody logged in?"),
    ("Where does the code run?", "A server that can keep a secret, or a browser / phone / desktop app that cannot?"),
    ("What scope?", "One envelope, one account, every account in the organization, or one customer's account?"),
    ("When?", "Instantly when something happens, later in a batch, only new items, or ones already running?"),
    ("Enforce or record?", "Must Docusign block or verify something, or only note what your app already did?"),
    ("Which product owns it?", "eSignature, Connect, Web Forms, Maestro workflow, Agreement Manager, an extension app, or Go-Live / Apps and Keys?"),
    ("What is noise?", "Company size, industry, tool brand names and 'the team prefers...' rarely change the answer. Find the ONE constraint that does."),
]

TACTICS = [
    "<b>Read the last sentence first</b> (what is asked: best approach, first step, two that apply), then read the scenario looking for that.",
    "<b>Underline the constraint words</b>: without, only, must, cannot, every, existing, already, real time, nobody, no server, all accounts, before sending.",
    "<b>Decide what it needs before you read the options.</b> Then pick the option that meets it, not the option with the most familiar words.",
    "<b>Two options look the same?</b> List the one detail that differs (level, flow, actor, timing, draft vs sent, enforce vs record) and check only that against the stem.",
    "<b>Select two and three look right?</b> Each option must be true AND needed for this scenario. The odd one out is usually true in general but wrong for one stated constraint.",
    "<b>Long options:</b> split each into 'what it does' + 'why'. A right action with a wrong reason (or wrong level) is still wrong.",
    "<b>Fact questions:</b> answer from memory first; if two values look familiar, recall what each value belongs to (e.g. 120 s = auth code, 5 min = signing URL).",
]

# section -> list of (level, business wording in the exam, what it really means, the Docusign choice)
PHRASES = [
    ("API Authentication", [
        ("H", "nightly / scheduled / unattended job; back-office service; no human at the keyboard; system account",
         "No user present; server-side", "JWT Grant (RSA key, impersonation consent once, token 1 h, no refresh token)"),
        ("H", "employees sign in with their own Docusign login; web portal on our servers",
         "User present; app can keep a secret", "Confidential Authorization Code Grant (secret, 8 h token, 30-day refresh)"),
        ("H", "single-page app / React front end with no back end; mobile or desktop app; field rep's tablet",
         "User present; app cannot keep a secret", "Public Authorization Code Grant + PKCE (no secret; code_verifier)"),
        ("H", "organization wants to approve the app once for all its users; IT pre-approves; avoid prompting every employee",
         "Admin consent", "Admin consent (needs Access Management + claimed domain); internal app via Connected Apps, external app via openid + admin_consent_scope"),
        ("H", "keep users signed in for weeks without re-login",
         "Long-lived refresh", "extended scope (refresh token rolls 30 days from last refresh), Auth Code flows only"),
        ("M", "which account / which server to call; multi-account user; works in every region",
         "Discover account + base URI", "/oauth/userinfo -> account_id + base_uri (is_default=true)"),
        ("M", "access must stop immediately when a user leaves",
         "Revocation limits", "Revoking consent kills refresh tokens; issued access tokens work until they expire"),
    ]),
    ("Go Live Process", [
        ("H", "built for our own staff / our customers' employees, runs in our account",
         "Own use", "Private custom integration"),
        ("H", "a partner / vendor product needs to call Docusign for us using our own key",
         "Partner app, your key", "Third-party integration key"),
        ("H", "sell the app to many Docusign customers; listed for others",
         "Multi-customer product", "Public integration (Partner Program)"),
        ("H", "customers use OUR Docusign account inside our product; they never get their own account",
         "ISV embed", "Embedded integration"),
        ("H", "Go-Live screen shows no accounts to choose / error instead of the account list",
         "Mismatch", "Integration type does not match the production account type"),
        ("H", "hit the hourly cap; calls blocked at the top of the hour; many apps share one account",
         "Account-wide limit", "3,000 calls per hour per account (shared); burst 500 per 30 s; use Connect, cache, batch"),
        ("H", "dashboard keeps checking envelope status every minute",
         "Polling abuse", "Max one GET per envelope per 15 min; switch to Connect; listStatusChanges for catch-up"),
        ("M", "works in demo, fails in production after approval",
         "Environment switch", "Production auth host (account.docusign.com), base_uri from userinfo, new secret / RSA keys / redirect URIs, new template IDs"),
    ]),
    ("Docusign Connect", [
        ("H", "listener was down; some events never arrived",
         "Lost events", "Turn on Require Acknowledgement (retries), then republish the missed envelopes"),
        ("H", "send last year's completed envelopes to the new system's listener",
         "Old envelopes", "Historical publish (API) or the Publish tab / CSV"),
        ("H", "notify our system the moment a contract is signed; real time; stop asking Docusign for status",
         "Push, not poll", "Connect webhook (does not count against API limits)"),
        ("H", "every account / subsidiary / business unit in the organization",
         "Many accounts", "Organization-level Connect (JSON SIM only)"),
        ("H", "everything our account's users send",
         "One account", "Account-level Connect (eSignature Admin or ConnectConfigurations API)"),
        ("H", "only the envelopes this app creates; each envelope to its own listener",
         "Per envelope", "Envelope-level: eventNotification on Envelopes:create (API only; misses web-app and partner-system sends)"),
        ("H", "only some of the organization's accounts; one configuration managed centrally",
         "Org subset", "Organization-level Connect with selected accounts (not one config per account)"),
        ("M", "one combined message when the last signer finishes",
         "Combined events", "Aggregate delivery mode (legacy; account / envelope level only)"),
        ("H", "prove the message really came from Docusign and was not altered; tamper-proof; security team audit",
         "Origin + integrity", "HMAC-SHA256 signature (X-DocuSign-Signature-1) over the raw body"),
        ("H", "listener sometimes slow / down; duplicates appear; messages arrive twice",
         "Retries", "Return 2xx fast, queue the work, process idempotently; non-2xx or timeout is retried"),
        ("M", "smaller messages, choose which data is included, modern format",
         "Payload format", "JSON SIM (Connect 2.0); XML / aggregate only for legacy"),
    ]),
    ("eSignature API", [
        ("H", "sign inside our website / app / kiosk without leaving it; no email to the signer",
         "Embedded signing", "clientUserId on the recipient + EnvelopeViews:createRecipient (URL 5 min, single use)"),
        ("H", "let our staff review, tag and send from inside our portal",
         "Embedded sending", "Create envelope as draft (status created) + EnvelopeViews:createSender"),
        ("H", "standard pack reused every time with different people",
         "One template", "templateId + templateRoles"),
        ("H", "combine several standard templates / template plus an extra uploaded document",
         "Mix templates + documents", "compositeTemplates (sequence; one document per composite object)"),
        ("H", "same document to hundreds of people, each signs their own copy",
         "One-to-many", "Bulk send (bulk send list -> envelope -> optional test -> send batch)"),
        ("H", "prepare now, send later after approval",
         "Draft", "status = created; send by updating to sent"),
        ("H", "cancel the deal permanently  vs  stop changes while we edit",
         "Void vs lock", "Void is permanent (voidedReason); lock is temporary"),
        ("M", "browser app calls Docusign directly without our server",
         "Cross-origin calls", "CORS (allowed origins in Apps and Keys) or a back-end proxy"),
        ("M", "modern embedded look inside our page; we control the frame",
         "Focused view", "Focused view with frameAncestors + messageOrigins; classic view for payments, IDV, some SBS, 21 CFR Part 11"),
    ]),
    ("eSignature Features and Web Forms", [
        ("H", "strong proof of who signed; government ID; regulated / high-value deal",
         "Enforce identity", "IDV: identityVerification.workflowId on the recipient (IDs from IdentityVerifications:list)"),
        ("H", "cheap / low-friction extra check; code shared by phone or in person",
         "Light auth", "Access code (free); phone / SMS next; KBA US only; all except access code cost per use"),
        ("H", "our portal already logged the user in; show that on the certificate",
         "Record, not enforce", "authenticationMethod on createRecipient (records only)"),
        ("H", "collect information from people, no signature needed",
         "Data only", "Standalone web form (no envelope)"),
        ("H", "collect information, then produce a signed agreement",
         "Data + signature", "Template-based web form (envelope created on submit)"),
        ("H", "form shown inside our site  vs  form emailed to the person",
         "Embedded vs remote instance", "Embedded: createInstance with clientUserId + Docusign JS; remote: sendOption + recipients with roleName"),
        ("H", "members should sign on the same page right after submitting, but get an email instead",
         "In-session vs email", "Embedded instance (clientUserId, submitter = template signer role); not useFocusedViewForSigning; check the 'Initiate signing session from email' setting"),
        ("H", "customers see an old / cached value although the back end sends the current one",
         "Prefill priority", "Docusign JS prefillValues override createInstance formValues, which override the default (read-only fields keep the createInstance value)"),
        ("M", "fields must be checked against our own customer database while signing",
         "Custom data", "Connected Fields (your data model); standard checks (bank, SSN, email, phone) = Data Verification"),
        ("M", "our logo, colours and email text on everything we send",
         "Branding", "Brand (logos, colours, email / signing resources, destination URLs) via brandId"),
    ]),
    ("Agreement Manager API", [
        ("H", "find contracts matching criteria; we don't know the ID; renewals due next quarter",
         "Search", "GetAgreementsList (filters, paging)"),
        ("H", "one known contract: parties, dates, clauses for our ERP / CRM",
         "Structured detail", "GetAgreement"),
        ("H", "short readable overview of a contract",
         "AI summary", "CreateAgreementSummary (POST .../ai/actions/summarize). No getAgreementSummary."),
        ("M", "contracts signed before we used Docusign / on paper / another tool",
         "Legacy import", "Bulk import; these have no envelope, so Connect / Envelopes calls miss them"),
        ("M", "our AI assistant should answer questions about contracts with sources",
         "RAG", "Pull agreement data via API, index by agreementId, cite the agreement"),
    ]),
    ("Workflow Builder and Workflow API", [
        ("H", "public intake page / self-service link in an email or website",
         "Self-start", "Start from a link"),
        ("H", "our app starts the process when its own event happens; pass data in",
         "Programmatic start", "From an API call: aow_manage -> GetWorkflowTriggerRequirements -> TriggerWorkflow"),
        ("H", "staff kick it off themselves inside Docusign",
         "Manual start", "Manually (Run workflow; Workflows: Prepare permission)"),
        ("H", "stop this one stuck instance  vs  stop new ones while we fix the flow",
         "Cancel vs pause", "cancelWorkflowInstance (one instance) vs pauseNewWorkflowInstances (new only; running continue)"),
        ("M", "read or write our system of record during the workflow; archive files at the end",
         "Extension steps", "Data IO / File output extension apps (installed from the App Center)"),
        ("M", "publish fails with a consent link",
         "Consent", "Grant consent at consentUrl, then publish again"),
    ]),
    ("App Center and Extension Apps", [
        ("H", "check values against our own database while the signer fills the form",
         "Verify own data", "Connected Fields extension (eSignature); Concerto type definitions"),
        ("H", "validate bank account / email / phone / address during signing",
         "Standard checks", "Data Verification extension (eSignature; email / phone also in Web Forms)"),
        ("H", "workflow must read or update a CRM / ERP record",
         "System of record", "Data IO extension (Maestro)"),
        ("H", "save the completed agreement to our storage",
         "File delivery", "File output (cloud storage) extension (Maestro); file archive = legacy"),
        ("H", "only our own company may install it  vs  any Docusign customer",
         "Distribution", "Private (listed production accounts)  vs  public (App Center listing)"),
        ("M", "our API sits behind a firewall / speaks a different format",
         "Reachability", "Allow-list Docusign or use an API proxy that also translates the format"),
    ]),
]

SYNONYMS = [
    ("No user present", "unattended, headless, scheduled, nightly, batch, background service, system account, robot user, no human at the keyboard"),
    ("Cannot keep a secret", "single-page app, browser-only, React / Angular front end, mobile app, desktop app, tablet, kiosk with no back end"),
    ("System of record", "CRM, ERP, HR system, line-of-business app, back office, internal database, core banking"),
    ("Signer", "customer, applicant, counterparty, member, patient, tenant, employee, client, borrower"),
    ("Real-time notification", "the moment it is signed, instantly, event-driven, push, webhook, callback, without asking"),
    ("Organization", "group, holding company, enterprise, subsidiaries, business units, divisions, regions, many accounts"),
    ("Embedded", "inside our portal / app / site, without leaving, no email, in-session, captive, in-person on our device"),
    ("Tamper-proof / trusted", "verify origin, integrity, security review, compliance, audit, signed message"),
]


def tint(level):
    return (RED, RED_BG) if level == "H" else (AMB, AMB_BG)


def numbered(items):
    rows = [[Paragraph(f"<b>{i}. {a}</b>", ST["cell"]), Paragraph(b, ST["cell"])] for i, (a, b) in enumerate(items, 1)]
    t = Table(rows, colWidths=[45 * mm, 135 * mm])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#eff4ff")), ("LINEBEFORE", (0, 0), (0, -1), 3, colors.HexColor("#2e90fa")),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
    return t


def phrase_table(section, items):
    head = Table([[Paragraph(section, ST["h2"])]], colWidths=[180 * mm])
    head.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    rows = [[Paragraph("The exam says...", ST["hcell"]), Paragraph("It means", ST["hcell"]), Paragraph("So choose", ST["hcell"])]]
    style = [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#475467")), ("GRID", (0, 0), (-1, -1), 0.4, GRID),
             ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    for i, (lvl, says, means, choose) in enumerate(items, 1):
        stripe, bg = tint(lvl)
        rows.append([Paragraph(f"<i>\"{says}\"</i>", ST["cell"]), Paragraph(f"<b>{means}</b>", ST["cell"]), Paragraph(choose, ST["cell"])])
        style += [("BACKGROUND", (0, i), (-1, i), bg), ("LINEBEFORE", (0, i), (0, i), 3, stripe)]
    t = Table(rows, colWidths=[70 * mm, 32 * mm, 78 * mm], repeatRows=1)
    t.setStyle(TableStyle(style))
    return [CondPageBreak(35 * mm), head, t, Spacer(1, 5)]


def main():
    story = [
        Paragraph("Scenario Decoder: business words -> Docusign choice", ST["title"]),
        Paragraph("For long exam scenarios written in business language. Decide what the scenario needs BEFORE reading the options. "
                  "<font color='#d92d20'><b>red = must know</b></font>, <font color='#b54708'><b>amber = important</b></font>.", ST["sub"]),
        Paragraph("1. Decode checklist: answer these before you look at the options", ST["h1"]),
        numbered(CHECKLIST),
        Paragraph("2. Close options and select-two: tactics", ST["h1"]),
    ]
    story += [Paragraph(t, ST["trap"], bulletText="•") for t in TACTICS]
    story += [Paragraph("3. Business wording -> what it means -> the Docusign choice", ST["h1"])]
    for section, items in PHRASES:
        story += phrase_table(section, items)
    story += [CondPageBreak(60 * mm), Paragraph("4. Same idea, different words", ST["h1"])]
    rows = [[Paragraph(f"<b>{a}</b>", ST["cell"]), Paragraph(b, ST["cell"])] for a, b in SYNONYMS]
    t = Table(rows, colWidths=[45 * mm, 135 * mm])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
    story.append(t)

    def page(c, doc):
        c.saveState(); c.setFont(FONT, 7.5); c.setFillColor(MUTED)
        c.drawString(15 * mm, 9 * mm, "Docusign IAM Integration & Extension Developer - scenario decoder")
        c.drawRightString(A4[0] - 15 * mm, 9 * mm, f"Page {doc.page}"); c.restoreState()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=12 * mm, bottomMargin=14 * mm,
                      title="Docusign IAM scenario decoder").build(story, onFirstPage=page, onLaterPages=page)
    print(OUT)


if __name__ == "__main__":
    main()

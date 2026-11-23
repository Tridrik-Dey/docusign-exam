from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


PRIMARY_OUT = Path("output/pdf/docusign_node_quickstart_technical_deep_dive.pdf")
FALLBACK_OUT = Path("output/pdf/docusign_node_quickstart_technical_deep_dive_updated.pdf")


def choose_output_path() -> Path:
    PRIMARY_OUT.parent.mkdir(parents=True, exist_ok=True)
    if not PRIMARY_OUT.exists():
        return PRIMARY_OUT
    try:
        with PRIMARY_OUT.open("ab"):
            pass
        return PRIMARY_OUT
    except PermissionError:
        return FALLBACK_OUT


OUT = choose_output_path()
OUT.parent.mkdir(parents=True, exist_ok=True)


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(esc(text), style)


def bullets(items: list[str], style: ParagraphStyle) -> ListFlowable:
    return ListFlowable(
        [ListItem(p(item, style), leftIndent=8) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=16,
        bulletFontName="Helvetica",
        bulletFontSize=6,
    )


def table(headers: list[str], rows: list[list[str]], widths: list[float], body_style: ParagraphStyle) -> Table:
    data = [[p(h, styles["TableHeader"]) for h in headers]]
    for row in rows:
        data.append([p(cell, body_style) for cell in row])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#153E75")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C4D6")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFC")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def section(title: str) -> list:
    return [Spacer(1, 8), p(title, styles["H2"]), Spacer(1, 4)]


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#526174"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(0.55 * inch, 0.35 * inch, "Docusign Node Quickstart technical exam guide")
    canvas.drawRightString(7.95 * inch, 0.35 * inch, f"Page {doc.page}")
    canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        "TitleMain",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#102033"),
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        "Subtitle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#526174"),
        spaceAfter=14,
    )
)
styles.add(
    ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13.5,
        leading=16,
        textColor=colors.HexColor("#153E75"),
        spaceBefore=8,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        "H3",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor("#102033"),
        spaceBefore=8,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.7,
        leading=11.5,
        textColor=colors.HexColor("#102033"),
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        "Small",
        parent=styles["Body"],
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#334155"),
    )
)
styles.add(
    ParagraphStyle(
        "CodeBlock",
        parent=styles["Body"],
        fontName="Courier",
        fontSize=7.3,
        leading=9.3,
        textColor=colors.HexColor("#0F172A"),
        backColor=colors.HexColor("#F1F5F9"),
        borderPadding=4,
        spaceBefore=3,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        "TableHeader",
        parent=styles["Body"],
        fontName="Helvetica-Bold",
        fontSize=7.7,
        leading=9.2,
        textColor=colors.white,
    )
)
styles.add(
    ParagraphStyle(
        "TableBody",
        parent=styles["Small"],
        fontSize=7.1,
        leading=8.7,
    )
)


story = []
story.append(p("Docusign Node Quickstart Technical Deep Dive", styles["TitleMain"]))
story.append(
    p(
        "Exam-focused notes from Quickstart App-1-node.js: OAuth, base paths, SDK clients, eSignature request bodies, Web Forms, Maestro, Navigator, Connect, and Extension Apps (exam-scoped).",
        styles["Subtitle"],
    )
)
story.append(
    p(
        "Sources read: c:/Users/Admin/Downloads/Quickstart App-1-node.js.zip and c:/Users/Admin/Downloads/code-examples-node-master.zip. The second zip has the same file inventory as the first, so this guide adds non-duplicate procedural depth instead of repeating the same endpoint catalog. Sensitive files such as config/private.key and config/appsettings.json were not quoted. Section 14D was added from the Docusign University \"Docusign Extension Apps\" certification learning path and developers.docusign.com, since the quickstart source code only reaches Extension Apps indirectly through Connected Fields.",
        styles["Small"],
    )
)

story += section("1. Project Mental Model")
story.append(
    table(
        ["Layer", "Files", "Technical meaning"],
        [
            ["Express launcher", "index.js", "Registers local routes such as /eg001, /weg001, /mae001, /nav001, /ds/login, /ds/callback. These are app routes, not Docusign API endpoints."],
            ["Auth helpers", "lib/common/DSAuthCodeGrant.js and lib/common/DSJwtAuth.js", "Own the token lifecycle. Before any API call, examples call req.dsAuth.checkToken(), then use accessToken, accountId, and basePath from the session."],
            ["Example controllers", "lib/*/controllers/*.js", "Validate form input, call the matching example function, render success or error pages."],
            ["Example implementations", "lib/*/examples/*.js", "Create SDK ApiClient instances, set basePath, attach Authorization: Bearer token, build request bodies, call SDK methods."],
            ["Config", "config/appsettings.example.json and config/index.js", "Defines OAuth server selection, app URL, API base URLs, signer defaults, and product-specific endpoints."],
        ],
        [1.2 * inch, 1.65 * inch, 4.55 * inch],
        styles["TableBody"],
    )
)
story.append(p("Exam trap: know the difference between a local Express route and the real Docusign API call hidden behind the controller.", styles["Body"]))

story += section("2. OAuth and Account Discovery")
story.append(
    table(
        ["Flow", "Where in project", "What happens technically", "Exam point"],
        [
            ["Authorization Code Grant", "index.js + DSAuthCodeGrant.js", "Passport redirects to Docusign authorize endpoint, receives the callback at /ds/callback, stores accessToken and refreshToken in req.user.", "Used when a user is present and the server can protect a client secret."],
            ["Authorization Code Grant with PKCE", "index.js docusignStrategyPKCE", "Same authorization-code pattern but adds PKCE for public-client style protection.", "PKCE protects public clients that cannot safely store a secret."],
            ["JWT Grant", "DSJwtAuth.js", "SDK requestJWTUserToken(clientId, impersonatedUserGuid, scopes, rsaKey, jwtLifeSec), then getUserInfo(accessToken).", "Used for unattended/service integration after consent, with RSA private key and impersonation."],
            ["UserInfo", "DSAuthCodeGrant.oauth_callback2 and DSJwtAuth.getUserInfo", "Finds target account or default account and sets accountId, accountName, basePath = baseUri + /restapi.", "Most API calls need both accountId and correct basePath, not just an access token."],
        ],
        [1.35 * inch, 1.55 * inch, 2.95 * inch, 1.45 * inch],
        styles["TableBody"],
    )
)
story.append(p("Auth code callback flow - three parallel tracks:", styles["H3"]))
story.append(
    table(
        ["Business/browser event", "Your Express app route/code", "Docusign OAuth/API URL shape"],
        [
            [
                "User clicks Login with Docusign.",
                "Browser calls GET https://www.abc.com/ds/login. Express login handler clears old session and starts Passport/Docusign OAuth.",
                "No Docusign API call yet.",
            ],
            [
                "Browser leaves your app and goes to Docusign login.",
                "Express builds the authorize URL using dsClientId, requested scopes, and callback URL.",
                "GET https://account-d.docusign.com/oauth/auth ? response_type=code & scope=signature & client_id={dsClientId} & redirect_uri=https://www.abc.com/ds/callback",
            ],
            [
                "User signs in and grants consent.",
                "Your app waits. No Express route is running while user is on Docusign login/consent page.",
                "Docusign hosted login/consent page. The user is authenticating with Docusign, not with your local /eg route.",
            ],
            [
                "Docusign sends the browser back to your app.",
                "Browser calls GET https://www.abc.com/ds/callback?code={authorization_code}. Express callback handler receives the temporary code.",
                "Docusign redirects to the exact redirect_uri and appends code. The callback URL normally has code, not client_id.",
            ],
            [
                "Your backend exchanges the temporary code for tokens.",
                "Server-side code inside /ds/callback calls token endpoint. In this project Passport handles the exchange.",
                "POST https://account-d.docusign.com/oauth/token with grant_type=authorization_code, code={authorization_code}, redirect_uri=https://www.abc.com/ds/callback, plus client authentication using dsClientId and dsClientSecret.",
            ],
            [
                "Docusign returns access token.",
                "Express stores accessToken, refreshToken, and token expiration on the authenticated user/session.",
                "Token response includes access_token, token_type=Bearer, expires_in, and often refresh_token for auth-code grant.",
            ],
            [
                "Your backend discovers account and base URI.",
                "Express/Passport userinfo result or helper code selects target/default account and stores accountId, accountName, basePath.",
                "GET https://account-d.docusign.com/oauth/userinfo with Authorization: Bearer {access_token}. Response has accounts[].account_id and accounts[].base_uri.",
            ],
            [
                "Your app prepares future API calls.",
                "Express sets basePath = base_uri + /restapi. Example: https://demo.docusign.net + /restapi.",
                "No new OAuth URL. This creates the eSignature API base path: https://demo.docusign.net/restapi.",
            ],
            [
                "User opens or submits a business example.",
                "GET /eg001 shows page. POST /eg001 runs controller and calls example code using stored accessToken, accountId, basePath.",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes. Example: POST https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes",
            ],
        ],
        [2.05 * inch, 2.65 * inch, 2.6 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "Key memory rule: /oauth/auth includes client_id and redirect_uri. /ds/callback receives code. /oauth/token exchanges code plus client credentials for access_token. /oauth/userinfo returns account_id and base_uri.",
        styles["Body"],
    )
)
story.append(p("JWT flow:", styles["H3"]))
story.append(p("requestJWTUserToken -> access_token -> getUserInfo -> choose default or target account -> basePath = account.baseUri + /restapi", styles["CodeBlock"]))

story += section("3. Base Paths and Product Endpoints")
story.append(
    table(
        ["Product/API", "Base path in project", "Typical real endpoint shape", "Important detail"],
        [
            ["OAuth", "https://account-d.docusign.com or https://account.docusign.com", "/oauth/auth, /oauth/token, /oauth/userinfo, /oauth/logout", "Demo uses account-d; production uses account."],
            ["eSignature REST", "account base_uri + /restapi", "/v2.1/accounts/{accountId}/envelopes", "base_uri comes from OAuth userinfo. Do not hardcode demo.docusign.net for every account."],
            ["Web Forms", "https://apps-d.docusign.com/api/webforms", "/v1/accounts/{accountId}/forms/{formId}/instances", "This SDK uses the Web Forms base path, separate from eSignature /restapi."],
            ["Admin", "https://api-d.docusign.net/management", "/v2/organizations/{organizationId}/...", "Organization-scoped. You often need organizationId in addition to accountId."],
            ["IAM/Navigator/Maestro", "IAM SDK or https://api-d.docusign.com/v1 / services path", "/v1/accounts/{accountId}/agreements or AOW management paths", "Agreement/IAM APIs use newer SDK surfaces and may not use eSignature basePath."],
        ],
        [1.35 * inch, 1.75 * inch, 2.25 * inch, 1.95 * inch],
        styles["TableBody"],
    )
)

story += section("4. eSignature API Calls in the Quickstart")
story.append(
    table(
        ["Feature", "SDK method", "REST shape", "What the request must include"],
        [
            ["Send envelope by email", "EnvelopesApi.createEnvelope(accountId, { envelopeDefinition })", "POST /v2.1/accounts/{accountId}/envelopes", "documents[], recipients, tabs, emailSubject, status='sent'."],
            ["Create draft", "createEnvelope", "POST /envelopes", "Same body as send, but status='created'."],
            ["Embedded signing", "createEnvelope then createRecipientView", "POST /envelopes then POST /envelopes/{envelopeId}/views/recipient", "Signer must include clientUserId. Recipient view requires returnUrl, authenticationMethod, email, userName, clientUserId."],
            ["Embedded sending", "createEnvelope then createSenderView", "POST /envelopes then POST /envelopes/{envelopeId}/views/sender", "Usually creates a draft first, then redirects sender into Docusign sender UI."],
            ["Template send", "createEnvelope with templateId and templateRoles", "POST /envelopes", "templateId identifies server template. templateRoles map roleName to real recipients."],
            ["Composite/document variants", "createEnvelope", "POST /envelopes", "Can mix HTML, PDF, DOCX, base64 documents, tabs, recipients, and routing."],
            ["List envelopes", "listStatusChanges(accountId, options)", "GET /v2.1/accounts/{accountId}/envelopes", "Uses filters such as fromDate and status. Better for search/list, not webhook replacement."],
            ["Envelope info", "getEnvelope", "GET /envelopes/{envelopeId}", "Returns status, subject, timestamps, sender, envelope metadata."],
            ["Recipients", "listRecipients", "GET /envelopes/{envelopeId}/recipients", "Shows routing, recipient statuses, IDs."],
            ["Documents", "listDocuments/getDocument", "GET /envelopes/{envelopeId}/documents", "Download combined or individual document bytes."],
            ["Tab/form data", "getFormData/listCustomFields", "GET /envelopes/{envelopeId}/form_data or custom_fields", "Retrieve entered tab values and custom fields after sending/signing."],
        ],
        [1.15 * inch, 1.75 * inch, 2.0 * inch, 2.4 * inch],
        styles["TableBody"],
    )
)

story.append(PageBreak())
story += section("5. EnvelopeDefinition Anatomy")
story.append(p("A large portion of eSignature technical exam depth is just knowing what is inside the envelope body and which fields belong to which object.", styles["Body"]))
story.append(
    table(
        ["Object/field", "Where it appears", "Meaning"],
        [
            ["EnvelopeDefinition.emailSubject", "Top-level envelope", "Subject shown in signing emails."],
            ["EnvelopeDefinition.status", "Top-level envelope", "'sent' sends immediately; 'created' saves draft; 'voided' cancels an in-process envelope via update."],
            ["documents[].documentBase64", "Document object", "Base64 encoded file bytes. Required when uploading documents directly."],
            ["documents[].documentId", "Document object", "Local reference for tabs. It is not the envelope ID."],
            ["recipients.signers[]", "Recipients object", "People who must sign or fill fields."],
            ["recipients.carbonCopies[]", "Recipients object", "Receives completed copy, generally after prior routing order completes."],
            ["recipientId", "Recipient object", "Local recipient reference used by tabs and APIs."],
            ["routingOrder", "Recipient object", "Lower order routes first. Same routingOrder means parallel delivery."],
            ["clientUserId", "Signer object", "Marks embedded/captive signing. Must match RecipientViewRequest."],
            ["tabs.signHereTabs[]", "Signer tabs", "Signature placement. Can use absolute x/y or anchorString plus offsets."],
            ["templateId", "EnvelopeDefinition", "Use an existing server template."],
            ["templateRoles[]", "EnvelopeDefinition", "Assign real name/email to template roleName values."],
        ],
        [1.75 * inch, 1.55 * inch, 4.0 * inch],
        styles["TableBody"],
    )
)
story.append(p("Anchor tabs exam distinction:", styles["H3"]))
story.append(p("anchorString places fields relative to text found in the document. xPosition/yPosition places fields at absolute page coordinates. Anchor placement is useful when page length can vary.", styles["Body"]))

story += section("6. Embedded Signing Versus Remote Signing")
story.append(
    table(
        ["Question", "Remote signing", "Embedded signing"],
        [
            ["How signer starts", "Email link sent by Docusign.", "Your app redirects or embeds a recipient view URL."],
            ["Signer object", "email, name, recipientId, routingOrder.", "Same, plus clientUserId."],
            ["Extra API call", "None after createEnvelope for start.", "createRecipientView(accountId, envelopeId, { recipientViewRequest })."],
            ["URL lifetime", "Docusign manages email link.", "Recipient view URL is short-lived; generate when user is ready."],
            ["Return path", "Brand destination URL or Docusign completion flow.", "returnUrl in RecipientViewRequest."],
            ["Common exam clue", "Signer receives email.", "Signer must sign inside host app or portal."],
        ],
        [1.35 * inch, 2.95 * inch, 2.95 * inch],
        styles["TableBody"],
    )
)
story.append(p("Embedded signing procedure:", styles["H3"]))
story.append(
    table(
        ["Step", "Your app / Express side", "Docusign API side", "Important memory"],
        [
            ["1", "User logs into your app or portal.", "No Docusign call yet.", "Your app knows who the signer is."],
            ["2", "App builds envelope with signer information.", "POST /v2.1/accounts/{accountId}/envelopes", "Signer must include email, name, recipientId, and clientUserId."],
            ["3", "App sends createEnvelope request.", "Docusign returns envelopeId.", "Store/use envelopeId for the next call."],
            ["4", "App builds RecipientViewRequest.", "POST /v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient", "email, userName, and clientUserId must match the envelope signer."],
            ["5", "App receives signing URL.", "Docusign returns a short-lived recipient view URL.", "Generate the URL when signer is ready."],
            ["6", "Browser redirects or embeds signer to the URL.", "Signer completes signing in Docusign view.", "After finish/decline/cancel/timeout, Docusign redirects browser to returnUrl."],
        ],
        [0.45 * inch, 2.05 * inch, 2.35 * inch, 2.15 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Embedded signing rule: clientUserId in createEnvelope plus the same clientUserId in createRecipientView equals embedded signing. If clientUserId is missing, Docusign treats the signer as remote/email signing.",
        styles["Body"],
    )
)
story.append(p("Remote vs embedded JSON body difference:", styles["H3"]))
story.append(
    table(
        ["Case", "createEnvelope signer body", "Next API call"],
        [
            [
                "Remote signing",
                "{\n  \"email\": \"john@example.com\",\n  \"name\": \"John Smith\",\n  \"recipientId\": \"1\",\n  \"routingOrder\": \"1\"\n}",
                "No createRecipientView call for starting signing. Docusign emails the signer based on the envelope routing.",
            ],
            [
                "Embedded signing",
                "{\n  \"email\": \"john@example.com\",\n  \"name\": \"John Smith\",\n  \"recipientId\": \"1\",\n  \"routingOrder\": \"1\",\n  \"clientUserId\": \"1000\"\n}",
                "Call POST /v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient with matching email, userName, and clientUserId.",
            ],
        ],
        [1.25 * inch, 3.0 * inch, 2.75 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Exam memory: the createEnvelope body is mostly the same. The embedded signer adds clientUserId. That one field changes the flow because your app must request the temporary recipient view URL.",
        styles["Body"],
    )
)
story.append(
    p(
        "Recipient view request body example:\n{\n  \"returnUrl\": \"https://www.abc.com/docusign/return\",\n  \"authenticationMethod\": \"none\",\n  \"email\": \"john@example.com\",\n  \"userName\": \"John Smith\",\n  \"clientUserId\": \"1000\"\n}",
        styles["CodeBlock"],
    )
)
story.append(p("Business example: managing short-lived embedded signing URLs:", styles["H3"]))
story.append(
    table(
        ["Moment", "What your app should do", "Why"],
        [
            ["Tenant logs in", "Authenticate tenant in your rental portal.", "Your app confirms who the signer is before embedded signing."],
            ["App prepares agreement", "Create the envelope and store envelopeId, signerEmail, signerName, and clientUserId.", "These stable values can be stored safely for later."],
            ["Tenant is not ready yet", "Do not depend on a stored recipient view URL.", "Recipient view URL is temporary and can expire before the tenant clicks."],
            ["Tenant clicks Sign Now", "Call createRecipientView for the stored envelopeId and signer details.", "Creates a fresh signing URL at the moment it is needed."],
            ["Docusign returns URL", "Immediately redirect or embed the signer to that URL.", "The signer uses the fresh short-lived URL."],
            ["URL/session expires", "Call createRecipientView again for the same active envelopeId and same embedded signer.", "A new temporary signing URL can be generated if the envelope is still active."],
        ],
        [1.45 * inch, 3.15 * inch, 2.4 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Store this kind of data: { envelopeId, signerEmail, signerName, clientUserId }. Do not rely on storing the recipient view URL for later. Exam memory: create envelope earlier if needed, but create recipient view URL only when signer is ready to sign.",
        styles["Body"],
    )
)

story += section("7. Templates, Tabs, and Dynamic Data")
story.append(
    table(
        ["Pattern", "Main methods", "Technical detail"],
        [
            ["Create template", "TemplatesApi.listTemplates, createTemplate", "Template is an EnvelopeTemplate with documents, recipients, tabs, status='created'."],
            ["Send from template", "EnvelopesApi.createEnvelope", "EnvelopeDefinition.templateId plus templateRoles. Role names must match the template."],
            ["Set template tab values", "createEnvelope from template, createRecipientView", "Use tabLabel and role mapping. Locked/optional fields affect signer editability."],
            ["Document generation", "TemplatesApi.createTemplate, updateDocument, createTabs; EnvelopesApi.getEnvelopeDocGenFormFields, updateEnvelopeDocGenFormFields, update", "Creates a template, updates doc-gen fields, then sends by updating envelope status."],
            ["Document visibility", "createEnvelope", "Recipient/document visibility rules decide which recipients see which docs."],
            ["Conditional recipients", "createEnvelope", "Routing can branch based on field/recipient conditions."],
        ],
        [1.45 * inch, 2.4 * inch, 3.45 * inch],
        styles["TableBody"],
    )
)
story.append(Spacer(1, 6))
story.append(
    table(
        ["Thing", "What it is", "How it is used"],
        [
            [
                "Document",
                "The actual file content: PDF, DOCX, HTML, etc.",
                "Placed in an envelope or template with documentBase64, name, fileExtension, and documentId.",
            ],
            [
                "Envelope",
                "One signing transaction/package.",
                "Contains document(s), real recipients, tabs, routing, email subject, and status such as created or sent.",
            ],
            [
                "Template",
                "Reusable blueprint for future envelopes.",
                "Stores reusable documents, placeholder recipient roles, tabs, routing, and default settings. API returns templateId.",
            ],
        ],
        [1.05 * inch, 2.65 * inch, 3.35 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Memory rule: Document = file. Envelope = one signing transaction. Template = reusable envelope blueprint.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Action", "SDK/API function", "URL shape", "Important body shape"],
        [
            [
                "Create template directly from your UI",
                "TemplatesApi.createTemplate(accountId, { envelopeTemplate })",
                "POST {basePath}/v2.1/accounts/{accountId}/templates",
                "EnvelopeTemplate: name, emailSubject, documents[], recipients with roleName, tabs, status='created'.",
            ],
            [
                "List/search templates",
                "TemplatesApi.listTemplates(accountId, options)",
                "GET {basePath}/v2.1/accounts/{accountId}/templates",
                "No body. Query/filter options such as searchText can be used.",
            ],
            [
                "Send from template",
                "EnvelopesApi.createEnvelope(accountId, { envelopeDefinition })",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes",
                "EnvelopeDefinition: templateId, templateRoles[] with roleName, email, name, tabs, status='sent'.",
            ],
            [
                "Set template tab values",
                "EnvelopesApi.createEnvelope from template",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes",
                "templateRoles[].tabs.textTabs[] or other tabs. Use tabLabel to choose the field and value to fill it.",
            ],
            [
                "Embedded signing from template",
                "createEnvelope then createRecipientView",
                "POST /envelopes then POST /envelopes/{envelopeId}/views/recipient",
                "Template role signer includes clientUserId. RecipientViewRequest must match email, userName, and clientUserId.",
            ],
        ],
        [1.25 * inch, 2.0 * inch, 1.65 * inch, 2.15 * inch],
        styles["Small"],
    )
)
story.append(Spacer(1, 6))
story.append(
    table(
        ["Important ID/body field", "Where it appears", "Purpose"],
        [
            ["accountId", "Every URL path", "Which Docusign account to use."],
            ["templateId", "Send-from-template body", "Which saved template to instantiate as an envelope."],
            ["documentId", "documents[] and tabs", "Which file inside the template/envelope the tab belongs to."],
            ["recipientId", "recipients and tabs", "Which recipient inside the template/envelope owns the tab."],
            ["roleName", "Template recipients and templateRoles", "Placeholder role in the template, such as Employee or Manager."],
            ["tabLabel", "Tabs such as textTabs", "Named field your app fills with dynamic data."],
            ["clientUserId", "Embedded signer/template role", "Marks signer as embedded; must match createRecipientView."],
            ["status", "Template/envelope body", "created saves draft/template; sent sends an envelope."],
        ],
        [1.45 * inch, 2.45 * inch, 2.95 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Typical create-template body: name, emailSubject, documents[], recipients.signers[] with roleName/recipientId/routingOrder/tabs, and status='created'. Typical send-from-template body: templateId, templateRoles[] with roleName/email/name/tabs, and status='sent'.",
        styles["Body"],
    )
)

story += section("7A. Composite Templates API")
story.append(
    p(
        "Project source: docusign-node-quickstart/app/lib/eSignature/examples/addDocToTemplate.js. This example uses compositeTemplates to create one envelope from a saved Docusign template plus an extra HTML document, then opens embedded signing with createRecipientView.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Question", "Answer"],
        [
            ["When to use it", "When one envelope must combine saved server templates, runtime recipients/tabs, and direct documents in one createEnvelope call."],
            ["Main API", "EnvelopesApi.createEnvelope(accountId, { envelopeDefinition })"],
            ["URL", "POST {basePath}/v2.1/accounts/{accountId}/envelopes"],
            ["Auth", "Authorization: Bearer {accessToken} header. The access token must include the signature scope."],
            ["Response", "Returns envelopeId. For embedded signing, app then calls createRecipientView using that envelopeId."],
            ["Exam clue", "If the question says combine server template plus inline recipient data plus extra documents, answer composite templates."],
        ],
        [1.35 * inch, 5.65 * inch],
        styles["Small"],
    )
)
story.append(p("Composite template parts:", styles["H3"]))
story.append(
    table(
        ["Part", "Where in body", "What it does"],
        [
            ["compositeTemplates[]", "EnvelopeDefinition root", "Array of composite template blocks. Each block contributes a saved template, inline data, a document, or a combination."],
            ["compositeTemplateId", "Each compositeTemplates[] item", "Local ID for that composite template block, such as '1' or '2'. It orders/identifies parts inside this request, not a saved Docusign template ID."],
            ["serverTemplates[]", "Inside a composite template", "References saved Docusign templates already stored in the account. This can be a template created in the Docusign UI or created earlier by API."],
            ["templateId", "serverTemplates[] item", "The real saved Docusign template ID."],
            ["inlineTemplates[]", "Inside a composite template", "Adds runtime data inside the API request: recipients, tabs, tab values, routing, or envelope settings. It can fill existing template roles and can also add extra recipients/tabs not already in the saved server template."],
            ["document", "Inside a composite template", "Adds a direct document to the envelope, such as HTML or PDF with documentBase64."],
            ["sequence", "serverTemplates[] and inlineTemplates[]", "Controls the order Docusign applies the saved template and inline runtime data."],
        ],
        [1.45 * inch, 2.2 * inch, 3.35 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Memory: server template = saved structure in Docusign. Inline template = runtime data from your API call. Inline data can fill fields in the saved template and can add extra recipients such as a CC or approver even when the saved server template has fewer recipients.",
        styles["Body"],
    )
)
story.append(p("Quickstart body shape:", styles["H3"]))
story.append(
    p(
        "POST https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes\n"
        "Authorization: Bearer {accessToken}\n"
        "Content-Type: application/json\n\n"
        "{\n"
        "  \"status\": \"sent\",\n"
        "  \"compositeTemplates\": [\n"
        "    {\n"
        "      \"compositeTemplateId\": \"1\",\n"
        "      \"serverTemplates\": [\n"
        "        { \"sequence\": \"1\", \"templateId\": \"{templateId}\" }\n"
        "      ],\n"
        "      \"inlineTemplates\": [\n"
        "        {\n"
        "          \"sequence\": \"2\",\n"
        "          \"recipients\": {\n"
        "            \"signers\": [\n"
        "              {\n"
        "                \"email\": \"signer@example.com\",\n"
        "                \"name\": \"Signer Name\",\n"
        "                \"roleName\": \"signer\",\n"
        "                \"recipientId\": \"1\",\n"
        "                \"clientUserId\": \"1000\"\n"
        "              }\n"
        "            ],\n"
        "            \"carbonCopies\": [\n"
        "              { \"email\": \"cc@example.com\", \"name\": \"CC Name\", \"roleName\": \"cc\", \"recipientId\": \"2\" }\n"
        "            ]\n"
        "          }\n"
        "        }\n"
        "      ]\n"
        "    },\n"
        "    {\n"
        "      \"compositeTemplateId\": \"2\",\n"
        "      \"inlineTemplates\": [\n"
        "        {\n"
        "          \"sequence\": \"1\",\n"
        "          \"recipients\": {\n"
        "            \"signers\": [\n"
        "              {\n"
        "                \"email\": \"signer@example.com\",\n"
        "                \"name\": \"Signer Name\",\n"
        "                \"recipientId\": \"1\",\n"
        "                \"tabs\": {\n"
        "                  \"signHereTabs\": [\n"
        "                    { \"anchorString\": \"**signature_1**\", \"anchorXOffset\": \"20\", \"anchorYOffset\": \"10\", \"anchorUnits\": \"pixels\" }\n"
        "                  ]\n"
        "                }\n"
        "              }\n"
        "            ]\n"
        "          }\n"
        "        }\n"
        "      ],\n"
        "      \"document\": {\n"
        "        \"documentBase64\": \"{base64HtmlOrPdf}\",\n"
        "        \"name\": \"Appendix 1--Sales order\",\n"
        "        \"fileExtension\": \"html\",\n"
        "        \"documentId\": \"1\"\n"
        "      }\n"
        "    }\n"
        "  ]\n"
        "}",
        styles["CodeBlock"],
    )
)
story.append(p("Important IDs and fields:", styles["H3"]))
story.append(
    table(
        ["ID / field", "Example", "What it identifies or controls"],
        [
            ["accountId", "URL path", "Docusign account where the envelope is created."],
            ["templateId", "{templateId}", "Saved Docusign server template used by serverTemplates."],
            ["compositeTemplateId", "'1', '2'", "Local block ID inside this createEnvelope request."],
            ["sequence", "'1', '2'", "Order of applying server template and inline template data."],
            ["recipientId", "'1', '2'", "Recipient inside the envelope. Tabs and recipient events use this ID."],
            ["roleName", "'signer', 'cc'", "Matches template placeholder roles to real recipients."],
            ["clientUserId", "'1000'", "Marks recipient as embedded/captive signing. This is the same embedded signing concept explained in section 6: the value in createEnvelope must match the value in createRecipientView."],
            ["documentId", "'1'", "Document inside the envelope; tabs can be tied to this document."],
            ["anchorString", "'**signature_1**'", "Text marker in the document where Docusign places a tab."],
            ["status", "'sent'", "Creates and sends the envelope immediately. Use 'created' to save as draft."],
        ],
        [1.35 * inch, 1.35 * inch, 4.3 * inch],
        styles["Small"],
    )
)
story.append(p("clientUserId cross-reference to embedded signing:", styles["H3"]))
story.append(
    table(
        ["Where", "Body example", "Why it matters"],
        [
            ["createEnvelope signer", "\"clientUserId\": \"1000\"", "Tells Docusign this recipient will sign inside your app, not only through a remote email link."],
            ["createRecipientView", "\"clientUserId\": \"1000\"", "Must match the envelope signer, along with email/userName, so Docusign knows which embedded signer view to generate."],
            ["If missing", "No clientUserId on signer", "Docusign treats the signer as remote/email signing; your app normally cannot create the embedded recipient view for that signer."],
        ],
        [1.35 * inch, 2.15 * inch, 3.5 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Memory from section 6: clientUserId is the bridge between the signer object in createEnvelope and the signing URL returned by createRecipientView. In composite templates, it works the same way even though the signer is inside inlineTemplates[].",
        styles["Body"],
    )
)
story.append(p("Process sequence in the quickstart:", styles["H3"]))
story.append(
    table(
        ["Step", "App action", "Docusign API / result"],
        [
            ["1", "App has accessToken, accountId, basePath, templateId, signer data, CC data, and extra document data.", "No Docusign call yet."],
            ["2", "Build EnvelopeDefinition with status='sent' and compositeTemplates[].", "Body combines saved template, inline recipients, tabs, and direct document."],
            ["3", "Call createEnvelope.", "POST /v2.1/accounts/{accountId}/envelopes returns envelopeId."],
            ["4", "For embedded signing, build RecipientViewRequest with returnUrl, authenticationMethod, email, userName, clientUserId, optional pingUrl.", "The recipient info must match the embedded signer from the envelope."],
            ["5", "Call createRecipientView.", "POST /v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient returns a signing URL."],
            ["6", "Browser redirects signer to the returned URL.", "Signer completes embedded signing, then Docusign returns to returnUrl."],
        ],
        [0.55 * inch, 3.3 * inch, 3.15 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Composite templates are not a separate product API. They are a request-body model used with the normal eSignature createEnvelope endpoint. The key difference from simple template sending is that simple template sending uses templateId plus templateRoles, while compositeTemplates can combine serverTemplates, inlineTemplates, and direct documents in one envelope.",
        styles["Body"],
    )
)

story += section("7B. High-Priority eSignature APIs from the Project")
story.append(
    p(
        "These examples are in docusign-node-quickstart/app/lib/eSignature/examples. They are common exam areas because they happen after createEnvelope or control how the envelope is viewed, routed, paused, restored, or queried.",
        styles["Body"],
    )
)
story.append(p("Envelope read APIs:", styles["H3"]))
story.append(
    table(
        ["Need", "SDK function", "URL shape", "Important IDs", "Returns / purpose"],
        [
            ["Envelope status/info", "envelopesApi.getEnvelope", "GET /v2.1/accounts/{accountId}/envelopes/{envelopeId}", "accountId, envelopeId", "Status, subject, sender, dates, envelope metadata."],
            ["Envelope recipients", "envelopesApi.listRecipients", "GET /v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients", "accountId, envelopeId, recipientId", "Signers, CCs, routing order, recipient status."],
            ["Envelope documents", "envelopesApi.listDocuments", "GET /v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents", "accountId, envelopeId, documentId", "Document list in the envelope."],
            ["Download document", "envelopesApi.getDocument", "GET /v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}", "accountId, envelopeId, documentId", "PDF/ZIP/document bytes."],
        ],
        [1.15 * inch, 1.45 * inch, 2.05 * inch, 1.15 * inch, 1.35 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: createEnvelope returns envelopeId. Later status, recipients, document list, download, tab data, custom field, and lifecycle calls use that envelopeId.", styles["Body"]))
story.append(p("Tabs, field values, and custom fields:", styles["H3"]))
story.append(
    table(
        ["Need", "SDK/API", "URL or body", "Important fields"],
        [
            ["Read filled tab/form data", "envelopesApi.getFormData", "GET /v2.1/accounts/{accountId}/envelopes/{envelopeId}/form_data", "accountId, envelopeId, tabLabel, field values."],
            ["Set tabs on new envelope", "EnvelopesApi.createEnvelope", "Tabs live under recipients.signers[].tabs.", "recipientId, documentId, tabLabel, value, locked, anchorString."],
            ["Set template tab values", "createEnvelope from template", "EnvelopeDefinition.templateRoles[].tabs", "templateId, roleName, tabLabel, value."],
            ["Add a new tab while using template", "templateRoles[].tabs.textTabs[]", "Set documentId/pageNumber/xPosition/yPosition or anchor placement.", "documentId, pageNumber, xPosition, yPosition, tabLabel."],
            ["Read envelope custom fields", "envelopesApi.listCustomFields", "GET /v2.1/accounts/{accountId}/envelopes/{envelopeId}/custom_fields", "accountId, envelopeId, custom field name/value."],
        ],
        [1.35 * inch, 1.65 * inch, 2.35 * inch, 1.75 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["Thing", "Meaning", "Exam distinction"],
        [
            ["tabLabel", "Field name/key your app uses to set or read a tab.", "Used for text/list/checkbox/radio/numerical tab values."],
            ["tabId", "Tab identifier used by Docusign/API.", "Do not confuse with recipientId or documentId."],
            ["anchorString", "Text marker in the document where Docusign places the tab.", "Anchor placement finds text such as /sn1/ or **signature_1**."],
            ["locked=true", "Signer cannot edit the value.", "Useful for prefilled values."],
            ["locked=false", "Signer can edit the value.", "Useful for signer-correctable fields."],
            ["customFields", "Envelope metadata, not normal visible document tabs.", "Tabs are document fields; custom fields are envelope metadata/search/reporting data."],
        ],
        [1.2 * inch, 3.05 * inch, 2.85 * inch],
        styles["Small"],
    )
)
story.append(p("Sender views versus recipient view:", styles["H3"]))
story.append(
    table(
        ["View", "SDK function", "URL shape", "For whom", "Purpose"],
        [
            ["Recipient view", "createRecipientView", "POST /envelopes/{envelopeId}/views/recipient", "Signer", "Embedded signing URL. Requires signer email/userName/clientUserId to match envelope signer."],
            ["Sender view", "createSenderView", "POST /envelopes/{envelopeId}/views/sender", "Sender", "Lets sender edit/tag/send a draft envelope inside your app."],
            ["Console view", "createConsoleView", "POST /v2.1/accounts/{accountId}/views/console", "Sender/admin", "Opens Docusign sending console / NDSE. May start at an envelope if envelopeId is supplied."],
            ["Focused View", "createRecipientView with frame settings", "POST /envelopes/{envelopeId}/views/recipient", "Signer", "Modern embedded signing with frameAncestors and messageOrigins controls."],
        ],
        [1.0 * inch, 1.55 * inch, 1.85 * inch, 0.85 * inch, 1.85 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: createRecipientView is for the signer. createSenderView and createConsoleView are for the sender/sending UI.", styles["Body"]))
story.append(p("Delivery, routing, and lifecycle controls:", styles["H3"]))
story.append(
    table(
        ["Feature", "Body/API idea", "Meaning", "Exam trap"],
        [
            ["Routing order", "recipient.routingOrder", "Controls who receives/signs first. Same routingOrder means parallel routing.", "Routing is timing/order, not identity proof."],
            ["Scheduled sending", "env.workflow.scheduledSending.rules[].resumeDate", "Envelope is created now but sent later at a scheduled date/time.", "Different from delayed routing between recipients."],
            ["Delayed routing", "workflowSteps[].delayedRouting.rules[].delay", "Delay before routing to the next recipient/routing order.", "Delay happens inside the recipient routing workflow."],
            ["Pause workflow", "workflowSteps[].action='pause_before'", "Envelope pauses before a later routing order until it is resumed.", "Pause does not void/cancel the envelope."],
            ["Multiple delivery", "deliveryMethod plus additionalNotifications", "Send the signing notification by email plus another channel such as SMS.", "Delivery channel is not signer authentication."],
            ["Delete/restore", "FoldersApi.moveEnvelopes", "Moves envelope between folders such as inbox and recycle bin.", "Delete/restore is folder movement; void cancels active signing."],
            ["Void", "Envelope update/status voided", "Cancels active envelope so it cannot be completed.", "Void is not the same as deleting from a folder."],
        ],
        [1.2 * inch, 2.15 * inch, 2.1 * inch, 1.65 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: delivery method is how the signer gets the link. Authentication is how the signer proves identity. Routing is who receives the envelope when.", styles["Body"]))
story.append(p("Document generation and specialized signing notes:", styles["H3"]))
story.append(
    table(
        ["Topic", "Process / API idea", "Exam distinction"],
        [
            ["Document generation", "Use/create DocGen-enabled template, create draft envelope, get DocGen form fields, update values, then send.", "DocGen fields generate document content; tabs are signing/document fields."],
            ["CFR embedded signing", "Embedded signing pattern for regulated/life-sciences style requirements.", "Still uses embedded signing concepts such as clientUserId and recipient view."],
            ["In-person signing", "A host/sender manages signing for a signer in the same physical session.", "Different from remote email signing and normal embedded signing."],
        ],
        [1.35 * inch, 3.3 * inch, 2.45 * inch],
        styles["Small"],
    )
)

story += section("8. Authentication, Identity, and Delivery Examples")
story.append(
    table(
        ["Method", "API/body setup", "How/when signer gets it", "Signer experience", "Remote or embedded"],
        [
            [
                "Access code",
                "EnvelopesApi.createEnvelope. Add recipient accessCode.",
                "Usually not in the Docusign email. Your app/company gives the code separately by phone, SMS, portal, or internal process.",
                "Signer opens the envelope and Docusign asks for the access code before showing signing.",
                "Both. Works with remote email signing and embedded signing.",
            ],
            [
                "Phone/SMS authentication",
                "createEnvelope with recipient phone/SMS authentication fields.",
                "Docusign sends SMS/call during the signing ceremony after signer opens the link/view.",
                "Signer receives a code/call on their phone and must verify before signing.",
                "Both. It protects the ceremony regardless of how the signer entered.",
            ],
            [
                "ID Verification",
                "AccountsApi.getAccountIdentityVerification to choose workflow, then createEnvelope with recipient IDV settings.",
                "Signer starts from email link or embedded view, then Docusign launches the IDV workflow.",
                "Signer follows identity steps such as document scan, selfie, or provider workflow depending account configuration.",
                "Both. Availability depends on account and region.",
            ],
            [
                "KBA",
                "createEnvelope with knowledge-based authentication settings and signer identity data.",
                "Signer opens signing; Docusign/identity provider asks questions during signing. No Docusign account is required.",
                "Provider checks answers against third-party/public-record or credit-header style data. Signer must be matchable in provider records.",
                "Both where available. Region/provider dependent.",
            ],
            [
                "SMS delivery",
                "createEnvelope with recipient delivery method/phone settings.",
                "Docusign sends the signing link by SMS instead of or in addition to email.",
                "Signer opens signing link from SMS.",
                "Mostly remote. Embedded usually uses createRecipientView, not Docusign delivery.",
            ],
            [
                "Multiple delivery",
                "createEnvelope with multiple delivery channel settings.",
                "Docusign may send email and SMS for the same envelope/recipient according to configuration.",
                "Signer can enter from one of the delivery channels.",
                "Mostly remote. It is delivery, not signer identity proof.",
            ],
            [
                "In-person signer",
                "createEnvelope with recipients.inPersonSigners.",
                "Host starts/controls the signing session while the signer is physically present.",
                "Signer signs with host present instead of receiving a normal independent email link.",
                "Separate recipient flow; not normal remote or normal embedded.",
            ],
        ],
        [0.95 * inch, 1.35 * inch, 1.75 * inch, 1.85 * inch, 1.15 * inch],
        styles["Small"],
    )
)
story.append(Spacer(1, 6))
story.append(
    table(
        ["Concept", "Exam rule"],
        [
            [
                "App OAuth authentication",
                "Access token proves your backend can call Docusign APIs. It does not prove the signer identity.",
            ],
            [
                "Recipient authentication",
                "Access code, SMS auth, IDV, and KBA protect the signing ceremony before the signer can sign.",
            ],
            [
                "Delivery",
                "Email/SMS/multiple delivery explains how the signer receives the link. It is different from identity proof.",
            ],
            [
                "KBA signer account",
                "Signer does not need a Docusign account, but must match the third-party KBA provider's identity records.",
            ],
            [
                "Remote vs embedded",
                "Authentication methods can work for both. Delivery methods are mostly remote because embedded signing uses createRecipientView.",
            ],
        ],
        [1.6 * inch, 5.45 * inch],
        styles["Small"],
    )
)

story.append(PageBreak())
story += section("9. Bulk Send, Payments, Brands, Permissions, Shared Access")
story.append(
    table(
        ["Area", "What it does", "API / URL shape", "Important IDs / body"],
        [
            ["Bulk send list", "Stores many recipient rows for one bulk send.", "BulkEnvelopesApi.createBulkSendList. POST {basePath}/v2.1/accounts/{accountId}/bulk_send_lists", "Returns listId / bulkSendListId. Body has name and bulkCopies[]. Each bulkCopies row has recipients with roleName, name, email, and optional tab values."],
            ["Start bulk send", "Starts the send job that uses the saved list.", "BulkEnvelopesApi.createBulkSendRequest. POST bulk send request endpoint for the account/list/envelope, depending SDK version.", "Returns batchId. Input connects accountId, listId, and the envelope/template setup."],
            ["Check bulk status", "Checks whether the bulk send job is processing, complete, or failed.", "BulkEnvelopesApi.getBulkSendBatchStatus. GET bulk send batch status endpoint.", "Uses batchId. Batch status is job-level status, not the same as each envelope's signing status."],
            ["Template/envelope source", "Defines what every copy looks like.", "TemplatesApi.createTemplate/listTemplates, or EnvelopesApi.createEnvelope using a template.", "templateId is the reusable design. envelopeId can be the draft/source envelope used for the batch. recipientId usually remains '1' inside each generated envelope."],
            ["CSV source", "CSV is read by your app or by the Docusign portal, then converted into recipient rows.", "API path: CSV -> your app parses it -> bulkCopies[] JSON -> createBulkSendList. Portal path: CSV -> Docusign Bulk Send import.", "CSV columns map to roleName, name, email, and tabLabel values. Docusign API does not directly parse a local CSV file from your computer."],
            ["Payments", "Collects money during signing.", "EnvelopesApi.createEnvelope with payment tabs, formula tabs, and paymentDetails.", "Important IDs: paymentGatewayAccountId, envelopeId, tabId. Payment is envelope configuration."],
            ["Branding", "Changes signer/email look, logo, colors, and recipient experience.", "AccountsApi.createBrand, listBrands; apply brandId on envelope/template.", "Important IDs: brandId, accountId, envelopeId/templateId. Branding does not authenticate API calls."],
            ["Permissions", "Controls what Docusign account users/admins are allowed to do.", "Permission profile APIs and GroupsApi assignment.", "Important IDs: permissionProfileId, groupId, userId, accountId. This is account administration, not signer identity."],
            ["Shared access", "Lets one user access another user's envelopes/mailbox by delegation.", "AccountsApi.getAgentUserAuthorizations, createUserAuthorization; EnvelopesApi.listStatusChanges.", "Important IDs: userId, agentUserId, accountId. This is delegated account access, not OAuth consent."],
            ["Delete/restore", "Moves envelopes between folders such as inbox and recycle bin.", "FoldersApi.moveEnvelopes, FoldersApi.list.", "Important IDs: folderId, envelopeId, accountId. Delete/restore is folder movement; voiding cancels an active envelope."],
        ],
        [1.0 * inch, 1.35 * inch, 2.25 * inch, 2.7 * inch],
        styles["Small"],
    )
)
story.append(p("Bulk send ID memory:", styles["H3"]))
story.append(
    table(
        ["ID", "Level", "Meaning"],
        [
            ["accountId", "Account", "The Docusign account used in every API URL."],
            ["templateId", "Template", "The reusable document/design and recipient roles."],
            ["listId / bulkSendListId", "Recipient list", "The saved list of 200 rows, for example. This is where many emails fit."],
            ["batchId", "Bulk job", "The running send process created when the list is launched."],
            ["envelopeId", "Envelope", "Each actual signing transaction created from the bulk list."],
            ["recipientId", "Recipient inside one envelope", "Signer number/role inside an envelope. It usually stays '1' for each generated envelope, not person 78 in the batch."],
            ["roleName", "Template role", "Matches CSV/list rows to the template role, such as Signer."],
            ["tabLabel", "Field name", "Maps custom CSV/list values into Docusign tabs."],
        ],
        [1.45 * inch, 1.5 * inch, 4.35 * inch],
        styles["Small"],
    )
)
story.append(p("Bulk send sequence:", styles["H3"]))
story.append(
    bullets(
        [
            "1. Create or reuse templateId. This is the document/design.",
            "2. Prepare CSV or database rows with signer name, email, roleName, and any custom field values.",
            "3. API option: your app parses CSV and builds bulkCopies[]. Portal option: upload CSV in Docusign Bulk Send.",
            "4. Call createBulkSendList and receive listId.",
            "5. Start bulk send using the listId and the envelope/template setup; Docusign returns batchId.",
            "6. Docusign creates separate envelopeIds for the rows in the list.",
            "7. Use batchId for job progress; use envelopeId for a specific signing transaction.",
        ],
        styles["Body"],
    )
)
story.append(p("Minimal bulk list body shape:", styles["H3"]))
story.append(
    p(
        "{\n"
        '  "name": "Contract bulk list",\n'
        '  "bulkCopies": [\n'
        '    { "recipients": [ { "roleName": "Signer", "name": "John Smith", "email": "john@example.com" } ] },\n'
        '    { "recipients": [ { "roleName": "Signer", "name": "Mary Jones", "email": "mary@example.com" } ] }\n'
        "  ]\n"
        "}",
        styles["CodeBlock"],
    )
)
story.append(p("Exam distinction: listId is the saved recipient list; batchId is the send job; envelopeId is the actual signing transaction; recipientId is the signer position inside each envelope.", styles["Body"]))
story.append(p("Branding, permission profile, and shared access API steps:", styles["H3"]))
story.append(
    table(
        ["Feature", "Step-by-step API flow", "Important body / ID details"],
        [
            [
                "Branding",
                "1. Get access token with account/admin rights. 2. Common path: create brand and upload logo once in the Docusign portal. 3. API lists brands with GET {basePath}/v2.1/accounts/{accountId}/brands. 4. Pick brandId. 5. Put brandId in createEnvelope or template body. Full API path can create/update brand settings when enabled for the account.",
                "brandId controls signer email/signing-page look. Example envelope body fields: brandId, templateId, templateRoles, status='sent'. Branding is appearance, not signer authentication.",
            ],
            [
                "Permission profile",
                "1. Get access token for an account admin. 2. List profiles with GET {basePath}/v2.1/accounts/{accountId}/permission_profiles. 3. Pick permissionProfileId. 4. Create or update an internal Docusign user with that profile. 5. Optionally use groups for assignment patterns.",
                "permissionProfileId defines allowed actions for internal users: send envelopes, manage templates, view reports, manage account settings, etc. It is not for external signers.",
            ],
            [
                "Shared access",
                "1. Get access token with shared access/admin rights. 2. Choose the envelope owner userId. 3. Choose the delegate/agent userId. 4. Create user authorization/shared access. 5. Delegate can view/manage allowed envelopes for the owner.",
                "userId is the owner; agentUserId is the delegate/assistant. Shared access is delegated envelope/mailbox access, not OAuth consent and not recipient authentication.",
            ],
        ],
        [1.15 * inch, 3.95 * inch, 2.2 * inch],
        styles["Small"],
    )
)
story.append(p("Admin memory: branding = look and feel; permission profile = what an internal Docusign user can do; shared access = one internal user accessing another user's envelopes.", styles["Body"]))

story += section("10. Connect Webhook Validation")
story.append(p("This quickstart includes HMAC validation only, not full Connect configuration creation.", styles["Body"]))
story.append(p("const hmac = crypto.createHmac('sha256', secret); hmac.write(payload); computed = hmac.read().toString('base64'); compare with crypto.timingSafeEqual(...)", styles["CodeBlock"]))
story.append(
    bullets(
        [
            "Connect pushes event messages to your listener so you do not poll envelope status repeatedly.",
            "HMAC validates that the payload was signed with the configured secret.",
            "Listeners must be idempotent because retry and duplicate delivery are normal webhook realities.",
            "JSON SIM appears in workflow/modern event contexts; legacy XML is a different payload style.",
        ],
        styles["Body"],
    )
)
story.append(p("Project route and local code:", styles["H3"]))
story.append(
    table(
        ["Project item", "Where in project", "What it does", "Exam meaning"],
        [
            ["/cneg001", "Connect launcher route", "Runs the Connect HMAC validation example.", "This is not a live webhook listener; it is a learning page for computing/validating HMAC."],
            ["validateWebhookMessage.js", "lib/connect/examples", "computeHash(secret, payload) uses crypto.createHmac('sha256', secret), writes raw payload, base64 encodes result.", "Shows how Docusign webhook authenticity is checked."],
            ["eg001ValidateWebhookMessage.js", "lib/connect/controllers", "Reads secret and payload from the form and displays computed hash.", "The quickstart validates the concept; production apps validate incoming POST requests automatically."],
        ],
        [1.25 * inch, 1.55 * inch, 2.4 * inch, 2.0 * inch],
        styles["Small"],
    )
)
story.append(p("Integration and Security Settings:", styles["H3"]))
story.append(
    table(
        ["Setting", "What it does", "Business situation"],
        [
            ["Include HMAC Signature", "Docusign signs the webhook payload with a shared secret. Your app recomputes HMAC from the raw body and compares.", "Best default for most webhook integrations that need to prove payload authenticity and integrity."],
            ["Manage Keys", "Manage/rotate the HMAC secret keys used for signature validation.", "Use when replacing old secrets, rotating keys, or responding to a suspected key leak."],
            ["Include Account Level OAuth", "Uses one OAuth connection across the account for Connect delivery authentication.", "Large company wants centralized auth for many Connect configurations."],
            ["Include Configuration Level OAuth", "Uses a separate OAuth connection for this specific Connect configuration.", "Different webhook endpoints need different auth, such as HR and Finance systems."],
            ["Include Basic Authentication Header", "Docusign sends a Basic Auth username/password header to your listener.", "Simple endpoint protection when OAuth/mTLS is not needed."],
            ["Enable Mutual TLS", "Docusign and your server use certificates during the HTTPS connection.", "High-security enterprise, banking, healthcare, or regulated integrations needing certificate-based trust."],
        ],
        [1.55 * inch, 3.0 * inch, 2.65 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["Security layer", "Protects / proves", "Exam memory"],
        [
            ["HTTPS", "Encrypts transport between Docusign and your listener.", "Required for URL to Publish."],
            ["HMAC", "Proves the message payload was not changed and was signed with the shared secret.", "HMAC checks the message."],
            ["OAuth / Basic Auth / mTLS", "Helps authenticate the caller or connection to your webhook endpoint.", "OAuth/Basic/mTLS check the caller/connection."],
        ],
        [1.45 * inch, 3.35 * inch, 2.4 * inch],
        styles["Small"],
    )
)
story.append(p("Security memory: most normal exam/API answers mention HMAC for webhook authenticity. Use OAuth, Basic Auth, or Mutual TLS when your receiving endpoint also requires caller/connection authentication.", styles["Body"]))
story.append(p("Best Connect security choice:", styles["H3"]))
story.append(
    table(
        ["Business situation", "Recommended security", "Why"],
        [
            ["Normal webhook/API app", "HTTPS + HMAC Signature", "HTTPS encrypts transport; HMAC verifies payload authenticity and integrity."],
            ["Enterprise centralized auth", "HTTPS + HMAC + Account Level OAuth", "Adds centralized caller/auth management across account Connect configurations."],
            ["Different systems per config", "HTTPS + HMAC + Configuration Level OAuth", "Each Connect configuration can authenticate to a different receiving system."],
            ["High-security regulated app", "HTTPS + HMAC + Mutual TLS", "mTLS adds certificate-based connection trust in addition to payload validation."],
            ["Simple internal endpoint", "HTTPS + Basic Auth + HMAC", "Basic Auth protects the endpoint, while HMAC verifies the message payload."],
        ],
        [1.8 * inch, 2.15 * inch, 3.25 * inch],
        styles["Small"],
    )
)
story.append(p("Exam memory: HMAC is the key webhook authenticity feature. HTTPS is required for transport encryption. For highest security, combine HMAC with Mutual TLS.", styles["Body"]))
story.append(p("Two ways to configure Connect:", styles["H3"]))
story.append(
    table(
        ["Type", "Where configured", "URL / API shape", "When used"],
        [
            ["Account-level Connect", "Docusign Admin UI or Connect configuration API.", "GET/POST {basePath}/v2.1/accounts/{accountId}/connect", "Use when many envelopes in the account should send events to the same listener."],
            ["Envelope-level Connect", "Inside the create-envelope request body as eventNotification.", "POST {basePath}/v2.1/accounts/{accountId}/envelopes with eventNotification", "Use when only this one envelope needs a webhook or needs envelope-specific listener settings."],
            ["Webhook listener", "Your app/server endpoint.", "POST https://www.abc.com/docusign/connect", "Docusign calls this URL. This is your app URL, not a Docusign API URL."],
        ],
        [1.35 * inch, 1.85 * inch, 2.3 * inch, 1.7 * inch],
        styles["Small"],
    )
)
story.append(p("Docusign Admin Connect fields:", styles["H3"]))
story.append(
    table(
        ["Admin field", "Meaning", "Example", "Exam memory"],
        [
            ["URL to Publish", "The webhook listener endpoint in your app where Docusign will POST Connect events.", "https://www.abc.com/docusign/connect", "This is your app URL, not a Docusign API URL."],
            ["HTTPS required", "The listener URL must use encrypted HTTPS and be reachable by Docusign.", "Valid: https://www.abc.com/docusign/connect. Not valid for production: http://www.abc.com/docusign/connect.", "Webhook payloads can include envelope/recipient data and sometimes documents, so transport must be secure."],
            ["What Docusign sends", "HTTP POST event messages to the URL to Publish.", "POST https://www.abc.com/docusign/connect", "Your listener receives the event, validates HMAC, processes idempotently, and returns success."],
        ],
        [1.25 * inch, 2.2 * inch, 2.25 * inch, 1.5 * inch],
        styles["Small"],
    )
)
story.append(p("Custom vs Custom Recipient in Add Account Configuration:", styles["H3"]))
story.append(
    table(
        ["UI option", "Tracks", "API/body equivalent", "Business question it answers"],
        [
            ["Custom", "Normal account Connect events. It can include Envelope Events and Recipient Events for envelopes in the account.", "envelopeEvents plus recipientEvents, for example Envelope Completed and Recipient Delivered.", "What happened to this envelope, and what happened to each recipient inside that envelope?"],
            ["Custom Recipient", "Special Recipient Connect setup focused on recipient-level tracking with organization/domain controls.", "Recipient Connect configuration, not just the normal recipientEvents list in Custom Connect.", "Do we need recipient-level event tracking under stricter organization/domain governance?"],
        ],
        [1.25 * inch, 1.8 * inch, 2.25 * inch, 1.9 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: In a Custom Connect configuration, the UI still shows Recipient Events because every envelope has recipients. You do not need Custom Recipient just to receive normal signer events such as Recipient Sent, Delivered, Completed, Declined, or Authentication Failure. Custom Recipient is a separate Recipient Connect use case with extra organization/domain requirements.", styles["Body"]))
story.append(p("Why Recipient Connect can require Organization and validated domain:", styles["H3"]))
story.append(
    table(
        ["Requirement", "What it means", "Why it matters for Custom Recipient / Recipient Connect"],
        [
            ["Organization", "A central Docusign admin/security boundary above accounts.", "Recipient Connect needs a trusted organization context for recipient-level event configuration."],
            ["Claimed domain", "Your company proves it owns a domain such as abc.com.", "Shows Docusign that the organization controls the email/domain space involved."],
            ["Validated domain", "Docusign confirms the claimed domain is valid and controlled by the organization.", "Adds stronger identity trust for recipient-level events."],
            ["Domain Name field", "The domain you enter when creating/validating the organization domain.", "Example: abc.com, not a full URL like https://www.abc.com."],
        ],
        [1.25 * inch, 2.15 * inch, 3.8 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: normal Custom Connect focuses on envelope events inside the account. Custom Recipient / Recipient Connect focuses on signer-level events, so Docusign can require Organization plus claimed and validated domain before enabling it.", styles["Body"]))
story.append(p("Envelope-level Connect request shape:", styles["H3"]))
story.append(p("POST https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes\nAuthorization: Bearer {access_token}\nContent-Type: application/json\n\n{\n  \"emailSubject\": \"Please sign\",\n  \"documents\": [ ... ],\n  \"recipients\": { ... },\n  \"status\": \"sent\",\n  \"eventNotification\": {\n    \"url\": \"https://www.abc.com/docusign/connect\",\n    \"requireAcknowledgment\": \"true\",\n    \"includeDocuments\": \"false\",\n    \"includeCertificateOfCompletion\": \"false\",\n    \"envelopeEvents\": [\n      { \"envelopeEventStatusCode\": \"sent\" },\n      { \"envelopeEventStatusCode\": \"completed\" },\n      { \"envelopeEventStatusCode\": \"declined\" },\n      { \"envelopeEventStatusCode\": \"voided\" }\n    ],\n    \"recipientEvents\": [\n      { \"recipientEventStatusCode\": \"Sent\" },\n      { \"recipientEventStatusCode\": \"Delivered\" },\n      { \"recipientEventStatusCode\": \"Completed\" }\n    ],\n    \"eventData\": { \"version\": \"restv2.1\", \"format\": \"json\" }\n  }\n}", styles["CodeBlock"]))
story.append(p("Event Settings data format: REST v2.1 vs Legacy:", styles["H3"]))
story.append(
    table(
        ["Format", "Meaning", "Payload style", "Exam memory"],
        [
            ["REST v2.1", "Modern Connect payload aligned with eSignature REST API v2.1.", "JSON-style event data with REST API naming.", "Use this for new integrations. It changes the body shape, not the business event."],
            ["Legacy", "Older Connect payload format.", "Older XML/SOAP-style structure.", "Use only for older integrations that already parse the legacy format."],
        ],
        [1.15 * inch, 2.2 * inch, 1.9 * inch, 1.95 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: the event can still be the same, for example envelope completed. REST v2.1 vs Legacy controls how the webhook body looks and therefore how your listener parses it. REST v2.1 = modern JSON; Legacy = old XML-style Connect.", styles["Body"]))
story.append(p("Event Message Delivery Mode: SIM vs Aggregate:", styles["H3"]))
story.append(
    table(
        ["Mode", "Meaning", "Payload your listener receives", "When to choose"],
        [
            ["Send Individual Messages (SIM)", "Docusign sends one webhook notification for each event.", "One event message in the webhook body.", "Use when your app needs near real-time updates and simpler event processing."],
            ["Aggregate", "Docusign groups event messages and sends them periodically.", "A grouped/batch payload containing multiple event messages.", "Use when your app wants fewer webhook calls and can process events in batches."],
        ],
        [1.65 * inch, 2.0 * inch, 1.85 * inch, 1.7 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["Why it cannot be changed after save", "Exam memory"],
        [
            ["The delivery mode changes delivery timing and webhook body shape. SIM listener code expects one event; Aggregate listener code expects a batch/list of events.", "Choose carefully before saving because your parser, retry handling, and business timing depend on the mode."],
        ],
        [3.8 * inch, 3.4 * inch],
        styles["Small"],
    )
)
story.append(p("Payload memory: SIM payload = one event. Aggregate payload = multiple events together. This is separate from REST v2.1 vs Legacy: format controls JSON/XML style; delivery mode controls single event vs grouped events.", styles["Body"]))
story.append(p("Simple payload difference: SIM body is like one event object with event and envelopeId. Aggregate body is like an events array/list containing multiple event objects. Your parser must match the mode.", styles["Body"]))
story.append(p("Webhook receive and validation flow:", styles["H3"]))
story.append(
    table(
        ["Step", "What happens", "Important detail"],
        [
            ["1. Event happens", "Envelope or recipient status changes, for example completed.", "Common envelope statuses: sent, delivered, completed, declined, voided."],
            ["2. Docusign posts", "Docusign sends HTTP POST to your listener URL.", "Payload includes Docusign identifiers and event/status data."],
            ["3. Keep raw body", "Your app keeps the exact raw payload bytes/string.", "Do not compute HMAC from reserialized JSON; whitespace/order changes can break the hash."],
            ["4. Compute HMAC", "HMAC-SHA256(rawPayload, connectSecret), then base64 encode.", "Project code uses crypto.createHmac('sha256', secret)."],
            ["5. Compare signature", "Compare computed hash with Docusign signature header using timing-safe comparison.", "Common header name: X-DocuSign-Signature-1."],
            ["6. Process idempotently", "If valid, update your local record, then return success.", "Duplicate/retry delivery can happen, so use envelopeId/event/time/status as a de-dup key."],
        ],
        [0.75 * inch, 3.0 * inch, 3.45 * inch],
        styles["Small"],
    )
)
story.append(p("Important IDs and fields in Connect:", styles["H3"]))
story.append(
    table(
        ["ID / field", "Meaning", "Used for"],
        [
            ["accountId", "Docusign account that owns the envelope/event.", "Build API paths and route event to the right tenant/account."],
            ["envelopeId", "Envelope that changed status.", "Primary key to update your local agreement/order status."],
            ["recipientId", "Recipient inside the envelope.", "Track which signer viewed/signed/declined."],
            ["connectId / configurationId", "Account-level Connect configuration identifier when using Connect config APIs.", "Manage one configured webhook destination."],
            ["listener URL", "Your public HTTPS endpoint.", "Where Docusign sends webhook POSTs."],
            ["HMAC secret", "Shared secret configured for Connect.", "Used to validate webhook authenticity."],
        ],
        [1.4 * inch, 2.75 * inch, 3.05 * inch],
        styles["Small"],
    )
)
story.append(p("Account Configuration screen summary:", styles["H3"]))
story.append(
    table(
        ["Area on screen", "What it controls", "Exam memory"],
        [
            ["Listener Settings", "Status, name, URL to Publish, logging, pause configuration.", "Where Docusign sends events and whether delivery is active."],
            ["Event Settings", "Data format and delivery mode.", "Format controls JSON/XML shape; delivery mode controls one event vs batch."],
            ["Envelope and Recipients", "Envelope Events and Recipient Events.", "Envelope = whole agreement; Recipient = one signer."],
            ["Include Data", "Custom fields, documents, attachments, folders, PowerForm, prefill tabs, document fields, templates, delegations, recipients, payment tabs, tabs.", "Adds extra objects to the payload. Include only what your app needs."],
            ["Other product event groups", "Template, Click, SMS Delivery, Maestro, Identity Verification, Extension Apps, Notary, Agreement Manager.", "Account-level Connect can listen to more than eSignature envelope events."],
        ],
        [1.55 * inch, 3.15 * inch, 2.5 * inch],
        styles["Small"],
    )
)
story.append(p("JSON payload sample fields:", styles["H3"]))
story.append(
    table(
        ["Payload field", "Meaning", "Exam use"],
        [
            ["event", "The event name, for example recipient-sent.", "Tells what happened."],
            ["uri", "REST API path for the related account/envelope.", "Useful for follow-up API lookup."],
            ["retryCount", "How many times Docusign retried this delivery.", "Explains duplicate/retry behavior."],
            ["configurationId", "The Connect configuration that sent the message.", "Useful when multiple Connect configs exist."],
            ["apiVersion", "API version used in the event payload, for example v2.1.", "Confirms REST payload version."],
            ["data.accountId", "Account where the event happened.", "Routes event to account/tenant."],
            ["data.envelopeId", "Envelope involved.", "Main ID to update local agreement status."],
            ["data.recipientId", "Recipient involved, when it is a recipient event.", "Track specific signer progress."],
            ["envelopeSummary", "Envelope details such as status, subject, sender, recipients, and documents if included.", "Payload detail depends on Include Data choices."],
        ],
        [1.6 * inch, 3.15 * inch, 2.45 * inch],
        styles["Small"],
    )
)
story.append(p("Full webhook process for exam:", styles["H3"]))
story.append(
    table(
        ["Order", "Process step", "App vs Docusign side", "What to remember"],
        [
            ["1", "Your app creates/sends envelope.", "App calls Docusign API.", "Create envelope is a Docusign API call using Authorization: Bearer {access_token}."],
            ["2", "Connect is configured.", "Docusign account config or envelope eventNotification.", "Account-level applies broadly; envelope-level applies only to that envelope."],
            ["3", "Signer action changes status.", "Docusign signing system.", "Examples: signer views, completes, declines; envelope completes or voids."],
            ["4", "Docusign sends webhook POST.", "Docusign calls your app URL.", "Listener URL is your app URL, for example POST https://www.abc.com/docusign/connect."],
            ["5", "Your app validates HMAC.", "App server.", "Use raw payload plus Connect secret; compare against Docusign signature header."],
            ["6", "Your app updates local data.", "App database/business system.", "Use envelopeId as main business correlation key."],
            ["7", "Your app returns success.", "App HTTP response back to Docusign.", "If Docusign does not receive success and acknowledgment is required, retries may happen."],
        ],
        [0.55 * inch, 1.75 * inch, 2.15 * inch, 2.75 * inch],
        styles["Small"],
    )
)
story.append(p("Connect exam Q/A:", styles["H3"]))
story.append(
    table(
        ["Question", "Exam answer"],
        [
            ["Why use Connect?", "To receive push status updates instead of polling Docusign repeatedly."],
            ["Is the webhook listener URL a Docusign URL?", "No. It is your app/server URL that Docusign calls."],
            ["Is create-envelope URL a Docusign URL?", "Yes. POST {basePath}/v2.1/accounts/{accountId}/envelopes."],
            ["What is the main business ID?", "envelopeId. Store it when creating/sending the envelope and use it when webhook events arrive."],
            ["What proves the webhook is authentic?", "HMAC signature validation using the raw payload and configured Connect secret."],
            ["Why raw body?", "Parsed/reformatted JSON can change bytes, causing HMAC mismatch."],
            ["Why idempotent listener?", "Connect events can be retried or duplicated, so processing the same event twice must not break the business record."],
            ["Should documents be included?", "Only when required. Documents make webhook payloads large and sensitive."],
        ],
        [2.15 * inch, 5.05 * inch],
        styles["Small"],
    )
)
story.append(p("Business example: a rental agreement envelope is sent. Instead of your app polling GET /envelopes/{envelopeId} every few seconds, Connect posts to https://www.abc.com/docusign/connect when the envelope is completed. Your app validates HMAC, finds the local rental record by envelopeId, marks it signed, and starts the next process such as payment collection or move-in workflow.", styles["Body"]))
story.append(p("Exam memory: Connect = Docusign pushes events to your app. Polling = your app repeatedly asks Docusign for status. HMAC proves authenticity. requireAcknowledgment=true means Docusign expects a successful response; failures can cause retries. Do not include documents in webhook payload unless you truly need them because payloads become large and sensitive.", styles["Body"]))
story.append(p("Official docs: Connect overview https://developers.docusign.com/platform/webhooks/connect/ ; HMAC validation https://developers.docusign.com/platform/webhooks/connect/validate/ ; create envelope/eventNotification https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/ ; Connect events https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/", styles["Small"]))

story.append(PageBreak())
story += section("11. Web Forms API")
story.append(
    table(
        ["Step", "SDK method / request URL", "Important IDs / body", "Business example"],
        [
            [
                "1. Authenticate",
                "OAuth/JWT token request, then use eSignature basePath for templates and webFormsApiUrl for Web Forms. Demo Web Forms base path in project: https://apps-d.docusign.com/api/webforms.",
                "accessToken, accountId, eSignature basePath, Web Forms basePath. Required scopes include webforms_read, webforms_instance_read, webforms_instance_write.",
                "University portal signs in service user, then prepares to show a financial-aid intake form.",
            ],
            [
                "2. Find/create backing template",
                "TemplatesApi.listTemplates(accountId, { searchText }); if missing: TemplatesApi.createTemplate(accountId, { envelopeTemplate }). URL: {basePath}/v2.1/accounts/{accountId}/templates.",
                "templateId, documentId, recipientId, roleName, tabLabel. The quickstart template includes signer role plus signHere, checkbox, text, and dateSigned tabs.",
                "Admin/developer creates the application PDF/template once; Web Forms uses that agreement setup later.",
            ],
            [
                "3. Find Web Form definition",
                "FormManagementApi.listForms(accountId, { search: formName }). URL shape: {webFormsBasePath}/v1/accounts/{accountId}/forms.",
                "formId is the Web Form definition/configuration. It is not an envelopeId and not a templateId.",
                "App searches for Financial Aid Application or Insurance Claim Intake form.",
            ],
            [
                "4A. Create embedded instance",
                "FormInstanceManagementApi.createInstance(body, accountId, formId). URL shape: {webFormsBasePath}/v1/accounts/{accountId}/forms/{formId}/instances.",
                "Body uses clientUserId, formValues, expirationOffset. Returned data includes an instance/URL that your site renders with Docusign JS.",
                "Student fills the form inside the university website without leaving the portal.",
            ],
            [
                "4B. Create remote instance",
                "Same createInstance method, but body includes recipients and sendOption='now'.",
                "Body uses formValues plus recipients[{ roleName, name, email }]. Docusign sends the form/signing experience to the recipient.",
                "Insurance company emails a claim intake form to a customer instead of embedding it in the app.",
            ],
            [
                "5. Render or send",
                "Embedded: app uses returned instance URL with Docusign JS. Remote: Docusign sends the experience using recipient email.",
                "formInstanceId / instance URL, clientUserId, externalReferenceId if used for your system correlation.",
                "Your app maps the form instance to a local business record reference in your own system.",
            ],
            [
                "6. Complete downstream flow",
                "Web Form data can populate agreement fields and feed envelope/signing or workflow steps.",
                "Final signing transaction may create envelopeId depending the Web Form/template/workflow configuration.",
                "User submits intake data first, then signs the generated/connected agreement.",
            ],
        ],
        [0.95 * inch, 2.45 * inch, 2.35 * inch, 1.55 * inch],
        styles["Small"],
    )
)
story.append(p("How the template is connected:", styles["H3"]))
story.append(
    bullets(
        [
            "The template/document is the agreement structure: document, recipient roles, tabs, signing fields, and field labels.",
            "The Web Form is the data collection layer: pages, questions, validation, conditional logic, and values the user enters.",
            "The Web Form instance is one user's runtime session created from the Web Form definition.",
            "Template tab labels and Web Form field names are the bridge: collected values can populate agreement fields.",
            "You normally do not send a blank Web Form by API without a form/template setup. Build/configure the form first, then create instances.",
        ],
        styles["Body"],
    )
)
story.append(p("Embedded versus remote Web Form instance:", styles["H3"]))
story.append(
    table(
        ["Mode", "Body shape", "What the user sees", "When to use"],
        [
            ["Embedded", "clientUserId, formValues, expirationOffset", "Your app renders the returned Web Form instance URL inline with Docusign JS.", "User is already inside your portal, such as student portal or customer dashboard."],
            ["Remote", "formValues, recipients[{ roleName, name, email }], sendOption='now'", "Docusign sends the Web Form/signing experience to the recipient by email.", "You want Docusign to email the user instead of embedding the form."],
        ],
        [1.1 * inch, 2.2 * inch, 2.1 * inch, 1.9 * inch],
        styles["Small"],
    )
)

story += section("12. Navigator / Agreement APIs")
story.append(
    table(
        ["Operation", "SDK call / URL shape", "Important IDs / response", "Exam highlight"],
        [
            ["List agreements", "client.navigator.agreements.getAgreementsList({ accountId })\nGET /v1/accounts/{accountId}/agreements", "Needs accountId. Can filter by status, title, source_id, source_name, languages, parties.name_in_agreement, provisions.effective_date, execution_date, expiration_date, term_length, and pagination token.", "Use first when the app does not know agreementId. This is repository data, not an envelope list."],
            ["Get one agreement", "client.navigator.agreements.getAgreement({ accountId, agreementId })\nGET /v1/accounts/{accountId}/agreements/{agreementId}", "Needs accountId + agreementId. Returns Agreement: title, fileName, type, category, summary, status, parties, provisions, custom fields, source data, metadata.", "Use when the app already selected one agreement record and needs extracted/detail data."],
            ["Create AI summary", "client.navigator.agreements.createAgreementSummary({ accountId, agreementId })\nPOST /v1/accounts/{accountId}/agreements/{agreementId}/ai/actions/summarize", "Needs accountId + agreementId. No body in this SDK operation. Returns AgreementSummary.summary.", "This is a specific AI summary action, not a general prompt/chat API."],
            ["Delete agreement", "client.navigator.agreements.deleteAgreement({ accountId, agreementId })\nDELETE /v1/accounts/{accountId}/agreements/{agreementId}", "Needs accountId + agreementId. Deletes the agreement record according to account/API permissions.", "Deletion is repository management, not voiding an envelope."],
        ],
        [1.05 * inch, 2.25 * inch, 2.35 * inch, 1.65 * inch],
        styles["Small"],
    )
)
story.append(p("EXAM HIGHLIGHT: Envelope APIs manage the sending/signing transaction. Navigator / Agreement APIs read agreement repository records, extracted terms, source metadata, and AI summary output after the agreement exists in the repository.", styles["Body"]))
story.append(p("What getAgreement exposes:", styles["H3"]))
story.append(
    table(
        ["Group", "Fields exposed", "Why it matters"],
        [
            ["Core identity", "id, title, fileName, type, category, status", "Identifies the agreement record and its lifecycle state."],
            ["AI / extracted context", "summary, parties, provisions", "These are the fields most likely to matter for exam questions about AI-extracted agreement data."],
            ["Custom data", "customProvisions, additionalUserDefinedData, additionalCustomClmData, additionalCustomEsignData", "Business-specific metadata or extracted fields can appear here, depending on account configuration and source system."],
            ["Source mapping", "sourceName, sourceId, sourceAccountId", "Connects the agreement record back to the originating system, for example eSign or CLM. sourceId may point to the original source object such as an envelope/source record."],
            ["Relationship / metadata", "relatedAgreementDocuments, languages, metadata", "Used for related documents, language tags, created/modified information, and governance/reporting."],
        ],
        [1.25 * inch, 3.0 * inch, 3.0 * inch],
        styles["Small"],
    )
)
story.append(p("Provision fields to recognize:", styles["H3"]))
story.append(
    table(
        ["Provision group", "Example fields", "Business meaning"],
        [
            ["Dates / lifecycle", "effectiveDate, expirationDate, executionDate, termLength", "When the agreement starts, ends, was executed, and how long it runs."],
            ["Renewal", "renewalType, renewalNoticePeriod, renewalNoticeDate, autoRenewalTermLength, renewalExtensionPeriod, renewalProcessOwner", "Supports renewal tracking, reminders, and owner assignment."],
            ["Legal clauses", "governingLaw, jurisdiction, ndaType, confidentialityObligationPeriod", "Important clauses extracted from the agreement text."],
            ["Money / payment", "annualAgreementValue, totalAgreementValue, currency codes, paymentTermsDueDate, late payment fields", "Useful for finance, ERP, revenue, and compliance reporting."],
            ["Risk / termination", "liabilityCapFixedAmount, liabilityCapMultiplier, terminationPeriodForCause, terminationPeriodForConvenience, priceCapPercentIncrease", "Used to understand risk, exit rights, liability, and pricing limits."],
        ],
        [1.35 * inch, 3.35 * inch, 2.55 * inch],
        styles["Small"],
    )
)
story.append(p("How your app uses it:", styles["H3"]))
story.append(
    table(
        ["Business flow", "What your app calls", "What your app reads"],
        [
            ["Find the contract", "GET /v1/accounts/{accountId}/agreements with filters such as title/status/source_id.", "Agreement list with ids and high-level metadata."],
            ["Open details", "GET /v1/accounts/{accountId}/agreements/{agreementId}.", "parties, provisions, summary, custom fields, sourceName/sourceId, metadata."],
            ["Show AI summary", "POST /v1/accounts/{accountId}/agreements/{agreementId}/ai/actions/summarize.", "summary text returned by AgreementSummary.summary."],
            ["Sync to another system", "Use getAgreement response, then map selected fields to CRM/ERP/compliance database.", "Example: expirationDate for renewal alert, totalAgreementValue for finance, governingLaw for legal reporting."],
        ],
        [1.45 * inch, 3.0 * inch, 2.8 * inch],
        styles["Small"],
    )
)
story.append(p("Navigator AI reality check: Docusign can expose structured extracted fields and a summary action through the SDK. It does not mean your app can send arbitrary natural-language prompts to a generic Docusign AI chat endpoint. For exam wording, choose list/get/summary based on whether the app needs discovery, one agreement's details, or a generated summary.", styles["Body"]))

story += section("13. Maestro / Workflow Builder API")
story.append(p("Important Maestro IDs:", styles["H3"]))
story.append(
    table(
        ["ID", "Meaning", "Used where"],
        [
            ["accountId", "Docusign account.", "Every Maestro call."],
            ["workflowId", "Published workflow definition ID.", "List result, trigger, pause, resume, and instance APIs."],
            ["instanceId", "One running workflow execution.", "Get/cancel a specific workflow run."],
            ["templateId", "eSignature template used inside a workflow Sign step.", "When building a workflow definition that signs from a template."],
            ["participantId", "Internal role/person in workflow, such as Signer or CC.", "Workflow definition participants and step config."],
            ["stepId", "Workflow step identifier.", "Variables, outputs, step wiring, and field references."],
        ],
        [1.2 * inch, 2.5 * inch, 3.55 * inch],
        styles["Small"],
    )
)
story.append(p("Maestro workflow and instance APIs:", styles["H3"]))
story.append(
    table(
        ["Action", "Method + URL", "Body", "Returns / purpose"],
        [
            ["List workflows", "GET /v1/accounts/{accountId}/workflows?status=active", "none", "Workflows with id, name, status, metadata."],
            ["Get trigger requirements", "GET /v1/accounts/{accountId}/workflows/{workflowId}/trigger-requirements", "none", "Tells what triggerInputs are required."],
            ["Trigger workflow", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger", "instance_name, trigger_inputs", "Returns instance_id, instance_url, request_id."],
            ["Pause new instances", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/pause", "none", "Pauses creation of new workflow runs. Running instances continue."],
            ["Resume workflow", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/resume", "none", "Allows new workflow runs again."],
            ["List instances", "GET /v1/accounts/{accountId}/workflows/{workflowId}/instances", "none", "All runs of one workflow."],
            ["Get instance", "GET /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}", "none", "Status, started/ended time, trigger inputs, step progress."],
            ["Cancel instance", "POST /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}/actions/cancel", "none", "Cancels that running workflow instance."],
        ],
        [1.2 * inch, 3.15 * inch, 1.35 * inch, 1.55 * inch],
        styles["Small"],
    )
)
story.append(p("requestId vs stepId debugging:", styles["H3"]))
story.append(
    table(
        ["ID", "What it identifies", "How your app uses it", "Not this"],
        [
            ["requestId", "One API request trace, such as the trigger API call.", "Keep it for troubleshooting with Docusign support if the API call failed or behaved unexpectedly.", "It is not the workflow run and not a workflow step."],
            ["instanceId", "One running Maestro workflow instance.", "Use it to check workflow status, progress, and cancel that specific run.", "It is not the original API request trace."],
            ["stepId", "One step inside the workflow definition or workflow instance.", "Use it to identify which form, sign, approval, branch, or update step completed, paused, or failed.", "It is not a log download ID and not the API request trace."],
        ],
        [1.05 * inch, 2.0 * inch, 2.7 * inch, 1.5 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["Debug situation", "Procedure", "Main ID to use"],
        [
            ["Trigger API did not start a workflow", "Check the trigger API response/error. Use requestId if asking Docusign support to trace that exact API call.", "requestId"],
            ["Workflow started but you need status", "Call GET /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}.", "instanceId"],
            ["A specific step failed or paused", "Read the workflow instance response and inspect step progress/details if exposed. Use stepId to identify the exact step.", "instanceId + stepId"],
            ["Need deeper internal logs", "Use Docusign UI/support. The API may expose status, output, and error details, but not always full internal logs.", "requestId + instanceId + stepId"],
        ],
        [1.5 * inch, 4.4 * inch, 1.35 * inch],
        styles["Small"],
    )
)
story.append(p("Exam memory: requestId traces the API call. instanceId tracks the workflow run. stepId identifies a step inside that run. requestId and stepId are not directly related; they answer different debugging questions.", styles["Body"]))
story.append(p("Workflow definition create/publish URLs from the quickstart raw axios code:", styles["H3"]))
story.append(
    table(
        ["Action", "URL", "Important note"],
        [
            ["Create workflow definition", "POST https://demo.services.docusign.net/aow-manage/v1.0/management/accounts/{accountId}/workflowDefinitions", "Body wraps workflowDefinition with workflowName, accountId, participants, trigger, variables, and steps."],
            ["Publish workflow", "POST https://demo.services.docusign.net/aow-manage/v1.0/management/accounts/{accountId}/workflowDefinitions/{workflowId}/publish?isPreRunCheck=true", "May return consentUrl if consent is required before publish completes."],
        ],
        [1.65 * inch, 3.9 * inch, 1.7 * inch],
        styles["Small"],
    )
)
story.append(p("Workflow definition core terms:", styles["H3"]))
story.append(
    bullets(
        [
            "trigger: how the workflow starts, for example API trigger with required input variables.",
            "variables: mapped values passed between trigger and steps.",
            "participants: roles such as Signer and CC.",
            "steps: modules such as DS-Sign and confirmation screen.",
            "triggerInputs: runtime values supplied when starting an instance.",
        ],
        styles["Body"],
    )
)
story.append(p("Idempotency:", styles["H3"]))
story.append(
    table(
        ["Question", "Answer"],
        [
            ["Is there built-in idempotency in this Maestro SDK trigger call?", "Not shown/exposed in the IAM SDK version inspected. The trigger/pause/resume/cancel request code has no idempotency key/header or idempotency body field."],
            ["What happens if you call trigger twice?", "Expect two workflow instances unless Docusign rejects the second call for another reason."],
            ["How should your app handle this?", "Store your own local business reference and do not trigger again if that business case already started."],
            ["What ID do you store after trigger?", "Store instanceId. Use it later to get status or cancel that specific workflow run."],
        ],
        [2.55 * inch, 4.7 * inch],
        styles["Small"],
    )
)
story.append(p("Exam memory: Maestro workflow = definition/process. Trigger workflow = creates one instanceId. Pause workflow = stops new instances, not existing running ones. Cancel instance = stops one running instanceId.", styles["Body"]))
story.append(p("Business flow example: rental application workflow", styles["H3"]))
story.append(
    table(
        ["Step", "Business action", "Maestro/API action", "Exposed URL used", "IDs involved"],
        [
            ["1", "Admin already built a rental workflow.", "Workflow definition exists in Docusign.", "Workflow Builder UI or create workflow definition API.", "accountId, workflowId"],
            ["2", "Your website needs the rental workflow.", "List active workflows and choose Rental Application Workflow.", "GET /v1/accounts/{accountId}/workflows?status=active", "accountId -> workflowId"],
            ["3", "Your app checks what data the workflow needs.", "Get trigger requirements.", "GET /v1/accounts/{accountId}/workflows/{workflowId}/trigger-requirements", "accountId, workflowId"],
            ["4", "Tenant fills the website form.", "Your app prepares trigger inputs; no Docusign call yet.", "Local app route/form submit.", "tenant form data; local business reference"],
            ["5", "Tenant submits application.", "Trigger workflow with instance_name and trigger_inputs.", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger", "accountId, workflowId -> instanceId"],
            ["6", "Maestro starts John Smith's one workflow run.", "Docusign creates a workflow instance.", "Trigger response includes instance_id, instance_url, request_id.", "instanceId, requestId"],
            ["7", "Workflow sends lease for signature.", "Internal Sign step uses the eSignature template configured in the workflow.", "Inside workflow definition, not a separate trigger URL.", "templateId, participantId, stepId, possible envelopeId"],
            ["8", "Your app checks progress later.", "Get workflow instance.", "GET /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}", "accountId, workflowId, instanceId"],
            ["9", "Admin temporarily stops new rental applications.", "Pause new workflow instances.", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/pause", "accountId, workflowId"],
            ["10", "Admin reopens rental applications.", "Resume workflow.", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/resume", "accountId, workflowId"],
            ["11", "One tenant submitted wrong information.", "Cancel that one workflow instance.", "POST /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}/actions/cancel", "accountId, workflowId, instanceId"],
        ],
        [0.35 * inch, 1.45 * inch, 1.55 * inch, 2.55 * inch, 1.35 * inch],
        styles["Small"],
    )
)
story.append(p("Business idempotency memory: if tenant John double-clicks Submit, your app should not call trigger twice. Store a local business reference together with workflowId and instanceId. If that local business reference already has an instanceId, reuse it instead of creating a second workflow run.", styles["Body"]))
story.append(
    table(
        ["Concept", "Rental example"],
        [
            ["workflowId", "The published Rental Application Workflow process."],
            ["instanceId", "John Smith's one rental application run."],
            ["templateId", "Lease agreement template used inside the Sign step."],
            ["participantId", "Tenant signer or property manager role inside the workflow."],
            ["stepId", "API trigger step, Sign step, confirmation step, or another workflow step."],
            ["envelopeId", "May be created by the eSignature Sign step if the workflow sends a signing envelope."],
        ],
        [1.3 * inch, 5.95 * inch],
        styles["Small"],
    )
)
story.append(p("How workflow start methods relate to trigger:", styles["H3"]))
story.append(p("Trigger means the start event that creates a workflow instance. The start method decides who or what performs that trigger.", styles["Body"]))
story.append(
    table(
        ["Start method", "Who/what triggers it?", "Does your app call trigger API?", "Business example", "How data enters the workflow"],
        [
            ["Manual", "A user inside Docusign clicks Run Workflow.", "No.", "Property manager logs into Docusign and manually starts Rental Application Workflow.", "User enters/selects data in Docusign UI. Docusign creates instanceId."],
            ["Link", "Someone opens a Docusign workflow link.", "Usually no.", "CRM button opens a Docusign workflow link for Start Rental Application.", "User enters or confirms data after opening the link. If the CRM button only redirects, it is link start, not API start."],
            ["API", "Your app/backend calls the Maestro trigger endpoint.", "Yes: POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger.", "Tenant submits rental form on your website; backend sends signerName and signerEmail.", "Your app sends trigger_inputs JSON and receives instance_id / instance_url."],
            ["Event", "A configured business/system event fires.", "Usually no direct trigger call from your app.", "Salesforce opportunity becomes Closed Won, or CRM application status changes to Approved.", "Event payload is mapped into workflow variables/inputs; Docusign starts the instance automatically."],
        ],
        [0.95 * inch, 1.35 * inch, 1.75 * inch, 1.65 * inch, 1.55 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["Memory point", "Meaning"],
        [
            ["Start method", "How the workflow starts: manual, link, API, or event."],
            ["Trigger requirements", "What data is required before the workflow can start."],
            ["Trigger inputs", "The actual values used to start one run."],
            ["Workflow instance", "The result after start: one running business case with instanceId."],
        ],
        [1.7 * inch, 5.55 * inch],
        styles["Small"],
    )
)
story.append(p("Connecting two workflows after the first one completes:", styles["H3"]))
story.append(p("A completed workflow run can lead to another workflow run. The first workflow keeps its own workflowId and instanceId. The second workflow has its own workflowId and receives a new instanceId when it starts.", styles["Body"]))
story.append(
    table(
        ["Connection pattern", "Business flow", "API call", "Real DocuSign IDs involved"],
        [
            ["Pure event start", "First workflow completes. A configured completion event starts the second workflow automatically.", "No direct POST /actions/trigger from your app.", "accountId; first workflow's workflowId and instanceId; second workflow's workflowId; new instanceId for the second workflow; possible envelopeId from signing step."],
            ["App-mediated API start", "First workflow completes. Event/webhook reaches your app. Your app starts the second workflow by API.", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger. Here workflowId is the second workflow's workflowId.", "accountId; first workflow's workflowId and instanceId; possible envelopeId; second workflow's workflowId; new instanceId returned for the second workflow."],
        ],
        [1.35 * inch, 2.25 * inch, 1.9 * inch, 1.75 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["Data from completed first workflow", "How second workflow uses it", "Important note"],
        [
            ["instanceId of the first workflow run", "Stored as a mapped variable in the second workflow for traceability.", "The field name is configured by the second workflow; it is not a new DocuSign ID type."],
            ["envelopeId from the signing step, if one was created", "Reference the signed lease/agreement in the second workflow.", "envelopeId is an eSignature ID, not a Maestro instanceId."],
            ["Signer name, signer email, property address, rent amount", "Prefill a form, address an email, fill a document, or drive branch logic.", "These are business values carried as event data or trigger_inputs."],
            ["Completion status/date", "Decide whether to start the second workflow or record completion timing.", "The second workflow still receives its own new instanceId."],
        ],
        [2.05 * inch, 3.0 * inch, 2.2 * inch],
        styles["Small"],
    )
)
story.append(p("Using a completed eSignature envelope to start a Maestro workflow:", styles["H3"]))
story.append(p("Yes, a completed eSignature envelope can be used as the event/source data for a Maestro workflow, depending on event/workflow configuration. The completed envelope does not become a Maestro workflow by itself; it either fires a configured event trigger or your app receives the completion event and calls the Maestro trigger API.", styles["Body"]))
story.append(
    table(
        ["Pattern", "What happens", "API call", "IDs required / used"],
        [
            ["Pure event trigger", "Envelope reaches completed status. A configured event trigger starts the workflow.", "No direct POST /actions/trigger from your app.", "accountId; envelopeId from eSignature event; workflowId of the Maestro workflow to start; new instanceId created by Maestro."],
            ["App-mediated API trigger", "Envelope reaches completed status. Your app receives the event, then starts the workflow by API.", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger", "accountId; envelopeId from completed envelope; workflowId of the Maestro workflow to start; new instanceId returned by Maestro."],
        ],
        [1.25 * inch, 2.05 * inch, 2.15 * inch, 1.85 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["ID / value", "Is it required to start the next workflow?", "Purpose"],
        [
            ["accountId", "Yes.", "Chooses the Docusign account for the Maestro API/event context."],
            ["workflowId", "Yes.", "Chooses which Maestro workflow definition starts."],
            ["envelopeId", "Usually yes for an envelope-completion business flow, but it is event data, not the workflow ID.", "Lets the workflow know which completed eSignature envelope caused the start."],
            ["first workflow instanceId", "Only if the source was a Maestro workflow. Not needed when the source is only an eSignature envelope.", "Traceability from a previous Maestro run."],
            ["trigger_inputs", "Required if the workflow's trigger requirements say fields are required.", "Carries values such as envelopeId, signerEmail, completedDate, or other mapped business data."],
            ["new instanceId", "Returned after start, not sent before start.", "Identifies the new running workflow instance."],
        ],
        [1.55 * inch, 2.2 * inch, 3.5 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        '{"instance_name":"Post-signing workflow","trigger_inputs":{"envelopeId":"{envelopeId}","status":"completed","signerEmail":"{signerEmailIfMapped}"}}',
        styles["CodeBlock"],
    )
)
story.append(p("Exam memory: envelopeId is an eSignature ID. workflowId is the Maestro workflow definition ID. instanceId is the Maestro run ID created after the workflow starts. To trigger the next workflow, the required path IDs are accountId and workflowId; envelopeId is passed as event data or trigger_inputs so the new workflow knows what completed envelope it is handling.", styles["Body"]))
story.append(p("Exam memory: workflowId identifies a workflow definition. instanceId identifies one run. When a second workflow starts, it does not reuse the first workflow's instanceId; it gets a new instanceId. Data from the first run is passed as event data or trigger_inputs, not by changing the ID names.", styles["Body"]))
story.append(p("Trigger requirements vs trigger inputs:", styles["H3"]))
story.append(
    table(
        ["Trigger concept", "Short meaning", "Example", "When your app uses it"],
        [
            ["Trigger requirement", "What the workflow says it needs before it can start. Think schema, checklist, or form definition.", '{"requiredFields":["signerName","signerEmail","ccName","ccEmail"]}', "Before triggering. Your app checks requirements so it knows which fields to collect."],
            ["Trigger input", "The actual values your app sends to start one workflow instance.", '{"signerName":"John Smith","signerEmail":"john@example.com","ccName":"Manager","ccEmail":"manager@example.com"}', "At trigger time. Your app sends these values inside trigger_inputs."],
            ["Workflow instance", "The running copy created after Docusign accepts the trigger inputs.", "Response includes instance_id and instance_url.", "After triggering. Store instanceId to check status or cancel that specific run."],
        ],
        [1.2 * inch, 2.25 * inch, 2.45 * inch, 1.35 * inch],
        styles["Small"],
    )
)
story.append(p("Trigger API difference table:", styles["H3"]))
story.append(
    table(
        ["Question", "Use this", "URL / payload", "Result"],
        [
            ["What fields are required?", "Trigger requirements", "GET /v1/accounts/{accountId}/workflows/{workflowId}/trigger-requirements", "Docusign tells your app the required input schema."],
            ["What values start this run?", "Trigger inputs", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger with trigger_inputs", "Docusign starts one workflow instance."],
            ["What happened after start?", "Workflow instance", "GET /v1/accounts/{accountId}/workflows/{workflowId}/instances/{instanceId}", "Docusign returns status, timestamps, triggerInputs, and progress."],
        ],
        [1.35 * inch, 1.45 * inch, 3.0 * inch, 1.45 * inch],
        styles["Small"],
    )
)
story.append(p("API trigger details: required body and what happens to values", styles["H3"]))
story.append(
    table(
        ["Question", "Answer", "Exam memory"],
        [
            ["Can API trigger run with only accountId and workflowId?", "No for normal required-input workflows. accountId and workflowId are only URL/path IDs. The trigger body still needs instance_name and the trigger_inputs required by the workflow.", "URL IDs choose the workflow. Body values start the business run."],
            ["Can trigger_inputs be empty?", "Only if the workflow has no required trigger inputs, or if later steps collect everything from the user. If the workflow requires signerName/signature email, empty inputs should fail or cannot start correctly.", "Empty trigger_inputs is design-dependent."],
            ["What does Docusign do with trigger_inputs?", "They become workflow variables for that instance. Steps can map those variables into forms, recipients, documents, notifications, branches, or external updates.", "trigger_inputs -> workflow variables -> mapped steps."],
            ["Will the first form be prefilled?", "Yes, if the form fields are mapped to the trigger input variables. If not mapped, the workflow has the values but the form will not automatically show them.", "Mapping controls whether values appear in the form/document."],
        ],
        [1.45 * inch, 4.05 * inch, 1.75 * inch],
        styles["Small"],
    )
)
story.append(
    table(
        ["Workflow step", "How trigger input values can be used"],
        [
            ["Web Form / data collection", "Pre-fill fields such as tenant name, email, rent amount, or local business reference if mapped."],
            ["eSignature Sign step", "Use signerName and signerEmail as recipient details; may create an envelopeId."],
            ["Document/template step", "Fill document fields/tabs with values such as rentAmount or tenantAddress."],
            ["Email/notification step", "Send messages to signerEmail or propertyManagerEmail."],
            ["Branch/condition step", "Route differently based on a value, for example rentAmount > 2000 or applicantType = corporate."],
            ["External update step", "Write status, instanceId, envelopeId, or completed data back to CRM/app database."],
        ],
        [1.8 * inch, 5.45 * inch],
        styles["Small"],
    )
)
story.append(p("Example trigger body:", styles["H3"]))
story.append(
    p(
        '{"instance_name":"Rental application for John","trigger_inputs":{"signerName":"John Smith","signerEmail":"john@example.com","ccName":"Manager","ccEmail":"manager@example.com"}}',
        styles["CodeBlock"],
    )
)
story.append(p("Simple flow: 1. Your app checks trigger requirements. 2. Docusign says this workflow needs fields such as signerName and signerEmail. 3. Your app sends trigger inputs such as John Smith and john@example.com. 4. Docusign starts the workflow instance. 5. Docusign returns instanceId/instanceUrl. 6. Your app uses instanceId for status or cancel.", styles["Body"]))

story.append(PageBreak())
story += section("14. Connected Fields, Extension Apps, and Other Project Examples")
story.append(p("These are smaller than the main launcher flows, but they are exam-relevant because they test product boundaries: regulated identity, embedded UI settings, generated documents, and extension-connected tabs.", styles["Body"]))
story.append(p("Four priority topics:", styles["H3"]))
story.append(
    table(
        ["Topic", "Project file", "Main APIs/functions", "Important IDs", "Exam memory"],
        [
            ["CFR embedded signing", "lib/eSignature/examples/embeddedSigningCFR.js", "AccountsApi.getAccountIdentityVerification, EnvelopesApi.createEnvelope, createRecipientView", "workflowId, accountId, envelopeId, recipientId, clientUserId", "Regulated embedded signing uses identityVerification workflow data."],
            ["Focused View", "lib/eSignature/examples/focusedView.js", "EnvelopesApi.createEnvelope, createRecipientView", "accountId, envelopeId, recipientId, clientUserId", "Modern embedded signing view with frameAncestors and messageOrigins."],
            ["Document Generation", "lib/eSignature/examples/documentGeneration.js", "TemplatesApi.createTemplate/updateDocument/createTabs, EnvelopesApi.get/updateEnvelopeDocGenFormFields", "templateId, documentId, documentIdGuid, recipientId, envelopeId", "Generate/fill document fields before sending."],
            ["Connected Fields", "lib/connectedFields/examples/setConnectedFields.js", "IamClient.connectedFields.tabInfo.getConnectedFieldsTabGroups, EnvelopesApi.createEnvelope", "appId, extensionGroupId, connectionKey, connectionValue, documentId, recipientId", "Text tabs can carry extensionData and verification policy."],
        ],
        [0.95 * inch, 1.35 * inch, 2.05 * inch, 1.25 * inch, 1.45 * inch],
        styles["Small"],
    )
)
story.append(p("CFR embedded signing body difference:", styles["H3"]))
story.append(
    p(
        "{\n  \"recipients\": {\n    \"signers\": [\n      {\n        \"email\": \"signer@example.com\",\n        \"name\": \"Signer Name\",\n        \"recipientId\": \"1\",\n        \"clientUserId\": \"1000\",\n        \"identityVerification\": {\n          \"workflowId\": \"{workflowId}\",\n          \"inputOptions\": [\n            { \"name\": \"phone_number_list\", \"valueType\": \"PhoneNumberList\", \"phoneNumberList\": [ { \"countryCode\": \"1\", \"number\": \"5551234567\" } ] }\n          ]\n        }\n      }\n    ]\n  },\n  \"status\": \"sent\"\n}",
        styles["CodeBlock"],
    )
)
story.append(p("CFR memory: workflowId here is the Docusign identity verification workflow ID returned by getAccountIdentityVerification. It is not a Maestro workflowId.", styles["Body"]))
story.append(p("Focused View recipient view fields:", styles["H3"]))
story.append(
    p(
        "{\n  \"returnUrl\": \"https://yourapp.com/ds-return?state=123\",\n  \"authenticationMethod\": \"none\",\n  \"email\": \"signer@example.com\",\n  \"userName\": \"Signer Name\",\n  \"clientUserId\": \"1000\",\n  \"pingUrl\": \"https://yourapp.com/ping\",\n  \"pingFrequency\": 600,\n  \"frameAncestors\": [\"https://yourapp.com\", \"https://apps-d.docusign.com\"],\n  \"messageOrigins\": [\"https://apps-d.docusign.com\"]\n}",
        styles["CodeBlock"],
    )
)
story.append(p("Focused View memory: createRecipientView still returns a short-lived signing URL, but the request includes frame/security settings so the modern embedded view can load inside the allowed app origin.", styles["Body"]))
story.append(p("Document Generation workflow:", styles["H3"]))
story.append(
    table(
        ["Step", "API/function", "Important IDs", "What it does"],
        [
            ["1", "TemplatesApi.createTemplate", "templateId", "Creates a draft reusable template shell."],
            ["2", "TemplatesApi.updateDocument", "templateId, documentId", "Uploads the DOCX generation document."],
            ["3", "TemplatesApi.createTabs", "recipientId", "Adds signing tabs to the template recipient."],
            ["4", "EnvelopesApi.createEnvelope", "templateId -> envelopeId", "Creates draft envelope from template."],
            ["5", "EnvelopesApi.getEnvelopeDocGenFormFields", "envelopeId -> documentIdGuid", "Reads generated document fields that can be filled."],
            ["6", "EnvelopesApi.updateEnvelopeDocGenFormFields", "documentIdGuid", "Fills values such as candidate name, salary, job title."],
            ["7", "EnvelopesApi.update status='sent'", "envelopeId", "Sends the final generated envelope."],
        ],
        [0.45 * inch, 2.1 * inch, 1.45 * inch, 2.9 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "DocGen field body shape:\n{\n  \"docGenFormFields\": [\n    {\n      \"documentId\": \"{documentIdGuid}\",\n      \"docGenFormFieldList\": [\n        { \"name\": \"Candidate_Name\", \"value\": \"John Smith\" },\n        { \"name\": \"Job_Title\", \"value\": \"Sales Manager\" },\n        { \"name\": \"Start_Date\", \"value\": \"2026-08-01\" }\n      ]\n    }\n  ]\n}",
        styles["CodeBlock"],
    )
)
story.append(p("Connected Fields workflow:", styles["H3"]))
story.append(
    table(
        ["Step", "API/function", "Important IDs", "What it does"],
        [
            ["1", "IamClient.connectedFields.tabInfo.getConnectedFieldsTabGroups({ accountId })", "accountId", "Reads available connected-field tab groups."],
            ["2", "Filter tabs for Verify/actionContract or connecteddata labels.", "appId", "Chooses the extension app/tab that can verify data."],
            ["3", "Extract extension metadata.", "extensionGroupId, actionName, actionInputKey, connectionKey, connectionValue", "Gets the values that wire the tab to the extension action."],
            ["4", "Create envelope with text tabs.", "documentId, recipientId", "Normal envelope, but tabs include extensionData."],
            ["5", "Signer fills/verifies field.", "envelopeId", "Docusign enforces extensionPolicy such as MustVerifyToSign."],
        ],
        [0.45 * inch, 2.6 * inch, 1.75 * inch, 2.1 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Connected field tab shape:\n{\n  \"tabType\": \"text\",\n  \"tabLabel\": \"connecteddata_customerId\",\n  \"required\": true,\n  \"extensionData\": {\n    \"applicationId\": \"{appId}\",\n    \"extensionGroupId\": \"{extensionGroupId}\",\n    \"actionName\": \"Verify\",\n    \"actionInputKey\": \"customerId\",\n    \"extensionPolicy\": \"MustVerifyToSign\",\n    \"connectionInstances\": [ { \"connectionKey\": \"{connectionKey}\", \"connectionValue\": \"{connectionValue}\" } ]\n  }\n}",
        styles["CodeBlock"],
    )
)
story.append(p("Remaining priority memory: CFR = regulated embedded identity workflow; Focused View = embedded signing with frame/origin controls; Document Generation = fill generated DOCX fields; Connected Fields = extension-backed field verification.", styles["Body"]))

story.append(Paragraph("14D. Extension Apps - Platform Concepts Beyond the Quickstart", styles["H2"]))
story.append(
    p(
        "Section 14C showed the consumer side: a Connected Fields tab carrying extensionData (appId, extensionGroupId, actionName, connectionKey/Value) that fires an already-published extension app during signing. This section is the other half - how that extension app gets built, registered, and published in the first place. None of this lives in the quickstart source code; it is Developer Console / App Center platform configuration, sourced from the Docusign University certification path and developers.docusign.com.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Concept", "What it is", "Exam distinction"],
        [
            ["Extension app", "A registered set of HTTP endpoints (documented by a manifest.json) that lets a third-party service plug into Docusign at defined trigger points.", "Not an envelope, template, or API client credential - it is a separate platform object with its own App ID."],
            ["Developer Console", "Self-serve tool to build, test, and publish extension apps.", "Different surface from Apps and Keys (which manages OAuth integration keys)."],
            ["Docusign App Center", "Where finished extension apps are listed for install. Production: apps.docusign.com/app-center. Demo: apps-d.docusign.com/app-center.", "Public apps: any customer can discover/install. Private apps: only specific accounts you approve."],
            ["Extension point", "A place inside an envelope (a Connected Fields tab) or a Maestro workflow (an Apps Step) where the extension app's action can be triggered.", "The extension app itself does nothing until it is wired into a tab or workflow step at an extension point."],
        ],
        [1.3 * inch, 3.55 * inch, 2.55 * inch],
        styles["TableBody"],
    )
)
story.append(p("Two ways to register an app:", styles["H3"]))
story.append(
    table(
        ["Path", "How it works", "When to use"],
        [
            ["Forms-based experience", "Developer Console form collects app name, publisher/support email, distribution type, and extension type(s) (File Input Output, Data Input Output, Data Verification, or Connected Fields). Create App assigns an App ID; you then edit Integration Details (Connection auth) and Extensions & Actions in the UI.", "Fastest path; Docusign builds the manifest for you behind the scenes."],
            ["Manifest file (JSON)", "Click Create App -> By editing the manifest, edit the file in the built-in editor (real-time validation) or download/edit locally, then Validate and Create App.", "Needed when you want full control of the JSON, or are scripting/versioning the manifest in source control."],
        ],
        [1.5 * inch, 4.5 * inch, 1.4 * inch],
        styles["TableBody"],
    )
)
story.append(p("Manifest file - four parts:", styles["H3"]))
story.append(
    table(
        ["Section", "Key fields", "What it defines"],
        [
            ["APP DETAILS", "name (unique), publicationRegions (public only), distribution (PUBLIC/PRIVATE), description, publisher (org/email/phone/website), termsOfServiceUrl, icon/screenshots (base64, up to 4 screenshots)", "App Center listing content and distribution rules."],
            ["CONNECTIONS", "connections[].name (unique, referenced later), params.clientId/clientSecret, params.provider (=CUSTOM), params.scopes, customConfig.tokenUrl/authorizationUrl/authorizationParams, authorizationMethod (header|body), scopeSeparator", "How your app authenticates to the external API/identity provider. One extension app can register multiple connections for multiple platforms."],
            ["EXTENSIONS", "extensions[].template (extension contract reference id provided by Docusign), extensions[].actionReferences[] (must match action names below)", "Which extension category this app fills (e.g. Connected Fields) and which actions implement it."],
            ["ACTIONS", "actions[].name/description, actions[].template (action contract reference id), actions[].connectionsReference (must equal a connections[].name), actions[].params (external API or API proxy endpoint)", "The individual functions that actually call out to the external platform."],
        ],
        [1.1 * inch, 4.1 * inch, 2.2 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "Manifest field trap: extensions[].template and actions[].template are both called template but point at different contract catalogs - an extension contract reference versus an action contract reference. Do not confuse them, and do not confuse actions[].connectionsReference (a name lookup) with an ID.",
        styles["Body"],
    )
)
story.append(p("API proxy note: if the external service does not conform to the Docusign Action schema, you place an API proxy in front of it to translate requests/responses into the expected shape before the action can call it.", styles["Body"]))
story.append(p("Supported extension categories (forms-based selector):", styles["H3"]))
story.append(
    table(
        ["Category", "Business meaning"],
        [
            ["Data Verification / Connected Fields", "Real-time verification of signer-provided data (bank account, SSN, address) against an external system of record. This is what Section 14C's extensionData tab wires into."],
            ["File Input Output", "Reads or writes files, split by official docs into cloud storage, system of record, and tabular format sub-types."],
            ["Data Input Output", "Reads data from an external system into Docusign, or writes Docusign data back out (mirrors Maestro's Read/Writeback steps below)."],
        ],
        [2.3 * inch, 5.1 * inch],
        styles["TableBody"],
    )
)
story.append(p("Test, publish, and manage lifecycle:", styles["H3"]))
story.append(
    table(
        ["Step", "What happens", "Exam memory"],
        [
            ["Test", "Developer Console App Testing page runs your app before publishing.", "Testing happens pre-publish, inside the same console."],
            ["Submit for review", "Publish to App Center -> Submit. Docusign reviews business, technical, security, and functional aspects.", "Review is mandatory even for private apps."],
            ["Status progression", "Draft -> In Review -> Approved (or Rejected) -> Live -> Discontinued.", "Only Approved apps can be clicked Publish to App Center to go Live."],
            ["Public distribution", "Click the App Center button to make an Approved app available to all customers.", "One click, no per-account step."],
            ["Private distribution", "Add each target production account's ID/GUID. Status is Pending until that account's admin accepts it in App Center, then becomes Accepted.", "Deleting a shared private app does not notify the account admin - be careful removing one already in use."],
            ["Manage", "Developer Console home lists your apps with name, distribution, status, last updated. The 3-dot menu opens App Overview, edits/downloads the manifest, or deletes the app.", "App ID is what you give Docusign Support if you need help with a specific extension app."],
        ],
        [1.25 * inch, 3.85 * inch, 2.4 * inch],
        styles["TableBody"],
    )
)
story.append(p("Extension apps inside Maestro (Workflow Builder) Apps Steps:", styles["H3"]))
story.append(
    table(
        ["Apps Step type", "What it does", "Example installed apps"],
        [
            ["Read Steps", "Import data from an external system into the running workflow.", "Salesforce, HubSpot, Dynamics 365"],
            ["Store Files Steps", "Automate storing completed agreements or ID Evidence data externally.", "Google Drive, Box, Dropbox, Salesforce, OneDrive, SharePoint"],
            ["Writeback Steps", "Automate pushing information updates back to an external system.", "Salesforce, HubSpot, Stripe, ServiceNow, Dynamics 365"],
        ],
        [1.5 * inch, 3.2 * inch, 2.8 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "Memory bridge: an extension app is the platform object a developer builds and publishes once; a Connected Fields tab (Section 14C) and a Maestro Apps Step are two different extension points that trigger it at runtime - one inside an eSignature envelope, one inside a workflow. An admin must install/authorize the app on the account before either extension point can use it.",
        styles["Body"],
    )
)
story.append(p("Exam traps - Extension Apps:", styles["H3"]))
story.append(
    table(
        ["If the question says...", "Do not confuse with...", "Correct answer clue"],
        [
            ["Where is the extension app actually configured?", "The eSignature envelope/template", "Docusign Developer Console, registered separately with its own App ID, then installed/authorized on an account."],
            ["What identifies the extension app to Docusign Support?", "clientId (OAuth integration key) or accountId", "App ID, assigned when the app is created in the Developer Console."],
            ["How does an extension app authenticate to the external service?", "The signer's Docusign access token", "A connections object in the manifest (clientId/clientSecret/provider/scopes/customConfig), unrelated to the signer's Docusign OAuth session."],
            ["How is an extension app actually triggered for a signer?", "A direct API call from the extension app to eSignature", "An extension point - a Connected Fields tab (extensionData) or a Maestro Apps Step - fires the action at the right moment."],
            ["Can any private app author target any customer account?", "Public App Center visibility", "No - private distribution requires the target account's ID/GUID and Pending/Accepted admin approval."],
        ],
        [2.0 * inch, 2.0 * inch, 3.5 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "For the full Extension Apps curriculum (extension contracts, action contracts, business scenario walkthroughs, and a complete glossary) see the companion guide: Docusign Extension Apps Exam Guide.",
        styles["Small"],
    )
)

story += section("15. Scopes Used by the Launcher")
story.append(p("In this project, scopes are collected in index.js and passed to Passport DocusignStrategy during Authorization Code login. The JWT flow in DSJwtAuth.js uses a similar broad scope string when requestJWTUserToken asks Docusign for an access token. After OAuth, scopes are not sent to every business API URL; the access token carries them, and each API checks whether the token has the scope it needs.", styles["Body"]))
story.append(p("Scope and response_type=code basics:", styles["H3"]))
story.append(
    table(
        ["Term", "Meaning", "Where it appears", "Example"],
        [
            ["scope", "Permission names requested for the access token.", "Authorization URL query string during login; JWT/token request during JWT flow; then stored inside the issued access token.", "scope=signature impersonation means the token can send envelopes and (with consent) impersonate the user via JWT."],
            ["response_type=code", "Tells Docusign to return an authorization code after user login/consent.", "Authorization URL query string.", "Docusign redirects back to /ds/callback?code={authorization_code}."],
            ["authorization code", "Short-lived one-time code, not the access token.", "Returned to your app's redirect URI.", "Your backend exchanges code at POST /oauth/token."],
            ["access_token", "Temporary token that carries the approved scopes.", "Sent in API request header after login.", "Authorization: Bearer {access_token}."],
            ["API request body", "Business data for the action being performed.", "POST/PUT API request body.", "For Envelopes:create, the body has emailSubject, documents, recipients, and status."],
        ],
        [1.35 * inch, 2.05 * inch, 2.1 * inch, 1.8 * inch],
        styles["Small"],
    )
)
story.append(p("More scope examples: Maestro, Web Forms, Agreement Manager / Navigator", styles["H3"]))
story.append(
    table(
        ["Product", "Scopes requested in OAuth", "OAuth URL example", "API call after token", "Why scope is needed"],
        [
            [
                "Maestro",
                "aow_manage, often signature if workflow sends envelopes",
                "GET https://account-d.docusign.com/oauth/auth?response_type=code&scope=aow_manage signature&client_id={integrationKey}&redirect_uri={redirectUri}",
                "POST https://api-d.docusign.com/v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger",
                "aow_manage lets the app trigger/manage workflows. signature may be needed when workflow/eSignature steps require envelope access.",
            ],
            [
                "Web Forms",
                "webforms_read, webforms_instance_write, webforms_instance_read",
                "GET https://account-d.docusign.com/oauth/auth?response_type=code&scope=webforms_read webforms_instance_write webforms_instance_read&client_id={integrationKey}&redirect_uri={redirectUri}",
                "POST https://apps-d.docusign.com/api/webforms/v1.1/accounts/{accountId}/forms/{formId}/instances",
                "Read Web Form definitions, create an instance, then read the submitted/created instance.",
            ],
            [
                "Agreement Manager / Navigator",
                "adm_store_unified_repo_read in this project scope set for agreement repository/connected data where exposed",
                "GET https://account-d.docusign.com/oauth/auth?response_type=code&scope=adm_store_unified_repo_read&client_id={integrationKey}&redirect_uri={redirectUri}",
                "GET https://api-d.docusign.com/v1/accounts/{accountId}/agreements or IAM/Navigator agreement list/get calls used by the SDK",
                "Read agreement records, agreement metadata, or repository-backed agreement data where the account/API exposes it.",
            ],
        ],
        [1.0 * inch, 1.35 * inch, 2.25 * inch, 1.75 * inch, 1.55 * inch],
        styles["Small"],
    )
)
story.append(p("Example bodies: Maestro trigger uses instance_name and trigger_inputs; Web Forms create instance sends form field values; Agreement Manager/Navigator read calls are usually GET calls with the Bearer token and no business body.", styles["Body"]))
story.append(p("Important URL encoding note for multiple scopes:", styles["H3"]))
story.append(
    table(
        ["How it is written for learning", "Real URL encoding", "Meaning"],
        [
            ["scope=aow_manage signature", "scope=aow_manage%20signature", "Scopes are separated by a space, but a real URL should encode that space as %20."],
            ["scope=webforms_read webforms_instance_write", "scope=webforms_read%20webforms_instance_write", "Multiple scopes are still one scope query parameter, not separate scope parameters."],
            ["scope=click.manage click.send", "scope=click.manage+click.send", "Some clients encode the space as +. %20 and + are both common URL-encoded forms for spaces in query strings."],
        ],
        [2.15 * inch, 2.05 * inch, 3.1 * inch],
        styles["Small"],
    )
)
story.append(p("Exam memory: Docusign scopes are space-separated conceptually. In the real browser URL, the space must be URL-encoded, for example aow_manage%20signature. Do not send two separate scope parameters.", styles["Body"]))
story.append(p("Where scopes are sent by flow:", styles["H3"]))
story.append(
    table(
        ["Flow / request", "Where scope is sent", "Example", "Do not confuse with"],
        [
            ["Authorization Code login", "OAuth authorization URL query string.", "GET /oauth/auth?response_type=code&scope=aow_manage%20signature&client_id={integrationKey}&redirect_uri={redirectUri}", "This is before the access token exists."],
            ["Authorization Code with PKCE", "OAuth authorization URL query string, same scope location as normal Authorization Code.", "GET /oauth/auth?response_type=code&scope=webforms_read%20webforms_instance_write&code_challenge={challenge}&code_challenge_method=S256", "PKCE adds code_challenge/code_verifier; it does not move scope to the API body."],
            ["JWT Grant", "JWT/token request scope value used when requesting the token.", "requestJWTUserToken(clientId, impersonatedUserGuid, scopes, rsaKey, jwtLifeSec)", "This is not a browser /oauth/auth URL flow."],
            ["Normal Docusign API call after login", "Scope text is not sent in URL or body. The Authorization header sends the access token that already carries the scopes.", "Authorization: Bearer {access_token}", "The POST body is business data, such as envelopeDefinition, trigger_inputs, or form values."],
        ],
        [1.55 * inch, 2.0 * inch, 2.55 * inch, 1.7 * inch],
        styles["Small"],
    )
)
story.append(p("Short rule: in browser OAuth login, scopes are in the URL. In normal product API calls, scopes are not in the URL or body; Docusign reads them from the Bearer token.", styles["Body"]))
story.append(p("Access token, refresh token, and extended scope:", styles["H3"]))
story.append(
    table(
        ["OAuth flow", "Access token?", "Refresh token?", "Where extended fits"],
        [
            ["Authorization Code Grant", "Yes. The code is exchanged at /oauth/token for an access_token.", "Usually yes when long-lived access is allowed and extended scope is requested.", "extended is requested with signature in the OAuth URL, for example scope=signature%20extended."],
            ["Authorization Code + PKCE", "Yes. The code plus code_verifier is exchanged for an access_token.", "Usually yes when extended scope is requested/allowed.", "Same idea as Authorization Code; PKCE changes client proof, not the meaning of extended."],
            ["JWT Grant", "Yes. The signed JWT assertion is exchanged for an access_token.", "No refresh token. When the access token expires, create/sign a new JWT assertion and call /oauth/token again.", "JWT commonly uses scopes such as signature impersonation. extended is not the refresh-token mechanism for JWT."],
            ["Refresh Token Grant", "Yes. The refresh_token is exchanged for a new access_token.", "It uses an existing refresh_token; the response may rotate/return another refresh_token depending on policy.", "This flow exists because the original OAuth login had refresh-token permission, commonly through extended."],
        ],
        [1.55 * inch, 1.9 * inch, 2.05 * inch, 2.3 * inch],
        styles["Small"],
    )
)
story.append(p("Exam memory: every OAuth flow that successfully authenticates produces an access_token for API calls. Refresh tokens are not for every flow; JWT Grant does not use refresh tokens. extended is a Docusign OAuth scope, like signature, but its job is long-term/refresh-token style access, not permission to create envelopes.", styles["Body"]))
story.append(p("PKCE and code_challenge:", styles["H3"]))
story.append(p("PKCE means Proof Key for Code Exchange. It is an Authorization Code flow variant for apps that cannot safely store a client secret, such as SPA/native/public-client style apps. Instead of proving itself with a client secret, the app proves it owns the original code_verifier.", styles["Body"]))
story.append(
    table(
        ["Term", "Where it lives", "What it means", "Exam memory"],
        [
            ["code_verifier", "Created inside your app and kept temporarily until token exchange.", "A high-entropy random secret string.", "Do not send it in the first browser URL. Send it later to /oauth/token."],
            ["code_challenge", "OAuth authorize URL query string.", "SHA-256 hash of code_verifier, base64url encoded.", "This is the public proof sent before login."],
            ["code_challenge_method=S256", "OAuth authorize URL query string.", "Tells Docusign the challenge was made using SHA-256.", "S256 is the normal secure method."],
            ["authorization_code", "Redirect URI query string after user login.", "Temporary code returned by Docusign.", "The code alone is not enough in PKCE; token exchange also needs code_verifier."],
            ["access_token", "Response from POST /oauth/token.", "Bearer token used in later API headers.", "After PKCE finishes, normal API calls look the same as other OAuth flows."],
        ],
        [1.25 * inch, 1.8 * inch, 2.25 * inch, 2.2 * inch],
        styles["Small"],
    )
)
story.append(p("PKCE step flow:", styles["H3"]))
story.append(
    table(
        ["Step", "Request / URL", "Important fields", "What happens"],
        [
            ["1. Create verifier", "Local app memory", "code_verifier={randomSecret}", "Your app creates and temporarily stores the verifier."],
            ["2. Create challenge", "Local app memory", "code_challenge=BASE64URL(SHA256(code_verifier))", "Your app derives a public challenge from the private verifier."],
            ["3. Start login", "GET https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20extended&client_id={integrationKey}&redirect_uri={redirectUri}&code_challenge={codeChallenge}&code_challenge_method=S256", "response_type=code, scope, client_id, redirect_uri, code_challenge, code_challenge_method", "Browser goes to Docusign login/consent. code_challenge is visible in this URL."],
            ["4. Callback", "{redirectUri}?code={authorization_code}", "code={authorization_code}", "Docusign redirects back to your app with a temporary authorization code."],
            ["5. Token exchange", "POST https://account-d.docusign.com/oauth/token", "grant_type=authorization_code, code, redirect_uri, client_id, code_verifier", "Your app sends the original verifier in the body. Docusign hashes it and compares it to the earlier challenge."],
            ["6. Use token", "Product API URL, for example POST /restapi/v2.1/accounts/{accountId}/envelopes", "Authorization: Bearer {access_token}", "No scope, code_challenge, or code_verifier is sent in normal product API calls."],
        ],
        [0.75 * inch, 2.75 * inch, 2.1 * inch, 1.9 * inch],
        styles["Small"],
    )
)
story.append(p("PKCE token request body:", styles["H3"]))
story.append(p("POST https://account-d.docusign.com/oauth/token\nContent-Type: application/x-www-form-urlencoded\n\ngrant_type=authorization_code&code={authorization_code}&redirect_uri={redirectUri}&client_id={integrationKey}&code_verifier={originalCodeVerifier}", styles["CodeBlock"]))
story.append(p("PKCE memory: code_challenge goes in the first browser OAuth URL. code_verifier goes later in the /oauth/token body. Docusign hashes the verifier and checks that it matches the earlier challenge. This protects the authorization code if it is intercepted.", styles["Body"]))
story.append(p("PKCE location, response, and creator memory:", styles["H3"]))
story.append(
    table(
        ["Question", "Short answer", "Example / exam memory"],
        [
            ["Where does code_challenge stay?", "In the first OAuth authorize URL query string.", "GET /oauth/auth?...&code_challenge={codeChallenge}&code_challenge_method=S256"],
            ["What is the response to that URL?", "Docusign redirects the browser to redirect_uri with code={authorization_code}.", "302 Location: {redirectUri}?code={authorization_code}. This is not the access_token yet."],
            ["Who creates code_challenge?", "Your app creates it at runtime.", "Your app creates code_verifier, hashes it with SHA-256, base64url-encodes it, then sends the result as code_challenge."],
            ["Can Apps and Keys create code_challenge?", "No. Apps and Keys stores configuration, not temporary PKCE values.", "Apps and Keys has Integration Key, Redirect URI, secret keys, RSA keys. PKCE challenge/verifier are created by your app for each login attempt."],
            ["Why are there verifier and challenge?", "One value is secret and one value is safe to expose.", "code_challenge is public in the URL. code_verifier is secret and sent later in the token body. Docusign checks SHA-256(code_verifier) against code_challenge."],
        ],
        [1.65 * inch, 2.05 * inch, 3.5 * inch],
        styles["Small"],
    )
)
story.append(p("SHA-256 vs RS256:", styles["H3"]))
story.append(
    table(
        ["Term", "What it does", "Key used?", "Where used in Docusign OAuth"],
        [
            ["SHA-256", "Hashing algorithm. Turns data into a fixed fingerprint.", "No key.", "PKCE: creates code_challenge from code_verifier."],
            ["RS256", "JWT signing algorithm. RSA signature plus SHA-256.", "Yes. Private key signs; public key verifies.", "JWT Grant: signs the JWT header.payload so Docusign can verify the integration."],
        ],
        [1.1 * inch, 2.4 * inch, 1.55 * inch, 2.15 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: SHA-256 is hash only. RS256 is signing with RSA plus SHA-256. PKCE uses SHA-256 for code_challenge. JWT Grant uses RS256 to sign the JWT.", styles["Body"]))
story.append(p("Where response_type=code is used:", styles["H3"]))
story.append(
    table(
        ["Request type", "Has response_type=code?", "Example", "Why"],
        [
            ["OAuth Authorization Code login URL", "Yes", "GET https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id={integrationKey}&redirect_uri={redirectUri}", "Tells Docusign to send an authorization code to the redirect URI after login/consent."],
            ["OAuth Authorization Code with PKCE URL", "Yes", "GET /oauth/auth?response_type=code&scope=signature&code_challenge={challenge}&code_challenge_method=S256", "Still asks for a code; PKCE adds code_challenge for public-client security."],
            ["Token exchange", "No", "POST https://account-d.docusign.com/oauth/token", "This step exchanges the code for access_token; it uses grant_type, code, redirect_uri, and client authentication/PKCE verifier."],
            ["JWT Grant token request", "No", "POST https://account-d.docusign.com/oauth/token with JWT assertion", "JWT does not use browser authorize URL and does not ask for response_type=code."],
            ["Normal product API call", "No", "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger", "Business APIs use Authorization: Bearer {access_token}; no response_type is involved."],
        ],
        [1.55 * inch, 0.95 * inch, 3.15 * inch, 1.65 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: response_type=code belongs only to the OAuth authorize/login URL. It is not used in /oauth/token and not used in Docusign product API calls.", styles["Body"]))
story.append(p("JWT Grant detailed process:", styles["H3"]))
story.append(p("JWT Grant is for backend/service automation, for example a nightly job sending rental renewal envelopes without an interactive browser login each time. It requires one-time setup: Integration Key, impersonated user GUID, RSA key pair, and user/admin consent.", styles["Body"]))
story.append(
    table(
        ["Step", "Request / object", "Important IDs / values", "What happens"],
        [
            ["0. Setup", "Apps and Keys / admin consent", "dsJWTClientId, impersonatedUserGuid, RSA private key, RSA public key, scopes", "Docusign stores the public key. Your backend keeps the private key. Consent allows the app to impersonate the user for approved scopes."],
            ["1. Build signed JWT", "Local backend object, then RSA signature", "iss={integrationKey}; sub={impersonatedUserGuid}; aud=account-d.docusign.com; scope='signature impersonation'; iat; exp", "Your backend creates a JWT claim set and signs it with the RSA private key."],
            ["2. Request token", "POST https://account-d.docusign.com/oauth/token", "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer; assertion={signed_jwt}", "Docusign verifies signature, iss, sub, aud, time window, consent, and scopes."],
            ["3. Receive token", "Token response", "access_token, token_type=Bearer, expires_in", "The token now carries the approved scopes."],
            ["4. Discover account", "GET https://account-d.docusign.com/oauth/userinfo", "Authorization: Bearer {access_token}; returns accounts[].account_id and accounts[].base_uri", "Your app gets accountId and baseUri, then builds basePath = baseUri + /restapi."],
            ["5. Call product API", "POST https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes", "Authorization: Bearer {access_token}; business body contains envelopeDefinition", "Docusign checks token scope, for example signature, then creates/sends the envelope."],
            ["6. Refresh by repeating JWT", "POST /oauth/token again with new signed JWT", "New iat/exp and signed_jwt", "When token expires, backend creates a new JWT and asks for a new access_token. No browser callback is needed."],
        ],
        [0.8 * inch, 2.0 * inch, 2.5 * inch, 2.0 * inch],
        styles["Small"],
    )
)
story.append(p("JWT token request body:", styles["H3"]))
story.append(p("POST https://account-d.docusign.com/oauth/token\nContent-Type: application/x-www-form-urlencoded\n\ngrant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion={signed_jwt}", styles["CodeBlock"]))
story.append(p("What assertion={signed_jwt} means:", styles["H3"]))
story.append(
    table(
        ["Term", "Where it is", "What it contains", "Exam memory"],
        [
            ["assertion", "Body field in POST /oauth/token.", "The value is the complete signed JWT string.", "assertion is not a URL parameter. It is form body data."],
            ["signed_jwt", "Value of the assertion body field.", "Three encoded parts: header.payload.signature.", "This is the object Docusign verifies before issuing access_token."],
            ["JWT header", "First part of signed_jwt.", "Algorithm/type, for example alg=RS256 and typ=JWT.", "RS256 means RSA signature with SHA-256."],
            ["JWT payload / claim set", "Second part of signed_jwt.", "Claims such as iss, sub, aud, scope, iat, exp.", "The claim set is JSON data inside the JWT, not a URL."],
            ["JWT signature", "Third part of signed_jwt.", "RSA signature created with your private key.", "Docusign verifies it with the public key saved on the integration."],
        ],
        [1.15 * inch, 1.65 * inch, 2.35 * inch, 2.15 * inch],
        styles["Small"],
    )
)
story.append(p("RS256 memory: RS256 is the JWT signing algorithm. Your backend signs the JWT header and payload with the RSA private key using RS256; Docusign verifies the signature using the RSA public key stored for the Integration Key. This proves the JWT came from the holder of the private key.", styles["Body"]))
story.append(p("Inside the signed JWT assertion:", styles["H3"]))
story.append(p("{\n  \"iss\": \"{integrationKey}\",\n  \"sub\": \"{impersonatedUserGuid}\",\n  \"aud\": \"account-d.docusign.com\",\n  \"scope\": \"signature impersonation\",\n  \"iat\": 1720000000,\n  \"exp\": 1720003600\n}", styles["CodeBlock"]))
story.append(p("JWT assertion fields:", styles["H3"]))
story.append(
    table(
        ["Field", "What it is", "Relevant example", "Why Docusign checks it"],
        [
            ["iss", "Issuer. This is the Integration Key / client ID of the app requesting the token.", "iss='a7f9c2d1-...'; in this project dsJWTClientId.", "Identifies which Docusign app/integration is making the JWT request."],
            ["sub", "Subject. This is the Docusign user GUID being impersonated.", "sub='6b12f3aa-...'; in this project impersonatedUserGuid.", "Identifies which Docusign user the backend app is acting as."],
            ["aud", "Audience. This is the Docusign OAuth server that should accept the JWT.", "Demo: account-d.docusign.com. Production: account.docusign.com.", "Prevents a JWT meant for one auth server/environment from being accepted somewhere else."],
            ["scope", "Requested permissions for the access token.", "signature impersonation, or signature impersonation aow_manage when workflow access is needed.", "Docusign checks whether these scopes were consented and allowed for the integration/user."],
            ["iat", "Issued at time, as a Unix timestamp.", "1720000000.", "Shows when the JWT was created so Docusign can reject stale or invalid timing."],
            ["exp", "Expiration time, as a Unix timestamp.", "1720003600.", "Limits how long the signed JWT assertion can be used."],
        ],
        [0.6 * inch, 2.25 * inch, 2.2 * inch, 2.25 * inch],
        styles["Small"],
    )
)
story.append(p("Business memory: for an automated rental renewal job, iss is the backend app, sub is the Docusign user the app acts as, aud is the Docusign OAuth server, scope is what the app may do, and iat/exp define the short valid time window for the signed JWT.", styles["Body"]))
story.append(p("Docusign validation memory: Docusign verifies that the app is real, the user is real, the RSA signature matches the public key, consent exists, requested scopes are allowed, and the JWT is within the iat/exp time window. If those checks pass, Docusign returns an access_token.", styles["Body"]))
story.append(p("JWT memory: Authorization Code uses response_type=code and a browser redirect. JWT Grant uses grant_type=jwt-bearer and a signed JWT assertion. There is no /oauth/auth URL, no response_type=code, and no redirect URI callback in the token request.", styles["Body"]))
story.append(p("How Docusign checks whether the token has the needed scope:", styles["H3"]))
story.append(
    table(
        ["Case", "Scopes approved when token was created", "Same API call later", "Docusign decision"],
        [
            [
                "Token has required scope",
                "scope=aow_manage%20signature, so the issued access token carries aow_manage and signature.",
                "POST /v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger with Authorization: Bearer {access_token}",
                "Allowed, because this Maestro trigger API requires aow_manage and the token has it.",
            ],
            [
                "Token missing required scope",
                "scope=signature only, so the issued access token carries signature but not aow_manage.",
                "Same Maestro trigger API call with Authorization: Bearer {access_token}",
                "Rejected, because the API still requires aow_manage but the token does not have it.",
            ],
        ],
        [1.45 * inch, 2.15 * inch, 2.35 * inch, 1.35 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: the API URL and body can be identical in both cases. The result changes because the access token was created with different approved scopes.", styles["Body"]))
story.append(p("Memory: response_type=code asks for the temporary authorization code. scope asks for permissions. The later API call does not send scope text; it sends the access token in the Authorization header, and the body contains the business data.", styles["Body"]))
story.append(
    table(
        ["Scope", "Product area", "API / URL example", "Where used in project", "Why it is used"],
        [
            ["signature", "eSignature", "{basePath}/v2.1/accounts/{accountId}/envelopes, /templates, /brands", "SCOPES, ROOM_SCOPES, CLICK_SCOPES, MONITOR_SCOPES, ADMIN_SCOPES, NOTARY_SCOPES, CONNECTED_FIELDS_SCOPES, MAESTRO_SCOPES; eSignature /eg001-/eg046 examples", "Core permission for envelope, recipient, template, tab, brand, and many eSignature operations."],
            ["impersonation", "JWT", "POST https://account-d.docusign.com/oauth/token using JWT grant", "MONITOR_SCOPES and JWT consent URL in DSJwtAuth.js", "Allows a JWT/service integration to act as an authorized user after consent; also used by Monitor examples."],
            ["organization_read", "Admin / Notary", "GET https://api-d.docusign.net/management/v2/organizations", "ADMIN_SCOPES and NOTARY_SCOPES", "Read organization-level data needed for admin and notary examples."],
            ["group_read", "Admin", "Admin group APIs", "ADMIN_SCOPES; group/permission examples", "Read Docusign groups."],
            ["permission_read", "Admin", "Product permission profile APIs", "ADMIN_SCOPES; permission profile examples", "Read permission profiles before assigning or updating users."],
            ["user_read", "Admin", "GET .../organizations/{organizationId}/users", "ADMIN_SCOPES; get/audit users", "Read organization user records."],
            ["user_write", "Admin", "POST/PATCH .../organizations/{organizationId}/users", "ADMIN_SCOPES; create/update/import user examples", "Create or update organization users."],
            ["account_read", "Admin", "Admin account APIs", "ADMIN_SCOPES; create user/account examples", "Read account information for admin operations."],
            ["domain_read", "Admin", "Domain APIs", "ADMIN_SCOPES", "Read organization domain information."],
            ["identity_provider_read", "Admin", "Identity provider APIs", "ADMIN_SCOPES", "Read SSO/identity provider configuration."],
            ["user_data_redact", "Admin", "User data deletion/redaction APIs", "ADMIN_SCOPES; delete user data examples", "Delete or redact user data where allowed."],
            ["asset_group_account_read", "Admin", "Asset group account APIs", "ADMIN_SCOPES; clone/create account examples", "Read asset group account data."],
            ["asset_group_account_clone_write", "Admin", "Clone account APIs", "ADMIN_SCOPES; clone account", "Start account clone operations."],
            ["asset_group_account_clone_read", "Admin", "Clone account APIs", "ADMIN_SCOPES; clone account", "Read clone operation status/results."],
            ["organization_sub_account_write", "Admin", "Sub-account creation APIs", "ADMIN_SCOPES; create account", "Create sub-accounts in an organization."],
            ["organization_sub_account_read", "Admin", "Sub-account APIs", "ADMIN_SCOPES; create account", "Read organization sub-account data."],
            ["webforms_read", "Web Forms", "GET https://apps-d.docusign.com/api/webforms/v1.1/accounts/{accountId}/forms", "WEBFORMS_SCOPES; /web001 and /web002", "Read Web Form definitions."],
            ["webforms_instance_read", "Web Forms", "GET .../form_instances/{instanceId}", "WEBFORMS_SCOPES; Web Form instance examples", "Read a created Web Form instance."],
            ["webforms_instance_write", "Web Forms", "POST .../forms/{formId}/instances", "WEBFORMS_SCOPES; create Web Form instance", "Create Web Form instances."],
            ["notary_read", "Notary", "Notary configuration APIs", "NOTARY_SCOPES; third-party notary example", "Read notary-related configuration."],
            ["notary_write", "Notary", "eSignature envelope with notary recipient", "NOTARY_SCOPES; third-party notary example", "Create/send notary-related envelope work."],
            ["adm_store_unified_repo_read", "Connected Fields", "IAM / connected fields repository APIs", "CONNECTED_FIELDS_SCOPES; connected fields example", "Read connected field source/repository data."],
            ["aow_manage", "Maestro", "POST https://api-d.docusign.com/v1/accounts/{accountId}/workflows/{workflowId}/actions/trigger", "MAESTRO_SCOPES; /maestro001-/maestro004", "Trigger and manage Maestro workflows."],
        ],
        [1.3 * inch, 1.05 * inch, 1.85 * inch, 1.75 * inch, 1.35 * inch],
        styles["Small"],
    )
)
story.append(p("OAuth request shape: GET https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature click.manage click.send ...&client_id={integrationKey}&redirect_uri={redirectUri}. API call shape after login: Authorization: Bearer {access_token}. Docusign checks the token scopes against the API being called.", styles["Body"]))
story.append(p("Exam trap: OAuth scopes authorize the app token. Recipient authentication, access codes, IDV, and brands are envelope/account features, not OAuth scopes.", styles["Body"]))

story += section("16. Rate Limits and Response Headers")
story.append(p("Rate limits control how many API requests your app can make in a time window. In many Docusign eSignature exam contexts, remember 3,000 API calls per account per hour as the standard hourly API-call limit. Other Docusign products/accounts can have their own limits, so runtime headers are the source of truth for the current request.", styles["Body"]))
story.append(
    table(
        ["Item", "Meaning", "Example", "Why it matters"],
        [
            ["Rate limit window", "The time bucket used for counting requests.", "For eSignature exam memory: 1 hour.", "When the window resets, the remaining-call counter refreshes."],
            ["Allowed calls", "How many requests can be made in that window.", "For eSignature exam memory: 3,000 API calls per account per hour.", "If the app burns through the limit, more calls can be rejected/throttled until reset."],
            ["x-ratelimit-remaining", "How many requests are still available in the current window.", "x-ratelimit-remaining: 50", "Use it to slow down or stop non-urgent calls before hitting zero."],
            ["x-ratelimit-reset", "When the current window resets. The project treats it as Unix epoch seconds.", "x-ratelimit-reset: 1720700000", "Convert to a Date and retry after that time if needed."],
            ["429 / rate-limit error", "Possible response when too many requests are made.", "Too Many Requests / rate limit reached", "Back off and retry after reset instead of looping immediately."],
        ],
        [1.35 * inch, 2.05 * inch, 1.75 * inch, 2.15 * inch],
        styles["Small"],
    )
)
story.append(p("Example API call and response headers:", styles["H3"]))
story.append(p("GET https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes\nAuthorization: Bearer {access_token}\n\nResponse headers:\nx-ratelimit-remaining: 50\nx-ratelimit-reset: 1720700000", styles["CodeBlock"]))
story.append(p("Project code pattern:", styles["H3"]))
story.append(p("remaining = headers['x-ratelimit-remaining']; reset = headers['x-ratelimit-reset']; resetInstant = new Date(Number(reset) * 1000)", styles["CodeBlock"]))
story.append(p("JWT timer vs rate-limit timer:", styles["H3"]))
story.append(
    table(
        ["Timer", "Controls", "Example", "If it runs out"],
        [
            ["JWT iat/exp", "How long the signed JWT assertion can be used to request a token.", "iat=1720000000, exp=1720003600", "The JWT token request fails; create a new signed JWT."],
            ["Access token expires_in", "How long the Bearer access token can be used for API calls.", "expires_in: 3600", "API calls using that token fail; request a new token."],
            ["Rate-limit reset", "When the API usage quota refreshes.", "x-ratelimit-reset: 1720700000", "Wait until reset; then the request allowance is refreshed."],
        ],
        [1.45 * inch, 2.5 * inch, 1.75 * inch, 1.6 * inch],
        styles["Small"],
    )
)
story.append(p("Memory: JWT/access-token timers protect authentication. Rate-limit reset controls traffic. A JWT can be valid while the API is rate-limited, and a rate-limit window can be available while your token is expired.", styles["Body"]))

story += section("17. Security and Production Notes")
story.append(
    bullets(
        [
            "Never commit config/private.key, config/appsettings.json, client secrets, refresh tokens, or generated JWT private keys.",
            "Use demo OAuth/account base paths for developer accounts and production OAuth/account base paths after go-live.",
            "For Authorization Code Grant, production apps should use refresh tokens securely instead of forcing repeated login.",
            "For JWT, consent is required before token requests succeed; admin consent may be appropriate for organization-wide service use.",
            "Cache baseUri/account selection, but be prepared to refresh it from /oauth/userinfo.",
            "Use Connect webhooks for event-driven status instead of frequent envelope polling.",
            "Validate webhook HMAC and make the listener idempotent.",
            "Use least-privilege scopes. The launcher asks for broad scopes because it demonstrates many products.",
        ],
        styles["Body"],
    )
)

story.append(PageBreak())
story += section("18. Exam-Style Technical Distinctions")
story.append(
    table(
        ["Clue in question", "Best technical answer", "Why"],
        [
            ["User signs inside your app", "Embedded signing with clientUserId and createRecipientView", "Remote email signing does not keep signer in host app."],
            ["Server-side app, user present, can store secret", "Confidential Authorization Code Grant", "Interactive user auth with protected client secret."],
            ["Unattended nightly service", "JWT Grant with consent and impersonated user", "No interactive user present."],
            ["SPA/native public client", "Authorization Code with PKCE", "Client cannot safely store a secret."],
            ["Need accountId and base URI after login", "/oauth/userinfo", "Token endpoint alone does not give account selection for API calls."],
            ["Send immediately", "Envelope status='sent'", "created means draft."],
            ["Save draft for sender editing", "Envelope status='created' plus sender view if embedded sending", "Draft is editable before send."],
            ["Cancel active envelope", "Update envelope status to voided", "Deleting/restoring is folder movement, not cancellation."],
            ["Reusable template", "templateId + templateRoles", "templateRoles bind roleName to actual recipients."],
            ["Variable document layout", "Anchor tabs", "Coordinates are brittle when content shifts."],
            ["Avoid polling", "Connect webhook", "Push delivery is designed for status/event updates."],
            ["Validate webhook authenticity", "HMAC SHA-256 validation", "Compares Docusign signature with computed signature."],
            ["Collect structured intake before signing", "Web Forms or Workflow Collect Data step", "This is not just a signing URL."],
            ["Retrieve agreement repository metadata", "Navigator/Agreement API", "Envelope APIs handle signing transaction data."],
            ["Start repeatable business process via API", "Maestro workflow trigger with triggerInputs", "Workflow instance is separate from envelope creation."],
        ],
        [2.05 * inch, 2.55 * inch, 2.7 * inch],
        styles["TableBody"],
    )
)

story += section("19. Route Map From This App")
story.append(
    table(
        ["Local route prefix", "Product", "Meaning"],
        [
            ["/eg001 - /eg046", "eSignature", "Envelope, template, embedded signing, recipients, docs, tabs, auth, brands, bulk send, routing, document generation, shared access."],
            ["/weg001 - /weg002", "Web Forms", "Create/embed local or remote Web Form instances."],
            ["/mae001 - /mae004", "Maestro", "Trigger, publish, pause, resume, cancel workflows."],
            ["/nav001 - /nav002", "Navigator", "List agreements and get a single agreement."],
            ["/cneg001", "Connect", "Validate webhook HMAC."],
            ["/aeg001 - /aeg013", "Admin", "Create/import/audit/delete users, profile permissions, clone/create accounts."],
        ],
        [1.55 * inch, 1.3 * inch, 4.45 * inch],
        styles["TableBody"],
    )
)

story += section("20. One-Page Build Pattern to Memorize")
story.append(
    KeepTogether(
        [
            p("Most examples follow this pattern:", styles["H3"]),
            p("1. Ensure token is valid with req.dsAuth.checkToken().", styles["Body"]),
            p("2. Read req.user.accessToken or JWT auth accessToken plus req.session.accountId and req.session.basePath.", styles["Body"]),
            p("3. Create product SDK ApiClient.", styles["Body"]),
            p("4. Set basePath. For eSignature use session.basePath from userinfo. For product APIs use their product base path or IAM SDK.", styles["Body"]),
            p("5. Add Authorization: Bearer accessToken.", styles["Body"]),
            p("6. Create product API object such as EnvelopesApi, TemplatesApi, AccountsApi, FormInstanceManagementApi, or IamClient.", styles["Body"]),
            p("7. Build request object: EnvelopeDefinition, RecipientViewRequest, TemplateRole, CreateInstanceRequestBody, workflowDefinition, etc.", styles["Body"]),
            p("8. Call SDK method and persist returned IDs: envelopeId, templateId, formId, agreementId, workflowId, bulkListId.", styles["Body"]),
        ]
    )
)

story += section("21. Files Worth Re-reading Before the Exam")
story.append(
    bullets(
        [
            "lib/common/DSAuthCodeGrant.js - account discovery, basePath, token lifetime checks.",
            "lib/common/DSJwtAuth.js - JWT user token, consent_required handling, userinfo.",
            "lib/eSignature/examples/signingViaEmail.js - complete EnvelopeDefinition with documents, recipients, anchor tabs.",
            "lib/eSignature/examples/useTemplate.js - templateId and templateRoles.",
            "lib/eSignature/examples/embeddedSending.js and focusedView.js - sender/recipient view distinctions.",
            "lib/webforms/examples/createInstance.js - eSignature template plus Web Forms instance creation.",
            "lib/maestro/workflowUtils.js and triggerWorkflow.js - workflow definition and trigger inputs.",
            "lib/navigator/examples/*.js - agreement list/get calls.",
            "lib/connect/examples/validateWebhookMessage.js - HMAC validation.",
            "index.js - route registration and scope list.",
        ],
        styles["Body"],
    )
)

story.append(PageBreak())
story += section("22. Process Sequences to Memorize")
story.append(
    p(
        "The code-examples-node-master zip matches the Quickstart project already studied. This appendix adds the missing exam skill: knowing the order of operations. These are not new endpoints; they are the sequence in which the existing code uses them.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Process", "What comes after what"],
        [
            [
                "Authorization Code Grant login",
                "1. User opens local app -> 2. /ds/login clears old session -> 3. Passport redirects to Docusign /oauth/auth with scopes and redirect URI -> 4. User authenticates/consents -> 5. Docusign redirects to /ds/callback with authorization code -> 6. Passport exchanges code for tokens -> 7. Passport/profile calls userinfo -> 8. app stores accessToken, accountId, accountName, basePath -> 9. user returns to requested example.",
            ],
            [
                "JWT Grant login",
                "1. App has integration key, impersonated user GUID, RSA private key, scopes -> 2. requestJWTUserToken asks Docusign for access token -> 3. if consent_required, redirect user/admin to consent URL -> 4. after consent, request token again -> 5. getUserInfo with token -> 6. choose default or target account -> 7. store accountId and basePath -> 8. call examples without interactive user login.",
            ],
            [
                "Every SDK example",
                "1. Controller receives local GET/POST -> 2. checkToken decides whether auth is still valid -> 3. collect accountId, accessToken, basePath from session/user -> 4. create product ApiClient or IamClient -> 5. set product base path -> 6. add Authorization: Bearer token -> 7. build request body -> 8. call SDK method -> 9. save returned ID in session when later steps need it -> 10. render success page.",
            ],
            [
                "Remote envelope signing",
                "1. Build EnvelopeDefinition -> 2. add documents as base64 with documentId -> 3. add signer and optional carbon copy recipients -> 4. add tabs to signer -> 5. set status='sent' -> 6. createEnvelope -> 7. Docusign emails signer -> 8. signer completes remote ceremony -> 9. carbon copy receives completed copy if configured.",
            ],
            [
                "Embedded signing",
                "1. Build envelope -> 2. signer includes clientUserId -> 3. createEnvelope with status sent or created according to flow -> 4. call createRecipientView with same signer identity and clientUserId -> 5. app redirects/embeds recipient view URL -> 6. signer signs inside host app -> 7. Docusign returns browser to returnUrl.",
            ],
            [
                "Embedded sending",
                "1. Create draft envelope, usually status='created' -> 2. call createSenderView -> 3. redirect sender to Docusign sender UI -> 4. sender edits documents, recipients, tabs, and sends -> 5. signing proceeds according to recipient routing.",
            ],
            [
                "Template send",
                "1. Template exists in account -> 2. app builds EnvelopeDefinition with templateId -> 3. app supplies templateRoles matching template roleName values -> 4. set status='sent' -> 5. createEnvelope -> 6. Docusign merges real recipients into template roles and starts routing.",
            ],
        ],
        [1.75 * inch, 5.55 * inch],
        styles["TableBody"],
    )
)

story += section("23. More Process Sequences")
story.append(
    table(
        ["Process", "What comes after what"],
        [
            [
                "Create template if missing",
                "1. listTemplates with searchText -> 2. if existing template is found, reuse templateId -> 3. otherwise build EnvelopeTemplate -> 4. add documents, placeholder recipients, and tabs -> 5. set status='created' -> 6. createTemplate -> 7. store returned templateId for later envelope creation.",
            ],
            [
                "Document generation",
                "1. create template -> 2. update template document with doc-gen document data -> 3. create tabs for template recipient -> 4. create draft envelope from template -> 5. getEnvelopeDocGenFormFields -> 6. updateEnvelopeDocGenFormFields with field values -> 7. update envelope status to sent.",
            ],
            [
                "Bulk send",
                "1. Build bulk recipient lists -> 2. createBulkSendList returns listId -> 3. create envelope or draft for the batch -> 4. create envelope custom field that stores listId when needed -> 5. createBulkSendRequest using envelopeId and listId -> 6. poll getBulkSendBatchStatus for processing status.",
            ],
            [
                "Connect webhook validation",
                "1. Docusign sends webhook payload -> 2. listener keeps exact raw payload bytes/string -> 3. compute HMAC SHA-256 using configured Connect secret -> 4. base64 encode computed hash -> 5. compare with received signature using timingSafeEqual -> 6. if valid, process event idempotently -> 7. return success so Docusign does not retry unnecessarily.",
            ],
            [
                "Web Forms embedded instance",
                "1. Ensure backing eSignature template exists -> 2. list Web Forms by form name -> 3. build CreateInstanceRequestBody with clientUserId, formValues, expirationOffset -> 4. createInstance(accountId, formId) -> 5. app receives Web Form instance URL/data -> 6. app embeds or opens form for user.",
            ],
            [
                "Web Forms remote instance",
                "1. Ensure backing template exists -> 2. list target Web Form -> 3. build instance body with formValues and recipients -> 4. set sendOption='now' -> 5. createInstance -> 6. Docusign sends the Web Form/signing experience to recipient instead of embedding locally.",
            ],
            [
                "Maestro workflow lifecycle",
                "1. Create or choose workflow definition -> 2. publish workflow, handling consentUrl if returned -> 3. list active workflows -> 4. triggerWorkflow with instanceName and triggerInputs -> 5. workflow runs configured trigger, variables, participants, and steps -> 6. pause/resume affects new workflow instances -> 7. cancel operates on a specific workflow instance.",
            ],
        ],
        [1.75 * inch, 5.55 * inch],
        styles["TableBody"],
    )
)

story.append(PageBreak())
story += section("24. Under-Covered Technical Areas from code-examples-node-master")
story.append(
    table(
        ["Area", "Sequence and exam detail"],
        [
            [
                "Connected Fields",
                "1. IamClient calls connectedFields.tabInfo.getConnectedFieldsTabGroups({ accountId }) -> 2. app filters tab groups for Verify/actionContract or connecteddata tab labels -> 3. user chooses extension app/tab -> 4. app extracts connected-field extension metadata such as extensionGroupId, actionName, actionInputKey, connectionKey, connectionValue -> 5. app creates normal eSignature envelope -> 6. text tabs include extensionData and extensionPolicy='MustVerifyToSign' -> 7. signer must satisfy verification during signing. Exam distinction: Connected Fields are tabs with extension metadata, not a separate envelope type.",
            ],
            [
                "Third-party notary",
                "1. Build normal envelope document -> 2. add signer with notaryId linking signer to notary recipient -> 3. signer can also have clientUserId for embedded ceremony -> 4. add notary recipient under recipients.notaries -> 5. include notaryType='remote', notarySourceType='thirdparty', notaryThirdPartyPartner, seal/signature provider -> 6. add notarySealTabs and notary signHere tabs -> 7. createEnvelope. Exam distinction: notary is a recipient category with notary-specific tabs and provider metadata.",
            ],
        ],
        [1.75 * inch, 5.55 * inch],
        styles["TableBody"],
    )
)

story += section("25. Process Traps That Cause Wrong Exam Answers")
story.append(
    table(
        ["If the question says...", "Do not jump to...", "Correct sequence clue"],
        [
            ["Need to know accountId/base URI after OAuth", "Calling /oauth/token again", "Use /oauth/userinfo after token; choose account; set basePath."],
            ["Need signer inside app", "Remote email signing", "Add clientUserId, create envelope, then create recipient view."],
            ["Need sender to edit before send", "Recipient view", "Create draft envelope, then sender view."],
            ["Need structured intake before signature", "Only createRecipientView", "Create Web Form instance or workflow Collect Data before Get Signatures."],
            ["Need repeated business process with conditions", "Single envelope create call only", "Workflow definition -> publish -> trigger instance with inputs."],
            ["Need event status updates", "listStatusChanges every few seconds", "Configure Connect; validate HMAC; process idempotently."],
            ["Need agreement repository data", "Envelope documents/listStatusChanges", "Navigator agreement list/get after agreement exists."],
            ["Need ID check before access", "OAuth scope change", "Recipient authentication/IDV settings inside envelope recipient."],
            ["Need Connected Fields validation", "Plain text tab", "Text tab must carry extensionData and verification policy."],
            ["Need notarial ceremony", "Carbon copy or ordinary signer", "Use notaries recipient collection plus notary tabs/provider data."],
        ],
        [2.35 * inch, 2.05 * inch, 2.9 * inch],
        styles["TableBody"],
    )
)

story.append(PageBreak())
story += section("26. App URL Wrapper Versus Docusign API Routes")
story.append(
    p(
        "Your hosted app is the wrapper that users see. Docusign API base URLs are the backend targets your wrapper calls. In a hosted app such as https://www.abc.com, users mostly see your domain. Docusign API URLs usually happen server-side and do not appear in the browser address bar.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Concept", "Example", "Who uses it", "Purpose"],
        [
            [
                "appUrl",
                "https://www.abc.com",
                "Browser user and Docusign OAuth redirect",
                "Public face of your app: pages, forms, local Express routes, login callback, and return pages.",
            ],
            [
                "Express route",
                "https://www.abc.com/eg001 or /ds/login",
                "Browser calls your Node/Express app",
                "A local wrapper route. It may render a page or run controller code that calls Docusign APIs.",
            ],
            [
                "OAuth redirect URI",
                "https://www.abc.com/ds/callback",
                "Docusign sends the browser here after login/consent",
                "Return address for OAuth. It must match the redirect URI configured in the Docusign app.",
            ],
            [
                "Docusign OAuth URL",
                "https://account-d.docusign.com/oauth/auth",
                "Browser temporarily visits Docusign",
                "Login/consent page. After success, Docusign redirects back to your redirect URI.",
            ],
            [
                "Docusign API base URL",
                "https://demo.docusign.net/restapi",
                "Your backend server code",
                "Target for real API work, such as creating envelopes, getting documents, or listing recipients.",
            ],
        ],
        [1.35 * inch, 1.85 * inch, 1.8 * inch, 2.3 * inch],
        styles["TableBody"],
    )
)

story += section("27. Parallel Route Example: Your App Beside Docusign")
story.append(
    table(
        ["Step", "Your app route", "Docusign route/API", "What happens next"],
        [
            [
                "1. Open app",
                "GET https://www.abc.com/",
                "None",
                "Your app shows a home page or example launcher.",
            ],
            [
                "2. Start login",
                "GET https://www.abc.com/ds/login",
                "Browser is redirected to https://account-d.docusign.com/oauth/auth",
                "Your app asks Docusign to authenticate the user and grant scopes.",
            ],
            [
                "3. Login/consent",
                "None",
                "Docusign login and consent screen",
                "User signs in and approves requested scopes.",
            ],
            [
                "4. OAuth return",
                "GET https://www.abc.com/ds/callback?code=...",
                "Docusign redirects browser back with an authorization code",
                "Your app receives the code.",
            ],
            [
                "5. Token exchange",
                "Backend code inside /ds/callback",
                "POST https://account-d.docusign.com/oauth/token",
                "Your app exchanges the code for an access token.",
            ],
            [
                "6. Account discovery",
                "Backend code",
                "GET https://account-d.docusign.com/oauth/userinfo",
                "Your app gets accountId and base_uri, then builds basePath = base_uri + /restapi.",
            ],
            [
                "7. User opens example",
                "GET https://www.abc.com/eg001",
                "None",
                "Your app shows the send-envelope page/form.",
            ],
            [
                "8. User submits",
                "POST https://www.abc.com/eg001",
                "POST https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes",
                "Your backend creates the envelope through the Docusign API.",
            ],
            [
                "9. Embedded signing",
                "Your app redirects user",
                "POST /envelopes/{envelopeId}/views/recipient returns a signing URL",
                "Browser opens the Docusign signing ceremony URL.",
            ],
            [
                "10. Return after signing",
                "GET https://www.abc.com/ds-return",
                "Docusign redirects browser to returnUrl",
                "Your app shows completion/next-step page.",
            ],
        ],
        [0.8 * inch, 2.0 * inch, 2.45 * inch, 2.05 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "Exam memory shortcut: browser-visible wrapper routes belong to your appUrl; real work endpoints belong to Docusign API base URLs. OAuth is the exception where the browser temporarily visits Docusign and then returns to your redirect URI.",
        styles["Body"],
    )
)

story += section("28. Docusign IDs, Keys, and URIs")
story.append(
    p(
        "These values look similar because they all appear during authentication or API setup, but each one answers a different question: which user, which account, which app, which server, and which proof method.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Item", "What it is", "Where you get it", "Where it is used", "Why it is used"],
        [
            [
                "User ID",
                "The GUID of a Docusign user.",
                "Docusign Developer Admin -> Apps and Keys.",
                "JWT OAuth as the impersonated user, often sent as the JWT subject/sub value.",
                "Tells Docusign which human user the integration is acting for.",
            ],
            [
                "API Account ID",
                "The Docusign account identifier that owns envelopes, templates, users, and settings.",
                "Apps and Keys, or the /oauth/userinfo response.",
                "REST API paths such as /v2.1/accounts/{accountId}/envelopes.",
                "Tells the API which account's data should be read or changed.",
            ],
            [
                "Account Base URI",
                "The account-specific Docusign host/base server URI.",
                "Usually discovered from /oauth/userinfo after login.",
                "Builds the API base path, normally {base_uri}/restapi.",
                "Routes API calls to the correct Docusign environment and account cluster.",
            ],
            [
                "Integration Key",
                "The public identifier for your registered app. This is the OAuth client_id.",
                "Apps and Keys -> your app/integration.",
                "/oauth/auth and /oauth/token requests.",
                "Identifies which registered application is requesting authorization.",
            ],
            [
                "Secret Keys",
                "Private app passwords. These are OAuth client_secret values.",
                "Apps and Keys -> your app -> Add Secret Key. Store it when created.",
                "Authorization Code Grant token exchange on the backend.",
                "Proves the backend is allowed to exchange the authorization code for tokens.",
            ],
            [
                "RSA Key Pair",
                "A public/private key pair. Docusign stores the public key; your server keeps the private key.",
                "Apps and Keys -> your app -> Generate RSA.",
                "JWT Grant. Your server signs a JWT with the private key.",
                "Proves the JWT came from your integration without using an interactive login each time.",
            ],
        ],
        [0.75 * inch, 1.25 * inch, 1.35 * inch, 1.75 * inch, 1.75 * inch],
        styles["Small"],
    )
)
story.append(Spacer(1, 6))
story.append(
    table(
        ["Flow", "Values used", "Short reason"],
        [
            [
                "Authorization Code Grant",
                "Integration Key, Secret Key, Redirect URI, API Account ID, Account Base URI.",
                "The user logs in interactively, then your backend exchanges the code for an access token.",
            ],
            [
                "JWT Grant",
                "Integration Key, User ID, RSA private key, API Account ID, Account Base URI.",
                "Your backend impersonates a consenting user using a signed JWT instead of browser login.",
            ],
            [
                "Create Envelope API call",
                "Access token, API Account ID, Account Base URI.",
                "The token authorizes the call; the account ID and base URI locate the account.",
            ],
        ],
        [1.45 * inch, 2.55 * inch, 2.85 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Memory rule: Integration Key = which app; Secret Key = app password for auth code flow; User ID = which user for JWT; API Account ID = which account; Account Base URI = which server; RSA key pair = JWT proof.",
        styles["Body"],
    )
)

story += section("29. Envelope API Short Exam Map")
story.append(
    p(
        "Use this as the quick mental model for eSignature envelope calls in the Node quickstart.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Action", "Endpoint", "Important body/header", "What Docusign returns / what happens"],
        [
            [
                "Create draft envelope",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes",
                "Authorization: Bearer access_token. Body has documents, recipients, tabs, emailSubject, status='created'.",
                "Returns envelopeId. Envelope is saved as a draft and is not sent.",
            ],
            [
                "Create and send envelope",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes",
                "Same body, but status='sent'. Remote signing body does not include clientUserId.",
                "Returns envelopeId. Docusign starts routing and emails remote signers.",
            ],
            [
                "Send existing draft",
                "PUT {basePath}/v2.1/accounts/{accountId}/envelopes/{envelopeId}",
                "Body: {'status':'sent'}.",
                "Draft becomes active/in progress. Some fields are harder to change after sending.",
            ],
            [
                "Embedded signing - mark signer",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes",
                "Signer includes clientUserId plus email, name, recipientId, tabs. status is usually 'sent'.",
                "Returns envelopeId. clientUserId means your app will create the signing URL.",
            ],
            [
                "Embedded signing - get signing URL",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient",
                "Body has returnUrl, authenticationMethod, email, userName, clientUserId. Values must match the embedded signer.",
                "Returns url. In quickstart this is redirectUrl; Express redirects browser to it.",
            ],
            [
                "Embedded sending",
                "POST {basePath}/v2.1/accounts/{accountId}/envelopes then POST {basePath}/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/sender",
                "Usually create draft first with status='created', then createSenderView body includes returnUrl.",
                "Returns sender view URL. Sender edits/sends from Docusign sender UI.",
            ],
        ],
        [1.1 * inch, 2.0 * inch, 2.2 * inch, 1.75 * inch],
        styles["Small"],
    )
)
story.append(Spacer(1, 6))
story.append(
    table(
        ["Concept", "Short meaning", "Exam memory rule"],
        [
            [
                "recipientId",
                "Docusign recipient number inside the envelope.",
                "Connects tabs and recipient APIs to the correct envelope recipient.",
            ],
            [
                "clientUserId",
                "Your app's embedded signer ID.",
                "Present = embedded signer. Must match in createRecipientView.",
            ],
            [
                "redirectUrl",
                "The temporary signing URL returned by createRecipientView.",
                "Your app sends browser TO Docusign signing.",
            ],
            [
                "returnUrl",
                "Your app URL sent inside RecipientViewRequest.",
                "Docusign sends browser BACK here after complete, cancel, decline, or timeout.",
            ],
            [
                "Remote signing",
                "Docusign emails the signer.",
                "No clientUserId and no createRecipientView. Re-clicking email link reopens existing envelope if still active.",
            ],
            [
                "Embedded signing",
                "Your app requests the signing URL.",
                "If ttl_expired happens, call createRecipientView again for the same envelopeId.",
            ],
        ],
        [1.15 * inch, 2.4 * inch, 3.3 * inch],
        styles["Small"],
    )
)
story.append(Spacer(1, 6))
story.append(
    table(
        ["Status/event", "Where it applies", "Meaning"],
        [
            ["created", "Envelope status", "Draft, not sent."],
            ["sent", "Envelope status", "In progress, waiting for recipients."],
            ["delivered", "Envelope/recipient status", "Recipient opened/viewed signing."],
            ["completed", "Envelope status", "All required recipients finished."],
            ["declined", "Envelope status", "Recipient refused to sign."],
            ["voided", "Envelope status", "Sender canceled envelope."],
            ["expired", "Envelope status", "Envelope lifetime expired."],
            ["ttl_expired", "Embedded signing return event", "Temporary recipient view URL/session timed out; request a fresh recipient view URL."],
        ],
        [1.25 * inch, 1.85 * inch, 3.75 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Memory chain: createEnvelope returns envelopeId. Remote signing stops there because Docusign emails the signer. Embedded signing continues with createRecipientView, which returns redirectUrl. returnUrl is where signing sends the browser back.",
        styles["Body"],
    )
)

story += section("30. Embedded Signing Business Flow")
story.append(
    p(
        "Embedded signing means the signer starts in your app, your backend asks Docusign for a temporary signing URL, and Docusign returns the browser to your app when the signing ceremony ends.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Business step", "Your Express app", "Docusign API / URL", "Key body or return value"],
        [
            [
                "1. User opens signing task",
                "GET https://www.abc.com/eg001",
                "No Docusign API yet",
                "App shows a form/page for signer name and email.",
            ],
            [
                "2. User submits form",
                "POST https://www.abc.com/eg001",
                "Backend prepares createEnvelope call",
                "Controller checks access token and builds envelopeArgs.",
            ],
            [
                "3. Create envelope",
                "Backend only",
                "POST https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes",
                "Body includes documents, recipients.signers[], tabs, status='sent'. Signer has recipientId and clientUserId.",
            ],
            [
                "4. Docusign returns envelope",
                "Backend receives response",
                "Response from createEnvelope",
                "Docusign returns envelopeId. This identifies the exact envelope for later calls.",
            ],
            [
                "5. Ask for embedded signing URL",
                "Backend only",
                "POST https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient",
                "Body includes returnUrl, authenticationMethod, email, userName, clientUserId. These signer values must match the envelope signer.",
            ],
            [
                "6. Docusign returns recipient view",
                "Backend receives response",
                "Response from createRecipientView",
                "Docusign returns url. In this guide this is called redirectUrl.",
            ],
            [
                "7. Send signer to signing",
                "res.redirect(redirectUrl)",
                "Browser opens https://demo.docusign.net/signing/...",
                "redirectUrl means go TO Docusign signing.",
            ],
            [
                "8. Signer completes/cancels/times out",
                "Browser leaves Docusign",
                "Docusign redirects to returnUrl",
                "Example returnUrl: https://www.abc.com/ds-return?event=signing_complete or event=ttl_expired.",
            ],
            [
                "9. App handles result",
                "GET https://www.abc.com/ds-return",
                "Optional later API calls: GET envelope, recipients, documents",
                "If ttl_expired and envelope is still active, call createRecipientView again for the same envelopeId.",
            ],
        ],
        [1.15 * inch, 1.6 * inch, 2.2 * inch, 1.9 * inch],
        styles["Small"],
    )
)
story.append(Spacer(1, 6))
story.append(
    table(
        ["Field", "Where it appears", "Why it matters"],
        [
            [
                "clientUserId",
                "Signer in createEnvelope and recipientViewRequest in createRecipientView.",
                "Marks signer as embedded and must match between both calls.",
            ],
            [
                "recipientId",
                "Signer object and tabs/recipient APIs.",
                "Docusign's recipient number inside the envelope. Tabs attach to this recipient.",
            ],
            [
                "redirectUrl",
                "Returned by createRecipientView as response.url.",
                "Temporary Docusign signing URL. Your app redirects the browser to it.",
            ],
            [
                "returnUrl",
                "Sent by your app inside recipientViewRequest.",
                "Where Docusign sends the browser back after complete, cancel, decline, exception, or timeout.",
            ],
            [
                "authenticationMethod",
                "Sent by your app inside recipientViewRequest.",
                "Describes how your app authenticated the signer before embedded signing. It is not OAuth app authentication.",
            ],
        ],
        [1.25 * inch, 2.6 * inch, 3.0 * inch],
        styles["Small"],
    )
)
story.append(
    p(
        "Authentication memory rule: OAuth access token proves your backend can call Docusign APIs. recipientViewRequest.authenticationMethod describes how your app verified the signer before sending them into embedded signing. The quickstart uses authenticationMethod='none' for simplicity.",
        styles["Body"],
    )
)

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    leftMargin=0.55 * inch,
    rightMargin=0.55 * inch,
    topMargin=0.55 * inch,
    bottomMargin=0.55 * inch,
    title="Docusign Node Quickstart Technical Deep Dive",
    author="Codex",
)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(f"Wrote {OUT}")

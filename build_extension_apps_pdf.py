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


PRIMARY_OUT = Path("output/pdf/docusign_extension_apps_exam_guide.pdf")
FALLBACK_OUT = Path("output/pdf/docusign_extension_apps_exam_guide_updated.pdf")


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
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#5B2A86")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D7C6E8")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8F4FC")]),
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


def subsection(title: str) -> Paragraph:
    return p(title, styles["H3"])


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#526174"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(0.55 * inch, 0.35 * inch, "Docusign Extension Apps exam guide")
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
        textColor=colors.HexColor("#2E1147"),
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
        textColor=colors.HexColor("#5B2A86"),
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
        textColor=colors.HexColor("#2E1147"),
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
        textColor=colors.HexColor("#2E1147"),
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        "Small",
        parent=styles["Body"],
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#4B3A5A"),
    )
)
styles.add(
    ParagraphStyle(
        "CodeBlock",
        parent=styles["Body"],
        fontName="Courier",
        fontSize=7.3,
        leading=9.3,
        textColor=colors.HexColor("#241933"),
        backColor=colors.HexColor("#F3ECFA"),
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
styles.add(
    ParagraphStyle(
        "Callout",
        parent=styles["Body"],
        backColor=colors.HexColor("#FDE9D9"),
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6,
    )
)


story = []
story.append(p("Docusign Extension Apps Exam Guide", styles["TitleMain"]))
story.append(
    p(
        "Complete exam-focused reference: what extension apps are, how they are registered, the manifest schema, testing/publishing lifecycle, distribution, and how they connect to Connected Fields and Maestro Workflow Builder.",
        styles["Subtitle"],
    )
)
story.append(
    p(
        "Sources: Docusign University certification learning path \"Docusign Extension Apps\" (course: Build Extension Apps for the Docusign App Center) and the \"Get Started with Docusign for Developers\" course, both from the Certified Docusign IAM Integration & Extension Developer curriculum; supplemented with terminology confirmed against developers.docusign.com (Extension Apps 101, supported extensions, extension contracts, manifest/action/connection schema pages). Where the certification snapshot did not expose an exact REST endpoint or full schema enumeration, this guide says so explicitly rather than inventing one.",
        styles["Small"],
    )
)

# ---------------------------------------------------------------------------
story += section("1. What Is an Extension App?")
story.append(
    p(
        "An extension app is a registered platform object - a set of HTTP endpoints described by a manifest.json - that lets a third-party service plug functionality into Docusign at defined moments in an agreement or workflow. It is built and published through the self-serve Docusign Developer Console, separate from the Apps and Keys page used for plain OAuth integration keys.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Capability", "Business meaning", "Example"],
        [
            ["Archive documents", "Send completed agreements/evidence to an external store.", "Archive a signed contract to Google Drive or SharePoint."],
            ["Verify data", "Check signer-provided information against a trusted external source in real time.", "Verify a bank account number, SSN, or postal/email address before signing continues."],
            ["Read/write data back", "Pull data into Docusign or push Docusign data out to another system.", "Pull a customer record from Salesforce; write a signed status back to HubSpot."],
        ],
        [1.4 * inch, 3.0 * inch, 3.0 * inch],
        styles["TableBody"],
    )
)
story.append(
    table(
        ["Fact", "Detail"],
        [
            ["Where built", "Docusign Developer Console (self-serve)."],
            ["Where listed", "Docusign App Center. Production: apps.docusign.com/app-center. Demo: apps-d.docusign.com/app-center."],
            ["Distribution", "Public (any App Center customer can discover/install) or Private (only specific accounts you approve)."],
            ["Identifier", "Each registered app is assigned an App ID, used when contacting Docusign Support about that app."],
        ],
        [1.5 * inch, 6.0 * inch],
        styles["TableBody"],
    )
)
story.append(
    Table(
        [[p(
            "Exam trap: an extension app is not an API integration key (client_id/client_secret from Apps and Keys) and it is not an envelope or template. It is a separately registered, separately published object with its own App ID and its own lifecycle (Draft -> In Review -> Approved -> Live -> Discontinued).",
            styles["Body"],
        )]],
        colWidths=[7.4 * inch],
        style=TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FDE9D9")),
                ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#EFC08E")),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        ),
    )
)

# ---------------------------------------------------------------------------
story += section("2. Extension Apps vs Normal API Integrations")
story.append(
    table(
        ["Question", "API integration (Apps and Keys / OAuth)", "Extension app"],
        [
            ["Who calls whom?", "Your backend calls Docusign APIs directly (push model - you initiate every request).", "Docusign calls your app's endpoints when a signer/workflow reaches a configured extension point (pull-triggered by Docusign)."],
            ["What identifies it?", "Integration Key (client_id) plus a secret/RSA key.", "App ID, plus its own manifest-defined connections to the external service."],
            ["Where configured?", "Apps and Keys page; used with OAuth flows (Auth Code, JWT, PKCE).", "Developer Console; published to the App Center; installed/authorized per account by an admin."],
            ["Runtime trigger", "Your code, on your schedule.", "A Connected Fields tab or a Maestro Apps Step, triggered when a recipient reaches that point."],
            ["Distribution", "Not distributed - it is your own app's private credential.", "Can be published publicly so other Docusign customers can install and use it too."],
        ],
        [1.5 * inch, 2.95 * inch, 2.95 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "Rule of thumb: if the integration reads/writes Docusign data on your own schedule from your own backend, that is a plain API integration. If the integration should run automatically at a specific moment inside someone else's envelope or workflow - including other Docusign customers who install your app - that is an extension app.",
        styles["Body"],
    )
)

# ---------------------------------------------------------------------------
story += section("3. Core Building Blocks")
story.append(
    table(
        ["Block", "Definition", "Key fields"],
        [
            ["Manifest", "The JSON file (or forms-based equivalent) that fully describes an extension app: identity, auth, and behavior.", "APP DETAILS, CONNECTIONS, EXTENSIONS, ACTIONS (see Section 6)."],
            ["Connection", "The auth configuration your app uses to reach the external API or identity provider.", "name, params.clientId/clientSecret, params.provider, params.scopes, customConfig.*"],
            ["Extension", "Declares which extension category (contract) this app implements and which actions fulfill it.", "template (extension contract reference), actionReferences[]"],
            ["Action", "One callable function: the actual external API/API-proxy endpoint invoked when triggered.", "name, template (action contract reference), connectionsReference, params"],
            ["Extension point", "The place inside Docusign - an envelope field (Connected Fields tab) or a Maestro workflow step (Apps Step) - where an action can be triggered.", "Not a manifest field; it is where an admin/sender wires the published app into their own agreement or workflow."],
            ["Extension contract", "Docusign-defined template describing the set of actions/capabilities a given extension category must implement (e.g. a File Archive contract).", "Referenced by extensions[].template; you do not invent your own contract types."],
        ],
        [1.1 * inch, 3.4 * inch, 2.9 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "How they fit together: your manifest registers one or more Connections (how to auth), one or more Extensions (which contract categories you support), and one or more Actions (the real work, each tied to exactly one Connection via connectionsReference). Docusign triggers an Action at an Extension Point, your Action calls out through its Connection to the external API, and the response flows back into the Docusign agreement or workflow.",
        styles["Body"],
    )
)
story.append(
    p(
        "Customer experience vs developer experience: extension apps have two sides. The developer experience is what this guide covers - defining actions and mapping them to extension points. The customer experience is what an account admin sees - installing the app from the App Center, then a sender/user seeing a Connected Fields tab or Apps Step that uses it.",
        styles["Body"],
    )
)

# ---------------------------------------------------------------------------
story += section("4. Supported Extension Types")
story.append(
    p(
        "When registering via the forms-based experience, you choose at least one extension type. The certification course names four categories; developers.docusign.com further splits File Input Output by sub-format.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Extension type", "What it does", "Typical use case"],
        [
            ["Connected Fields (Data Verification)", "Performs real-time verification of signer-entered data against an external system of record, surfaced as a signing tab.", "Verify a bank account, SSN, or customer ID before the signer can proceed."],
            ["Data Input Output", "Reads external data into Docusign, or writes Docusign data out to an external system.", "Pull a CRM record to pre-fill a workflow; push a completed agreement's status back to Salesforce."],
            ["File Input Output - cloud storage", "Reads or writes whole files from/to a cloud storage provider.", "Import a document from Google Drive; archive a signed PDF to Box or Dropbox."],
            ["File Input Output - system of record", "Reads or writes files from/to a business system of record (not general cloud storage).", "Pull a contract template stored in an internal document management system."],
            ["File Input Output - tabular format", "Reads or writes structured/tabular file data.", "Import recipient rows for a bulk send from an external spreadsheet-like source."],
        ],
        [2.1 * inch, 2.7 * inch, 2.6 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "For a deep dive on telling File IO, Data IO, Data Verification, and Connected Fields apart (with worked examples and a dedicated exam-trap table), see the companion guide important_distinctions.pdf.",
        styles["Small"],
    )
)

# ---------------------------------------------------------------------------
story.append(PageBreak())
story += section("5. Registration Path A: Forms-Based Experience")
story.append(
    table(
        ["Step", "Action", "Detail"],
        [
            ["1", "Open Developer Console -> Create App -> Using a form-based experience.", "Requires a Docusign developer account."],
            ["2", "Complete \"Tell us about your app\".", "App name (must be unique), Published by / Support email, Distribution Type (Public or Private), and at least one Extension type."],
            ["3", "Click Create App.", "You land on the App Overview page. An App ID is assigned."],
            ["4", "Configure Integration Details -> Connection.", "Sets up how the app obtains authorization from the external API/identity provider (Basic Information, Parameters, Custom Config, Auth Params)."],
            ["5", "Configure Extensions & Actions.", "Provide extension name/description, then for each action: Name, Description, and Params URI. Click Add Extension to support more than one extension category."],
            ["6", "Configure App Center Listing.", "Icon and screenshots (up to four), basic app info, publisher/contact details, and distribution regions."],
        ],
        [0.5 * inch, 2.9 * inch, 4.0 * inch],
        styles["TableBody"],
    )
)

# ---------------------------------------------------------------------------
story += section("6. Registration Path B: Manifest File (JSON)")
story.append(
    p(
        "The manifest is edited in the Developer Console's built-in editor (real-time validation) or downloaded, edited locally, and re-uploaded. It has four logical parts, always built in this order because later parts reference earlier ones by name.",
        styles["Body"],
    )
)
story.append(subsection("6.1 APP DETAILS"))
story.append(
    table(
        ["Field", "Meaning"],
        [
            ["name", "Unique, descriptive app name. Shown in the App Center listing and in Workflow Builder / Agreement Manager / eSignature selectors."],
            ["publicationRegions", "Public apps only - which regions the app can be installed from."],
            ["distribution", "PUBLIC (any App Center user can install) or PRIVATE (only accounts you explicitly share with)."],
            ["description", "Short and long description shown on the listing."],
            ["publisher", "Organization name, email, phone, and website."],
            ["termsOfServiceUrl", "URLs for terms of service, privacy policy, and support."],
            ["icon / screenshots", "Base64-encoded images; up to four screenshots."],
        ],
        [1.6 * inch, 5.8 * inch],
        styles["TableBody"],
    )
)
story.append(subsection("6.2 CONNECTIONS"))
story.append(
    p(
        "A connections object holds everything needed to authenticate to one external API, API proxy, or identity provider. The connection name is unique within the manifest and is referenced later by actions. Register multiple connections to extend your workflow to multiple external platforms.",
        styles["Body"],
    )
)
story.append(
    table(
        ["Field (inside params)", "Meaning"],
        [
            ["clientId / clientSecret", "Credentials issued by the external platform or identity provider."],
            ["provider", "Set to CUSTOM in the certification course's examples."],
            ["scopes", "List of scopes requested during authorization."],
            ["customConfig.tokenUrl / authorizationUrl", "Endpoints used to get the access token and to authorize."],
            ["customConfig.authorizationParams", "Extra query parameters needed on the authorization endpoint."],
            ["customConfig.authorizationMethod", "header or body - where credentials are sent."],
            ["customConfig.scopeSeparator", "Delimiter used to join multiple requested scopes."],
        ],
        [2.3 * inch, 5.1 * inch],
        styles["TableBody"],
    )
)
story.append(subsection("6.3 EXTENSIONS"))
story.append(
    table(
        ["Field", "Meaning"],
        [
            ["template", "The unique string identifier of the predefined extension contract reference for your extension category, provided by Docusign."],
            ["actionReferences[]", "The names of the actions (defined in the ACTIONS section) that implement this extension."],
        ],
        [1.6 * inch, 5.8 * inch],
        styles["TableBody"],
    )
)
story.append(subsection("6.4 ACTIONS"))
story.append(
    table(
        ["Field", "Meaning"],
        [
            ["name / description", "Identifies the action; name is what actionReferences[] points back to."],
            ["template", "The action contract reference - the unique string ID of the contract template this action fulfills. Different catalog from the extension-level template."],
            ["connectionsReference", "Must equal the name of a connections[] entry - a name match, not an ID lookup."],
            ["params", "The external API endpoint (or API proxy endpoint) this action actually calls."],
        ],
        [1.6 * inch, 5.8 * inch],
        styles["TableBody"],
    )
)
story.append(
    Table(
        [[p(
            "Exam trap: extensions[].template and actions[].template share a field name but point at two different contract catalogs - an extension contract reference versus an action contract reference. And actions[].connectionsReference must exactly match a connections[].name string, not an App ID or client ID.",
            styles["Body"],
        )]],
        colWidths=[7.4 * inch],
        style=TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FDE9D9")),
                ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#EFC08E")),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        ),
    )
)
story.append(
    p(
        "If your external service does not conform to the Docusign Action schema, you set up an API proxy in front of it to translate requests/responses to the format Docusign expects, and point actions[].params at the proxy instead of the raw external endpoint.",
        styles["Body"],
    )
)
story.append(subsection("Illustrative manifest shape (structure only - values are placeholders):"))
story.append(
    p(
        "{\n"
        "  \"name\": \"Bank Account Verifier\",\n"
        "  \"distribution\": \"PRIVATE\",\n"
        "  \"description\": { \"short\": \"...\", \"long\": \"...\" },\n"
        "  \"publisher\": { \"name\": \"Acme Inc\", \"email\": \"support@acme.com\" },\n"
        "  \"connections\": [ {\n"
        "    \"name\": \"acmeAuth\",\n"
        "    \"params\": { \"clientId\": \"{clientId}\", \"clientSecret\": \"{clientSecret}\", \"provider\": \"CUSTOM\",\n"
        "      \"scopes\": [\"verify:bank\"],\n"
        "      \"customConfig\": { \"tokenUrl\": \"https://acme.example.com/oauth/token\",\n"
        "        \"authorizationUrl\": \"https://acme.example.com/oauth/authorize\",\n"
        "        \"authorizationMethod\": \"header\", \"scopeSeparator\": \" \" } }\n"
        "  } ],\n"
        "  \"extensions\": [ { \"template\": \"{connectedFieldsContractId}\", \"actionReferences\": [\"verifyBankAccount\"] } ],\n"
        "  \"actions\": [ {\n"
        "    \"name\": \"verifyBankAccount\", \"description\": \"Verify a bank account number\",\n"
        "    \"template\": \"{actionContractId}\", \"connectionsReference\": \"acmeAuth\",\n"
        "    \"params\": { \"uri\": \"https://acme.example.com/api/verify-bank\" }\n"
        "  } ]\n"
        "}",
        styles["CodeBlock"],
    )
)

# ---------------------------------------------------------------------------
story.append(PageBreak())
story += section("7. Test, Validate, Publish, and Manage")
story.append(
    table(
        ["Stage", "What happens", "Exam memory"],
        [
            ["Validate", "Manifest editor runs real-time validation; Validate button checks for errors before app creation.", "Catches structural/schema errors before Create App is even clickable for the manifest path."],
            ["Test", "App Testing page in the Developer Console.", "Testing happens pre-publish, inside the same console - not a separate sandbox account."],
            ["Submit for review", "Publish to App Center -> Submit.", "Review evaluates business, technical, security, and functional aspects. Required even for private apps."],
            ["Status progression", "Draft -> In Review -> Approved / Rejected -> Live -> Discontinued.", "Only an Approved app can be clicked Publish to App Center to actually go Live."],
            ["Resubmission", "If Docusign finds issues, you get guidance, fix, and resubmit for review.", "Rejected is not terminal - it is a loop back to fixing and resubmitting."],
            ["Go public", "Click the App Center button on an Approved public app.", "One click; no per-customer step for public apps."],
            ["Go private", "Add each target production account's ID (GUID) with an alias.", "Status is Pending until that account's admin accepts it in App Center; then Accepted."],
            ["Remove access", "Delete icon removes the app from a customer's account.", "The account administrator is NOT notified when you remove it - be careful if it is already in active use."],
            ["Manage", "Developer Console home lists name, distribution, status, last updated.", "Three-dot menu: return to App Overview, edit/download manifest, or delete the app."],
        ],
        [1.3 * inch, 3.15 * inch, 2.95 * inch],
        styles["TableBody"],
    )
)

# ---------------------------------------------------------------------------
story += section("8. Extension Apps Inside Maestro (Workflow Builder)")
story.append(
    p(
        "Workflow Builder is deliberately extensible to third-party products through extension apps an admin has authorized for the account. These show up as Apps Steps alongside native Docusign Steps (ID Verification, Web Forms, eSignature) and Utility Steps (branching, email, confirmation screens).",
        styles["Body"],
    )
)
story.append(
    table(
        ["Apps Step type", "What it automates", "Example installed apps"],
        [
            ["Read Steps", "Import data from an external system into the running workflow.", "Salesforce, HubSpot, Dynamics 365"],
            ["Store Files Steps", "Store completed agreements and ID Evidence data externally.", "Google Drive, Box, Dropbox, Salesforce, OneDrive, SharePoint"],
            ["Writeback Steps", "Push information updates back out to an external system.", "Salesforce, HubSpot, Stripe, ServiceNow, Dynamics 365"],
        ],
        [1.5 * inch, 3.2 * inch, 2.7 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "Mapping back to Section 4: Read Steps correspond to Data Input, Store Files Steps to File Output, and Writeback Steps to Data Output - the same extension categories a developer chose when registering the app, now surfaced as installable workflow steps for an admin.",
        styles["Body"],
    )
)

# ---------------------------------------------------------------------------
story += section("9. Extension Apps Inside eSignature: the Connected Fields Bridge")
story.append(
    p(
        "This is the runtime, signer-facing half of a Connected Fields / Data Verification extension app. A normal text tab carries an extensionData block that wires it to a published app's action.",
        styles["Body"],
    )
)
story.append(
    p(
        "{\n"
        "  \"tabType\": \"text\",\n"
        "  \"tabLabel\": \"connecteddata_customerId\",\n"
        "  \"required\": true,\n"
        "  \"extensionData\": {\n"
        "    \"applicationId\": \"{appId}\",\n"
        "    \"extensionGroupId\": \"{extensionGroupId}\",\n"
        "    \"actionName\": \"Verify\",\n"
        "    \"actionInputKey\": \"customerId\",\n"
        "    \"extensionPolicy\": \"MustVerifyToSign\",\n"
        "    \"connectionInstances\": [ { \"connectionKey\": \"{connectionKey}\", \"connectionValue\": \"{connectionValue}\" } ]\n"
        "  }\n"
        "}",
        styles["CodeBlock"],
    )
)
story.append(
    table(
        ["Field", "Bridges to..."],
        [
            ["applicationId (appId)", "The App ID assigned when the extension app was registered in the Developer Console (Section 1)."],
            ["actionName / actionInputKey", "The action's name and the specific input parameter it expects, as defined in the manifest ACTIONS section (Section 6.4)."],
            ["connectionKey / connectionValue", "Runtime values fed into the app's connection at signing time - not the same as the manifest's clientId/clientSecret, which are the app's own credentials to the external service."],
            ["extensionPolicy", "e.g. MustVerifyToSign - an eSignature-side enforcement rule, not a manifest field."],
        ],
        [2.1 * inch, 5.3 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "For the full Node.js SDK/API mechanics of building this tab and the surrounding envelope, see the companion guide docusign_node_quickstart_technical_deep_dive.pdf, Section 14C (Connected Fields workflow) and Section 14D (this extension-app platform context).",
        styles["Small"],
    )
)

# ---------------------------------------------------------------------------
story.append(PageBreak())
story += section("10. IDs and Terminology Glossary")
story.append(
    table(
        ["Term", "What it identifies", "Do not confuse with"],
        [
            ["App ID", "One registered extension app in the Developer Console.", "clientId (OAuth integration key) or accountId - different identifier families entirely."],
            ["clientId / clientSecret (connections)", "The extension app's own credentials to authenticate to the EXTERNAL service.", "The Docusign Integration Key/Secret used in Apps and Keys OAuth flows - unrelated."],
            ["connections[].name", "A local label inside one manifest, referenced by actions[].connectionsReference.", "Not a global ID - only unique within that manifest."],
            ["extensions[].template", "Extension contract reference (which extension category contract this fulfills).", "actions[].template, which is a different catalog (action contract reference)."],
            ["actions[].template", "Action contract reference (the shape of request/response this action must implement).", "extensions[].template - see above."],
            ["appId (in extensionData)", "The runtime reference, inside a Connected Fields tab, back to the registered App ID.", "accountId (whose Docusign account) or documentId/recipientId (where the tab lives)."],
            ["extensionGroupId, connectionKey/Value, actionInputKey", "Runtime wiring values inside a signing tab's extensionData that route to the right action/input/connection instance.", "The manifest's design-time connections[].name or actions[].name - related concepts, different values."],
            ["Extension point", "A location (Connected Fields tab or Maestro Apps Step) where an action can be triggered.", "The action or extension itself - the point is where it fires, not what it does."],
        ],
        [1.5 * inch, 2.9 * inch, 3.0 * inch],
        styles["TableBody"],
    )
)

# ---------------------------------------------------------------------------
story += section("11. Business Scenario Walkthrough: Bank Account Verification")
story.append(
    table(
        ["Step", "Who", "What happens"],
        [
            ["1", "Extension-app developer", "Registers \"Bank Account Verifier\" in the Developer Console with extension type Data Verification / Connected Fields; gets App ID."],
            ["2", "Extension-app developer", "Defines a connection to the bank's verification API (clientId/clientSecret, tokenUrl, authorizationUrl)."],
            ["3", "Extension-app developer", "Defines an extension referencing the Connected Fields contract, with one action \"verifyBankAccount\" whose params point at the bank's API endpoint."],
            ["4", "Extension-app developer", "Tests the app, submits for review, and (once Approved) publishes it - Private, shared with specific customer account GUIDs."],
            ["5", "Customer account admin", "Sees the app as Pending in App Center, accepts it - status becomes Accepted, app is installed on the account."],
            ["6", "Customer's own developer/sender", "Adds a text tab to an envelope/template with extensionData referencing the installed app's appId, actionName \"verifyBankAccount\", and extensionPolicy MustVerifyToSign."],
            ["7", "Signer", "Enters their bank account number in that tab; Docusign triggers the action; the action calls the bank's API through the registered connection; the signer cannot proceed until verification succeeds."],
        ],
        [0.5 * inch, 1.9 * inch, 5.0 * inch],
        styles["TableBody"],
    )
)
story.append(
    p(
        "This scenario threads every layer covered in this guide: registration (Sections 5-6), review/publish/distribution (Section 7), and the Connected Fields runtime bridge (Section 9) - which is exactly the kind of end-to-end question an exam is likely to ask.",
        styles["Body"],
    )
)

# ---------------------------------------------------------------------------
story += section("12. Exam-Style Distinctions")
story.append(
    table(
        ["Clue in question", "Best technical answer", "Why"],
        [
            ["\"Build a solution other Docusign customers can install\"", "Register and publish an extension app (public distribution).", "That is the defining purpose of the App Center - discoverable, installable third-party functionality."],
            ["\"Only our own org should ever use this integration\"", "Either a plain OAuth API integration, or an extension app with PRIVATE distribution.", "Private distribution restricts install to specific account GUIDs you approve; a plain API integration never appears in the App Center at all."],
            ["\"Verify signer data before they can sign\"", "Connected Fields / Data Verification extension, wired via extensionData with extensionPolicy=MustVerifyToSign.", "This is the dedicated mechanism for in-signing-ceremony verification against an external source."],
            ["\"Automatically archive completed agreements externally\"", "File Input Output (Store Files) extension, or a Maestro Store Files Apps Step.", "File IO/Store Files Steps are the categories built specifically for moving whole files out of Docusign."],
            ["\"Import CRM data into a running workflow\"", "Data Input Output extension, or a Maestro Read Apps Step.", "Read Steps/Data IO pull structured data in, distinct from file movement or field-level verification."],
            ["\"Which contract catalog does this template ID reference?\"", "Check whether it is on extensions[] (extension contract reference) or actions[] (action contract reference).", "Same field name (template), two different contract catalogs - a classic manifest trap."],
            ["\"App works for us but rejected for other customers to install\"", "Check distribution is set to PRIVATE and the target account's GUID is added/Accepted.", "Public vs Private plus the Pending/Accepted approval flow controls exactly who can install."],
        ],
        [2.0 * inch, 2.3 * inch, 3.1 * inch],
        styles["TableBody"],
    )
)

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    leftMargin=0.55 * inch,
    rightMargin=0.55 * inch,
    topMargin=0.55 * inch,
    bottomMargin=0.55 * inch,
    title="Docusign Extension Apps Exam Guide",
    author="Codex",
)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(f"Wrote {OUT}")

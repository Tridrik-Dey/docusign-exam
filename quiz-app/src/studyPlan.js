// Reusable one-week plan generator.
// You set the exam date and your latest section scores; the plan builds the 7 days ending on the exam date and
// puts the weakest (weighted) sections first. Task actions:
//   { type: 'pdf', file }                       open a study PDF (served from /pdf/...)
//   { type: 'practice', domain, importance }    open practice mode (normal bank) with filters
//   { type: 'review', domain }                  practice mode, "Review incorrect"
//   { type: 'drill', domain }                   decode drill (hard scenario questions, decode first)
//   { type: 'mock' }                            mock exam screen (Papers A-D or random)
//   { type: 'link', url }                       external page

export const SECTIONS = [
  { name: 'API Authentication', weight: 13, pdf: 'sections/01_api_authentication.pdf' },
  { name: 'Go Live Process', weight: 11, pdf: 'sections/02_go_live_process.pdf' },
  { name: 'Docusign Connect', weight: 12, pdf: 'sections/03_docusign_connect.pdf' },
  { name: 'eSignature API', weight: 16, pdf: 'sections/04_esignature_api.pdf' },
  { name: 'eSignature Features and Web Forms', weight: 11, pdf: 'sections/05_esignature_features_web_forms.pdf' },
  { name: 'Agreement Manager API', weight: 6, pdf: 'sections/06_agreement_manager_api.pdf' },
  { name: 'Workflow Builder and Workflow API', weight: 15, pdf: 'sections/07_workflow_builder_and_api.pdf' },
  { name: 'App Center and Extension Apps', weight: 16, pdf: 'sections/08_app_center_extension_apps.pdf' },
];

// First attempt, 22 Nov 2026 (official score report). Used until you enter newer scores.
export const DEFAULT_SCORES = {
  'API Authentication': 80,
  'Go Live Process': 58,
  'Docusign Connect': 48,
  'eSignature API': 46,
  'eSignature Features and Web Forms': 37,
  'Agreement Manager API': 80,
  'Workflow Builder and Workflow API': 65,
  'App Center and Extension Apps': 70,
};

const TARGET = 85;
export const DSU = 'https://dsupartners.docusign.com/page/certified-docusign-iam-integration-extension-developer';

export const MEMORIZE = {
  'API Authentication': [
    'Auth code 120 s; Auth Code access token 8 h; refresh 30 d (confidential) / 24 h (public); JWT token 1 h, no refresh token',
    'Secret can be kept on a server = Confidential; SPA / mobile = Public + PKCE; nobody logged in = JWT (consent once: signature impersonation)',
    'After any flow: /oauth/userinfo -> account_id + base_uri (is_default=true); revoking consent kills refresh tokens, live access tokens keep working',
  ],
  'Go Live Process': [
    'No 20-API-call test any more; Start Go live -> log in to the production account as its admin; manual review up to 48 h; Review Expired after 90 days',
    'Classification: Private custom / Third-party integration key / Public / Embedded; "no accounts listed" = integration type does not match account type',
    '3,000 calls per hour per account (shared by all apps); burst 500 per 30 s; poll an envelope at most once every 15 min',
    'After promotion: production auth host + base_uri, new secrets / RSA keys / redirect URIs, new template IDs',
  ],
  'Docusign Connect': [
    'Org level = many accounts, JSON SIM only; account level = one account; envelope level = eventNotification on create, API only',
    'Connect messages do not count against API limits; HMAC-SHA256 over the raw body proves origin and integrity',
    'Any non-2xx or timeout is retried: return 200 fast, queue the work, make processing idempotent; JSON SIM recommended, XML/aggregate legacy',
  ],
  'eSignature API': [
    'One template = templateId + templateRoles; several templates or templates + extra documents = compositeTemplates (sequence, one document each)',
    'status created = draft (needed for createSender / doc generation); sent = send now; void permanent, lock temporary',
    'Embedded signing = clientUserId + createRecipient (URL 5 min, single use); focused view needs frameAncestors + messageOrigins',
    'Same document to many people, each their own envelope = bulk send (list -> envelope -> test -> send); confirm status with Connect, not returnUrl',
  ],
  'eSignature Features and Web Forms': [
    'Access code (light, free) < phone < KBA (US only) < IDV (government ID); phone, KBA, IDV cost per use',
    'identityVerification.workflowId ENFORCES IDV (IDs from IdentityVerifications:list); authenticationMethod only RECORDS your own login',
    'Template-based web form = envelope created; standalone = no envelope; embedded instance needs clientUserId; remote uses sendOption + roleName',
    'Connected Fields send: GetConnectedFieldsTabGroups -> extensionData on tabs -> Envelopes:create; Data Verification = standard checks (bank, SSN, email)',
  ],
  'Agreement Manager API': [
    'Four operations: GetAgreementsList (search, ID unknown), GetAgreement (one known ID), DeleteAgreement, CreateAgreementSummary (POST .../ai/actions/summarize)',
    'Imported legacy agreements have no envelope; RAG = index agreement data keyed by agreementId and cite the source',
  ],
  'Workflow Builder and Workflow API': [
    'Start: manually (staff in Docusign), from a link (self-service intake), from an API call (your app); scope aow_manage',
    'GetWorkflowTriggerRequirements -> TriggerWorkflow; cancel = one instance; pause / resume = new instances only',
  ],
  'App Center and Extension Apps': [
    'Connected Fields + Data Verification -> eSignature; Data IO + File output -> Maestro workflows',
    'Public = any App Center customer; private = listed production accounts; register and test in the Developer Console, then review and publish',
  ],
};

export function iso(d) {
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

function addDays(isoDate, n) {
  const d = new Date(`${isoDate}T00:00:00`);
  d.setDate(d.getDate() + n);
  return d;
}

export function label(d) {
  return d.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' });
}

// Weighted gap: how many exam marks a section can still give you.
export function prioritize(scores) {
  return SECTIONS.map((s) => {
    const score = Number.isFinite(scores?.[s.name]) ? scores[s.name] : DEFAULT_SCORES[s.name];
    return { ...s, score, priority: s.weight * Math.max(5, TARGET - score) };
  }).sort((a, b) => b.priority - a.priority);
}

function sectionDay(id, primary, secondary) {
  const p = primary.name;
  const s = secondary.name;
  return {
    title: `${p} (${primary.weight}%, you: ${primary.score}%) + refresh ${s}`,
    domains: [p, s],
    tasks: [
      { id: `${id}-guide`, minutes: 15, text: `Read the red and amber boxes: ${p} study guide`, action: { type: 'pdf', file: primary.pdf } },
      { id: `${id}-decoder`, minutes: 10, text: `Read the ${p} part of the Scenario Decoder (business words -> Docusign meaning)`, action: { type: 'pdf', file: '00_scenario_decoder.pdf' } },
      { id: `${id}-facts`, minutes: 33, text: `Topic test: ${p} (15 questions, 23 min), then review every miss`, action: { type: 'topic', domain: p, size: 15 } },
      { id: `${id}-drill`, minutes: 30, text: `Decode drill: ${p} (hard scenarios, decide what it needs before you see the options)`, action: { type: 'drill', domain: p } },
      { id: `${id}-review`, minutes: 20, text: `Decode drill again: ${p} (missed questions come back first after unseen ones; read every TRAP note)`, action: { type: 'drill', domain: p } },
      { id: `${id}-refresh`, minutes: 20, text: `Refresh (20 min): ${s} decode drill (you: ${secondary.score}%)`, action: { type: 'drill', domain: s } },
    ],
    memorize: [...(MEMORIZE[p] || []), ...(MEMORIZE[s] || []).slice(0, 1)],
  };
}

export function generatePlan(examDate, scores) {
  const order = prioritize(scores);
  const day = (offset, body, phase) => {
    const d = addDays(examDate, offset - 6);
    return { date: iso(d), label: label(d), phase, ...body };
  };
  const days = [
    day(0, {
      title: 'Diagnostic: Paper C under exam conditions + the Scenario Decoder',
      domains: [],
      tasks: [
        { id: 'd1-decoder', minutes: 10, text: 'Read the Scenario Decoder checklist (page 1) before the paper', action: { type: 'pdf', file: '00_scenario_decoder.pdf' } },
        { id: 'd1-paper', minutes: 150, text: 'Take Paper C: 60 questions, 150 min, real-exam style (Mock exam > Start Paper C)', action: { type: 'mock' } },
        { id: 'd1-scores', minutes: 2, text: 'On the results page, press "Use these scores for my plan" so days 2 to 5 target your weakest sections', action: null },
        { id: 'd1-review', minutes: 40, text: 'Review Paper C: for each miss, read the decode clues, the TRAP and why-not notes', action: { type: 'pdf', file: 'docusign_hard_papers_C_D.pdf' } },
        { id: 'd1-concepts', minutes: 15, text: 'Read the Paper C concepts sheet', action: { type: 'pdf', file: 'paper_C_concepts.pdf' } },
      ],
      memorize: [
        'Decode first: who acts? is a person present? where does the code run? which level (envelope / account / org)? now or later? enforce or record?',
        'Select two: three options will look right; find the one detail that breaks one of them',
      ],
    }, 'quick'),
    day(1, sectionDay('d2', order[0], order[4]), 'risk'),
    day(2, sectionDay('d3', order[1], order[5]), 'risk'),
    day(3, sectionDay('d4', order[2], order[6]), 'broad'),
    day(4, sectionDay('d5', order[3], order[7]), 'broad'),
    day(5, {
      title: 'Final simulation: Paper D + light review',
      domains: [],
      tasks: [
        { id: 'd6-paper', minutes: 150, text: 'Morning: Paper D, 60 questions, 150 min (Mock exam > Start Paper D). Target 70% or higher', action: { type: 'mock' } },
        { id: 'd6-review', minutes: 40, text: 'Review Paper D misses (decode clues + TRAP notes)', action: { type: 'pdf', file: 'docusign_hard_papers_C_D.pdf' } },
        { id: 'd6-concepts', minutes: 15, text: 'Read the Paper D concepts sheet', action: { type: 'pdf', file: 'paper_D_concepts.pdf' } },
        { id: 'd6-cheat', minutes: 15, text: 'Read the 3-page Confusion Cheat Sheet', action: { type: 'pdf', file: '00_confusion_cheat_sheet.pdf' } },
        { id: 'd6-logistics', minutes: 20, text: 'Run the Certiverse system check, install Safe Exam Browser, check your ID; stop by evening and sleep', action: null },
      ],
      memorize: [],
    }, 'sim'),
    day(6, {
      title: 'EXAM DAY',
      domains: [],
      tasks: [
        { id: 'd7-red', minutes: 30, text: '30 min before: skim only the red rows of the Confusion Cheat Sheet (nothing new)', action: { type: 'pdf', file: '00_confusion_cheat_sheet.pdf' } },
        { id: 'd7-decode', minutes: 0, text: 'For every long scenario: decide what it needs (who, user present, level, timing) BEFORE reading the options', action: null },
        { id: 'd7-tactics', minutes: 0, text: 'Two options look the same? Find the one detail that differs and check it against the stem. Flag and return; about 2.5 min per question', action: null },
      ],
      memorize: [],
    }, 'exam'),
  ];
  return days;
}

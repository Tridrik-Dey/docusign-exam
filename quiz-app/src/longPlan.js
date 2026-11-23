// 45-day plan: Phase 1 (rebuild, 45-60 min weekdays), Phase 2 (deepen, 75-90 min weekdays), then the one-week sprint
// (studyPlan.js generatePlan) for the last 7 days. Built from the plan start date and the exam date; adapts to the
// section scores and to topic-test results.
import { DEFAULT_SCORES, DSU, MEMORIZE, SECTIONS, generatePlan, iso, label, prioritize } from './studyPlan.js';

export const WEAK_BELOW = 70; // a section scoring under this is "weak"
export const MASTERED_AT = 85; // two topic tests in a row at or above this = mastered

export function sectionStatus(scores, topicHistory = []) {
  const out = {};
  SECTIONS.forEach((s) => {
    const score = Number.isFinite(scores?.[s.name]) ? scores[s.name] : DEFAULT_SCORES[s.name];
    const tests = topicHistory.filter((t) => t.section === s.name);
    const lastTwo = tests.slice(-2);
    const mastered = lastTwo.length === 2 && lastTwo.every((t) => t.pct >= MASTERED_AT);
    out[s.name] = {
      score,
      tests,
      last: tests.length ? tests[tests.length - 1] : null,
      status: mastered ? 'mastered' : score < WEAK_BELOW ? 'weak' : 'strong',
    };
  });
  return out;
}

const byName = Object.fromEntries(SECTIONS.map((s) => [s.name, s]));
export const LAB_PDF = {
  esignature: 'labs/lab_1_esignature_api.pdf',
  connect_golive: 'labs/lab_2_connect_golive.pdf',
  features_webforms: 'labs/lab_3_features_webforms.pdf',
  auth: 'labs/lab_4_api_authentication.pdf',
  workflow: 'labs/lab_5_workflow.pdf',
  extension_apps: 'labs/lab_6_extension_apps.pdf',
  agreement_manager: 'labs/lab_7_agreement_manager.pdf',
  embedding: 'labs/lab_8_embedding.pdf',
};
const STRONG_LAB = {
  'API Authentication': 'auth',
  'Workflow Builder and Workflow API': 'workflow',
  'App Center and Extension Apps': 'extension_apps',
  'Agreement Manager API': 'agreement_manager',
};

// Daily time budgets (minutes). Flexible items (decode drill, mistakes review, keep-alive drill) are stretched or
// shrunk so every day lands inside its budget; labs, tests and papers keep their own length.
const BUDGET = { p1: { weekday: [45, 60], weekend: [90, 120] }, p2: { weekday: [75, 90], weekend: [150, 180] } };
function fitToBudget(tasks, [min, max]) {
  const total = tasks.reduce((m, t) => m + (t.minutes || 0), 0);
  const flex = tasks.filter((t) => t.flex);
  const flexTotal = flex.reduce((m, t) => m + t.minutes, 0);
  if (!flexTotal || (total >= min && total <= max)) return tasks;
  const target = total > max ? max : min;
  const scale = Math.max(0.3, (flexTotal + target - total) / flexTotal);
  return tasks.map((t) => (t.flex ? { ...t, minutes: Math.max(5, Math.round((t.minutes * scale) / 5) * 5) } : t));
}

function diffDays(a, b) {
  return Math.round((new Date(`${b}T00:00:00`) - new Date(`${a}T00:00:00`)) / 86400000);
}

const ES = 'eSignature API';
const CO = 'Docusign Connect';
const GL = 'Go Live Process';
const FE = 'eSignature Features and Web Forms';

export function generateLongPlan({ planStart, examDate, scores, topicHistory = [], labs = {} }) {
  const status = sectionStatus(scores, topicHistory);
  const ranked = prioritize(scores).filter((s) => status[s.name].status !== 'mastered');
  const weakest = ranked.length ? ranked : prioritize(scores);
  const strong = SECTIONS.filter((s) => status[s.name].status !== 'weak').map((s) => s.name);
  const sprint = generatePlan(examDate, scores).map((d, i) => ({
    ...d,
    phaseNo: 3,
    week: null,
    sprintDay: i + 1,
    budget: i === 6 ? 'exam day' : i === 0 || i === 5 ? 'paper day, about 3.5 h' : 'about 2 h',
  }));
  const total = diffDays(planStart, sprint[0].date);
  if (total <= 0) return sprint;

  // Labs: explicit exercise numbers per day (basic exercises are skipped: the learner already knows them).
  function lab(key, nums, fallback) {
    const ex = labs?.[key]?.exercises || [];
    const picked = nums.map((n) => ex[n - 1]).filter(Boolean);
    const strip = (t) => t.replace(/^\d+\.\s*/, '');
    if (!picked.length) return { text: `Lab: ${fallback || 'see the lab guide'}`, minutes: 20, action: { type: 'pdf', file: LAB_PDF[key] } };
    return {
      text: `Lab ${nums.join(' + ')}: ${picked.map((e) => strip(e.title)).join(' + ')}`,
      minutes: picked.reduce((m, e) => m + (e.minutes || 15), 0),
      action: { type: 'pdf', file: LAB_PDF[key] },
    };
  }
  const redoLab = (key, sec) => ({ text: `Lab: redo the exercise behind your latest ${sec} misses (change one thing and predict the result first)`, minutes: 20, action: { type: 'pdf', file: LAB_PDF[key] } });
  // Spaced keep-alive: strong sections plus Workflow (65%, just under the line) twice per cycle.
  const KEEP = ['Workflow Builder and Workflow API', 'API Authentication', 'App Center and Extension Apps', 'Workflow Builder and Workflow API', 'Agreement Manager API'];
  let keepIdx = 0;
  const labCursor = {};
  function keepAlive(minutes) {
    const name = KEEP[keepIdx % KEEP.length];
    const useLab = keepIdx % 2 === 1;
    keepIdx += 1;
    const key = STRONG_LAB[name];
    const ex = labs?.[key]?.exercises || [];
    if (useLab && ex.length) {
      const i = (labCursor[key] || 0) % ex.length;
      labCursor[key] = i + 1;
      const e = ex[i];
      return { text: `Mini-lab (keep-alive, ${name}): exercise ${i + 1} - ${e.title.replace(/^\d+\.\s*/, '')}`, minutes: Math.max(minutes, Math.min(e.minutes || 15, 15)), action: { type: 'pdf', file: LAB_PDF[key] } };
    }
    return { text: `Keep-alive: ${name} (5 decode-drill questions + its red facts)`, minutes, action: { type: 'drill', domain: name }, flex: true };
  }
  const embed = (what, minutes) => ({ text: `Embedding lab: ${what} (app page + Lab 8 guide)`, minutes, action: { type: 'embed' } });
  const topic = (name, size) => ({
    text: size <= 5 ? `Timed set: ${size} ${name} scenario questions (${Math.round(size * 1.5)} min), no feedback until the end` : `Topic test: ${name} (${size} questions, ${Math.round(size * 1.5)} min), then review every miss`,
    minutes: Math.round(size * 1.5) + (size <= 5 ? 2 : 10),
    action: { type: 'topic', domain: name, size },
  });
  const drill = (name, minutes) => ({ text: `Decode drill: ${name} (decide what the scenario needs before the options)`, minutes, action: { type: 'drill', domain: name }, flex: true });
  const misses = (name, minutes) => ({ text: `My mistakes: ${name} (your repeat mistakes with full explanations), then only the red facts behind them`, minutes, action: { type: 'mistakes', domain: name }, flex: true });
  const extraFor = (focus) => {
    const t = Object.entries(status)
      .filter(([n, s]) => n !== focus && s.last && s.last.pct < WEAK_BELOW)
      .sort((x, y) => x[1].last.pct - y[1].last.pct)[0];
    return t ? { text: `Extra (last topic test ${t[1].last.pct}%): decode drill ${t[0]}`, minutes: 20, action: { type: 'drill', domain: t[0] } } : null;
  };
  const W = (n) => weakest[n % weakest.length].name;
  // A normal weekday: ~40% decode, ~30% lab, ~20% review of own misses, ~10% keep-alive; Tue/Thu end with a timed set.
  function weekday(sec, labTask, wd, phaseNo) {
    const p2 = phaseNo === 2;
    const timed = wd === 1 || wd === 3;
    return [
      drill(sec, timed ? (p2 ? 25 : 15) : p2 ? 35 : 25),
      labTask,
      misses(sec, p2 ? 15 : 10),
      timed ? topic(sec, 5) : null,
      keepAlive(p2 ? 10 : 6),
    ];
  }

  const days = [];
  for (let off = 0; off < total; off += 1) {
    const d = new Date(`${planStart}T00:00:00`);
    d.setDate(d.getDate() + off);
    const date = iso(d);
    const wd = (d.getDay() + 6) % 7; // 0 = Monday
    const week = Math.floor(off / 7);
    const phaseNo = off < 21 ? 1 : 2;
    const weekend = wd >= 5;
    const md = `${d.getMonth() + 1}-${d.getDate()}`;
    let title;
    let focus = [];
    let tasks = [];

    if (md === '12-24' || md === '12-25' || md === '12-26') {
      title = 'Holiday: light keep-alive only (or take the day off)';
      tasks = [keepAlive(20), topic(W(0), 5)];
    } else if (md === '1-1') {
      title = 'Rest day';
    } else if (week === 0) {
      focus = [ES];
      if (wd === 0) {
        title = 'Diagnostic 1: where exactly are the gaps? (eSignature API + Features & Web Forms)';
        focus = [ES, FE];
        tasks = [topic(ES, 8), topic(FE, 8), { text: 'Write down the 3 points you were least sure of in each test; the next days start from them', minutes: 10, action: null }];
      } else if (wd === 1) {
        title = 'Diagnostic 2: Docusign Connect + Go Live, and a 15-minute lab setup';
        focus = [CO, GL];
        tasks = [
          topic(CO, 8),
          topic(GL, 8),
          { text: 'Lab setup (15 min): new developer account + integration key, quickstart running, then lab 1 exercise 1 (userinfo -> base_uri -> accountId). Never commit secrets to git', minutes: 15, action: { type: 'pdf', file: LAB_PDF.esignature } },
        ];
      } else if (!weekend) {
        title = 'eSignature API: decode + the tricky labs';
        tasks = weekday(ES, lab('esignature', [[4], [5], [7]][wd - 2]), wd, 1);
        if (wd === 4) tasks.splice(2, 0, embed('open your recipient view as redirect, plain iframe and Docusign JS', 15));
      } else if (wd === 5) {
        title = 'Saturday: bulk send end to end + timed set';
        tasks = [lab('esignature', [9]), drill(ES, 20), topic(ES, 5), keepAlive(10)];
      } else {
        title = 'Topic tests: eSignature API + API Authentication check';
        tasks = [topic(ES, 15), topic('API Authentication', 8)];
      }
    } else if (week === 1) {
      focus = [ES];
      if (!weekend) {
        title = 'eSignature API: decode + labs (16% of the exam)';
        const labs1 = [embed('classic vs focused view: frameAncestors + messageOrigins, what breaks without them (Lab 1 ex 6)', 20), lab('esignature', [8]), redoLab('esignature', 'eSignature API'), lab('esignature', [3]), redoLab('esignature', 'eSignature API')];
        tasks = weekday(ES, labs1[wd], wd, 1);
      } else if (wd === 5) {
        title = 'Saturday: build one realistic flow end to end';
        tasks = [
          { text: 'Lab: composite envelope (server template + extra document) with an embedded signer, then confirm completion with a Connect message instead of the returnUrl', minutes: 60, action: { type: 'pdf', file: LAB_PDF.esignature } },
          drill(ES, 20),
          keepAlive(10),
        ];
      } else {
        title = 'Topic tests: eSignature API retest + Workflow check';
        tasks = [topic(ES, 15), topic('Workflow Builder and Workflow API', 8)];
      }
    } else if (week === 2) {
      const sec = wd <= 2 ? CO : GL;
      focus = [CO, GL];
      if (!weekend) {
        title = wd <= 2 ? 'Docusign Connect: decode + labs (12%)' : 'Go Live: decode + walkthrough (11%)';
        const labs2 = [lab('connect_golive', [1, 8]), lab('connect_golive', [2]), lab('connect_golive', [3, 4]), lab('connect_golive', [6]), lab('connect_golive', [7, 9])];
        tasks = weekday(sec, labs2[wd], wd, 1);
      } else if (wd === 5) {
        title = 'Topic tests: Connect + Go Live, then the listener lab';
        tasks = [topic(CO, 15), topic(GL, 8), lab('connect_golive', [5])];
      } else {
        title = 'CHECKPOINT: Paper E (60 questions, 150 min)';
        tasks = [
          { text: 'Paper E under exam conditions (Mock exam > Start Paper E)', minutes: 150, action: { type: 'mock' } },
          { text: 'Press "Use these scores for my plan" on the results page, then review every miss (decode + TRAP notes)', minutes: 40, action: { type: 'pdf', file: 'docusign_hard_papers_E_F.pdf' } },
        ];
      }
    } else if (week === 3) {
      focus = [FE];
      if (!weekend) {
        title = 'eSignature Features & Web Forms: decode + labs (11%, your weakest)';
        const labs3 = [lab('features_webforms', [2]), lab('features_webforms', [3]), lab('features_webforms', [4]), lab('features_webforms', [6]), lab('features_webforms', [8])];
        tasks = weekday(FE, labs3[wd], wd, 2);
        if (wd === 1 || wd === 3) tasks.push(extraFor(FE));
      } else if (wd === 5) {
        title = 'Saturday: web form instances (embedded and remote) + branding';
        tasks = [lab('features_webforms', [7, 5]), embed('render your embedded web form instance with Docusign JS (formUrl + instanceToken)', 15), drill(FE, 30), topic(FE, 5), extraFor(FE)];
      } else {
        const retest = W(0) === FE ? W(1) : W(0);
        title = `Topic tests: Features & Web Forms + App Center + ${retest} retest`;
        tasks = [topic(FE, 15), topic('App Center and Extension Apps', 8), topic(retest, 15)];
      }
    } else if (week === 4) {
      const a = W(0);
      const b = W(1);
      focus = [a, b];
      if (wd <= 2) {
        const sec = wd === 1 ? b : a;
        title = `Adaptive: ${sec} (one of your two lowest right now)`;
        tasks = [drill(sec, 35), misses(sec, 20), topic(sec, 5), keepAlive(15)];
      } else {
        title = 'CHECKPOINT: Paper F (60 questions, 150 min)';
        tasks = [
          { text: 'Paper F under exam conditions (Mock exam > Start Paper F)', minutes: 150, action: { type: 'mock' } },
          { text: 'Press "Use these scores for my plan", then review every miss', minutes: 40, action: { type: 'pdf', file: 'docusign_hard_papers_E_F.pdf' } },
        ];
      }
    } else if (week === 5) {
      const a = W(0);
      const b = W(1);
      focus = [a, b];
      if (wd === 0) {
        title = `Adaptive: ${a} + embedding a workflow`;
        tasks = [drill(a, 40), misses(a, 20), topic(a, 5), embed('trigger a workflow and open its instance URL as redirect vs iframe (Lab 5)', 15)];
      } else if (wd === 1) {
        title = `Strength checks: Agreement Manager + Auth + ${a} retest`;
        tasks = [topic('Agreement Manager API', 8), topic('API Authentication', 8), topic(a, 15)];
      } else if (wd <= 3) {
        const sec = wd === 2 ? a : b;
        title = `Fix ${sec} + speed run`;
        tasks = [drill(sec, 30), topic(sec, 15), { text: 'Speed run: Paper A or B, 2 min per question, decode before reading the options', minutes: 45, action: { type: 'mock' } }];
      } else if (wd === 5) {
        title = 'Official practice + book the retake';
        tasks = [
          { text: 'Docusign University: official Practice Exam and the free Integration Developer Pro exam', minutes: 90, action: { type: 'link', url: DSU } },
          { text: 'Book the retake; run the Certiverse system check and install Safe Exam Browser', minutes: 30, action: null },
          misses(a, 20),
        ];
      } else {
        title = `Adaptive: ${a}`;
        tasks = [drill(a, 40), topic(a, 5), keepAlive(20)];
      }
    } else {
      const a = W(off);
      focus = [a];
      title = `Adaptive: ${a}`;
      tasks = [drill(a, 30), misses(a, 15), topic(a, 15), keepAlive(15)];
    }
    tasks = tasks.filter(Boolean);
    const isPaper = tasks.some((t) => t.minutes >= 150);
    const holiday = title.indexOf('Holiday') === 0;
    const range = BUDGET[phaseNo === 1 ? 'p1' : 'p2'][weekend ? 'weekend' : 'weekday'];
    if (tasks.length && !isPaper && !holiday) {
      const sum = tasks.reduce((m, t) => m + (t.minutes || 0), 0);
      if (sum < range[0] && !tasks.some((t) => t.flex)) {
        const sec = focus[0] || W(0);
        tasks.push(misses(sec, Math.min(30, range[0] - sum)), drill(sec, Math.max(10, range[0] - sum - 30)));
      }
      tasks = fitToBudget(tasks, range);
    }
    tasks = tasks.map((t, i) => ({ ...t, id: `${date}-${i}` }));
    days.push({
      date,
      label: label(d),
      phase: phaseNo === 1 ? 'quick' : 'broad',
      phaseNo,
      week: week + 1,
      title,
      domains: focus,
      tasks,
      memorize: focus.flatMap((f) => (MEMORIZE[f] || []).slice(0, 2)),
      budget: !tasks.length ? 'rest'
        : tasks.some((t) => t.minutes >= 150) ? 'paper day, about 3 h'
          : title.indexOf('Holiday') === 0 ? 'light, optional'
            : weekend ? (phaseNo === 1 ? '1.5-2 h' : '2.5-3 h') : phaseNo === 1 ? '45-60 min' : '75-90 min',
    });
  }
  return [...days, ...sprint];
}

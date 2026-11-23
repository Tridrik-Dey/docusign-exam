import React, { useMemo, useState } from 'react';
import { BookOpen, CalendarDays, Frame, CheckCircle2, Circle, ClipboardCheck, ExternalLink, FileText, ListChecks, PlayCircle, RotateCcw, Search, Timer } from 'lucide-react';
import questions from './questions.json';
import labs from './labs.json';
import { DEFAULT_SCORES, SECTIONS } from './studyPlan.js';
import { generateLongPlan, sectionStatus } from './longPlan.js';

export const PREP_KEY = 'docusign-iam-prep-v2';
const DONE_KEY = 'docusign-iam-plan-v2';
const TOPIC_KEY = 'docusign-iam-topic-v1';
// cleared by "Start a new plan" (mock and topic-test history are kept)
const RESET_KEYS = ['docusign-iam-quiz-state-v4', 'docusign-iam-drill-v1', 'docusign-iam-mock-exam-v2', 'docusign-iam-topic-run-v1'];
const FIRST_PLAN_START = '2026-11-23';

function readJson(key, fallback) {
  try {
    const value = JSON.parse(localStorage.getItem(key) || 'null');
    return value ?? fallback;
  } catch {
    return fallback;
  }
}

function writeJson(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch {
    /* ignore: settings just won't persist */
  }
}

function todayIso() {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

export function loadPrep() {
  const saved = readJson(PREP_KEY, null);
  return {
    examDate: saved?.examDate || '2027-01-09',
    planStart: saved?.planStart || FIRST_PLAN_START,
    scores: { ...DEFAULT_SCORES, ...(saved?.scores || {}) },
    scoresSource: saved?.scoresSource || 'Official score report, 22 Nov 2026',
    weekId: saved?.weekId || 'week-1',
  };
}

export function savePrepScores(scores, source) {
  const prep = loadPrep();
  writeJson(PREP_KEY, { ...prep, scores: { ...prep.scores, ...scores }, scoresSource: source });
}

function correctIds(q) {
  return Array.isArray(q.correctAnswers) ? q.correctAnswers : [q.correct];
}

function isRight(q, answer) {
  const chosen = (Array.isArray(answer) ? answer : answer ? [answer] : []).slice().sort();
  const right = correctIds(q).slice().sort();
  return chosen.length === right.length && chosen.every((id, i) => id === right[i]);
}

const ACTION_LABEL = {
  pdf: { icon: FileText, label: 'Open PDF' },
  practice: { icon: PlayCircle, label: 'Practice' },
  review: { icon: ListChecks, label: 'Review incorrect' },
  drill: { icon: Search, label: 'Decode drill' },
  topic: { icon: ClipboardCheck, label: 'Topic test' },
  mistakes: { icon: ListChecks, label: 'My mistakes' },
  embed: { icon: Frame, label: 'Embedding lab' },
  mock: { icon: Timer, label: 'Mock exam' },
  link: { icon: ExternalLink, label: 'Open' },
};
const PHASE_NAME = { 1: 'Phase 1: Rebuild', 2: 'Phase 2: Deepen', 3: 'Phase 3: One-week sprint' };
const STATUS_LABEL = { weak: 'weak', strong: 'strong', mastered: 'mastered' };

export default function StudyPlan({ practiceState, onAction }) {
  const today = todayIso();
  const [prep, setPrep] = useState(loadPrep);
  const topicHistory = useMemo(() => readJson(TOPIC_KEY, { results: [] }).results || [], []);
  const plan = useMemo(
    () => generateLongPlan({ planStart: prep.planStart, examDate: prep.examDate, scores: prep.scores, topicHistory, labs }),
    [prep.planStart, prep.examDate, prep.scores, topicHistory],
  );
  const status = useMemo(() => sectionStatus(prep.scores, topicHistory), [prep.scores, topicHistory]);
  const defaultDay = plan.find((d) => d.date === today)?.date || (today < plan[0].date ? plan[0].date : plan[plan.length - 1].date);
  const [selected, setSelected] = useState(defaultDay);
  const [allDone, setAllDone] = useState(() => readJson(DONE_KEY, {}));
  const done = allDone[prep.weekId] || {};

  const day = plan.find((d) => d.date === selected) || plan[0];
  const dayIndex = plan.indexOf(day);
  const daysLeft = Math.round((new Date(`${prep.examDate}T00:00:00`) - new Date(`${today}T00:00:00`)) / 86400000);
  const minutes = day.tasks.reduce((sum, t) => sum + (t.minutes || 0), 0);

  const practice = useMemo(() => {
    const answers = practiceState.answers || {};
    const submitted = practiceState.submitted || {};
    const out = {};
    questions.forEach((q) => {
      const s = (out[q.domain] = out[q.domain] || { answered: 0, correct: 0 });
      if (submitted[q.id]) {
        s.answered += 1;
        if (isRight(q, answers[q.id])) s.correct += 1;
      }
    });
    return out;
  }, [practiceState]);

  // group the days into weeks for the left column
  const groups = useMemo(() => {
    const out = [];
    plan.forEach((d) => {
      const key = d.phaseNo === 3 ? 'sprint' : `w${d.week}`;
      let g = out.find((x) => x.key === key);
      if (!g) {
        g = { key, title: d.phaseNo === 3 ? PHASE_NAME[3] : `Week ${d.week} · ${PHASE_NAME[d.phaseNo]}`, days: [] };
        out.push(g);
      }
      g.days.push(d);
    });
    return out;
  }, [plan]);

  function updatePrep(next) {
    setPrep(next);
    writeJson(PREP_KEY, next);
  }

  function setScore(name, value) {
    const n = Math.max(0, Math.min(100, Number(value)));
    if (!Number.isFinite(n)) return;
    updatePrep({ ...prep, scores: { ...prep.scores, [name]: n }, scoresSource: 'Entered by you' });
  }

  function toggle(id) {
    const next = { ...allDone, [prep.weekId]: { ...done, [id]: !done[id] } };
    setAllDone(next);
    writeJson(DONE_KEY, next);
  }

  function newPlan() {
    if (!window.confirm('Start a new plan from today? Ticks, practice answers, decode-drill progress and any unfinished test are cleared. Mock exam and topic-test history and your section scores are kept. Set the exam date afterwards (for a one-week plan, pick a date 6 days from today).')) return;
    RESET_KEYS.forEach((k) => {
      try {
        localStorage.removeItem(k);
      } catch {
        /* ignore */
      }
    });
    updatePrep({ ...prep, planStart: today, weekId: `plan-${Date.now()}` });
    window.location.reload();
  }

  function run(action) {
    if (!action) return;
    if (action.type === 'pdf') window.open(`/pdf/${action.file}`, '_blank', 'noopener');
    else if (action.type === 'link') window.open(action.url, '_blank', 'noopener');
    else onAction(action);
  }

  return (
    <div className="app-shell plan-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="mark">DS</div>
          <div>
            <h1>Exam plan</h1>
            <p>{daysLeft > 0 ? `${daysLeft} day${daysLeft === 1 ? '' : 's'} to the exam` : daysLeft === 0 ? 'Exam today' : 'Exam date passed: set the next one'}</p>
          </div>
        </div>
        <div className="plan-dates">
          <label className="plan-date">
            Exam date
            <input type="date" value={prep.examDate} onChange={(e) => e.target.value && updatePrep({ ...prep, examDate: e.target.value })} />
          </label>
          <label className="plan-date">
            Plan start
            <input type="date" value={prep.planStart} onChange={(e) => e.target.value && updatePrep({ ...prep, planStart: e.target.value })} />
          </label>
        </div>
        <div className="plan-days compact">
          {groups.map((g) => (
            <div key={g.key} className="plan-week">
              <div className="plan-week-title">{g.title}</div>
              {g.days.map((d) => {
                const total = d.tasks.length;
                const finished = d.tasks.filter((t) => done[t.id]).length;
                return (
                  <button
                    key={d.date}
                    className={`plan-day phase-${d.phase} ${d.date === selected ? 'active' : ''} ${d.date === today ? 'today' : ''} ${d.date < today ? 'past' : ''}`}
                    onClick={() => setSelected(d.date)}
                  >
                    <span className="plan-day-label">
                      <CalendarDays size={13} /> {d.label}
                      {d.date === today && <em>today</em>}
                      <span className="plan-day-count">{total ? `${finished}/${total}` : ''}</span>
                    </span>
                    <span className="plan-day-title">{d.title}</span>
                  </button>
                );
              })}
            </div>
          ))}
        </div>
        <button className="side-action" onClick={() => onAction({ type: 'topic', domain: 'All' })}><ClipboardCheck size={17} /> Topic test</button>
        <button className="side-action" onClick={() => onAction({ type: 'drill', domain: 'All' })}><Search size={17} /> Decode drill</button>
        <button className="side-action" onClick={() => onAction({ type: 'mistakes', domain: 'All' })}><ListChecks size={17} /> My mistakes</button>
        <button className="side-action" onClick={() => onAction({ type: 'embed' })}><Frame size={17} /> Embedding lab</button>
        <button className="side-action" onClick={() => onAction({ type: 'practice', domain: 'All' })}><BookOpen size={17} /> Practice all questions</button>
        <button className="side-action mock-entry" onClick={() => onAction({ type: 'mock' })}><Timer size={17} /> Mock exam / Papers A-F</button>
        <button className="side-action" onClick={newPlan}><RotateCcw size={17} /> Start a new plan</button>
      </aside>

      <main className="question-area">
        <div className="topbar">
          <div>
            <span className="section-label">
              {day.phaseNo === 3 ? `Sprint day ${day.sprintDay}` : `Day ${dayIndex + 1} · week ${day.week}`} &middot; {day.label}{day.date === today ? ' · today' : ''} &middot; {PHASE_NAME[day.phaseNo]}
            </span>
            <h2>{day.title}</h2>
          </div>
        </div>
        <section className="question-card">
          <h3 className="plan-h3">
            What to do {day.budget && <small className="plan-budget">time budget {day.budget}{minutes ? ` · planned ${minutes} min` : ''}</small>}
          </h3>
          {day.tasks.length === 0 && <p className="plan-note">Nothing planned: rest.</p>}
          <div className="plan-tasks">
            {day.tasks.map((t) => {
              const meta = t.action ? ACTION_LABEL[t.action.type] : null;
              const Icon = meta?.icon;
              return (
                <div key={t.id} className={`plan-task ${done[t.id] ? 'done' : ''}`}>
                  <button className="plan-check" onClick={() => toggle(t.id)} aria-pressed={!!done[t.id]} title="Mark done">
                    {done[t.id] ? <CheckCircle2 size={22} /> : <Circle size={22} />}
                  </button>
                  <span className="plan-task-text">
                    {t.text}
                    {t.minutes ? <small className="plan-min"> &middot; {t.minutes} min</small> : null}
                  </span>
                  {meta && (
                    <button className="plan-go" onClick={() => run(t.action)}>
                      <Icon size={16} /> {meta.label}
                    </button>
                  )}
                </div>
              );
            })}
          </div>
          {day.memorize?.length > 0 && (
            <>
              <h3 className="plan-h3">Memorize today</h3>
              <ul className="plan-memo">
                {day.memorize.map((m) => <li key={m}>{m}</li>)}
              </ul>
            </>
          )}
        </section>
      </main>

      <aside className="analysis-panel">
        <div className="analysis-header">
          <h2>Your sections</h2>
          <p>Scores drive the plan. Latest source: {prep.scoresSource}. Topic tests and mock results update them.</p>
        </div>
        <table className="mock-table plan-stats">
          <thead><tr><th>Section</th><th>Score %</th><th>Status</th><th>Last test</th></tr></thead>
          <tbody>
            {SECTIONS.map((s) => {
              const st = status[s.name];
              const pr = practice[s.name];
              return (
                <tr key={s.name} className={day.domains.includes(s.name) ? 'plan-focus' : ''}>
                  <td>{s.name} <small className="plan-weight">({s.weight}%)</small>{pr?.answered ? <small className="plan-weight"> · practice {Math.round((pr.correct / pr.answered) * 100)}%</small> : null}</td>
                  <td><input className="plan-score" type="number" min="0" max="100" value={st.score} onChange={(e) => setScore(s.name, e.target.value)} /></td>
                  <td><span className={`status-badge status-${st.status}`}>{STATUS_LABEL[st.status]}</span></td>
                  <td>{st.last ? `${st.last.pct}%` : '-'}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <ul className="plan-rules">
          <li><strong>weak</strong> = under 70%: labs, decode drills and 15-question topic tests.</li>
          <li><strong>strong</strong> = 70% or more: keep-alive every few days and 8-question checks.</li>
          <li><strong>mastered</strong> = two topic tests in a row at 85% or more.</li>
          <li>A topic test under 70% adds extra drill slots; adaptive days always take your two lowest sections.</li>
        </ul>
      </aside>
    </div>
  );
}

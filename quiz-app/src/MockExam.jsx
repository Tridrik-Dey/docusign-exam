import React, { useEffect, useMemo, useState } from 'react';
import { ArrowLeft, ArrowRight, Clock, Flag, LogOut, RotateCcw, Trash2, Trophy } from 'lucide-react';
import { ReviewList, recordAnswers } from './review.jsx';
import questions from './questions.json';
import papers from './papers.json';
import { ImportanceTag } from './importance.jsx';
import { savePrepScores } from './StudyPlan.jsx';

// Official Prep Guide (v. 2026) section weights. The mock exam samples 60 questions in these proportions.
const SECTION_WEIGHTS = [
  ['API Authentication', 13],
  ['Go Live Process', 11],
  ['Docusign Connect', 12],
  ['eSignature API', 16],
  ['eSignature Features and Web Forms', 11],
  ['Agreement Manager API', 6],
  ['Workflow Builder and Workflow API', 15],
  ['App Center and Extension Apps', 16],
];
const EXAM_SIZE = 60;
const EXAM_MINUTES = 150;
const PASS_PERCENT = 70;
const EXAM_KEY = 'docusign-iam-mock-exam-v2';
const HISTORY_KEY = 'docusign-iam-mock-history-v2';

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
    /* storage unavailable: exam still works for this session */
  }
}

function shuffle(list) {
  const copy = list.slice();
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

// Largest-remainder rounding so the per-section counts add up to exactly EXAM_SIZE.
function sectionQuotas() {
  const raw = SECTION_WEIGHTS.map(([name, w]) => ({ name, exact: (EXAM_SIZE * w) / 100 }));
  const quotas = raw.map((r) => ({ name: r.name, count: Math.floor(r.exact), rem: r.exact - Math.floor(r.exact) }));
  let missing = EXAM_SIZE - quotas.reduce((sum, q) => sum + q.count, 0);
  quotas
    .map((q, index) => ({ index, rem: q.rem }))
    .sort((a, b) => b.rem - a.rem)
    .forEach(({ index }) => {
      if (missing > 0) {
        quotas[index].count += 1;
        missing -= 1;
      }
    });
  return quotas;
}

// Fixed papers (A / B): hard questions built from the options of the 47 Docusign University questions.
export const PAPERS = ['A', 'B', 'C', 'D', 'E', 'F'].map((id) => ({ id, ids: papers.filter((q) => q.paper === id).map((q) => q.id) }));

function buildExam(paper = null) {
  if (paper) {
    const p = PAPERS.find((x) => x.id === paper);
    return { paper, ids: p.ids.slice(), answers: {}, flagged: {}, current: 0, startedAt: Date.now(), finishedAt: null };
  }
  const picked = [];
  sectionQuotas().forEach(({ name, count }) => {
    const pool = shuffle(questions.filter((q) => q.domain === name));
    picked.push(...pool.slice(0, count).map((q) => q.id));
  });
  return {
    ids: shuffle(picked),
    answers: {},
    flagged: {},
    current: 0,
    startedAt: Date.now(),
    finishedAt: null,
  };
}

function correctIds(q) {
  return Array.isArray(q.correctAnswers) ? q.correctAnswers : [q.correct];
}

function isRight(q, answer) {
  const chosen = (Array.isArray(answer) ? answer : answer ? [answer] : []).slice().sort();
  const right = correctIds(q).slice().sort();
  return chosen.length === right.length && chosen.every((id, i) => id === right[i]);
}

function formatTime(ms) {
  const total = Math.max(0, Math.round(ms / 1000));
  const h = Math.floor(total / 3600);
  const m = Math.floor((total % 3600) / 60);
  const s = total % 60;
  return `${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

const byId = new Map([...questions, ...papers].map((q) => [q.id, q]));
const examLabel = (e) => (e && e.paper ? `Paper ${e.paper}` : 'Random mock');
const PAPER_NOTE = {
  A: 'hard, built from the 47 Docusign University questions',
  B: 'hard, built from the 47 Docusign University questions',
  C: 'real-exam style: business scenarios, close options, select-2 only (one-week plan, day 1)',
  D: 'real-exam style: business scenarios, close options, select-2 only (one-week plan, day 6)',
  E: 'real-exam style checkpoint (45-day plan, end of week 3)',
  F: 'real-exam style checkpoint (45-day plan, week 6)',
};

export default function MockExam({ onExit }) {
  const [exam, setExam] = useState(() => readJson(EXAM_KEY, null));
  const [history, setHistory] = useState(() => {
    const h = readJson(HISTORY_KEY, []);
    const last = readJson(EXAM_KEY, null);
    if (last?.finishedAt) {
      const match = h.find((e) => !e.ids && Math.abs(new Date(e.date) - last.finishedAt) < 15000);
      if (match) {
        match.ids = last.ids;
        match.answers = last.answers;
        match.paper = last.paper || null;
        writeJson(HISTORY_KEY, h);
      }
    }
    return h;
  });
  const [viewing, setViewing] = useState(null);
  const [now, setNow] = useState(Date.now());
  const [reviewIndex, setReviewIndex] = useState(null);

  useEffect(() => {
    if (!exam || exam.finishedAt) return undefined;
    const timer = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(timer);
  }, [exam]);

  const deadline = exam ? exam.startedAt + EXAM_MINUTES * 60 * 1000 : 0;
  const remaining = exam ? deadline - now : 0;

  function save(next) {
    setExam(next);
    writeJson(EXAM_KEY, next);
  }

  function finish(current = exam) {
    if (!current || current.finishedAt) return;
    const done = { ...current, finishedAt: Date.now() };
    const qs = done.ids.map((id) => byId.get(id)).filter(Boolean);
    const correct = qs.filter((q) => isRight(q, done.answers[q.id])).length;
    const sections = {};
    SECTION_WEIGHTS.forEach(([name]) => {
      const items = qs.filter((q) => q.domain === name);
      if (items.length) sections[name] = Math.round((items.filter((q) => isRight(q, done.answers[q.id])).length / items.length) * 100);
    });
    const entry = {
      label: examLabel(done),
      sections,
      date: new Date().toISOString(),
      correct,
      total: qs.length,
      percent: Math.round((correct / qs.length) * 100),
      minutes: Math.round((done.finishedAt - done.startedAt) / 60000),
      paper: done.paper || null,
      ids: done.ids,
      answers: done.answers,
    };
    recordAnswers(qs.map((q) => ({ q, answer: done.answers[q.id] })), examLabel(done));
    const nextHistory = [entry, ...history].slice(0, 30);
    setHistory(nextHistory);
    writeJson(HISTORY_KEY, nextHistory);
    save(done);
  }

  useEffect(() => {
    if (exam && !exam.finishedAt && remaining <= 0) finish(exam);
  }, [remaining]); // eslint-disable-line react-hooks/exhaustive-deps

  function start(paper = null) {
    setReviewIndex(null);
    save(buildExam(paper));
    setNow(Date.now());
  }

  function removeAttempt(h) {
    if (!window.confirm(`Delete the ${h.label || 'Random mock'} attempt from ${new Date(h.date).toLocaleString()} (${h.correct}/${h.total})?`)) return;
    const next = history.filter((x) => x !== h);
    setHistory(next);
    writeJson(HISTORY_KEY, next);
    setViewing(null);
  }

  function abandon() {
    if (!window.confirm('Discard this mock exam without scoring it?')) return;
    setExam(null);
    writeJson(EXAM_KEY, null);
  }

  // ---------- review of a saved attempt ----------
  if (viewing !== null && history[viewing]) {
    const h = history[viewing];
    const qs = (h.ids || []).map((id) => byId.get(id)).filter(Boolean);
    return (
      <div className="mock-shell">
        <section className="mock-card topic-results">
          <div className={`mock-score ${h.percent >= PASS_PERCENT ? 'pass' : 'fail'}`}>
            <div className="mock-score-num">{h.percent}%</div>
            <div>
              <strong>{h.label || 'Random mock'}: {h.percent >= PASS_PERCENT ? 'PASS' : 'FAIL'}</strong>
              <span>{h.correct} of {h.total} correct &middot; {new Date(h.date).toLocaleString()} &middot; {h.minutes} min</span>
            </div>
          </div>
          {qs.length ? <ReviewList questions={qs} answers={h.answers || {}} /> : <p className="plan-note">This older attempt saved only its score, so its questions cannot be shown.</p>}
          <div className="mock-actions">
            <button className="nav-button" onClick={() => setViewing(null)}><ArrowLeft size={18} /> Back to papers</button>
            <button className="nav-button" onClick={onExit}>Back to study plan</button>
          </div>
        </section>
      </div>
    );
  }

  // ---------- start screen ----------
  if (!exam || (exam.finishedAt && exam.closed)) {
    const quotas = sectionQuotas();
    return (
      <div className="mock-shell">
        <section className="mock-card">
          <div className="mock-head">
            <Trophy size={28} />
            <div>
              <h1>Mock Exam</h1>
              <p>Certified Docusign IAM Integration &amp; Extension Developer</p>
            </div>
          </div>
          <ul className="mock-rules">
            <li><strong>{EXAM_SIZE} questions</strong> drawn at random in the official section proportions</li>
            <li><strong>{EXAM_MINUTES} minutes</strong>; the exam submits itself when time runs out</li>
            <li>No feedback until you submit, like the real exam. Flag questions to revisit them</li>
            <li>Multiple-answer questions tell you how many to select; a partially correct answer scores zero in this mock</li>
            <li>Pass mark <strong>{PASS_PERCENT}%</strong> ({Math.ceil((EXAM_SIZE * PASS_PERCENT) / 100)} of {EXAM_SIZE})</li>
          </ul>
          <table className="mock-table">
            <thead><tr><th>Section</th><th>Weight</th><th>Questions</th></tr></thead>
            <tbody>
              {quotas.map((q, i) => (
                <tr key={q.name}><td>{q.name}</td><td>{SECTION_WEIGHTS[i][1]}%</td><td>{q.count}</td></tr>
              ))}
            </tbody>
          </table>
          <div className="mock-actions">
            <button className="nav-button" onClick={onExit}><ArrowLeft size={18} /> Back to study plan</button>
            <button className="submit-button" onClick={() => start()}>Start random mock</button>
          </div>
          {PAPERS.some((p) => p.ids.length) && (
            <>
              <h3 className="mock-subtitle">Fixed hard papers (60 questions, 150 minutes each)</h3>
              <div className="paper-list">
                {PAPERS.filter((p) => p.ids.length).map((p) => (
                  <div key={p.id} className="paper-row">
                    <button className="submit-button" onClick={() => start(p.id)}>Start Paper {p.id}</button>
                    <span className="mock-paper-note">{PAPER_NOTE[p.id]}</span>
                  </div>
                ))}
              </div>
            </>
          )}
          {history.length > 0 && (
            <>
              <h3 className="mock-subtitle">Previous attempts (click a row to review it)</h3>
              <table className="mock-table history-table">
                <thead><tr><th>Exam</th><th>Date</th><th>Score</th><th>Result</th><th>Time</th><th /></tr></thead>
                <tbody>
                  {history.map((h, hi) => (
                    <tr key={h.date} className="history-row" onClick={() => setViewing(hi)} title="Review this attempt">
                      <td>{h.label || 'Random mock'}</td>
                      <td>{new Date(h.date).toLocaleString()}</td>
                      <td>{h.correct}/{h.total} ({h.percent}%)</td>
                      <td className={h.percent >= PASS_PERCENT ? 'mock-pass' : 'mock-fail'}>{h.percent >= PASS_PERCENT ? 'PASS' : 'FAIL'}</td>
                      <td>{h.minutes} min{!h.ids && <small className="plan-weight"> score only</small>}</td>
                      <td className="history-actions">
                        <button className="icon-button" title="Delete this attempt" onClick={(e) => { e.stopPropagation(); removeAttempt(h); }}><Trash2 size={16} /></button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </>
          )}
        </section>
      </div>
    );
  }

  const examQuestions = exam.ids.map((id) => byId.get(id)).filter(Boolean);

  // ---------- results ----------
  if (exam.finishedAt) {
    const results = examQuestions.map((q) => ({ q, ok: isRight(q, exam.answers[q.id]) }));
    const correct = results.filter((r) => r.ok).length;
    const percent = Math.round((correct / results.length) * 100);
    const passed = percent >= PASS_PERCENT;
    const perSection = SECTION_WEIGHTS.map(([name]) => {
      const items = results.filter((r) => r.q.domain === name);
      const ok = items.filter((r) => r.ok).length;
      return { name, ok, total: items.length, pct: items.length ? Math.round((ok / items.length) * 100) : 0 };
    });
    const review = reviewIndex !== null ? results[reviewIndex] : null;

    return (
      <div className="mock-shell">
        <section className="mock-card">
          <div className={`mock-score ${passed ? 'pass' : 'fail'}`}>
            <div className="mock-score-num">{percent}%</div>
            <div>
              <strong>{examLabel(exam)}: {passed ? 'PASS' : 'FAIL'}</strong>
              <span>{correct} of {results.length} correct &middot; pass mark {PASS_PERCENT}% &middot; time used {formatTime(exam.finishedAt - exam.startedAt)}</span>
            </div>
          </div>

          <h3 className="mock-subtitle">By section (weakest first)</h3>
          <table className="mock-table">
            <thead><tr><th>Section</th><th>Correct</th><th>Score</th></tr></thead>
            <tbody>
              {perSection.slice().sort((a, b) => a.pct - b.pct).map((s) => (
                <tr key={s.name}>
                  <td>{s.name}</td>
                  <td>{s.ok}/{s.total}</td>
                  <td className={s.pct >= PASS_PERCENT ? 'mock-pass' : 'mock-fail'}>{s.pct}%</td>
                </tr>
              ))}
            </tbody>
          </table>

          <h3 className="mock-subtitle">Review answers (every question, right answer and why)</h3>
          <ReviewList questions={examQuestions} answers={exam.answers} />

          <div className="mock-actions">
            <button className="nav-button" onClick={onExit}><ArrowLeft size={18} /> Back to study plan</button>
            <button
              className="nav-button"
              onClick={() => {
                savePrepScores(Object.fromEntries(perSection.filter((s) => s.total).map((s) => [s.name, s.pct])), `${examLabel(exam)}, ${new Date(exam.finishedAt).toLocaleDateString()}`);
                window.alert('Saved. The one-week plan now targets your weakest sections from this exam.');
              }}
            >
              Use these scores for my plan
            </button>
            {exam.paper && (
              <a className="nav-button concept-link" href={`/pdf/paper_${exam.paper}_concepts.pdf`} target="_blank" rel="noreferrer">
                Paper {exam.paper} concepts (PDF)
              </a>
            )}
            <button className="nav-button" onClick={() => save({ ...exam, closed: true })}>All papers and attempts</button>
            <button className="submit-button" onClick={() => start(exam.paper || null)}><RotateCcw size={16} /> {exam.paper ? `Retake Paper ${exam.paper}` : 'New mock exam'}</button>
          </div>
        </section>
      </div>
    );
  }

  // ---------- running exam ----------
  const index = Math.min(exam.current, examQuestions.length - 1);
  const q = examQuestions[index];
  const need = correctIds(q).length;
  const chosen = [].concat(exam.answers[q.id] || []);
  const answeredCount = examQuestions.filter((x) => [].concat(exam.answers[x.id] || []).length > 0).length;

  function choose(optionId) {
    let next;
    if (need > 1) {
      const set = new Set(chosen);
      if (set.has(optionId)) set.delete(optionId);
      else if (set.size < need) set.add(optionId);
      next = Array.from(set).sort();
    } else {
      next = optionId;
    }
    save({ ...exam, answers: { ...exam.answers, [q.id]: next } });
  }

  function go(i) {
    save({ ...exam, current: Math.max(0, Math.min(i, examQuestions.length - 1)) });
  }

  function toggleFlag() {
    save({ ...exam, flagged: { ...exam.flagged, [q.id]: !exam.flagged[q.id] } });
  }

  function submit() {
    const unanswered = examQuestions.length - answeredCount;
    const msg = unanswered ? `${unanswered} question(s) are unanswered. Submit anyway?` : 'Submit the exam for scoring?';
    if (window.confirm(msg)) finish();
  }

  return (
    <div className="app-shell mock-running">
      <aside className="sidebar">
        <div className={`mock-timer ${remaining < 10 * 60 * 1000 ? 'low' : ''}`}>
          <Clock size={18} /> {formatTime(remaining)}
        </div>
        <div className="score-grid">
          <span><strong>{answeredCount}</strong> answered</span>
          <span><strong>{examQuestions.length - answeredCount}</strong> left</span>
          <span><strong>{Object.values(exam.flagged).filter(Boolean).length}</strong> flagged</span>
        </div>
        <div className="mock-grid">
          {examQuestions.map((x, i) => {
            const done = [].concat(exam.answers[x.id] || []).length > 0;
            return (
              <button key={x.id} className={`mock-cell ${done ? 'done' : ''} ${exam.flagged[x.id] ? 'flag' : ''} ${i === index ? 'current' : ''}`} onClick={() => go(i)}>
                {i + 1}
              </button>
            );
          })}
        </div>
        <button className="submit-button mock-submit" onClick={submit}>Submit exam</button>
        <button className="side-action danger" onClick={abandon}><LogOut size={17} /> Quit without scoring</button>
      </aside>

      <main className="question-area">
        <div className="topbar">
          <div>
            <span className="section-label">{examLabel(exam)}</span>
            <h2>Question {index + 1} of {examQuestions.length}</h2>
          </div>
          <button className={`nav-button ${exam.flagged[q.id] ? 'mock-flagged' : ''}`} onClick={toggleFlag}>
            <Flag size={16} /> {exam.flagged[q.id] ? 'Flagged' : 'Flag for review'}
          </button>
        </div>
        <section className="question-card">
          <p className="stem">{q.stem}</p>
          {need > 1 && <div className="multi-note">Select {need} answers. Selected {chosen.length} / {need}.</div>}
          <div className="options">
            {q.options.map((o) => (
              <button key={o.id} className={`option ${chosen.includes(o.id) ? 'selected' : ''}`} onClick={() => choose(o.id)} aria-pressed={chosen.includes(o.id)}>
                <span className="option-letter">{o.id}</span>
                <span>{o.text}</span>
              </button>
            ))}
          </div>
          <div className="question-actions">
            <button className="nav-button" onClick={() => go(index - 1)} disabled={index === 0}><ArrowLeft size={18} /> Previous</button>
            <button className="nav-button" onClick={() => go(index + 1)} disabled={index >= examQuestions.length - 1}>Next <ArrowRight size={18} /></button>
          </div>
        </section>
      </main>

      <aside className="analysis-panel">
        <div className="analysis-header">
          <h2>Exam conditions</h2>
          <p>Answers and explanations appear after you submit. Section names are hidden, as on the real exam.</p>
        </div>
        <div className="pending-panel">
          <p>Tip: answer every question (no penalty for guessing), flag uncertain ones, then use the grid to revisit flagged questions before submitting.</p>
        </div>
      </aside>
    </div>
  );
}

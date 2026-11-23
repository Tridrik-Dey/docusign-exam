import React, { useEffect, useMemo, useState } from 'react';
import { ArrowLeft, ArrowRight, CalendarDays, Clock, ClipboardCheck, Flag, Trash2 } from 'lucide-react';
import papers from './papers.json';
import { savePrepScores } from './StudyPlan.jsx';
import { DEFAULT_SCORES, SECTIONS } from './studyPlan.js';
const CHEAT = Object.fromEntries(SECTIONS.map((s) => [s.name, s.cheat]));
import { ReviewList, correctIds, isActiveMistake, isRight, loadMistakes, orderByMistakes, recordAnswers, MISTAKES_KEY } from './review.jsx';

// Timed section test (1.5 min per question). Pool: topic bank (T) + Papers A and B for that section, plus questions
// you got wrong in Papers C-F you have already taken. Order: your active mistakes first (repeat ones first), then
// unseen questions, then the rest. Papers C-F are otherwise never used here (kept fresh for timed papers).
export const TOPIC_KEY = 'docusign-iam-topic-v1';
const RUN_KEY = 'docusign-iam-topic-run-v1';
const byId = new Map(papers.map((q) => [q.id, q]));

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
    /* ignore */
  }
}

export function loadTopicHistory() {
  return readJson(TOPIC_KEY, { results: [], used: {} }).results || [];
}

// attach the questions/answers of the last finished run to its (older, score-only) history entry
function loadStore() {
  const store = readJson(TOPIC_KEY, { results: [], used: {} });
  store.results = store.results || [];
  store.used = store.used || {};
  const run = readJson(RUN_KEY, null);
  if (run?.finishedAt) {
    const match = store.results.find((r) => !r.ids && r.section === run.domain && Math.abs(new Date(r.date) - run.finishedAt) < 15000);
    if (match) {
      match.ids = run.ids;
      match.answers = run.answers;
      writeJson(TOPIC_KEY, store);
    }
  }
  return store;
}

function poolFor(domain, mistakes) {
  return papers.filter((q) => q.domain === domain && (['T', 'A', 'B'].includes(q.paper) || isActiveMistake(mistakes[q.id])));
}

function fmt(ms) {
  const t = Math.max(0, Math.round(ms / 1000));
  return `${Math.floor(t / 60)}:${String(t % 60).padStart(2, '0')}`;
}

export default function TopicTest({ initialDomain, initialSize, onPlan }) {
  const [store, setStore] = useState(loadStore);
  const [run, setRun] = useState(() => readJson(RUN_KEY, null));
  const [domain, setDomain] = useState(initialDomain && initialDomain !== 'All' ? initialDomain : SECTIONS[0].name);
  const [size, setSize] = useState(initialSize || 15);
  const [now, setNow] = useState(Date.now());
  // 'start' = start screen, 'results' = results of the run just finished, number = saved attempt being reviewed
  const [view, setView] = useState(() => (readJson(RUN_KEY, null)?.finishedAt ? 'start' : 'results'));

  const mistakes = useMemo(() => loadMistakes(), [store, run?.finishedAt]); // eslint-disable-line react-hooks/exhaustive-deps
  const available = useMemo(() => poolFor(domain, mistakes), [domain, mistakes]);
  const active = available.filter((q) => isActiveMistake(mistakes[q.id]));
  const repeat = active.filter((q) => mistakes[q.id].wrong >= 2).length;
  const unseen = available.filter((q) => !mistakes[q.id] && !store.used[q.id]).length;

  useEffect(() => {
    if (!run || run.finishedAt) return undefined;
    const t = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(t);
  }, [run]);

  function saveRun(next) {
    setRun(next);
    writeJson(RUN_KEY, next);
  }

  function saveStore(next) {
    setStore(next);
    writeJson(TOPIC_KEY, next);
  }

  function start() {
    const ordered = orderByMistakes(available, mistakes, store.used);
    const ids = ordered.slice(0, Math.min(size, ordered.length)).map((q) => q.id);
    setNow(Date.now());
    setView('results');
    saveRun({ domain, ids, answers: {}, flagged: {}, current: 0, startedAt: Date.now(), minutes: Math.round(ids.length * 1.5), finishedAt: null });
  }

  const remaining = run ? run.startedAt + run.minutes * 60000 - now : 0;

  function finish(current = run) {
    if (!current || current.finishedAt) return;
    const qs = current.ids.map((id) => byId.get(id)).filter(Boolean);
    const correct = qs.filter((q) => isRight(q, current.answers[q.id])).length;
    const pct = Math.round((correct / qs.length) * 100);
    const finishedAt = Date.now();
    recordAnswers(qs.map((q) => ({ q, answer: current.answers[q.id], flagged: Boolean(current.flagged?.[q.id]) })), 'topic');
    saveStore({
      results: [...store.results, { section: current.domain, date: new Date(finishedAt).toISOString(), correct, total: qs.length, pct, ids: current.ids, answers: current.answers, flagged: current.flagged || {} }],
      used: { ...store.used, ...Object.fromEntries(current.ids.map((id) => [id, true])) },
    });
    savePrepScores({ [current.domain]: pct }, `Topic test ${current.domain}, ${new Date().toLocaleDateString()}`);
    saveRun({ ...current, finishedAt, pct, correct });
    setView('results');
    window.scrollTo(0, 0);
  }

  useEffect(() => {
    if (run && !run.finishedAt && remaining <= 0) finish(run);
  }, [remaining]); // eslint-disable-line react-hooks/exhaustive-deps

  function remove(result) {
    if (!window.confirm(`Delete the ${result.section} result from ${new Date(result.date).toLocaleString()} (${result.correct}/${result.total})? Its score is removed from your plan and its questions count as unseen again.`)) return;
    const results = store.results.filter((r) => r !== result);
    const used = { ...store.used };
    (result.ids || []).forEach((id) => delete used[id]);
    // undo what this attempt added to the mistake list
    if (result.ids) {
      const m = loadMistakes();
      result.ids.forEach((id) => {
        const q = byId.get(id);
        const r = m[id];
        if (!q || !r) return;
        r.seen = Math.max(0, r.seen - 1);
        if (!isRight(q, result.answers?.[id])) r.wrong = Math.max(0, r.wrong - 1);
        else if (result.flagged?.[id]) r.unsure = Math.max(0, (r.unsure || 0) - 1);
        if (!r.seen) delete m[id];
      });
      writeJson(MISTAKES_KEY, m);
    }
    saveStore({ results, used });
    const left = results.filter((r) => r.section === result.section);
    const restore = left.length ? left[left.length - 1].pct : DEFAULT_SCORES[result.section];
    savePrepScores({ [result.section]: restore }, left.length ? `Topic test ${result.section}, ${new Date(left[left.length - 1].date).toLocaleDateString()}` : 'Official score report, 22 Nov 2026');
    if (run?.finishedAt && result.ids && run.ids.join() === result.ids.join()) {
      setRun(null);
      writeJson(RUN_KEY, null);
    }
    setView('start');
  }

  // ---------- review of a saved attempt ----------
  if (typeof view === 'number' && store.results[view]) {
    const res = store.results[view];
    const qs = (res.ids || []).map((id) => byId.get(id)).filter(Boolean);
    return (
      <div className="mock-shell">
        <section className="mock-card topic-results">
          <div className={`mock-score ${res.pct >= 70 ? 'pass' : 'fail'}`}>
            <div className="mock-score-num">{res.pct}%</div>
            <div>
              <strong>{res.section}</strong>
              <span>{res.correct} of {res.total} correct &middot; {new Date(res.date).toLocaleString()}</span>
            </div>
          </div>
          {qs.length ? (
            <ReviewList
              questions={qs}
              answers={res.answers || {}}
              actions={<>
                <button className="nav-button" onClick={() => setView('start')}><ArrowLeft size={18} /> Back to topic tests</button>
                <button className="nav-button" onClick={onPlan}><CalendarDays size={18} /> Back to plan</button>
              </>}
            />
          ) :<p className="plan-note">This older attempt saved only its score, so its questions cannot be shown.</p>}
          <div className="mock-actions">
            <button className="nav-button" onClick={() => setView('start')}><ArrowLeft size={18} /> Back to topic tests</button>
            <button className="nav-button" onClick={onPlan}><CalendarDays size={18} /> Back to plan</button>
          </div>
        </section>
      </div>
    );
  }

  // ---------- start screen ----------
  if (!run || (run.finishedAt && view === 'start')) {
    const history = store.results.map((r, i) => ({ r, i })).filter(({ r }) => r.section === domain).reverse();
    return (
      <div className="mock-shell">
        <section className="mock-card">
          <div className="mock-head">
            <ClipboardCheck size={28} />
            <div>
              <h1>Topic test</h1>
              <p>Timed section test in real-exam style. Your score updates that section in the plan.</p>
            </div>
          </div>
          <div className="topic-setup">
            <label className="plan-date">Section
              <select value={domain} onChange={(e) => setDomain(e.target.value)}>
                {SECTIONS.map((s) => <option key={s.name} value={s.name}>{s.name}</option>)}
              </select>
            </label>
            <label className="plan-date">Length
              <select value={size} onChange={(e) => setSize(Number(e.target.value))}>
                <option value={5}>5 questions, 8 min (timed set)</option>
                <option value={8}>8 questions, 12 min (strength check)</option>
                <option value={15}>15 questions, 23 min (weak section)</option>
              </select>
            </label>
          </div>
          <p className="mock-paper-note">
            {available.length} questions in this section's pool &middot; {unseen} not seen yet.
            {active.length > 0 && <strong className="mistake-note"> {active.length} of your mistakes come first ({repeat} repeated).</strong>} No feedback until you submit.
          </p>
          <div className="mock-actions">
            <button className="nav-button" onClick={onPlan}><ArrowLeft size={18} /> Back to plan</button>
            <button className="submit-button" onClick={start} disabled={!available.length}>Start topic test</button>
          </div>
          {history.length > 0 && (
            <>
              <h3 className="mock-subtitle">Recent results: {domain} (click a row to review it)</h3>
              <table className="mock-table history-table">
                <thead><tr><th>Date</th><th>Score</th><th /></tr></thead>
                <tbody>
                  {history.map(({ r, i }) => (
                    <tr key={r.date} className="history-row" onClick={() => setView(i)} title="Review this attempt">
                      <td>{new Date(r.date).toLocaleString()}</td>
                      <td className={r.pct >= 70 ? 'mock-pass' : 'mock-fail'}>{r.correct}/{r.total} ({r.pct}%){!r.ids && <small className="plan-weight"> score only</small>}</td>
                      <td className="history-actions">
                        <button className="icon-button" title="Delete this result" onClick={(e) => { e.stopPropagation(); remove(r); }}><Trash2 size={16} /></button>
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

  const qs = run.ids.map((id) => byId.get(id)).filter(Boolean);

  // ---------- results of the run just finished ----------
  if (run.finishedAt) {
    return (
      <div className="mock-shell">
        <section className="mock-card topic-results">
          <div className={`mock-score ${run.pct >= 70 ? 'pass' : 'fail'}`}>
            <div className="mock-score-num">{run.pct}%</div>
            <div>
              <strong>{run.domain}</strong>
              <span>{run.correct} of {qs.length} correct &middot; saved to your plan scores; wrong ones go to your mistake list {run.pct >= 85 ? '(85%+ twice in a row = mastered)' : run.pct < 70 ? '(under 70%: extra practice gets added)' : ''}</span>
            </div>
          </div>
          <ReviewList questions={qs} answers={run.answers} actions={<>
            <button className="nav-button" onClick={onPlan}><CalendarDays size={18} /> Back to plan</button>
            <a className="nav-button concept-link" href={`/pdf/${CHEAT[run.domain]}`} target="_blank" rel="noreferrer">{run.domain} cheat sheet (PDF)</a>
            <button className="submit-button" onClick={() => setView('start')}>New topic test</button>
</>} />
          <div className="mock-actions">
            <button className="nav-button" onClick={onPlan}><CalendarDays size={18} /> Back to plan</button>
            <a className="nav-button concept-link" href={`/pdf/${CHEAT[run.domain]}`} target="_blank" rel="noreferrer">{run.domain} cheat sheet (PDF)</a>
            <button className="submit-button" onClick={() => setView('start')}>New topic test</button>
          </div>
        </section>
      </div>
    );
  }

  // ---------- running ----------
  const index = Math.min(run.current, qs.length - 1);
  const q = qs[index];
  const need = correctIds(q).length;
  const chosen = [].concat(run.answers[q.id] || []);
  const answered = qs.filter((x) => [].concat(run.answers[x.id] || []).length > 0).length;

  function choose(id) {
    let next;
    if (need > 1) {
      const set = new Set(chosen);
      if (set.has(id)) set.delete(id);
      else if (set.size < need) set.add(id);
      next = Array.from(set).sort();
    } else next = id;
    saveRun({ ...run, answers: { ...run.answers, [q.id]: next } });
  }
  const go = (i) => saveRun({ ...run, current: Math.max(0, Math.min(i, qs.length - 1)) });

  return (
    <div className="app-shell mock-running">
      <aside className="sidebar">
        <div className={`mock-timer ${remaining < 3 * 60000 ? 'low' : ''}`}><Clock size={18} /> {fmt(remaining)}</div>
        <div className="score-grid">
          <span><strong>{answered}</strong> answered</span>
          <span><strong>{qs.length - answered}</strong> left</span>
        </div>
        <div className="mock-grid">
          {qs.map((x, i) => (
            <button key={x.id} className={`mock-cell ${[].concat(run.answers[x.id] || []).length ? 'done' : ''} ${run.flagged[x.id] ? 'flag' : ''} ${i === index ? 'current' : ''}`} onClick={() => go(i)}>{i + 1}</button>
          ))}
        </div>
        <button className="submit-button mock-submit" onClick={() => window.confirm(answered < qs.length ? `${qs.length - answered} unanswered. Submit anyway?` : 'Submit the test?') && finish()}>Submit test</button>
      </aside>
      <main className="question-area">
        <div className="topbar">
          <div>
            <span className="section-label">Topic test &middot; {run.domain}</span>
            <h2>Question {index + 1} of {qs.length}</h2>
          </div>
          <button className={`nav-button ${run.flagged[q.id] ? 'mock-flagged' : ''}`} onClick={() => saveRun({ ...run, flagged: { ...run.flagged, [q.id]: !run.flagged[q.id] } })}>
            <Flag size={16} /> {run.flagged[q.id] ? 'Flagged: unsure' : 'Flag if unsure'}
          </button>
        </div>
        <section className="question-card">
          <p className="stem">{q.stem}</p>
          {need > 1 && <div className="multi-note">Select {need} answers. Selected {chosen.length} / {need}.</div>}
          <div className="options">
            {q.options.map((o) => (
              <button key={o.id} className={`option ${chosen.includes(o.id) ? 'selected' : ''}`} onClick={() => choose(o.id)}>
                <span className="option-letter">{o.id}</span><span>{o.text}</span>
              </button>
            ))}
          </div>
          <div className="question-actions">
            <button className="nav-button" onClick={() => go(index - 1)} disabled={index === 0}><ArrowLeft size={18} /> Previous</button>
            <button className="nav-button" onClick={() => go(index + 1)} disabled={index >= qs.length - 1}>Next <ArrowRight size={18} /></button>
          </div>
        </section>
      </main>
      <aside className="analysis-panel">
        <div className="analysis-header">
          <h2>Decode first</h2>
          <p>Who acts? Is a user present? Which level? When? Enforce or record? Which product? Then read the options.</p>
        </div>
      </aside>
    </div>
  );
}

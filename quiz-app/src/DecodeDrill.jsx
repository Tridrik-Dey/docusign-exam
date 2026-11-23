import React, { useMemo, useState } from 'react';
import { ArrowLeft, ArrowRight, CalendarDays, Search } from 'lucide-react';
import papers from './papers.json';
import { ImportanceTag } from './importance.jsx';
import { isActiveMistake, loadMistakes, orderByMistakes, recordAnswers } from './review.jsx';

// Decode drill: hard scenario questions (Papers A and B; C and D stay unseen for the timed papers).
// Step 1: read the scenario WITHOUT the options and pick what it really needs.
// Step 2: answer the real question. Step 3: see the clues, the trap and why the others fail.
const DRILL_KEY = 'docusign-iam-drill-v1';
const POOL = papers.filter((q) => q.paper === 'A' || q.paper === 'B');

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

function correctIds(q) {
  return Array.isArray(q.correctAnswers) ? q.correctAnswers : [q.correct];
}

function sameSet(a, b) {
  const x = a.slice().sort();
  const y = b.slice().sort();
  return x.length === y.length && x.every((v, i) => v === y[i]);
}

export default function DecodeDrill({ initialDomain = 'All', onPlan }) {
  const saved = useMemo(() => readJson(DRILL_KEY, {}), []);
  const [domain, setDomain] = useState(initialDomain || saved.domain || 'All');
  const [results, setResults] = useState(saved.results || {});
  const [index, setIndex] = useState(0);
  const [step, setStep] = useState('decode');
  const [decodePick, setDecodePick] = useState(null);
  const [picks, setPicks] = useState([]);

  const domains = useMemo(() => ['All', ...Array.from(new Set(POOL.map((q) => q.domain)))], []);
  // your mistakes first (repeat ones first; also misses from Papers C-F you already took), then unseen, then the rest
  const list = useMemo(() => {
    const m = loadMistakes();
    const pool = papers.filter((q) => (domain === 'All' || q.domain === domain) && (POOL.includes(q) || isActiveMistake(m[q.id])));
    const seen = Object.fromEntries(Object.keys(results).map((id) => [id, true]));
    return orderByMistakes(pool, m, seen);
  }, [domain]); // eslint-disable-line react-hooks/exhaustive-deps

  const q = list[Math.min(index, list.length - 1)];
  const hasDecode = Boolean(q?.decode?.options?.length);
  const need = q ? correctIds(q).length : 1;
  const effectiveStep = step === 'decode' && !hasDecode ? 'answer' : step;

  function persist(nextResults, nextDomain = domain) {
    writeJson(DRILL_KEY, { domain: nextDomain, results: nextResults });
  }

  function go(i) {
    setIndex(Math.max(0, Math.min(i, list.length - 1)));
    setStep('decode');
    setDecodePick(null);
    setPicks([]);
  }

  function changeDomain(d) {
    setDomain(d);
    persist(results, d);
    setIndex(0);
    setStep('decode');
    setDecodePick(null);
    setPicks([]);
  }

  function checkDecode() {
    setStep('decoded');
  }

  function choose(id) {
    if (effectiveStep !== 'answer') return;
    if (need > 1) {
      const set = new Set(picks);
      if (set.has(id)) set.delete(id);
      else if (set.size < need) set.add(id);
      setPicks(Array.from(set).sort());
    } else setPicks([id]);
  }

  function checkAnswer() {
    const ok = sameSet(picks, correctIds(q));
    const decodeOk = hasDecode ? decodePick === q.decode.correct : null;
    const next = { ...results, [q.id]: { ok, decode: decodeOk } };
    setResults(next);
    persist(next);
    recordAnswers([{ q, answer: picks }], 'drill');
    setStep('done');
  }

  const stats = useMemo(() => {
    const items = POOL.filter((x) => domain === 'All' || x.domain === domain);
    const seen = items.filter((x) => results[x.id]);
    const dec = seen.filter((x) => results[x.id].decode !== null);
    return {
      total: items.length,
      seen: seen.length,
      ok: seen.filter((x) => results[x.id].ok).length,
      decSeen: dec.length,
      decOk: dec.filter((x) => results[x.id].decode).length,
    };
  }, [results, domain]);

  if (!q) {
    return (
      <div className="mock-shell"><section className="mock-card"><p>No drill questions for this section yet.</p>
        <button className="nav-button" onClick={onPlan}><ArrowLeft size={18} /> Back to plan</button></section></div>
    );
  }

  const correct = correctIds(q);
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="mark"><Search size={18} /></div>
          <div>
            <h1>Decode drill</h1>
            <p>Decide what the scenario needs, then answer</p>
          </div>
        </div>
        <label className="plan-date">
          Section
          <select value={domain} onChange={(e) => changeDomain(e.target.value)}>
            {domains.map((d) => <option key={d} value={d}>{d}</option>)}
          </select>
        </label>
        <div className="score-grid">
          <span><strong>{stats.seen}</strong>/{stats.total} done</span>
          <span><strong>{stats.seen ? Math.round((stats.ok / stats.seen) * 100) : 0}%</strong> answers right</span>
          <span><strong>{stats.decSeen ? Math.round((stats.decOk / stats.decSeen) * 100) : 0}%</strong> decoded right</span>
        </div>
        <p className="plan-note">Your mistakes come first (repeat ones first), then unseen questions. Pool: Papers A and B, plus questions you missed in Papers C-F you already took.</p>
        <button className="side-action" onClick={onPlan}><CalendarDays size={17} /> Back to plan</button>
      </aside>

      <main className="question-area">
        <div className="topbar">
          <div>
            <span className="section-label">{q.domain} &middot; Question {Math.min(index, list.length - 1) + 1} of {list.length}</span>
            <h2>{effectiveStep === 'decode' ? 'Step 1: what does this scenario need?' : effectiveStep === 'decoded' ? 'Step 1: check your reading' : effectiveStep === 'answer' ? 'Step 2: answer the question' : 'Step 3: learn from it'}</h2>
          </div>
        </div>
        <section className="question-card">
          {effectiveStep === 'done' && <div className="topic-row"><ImportanceTag level={q.importance} /><span className="topic">{q.topic}</span></div>}
          <p className="stem">{q.stem}</p>

          {(effectiveStep === 'decode' || effectiveStep === 'decoded') && (
            <>
              <p className="drill-prompt">{q.decode.prompt}</p>
              <div className="options">
                {q.decode.options.map((o) => {
                  const shown = effectiveStep === 'decoded';
                  const cls = shown ? (o.id === q.decode.correct ? 'correct' : o.id === decodePick ? 'wrong' : '') : decodePick === o.id ? 'selected' : '';
                  return (
                    <button key={o.id} className={`option ${cls}`} onClick={() => !shown && setDecodePick(o.id)}>
                      <span className="option-letter">{o.id}</span><span>{o.text}</span>
                    </button>
                  );
                })}
              </div>
              {effectiveStep === 'decoded' && (
                <div className="why-not drill-box">
                  <h3>{decodePick === q.decode.correct ? 'Good reading.' : 'Not quite.'} The scenario needs:</h3>
                  <p>{q.decode.needs || q.decode.explanation}</p>
                  {q.decode.explanation && q.decode.needs && <p>{q.decode.explanation}</p>}
                  {q.decode.clues?.length > 0 && <ul>{q.decode.clues.map((c) => <li key={c}>{c}</li>)}</ul>}
                </div>
              )}
              <div className="question-actions">
                {effectiveStep === 'decode'
                  ? <button className="submit-button" disabled={!decodePick} onClick={checkDecode}>Check my reading</button>
                  : <button className="submit-button" onClick={() => setStep('answer')}>Show the answer options <ArrowRight size={16} /></button>}
              </div>
            </>
          )}

          {(effectiveStep === 'answer' || effectiveStep === 'done') && (
            <>
              {need > 1 && <div className="multi-note">Select {need} answers. Selected {picks.length} / {need}.</div>}
              <div className="options">
                {q.options.map((o) => {
                  const done = effectiveStep === 'done';
                  const cls = done ? (correct.includes(o.id) ? 'correct' : picks.includes(o.id) ? 'wrong' : '') : picks.includes(o.id) ? 'selected' : '';
                  return (
                    <button key={o.id} className={`option ${cls}`} onClick={() => choose(o.id)}>
                      <span className="option-letter">{o.id}</span>
                      <span>
                        {o.text}
                        {done && q.trapOption === o.id && <em className="trap-badge">TRAP</em>}
                        {done && <small className="mock-why">{q.optionExplanations?.[o.id]}</small>}
                      </span>
                    </button>
                  );
                })}
              </div>
              {effectiveStep === 'done' && (
                <>
                  <p className="mock-expl"><strong>Explanation:</strong> {q.explanation}</p>
                  {q.whyNotOthers && <p className="mock-expl why-not"><strong>Why this answer and not the others:</strong> {q.whyNotOthers}</p>}
                </>
              )}
              <div className="question-actions">
                <button className="nav-button" onClick={() => go(index - 1)} disabled={index === 0}><ArrowLeft size={18} /> Previous</button>
                {effectiveStep === 'answer'
                  ? <button className="submit-button" disabled={picks.length !== need} onClick={checkAnswer}>Check answer</button>
                  : <button className="nav-button" onClick={() => go(index + 1)} disabled={index >= list.length - 1}>Next <ArrowRight size={18} /></button>}
              </div>
            </>
          )}
        </section>
      </main>

      <aside className="analysis-panel">
        <div className="analysis-header">
          <h2>How to decode</h2>
          <p>Answer these before you look at the options:</p>
        </div>
        <ol className="drill-checklist">
          <li><strong>Who acts?</strong> A signer, a sender, an admin, or a system with nobody logged in?</li>
          <li><strong>Where does the code run?</strong> A server that can keep a secret, or a browser / phone app?</li>
          <li><strong>What scope?</strong> One envelope, one account, or every account in the organization?</li>
          <li><strong>When?</strong> In real time, later in a batch, only for new items, or for ones already running?</li>
          <li><strong>Enforce or record?</strong> Must Docusign block / verify something, or only note it?</li>
          <li><strong>Which product owns it?</strong> eSignature, Connect, Web Forms, Maestro workflow, Agreement Manager, or an extension app?</li>
          <li><strong>Ignore the noise:</strong> company size, industry and tool names rarely change the answer.</li>
        </ol>
      </aside>
    </div>
  );
}

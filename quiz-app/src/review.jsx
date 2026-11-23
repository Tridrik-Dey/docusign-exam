import React, { useState } from 'react';
import { ImportanceTag } from './importance.jsx';

// ---------------------------------------------------------------------------------------------------------------
// Personal mistake list. Every answer from topic tests, the decode drill, mock exams and papers is recorded per
// question id. A question is an "active mistake" while it has been answered wrong and not yet answered right twice
// in a row. Active mistakes are served first (repeat mistakes before one-off ones), then unseen questions, then the
// ones already answered right.
// ---------------------------------------------------------------------------------------------------------------
export const MISTAKES_KEY = 'docusign-iam-mistakes-v1';

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

export function correctIds(q) {
  return Array.isArray(q.correctAnswers) ? q.correctAnswers : [q.correct];
}

export function isRight(q, answer) {
  const chosen = [].concat(answer || []).slice().sort();
  const right = correctIds(q).slice().sort();
  return chosen.length === right.length && chosen.every((id, i) => id === right[i]);
}

export function loadMistakes() {
  return readJson(MISTAKES_KEY, {});
}

// items: [{ q, answer, flagged }]  (answer = what the learner chose; empty = unanswered = wrong;
// flagged = the learner marked it as unsure: a right but flagged answer still goes on the list as 'unsure')
export function recordAnswers(items, source) {
  const store = loadMistakes();
  const now = new Date().toISOString();
  items.forEach(({ q, answer, flagged }) => {
    const ok = isRight(q, answer);
    const r = store[q.id] || { seen: 0, wrong: 0, rightStreak: 0, section: q.domain };
    r.seen += 1;
    r.section = q.domain;
    r.lastSeenAt = now;
    r.lastSource = source;
    if (ok && flagged) {
      // right but unsure: keep it on the list until it is answered right once more without a flag
      r.unsure = (r.unsure || 0) + 1;
      r.rightStreak = 1;
      r.lastWrongAt = now;
    } else if (ok) {
      r.rightStreak = (r.rightStreak || 0) + 1;
    } else {
      r.wrong += 1;
      r.rightStreak = 0;
      r.lastWrongAt = now;
      r.lastAnswer = [].concat(answer || []);
    }
    store[q.id] = r;
  });
  writeJson(MISTAKES_KEY, store);
  return store;
}

export function isActiveMistake(r) {
  return Boolean(r && (r.wrong > 0 || r.unsure > 0) && (r.rightStreak || 0) < 2);
}

// 0 = repeat mistake, 1 = one-off mistake, 2 = unseen, 3 = seen and fine
export function mistakeRank(r) {
  if (isActiveMistake(r)) return r.wrong >= 2 ? 0 : 1;
  return r ? 3 : 2;
}

function shuffle(list) {
  const copy = list.slice();
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

// Order a question pool: active mistakes first (repeat ones, then most recent), unseen next, then the rest (random).
export function orderByMistakes(pool, store = loadMistakes(), extraSeen = {}) {
  const rank = (q) => {
    const r = store[q.id];
    if (!r && extraSeen[q.id]) return 3;
    return mistakeRank(r);
  };
  return shuffle(pool).sort((a, b) => {
    const d = rank(a) - rank(b);
    if (d) return d;
    const ra = store[a.id];
    const rb = store[b.id];
    if (ra?.wrong !== rb?.wrong) return (rb?.wrong || 0) - (ra?.wrong || 0);
    return String(rb?.lastWrongAt || '').localeCompare(String(ra?.lastWrongAt || ''));
  });
}

export function activeMistakesFor(section, papersPool, store = loadMistakes()) {
  return papersPool
    .filter((q) => (section === 'All' || q.domain === section) && isActiveMistake(store[q.id]))
    .sort((a, b) => store[b.id].wrong - store[a.id].wrong || String(store[b.id].lastWrongAt).localeCompare(String(store[a.id].lastWrongAt)));
}

// ---------------------------------------------------------------------------------------------------------------
// One-page review: every question with the learner's answer, the right answer, the trap, a reason per option,
// why-not-others and the decode notes.
// ---------------------------------------------------------------------------------------------------------------
export function ReviewList({ questions, answers = {}, showAnswerLabel = true, mistakes = null, startFilteredToWrong = false, actions = null, hideBar = false, numberFrom = 0 }) {
  const [onlyWrong, setOnlyWrong] = useState(startFilteredToWrong);
  const rows = questions.map((q, i) => ({ q, i, ok: answers ? isRight(q, answers[q.id]) : false }));
  const wrongCount = rows.filter((r) => !r.ok).length;
  const shown = rows.filter((r) => !(onlyWrong && r.ok));
  return (
    <>
      {!hideBar && <div className="topic-review-bar">
        {actions && <div className="mock-actions review-top-actions">{actions}</div>}
        <div className="mock-grid">
          {rows.map(({ q, i, ok }) => (
            <a key={q.id} href={`#rq-${i + 1}`} className={`mock-cell ${showAnswerLabel ? (ok ? 'ok' : 'bad') : ''}`}>{i + 1}</a>
          ))}
        </div>
        {showAnswerLabel && (
          <label className="topic-filter">
            <input type="checkbox" checked={onlyWrong} onChange={(e) => setOnlyWrong(e.target.checked)} /> Show only the {wrongCount} I got wrong
          </label>
        )}
      </div>}
      {shown.map(({ q: r, i, ok }) => {
        const chosen = [].concat((answers && answers[r.id]) || (mistakes?.[r.id]?.lastAnswer) || []);
        const m = mistakes?.[r.id];
        return (
          <div key={r.id} id={`rq-${i + 1}`} className={`mock-review topic-item ${showAnswerLabel ? (ok ? 'is-ok' : 'is-bad') : 'is-bad'}`}>
            <div className="section-label">
              {showAnswerLabel && <span className={`topic-verdict ${ok ? 'ok' : 'bad'}`}>{ok ? 'Correct' : 'Wrong'}</span>}
              {m && m.wrong > 0 && <span className="topic-verdict bad" title={`answered wrong ${m.wrong} time(s)`}>{m.wrong}x</span>}
              {m && !m.wrong && m.unsure > 0 && <span className="topic-verdict unsure">unsure</span>}
              {' '}Question {numberFrom + i + 1} &middot; <ImportanceTag level={r.importance} /> {r.domain} &middot; {r.topic}
            </div>
            <p className="stem">{r.stem}</p>
            {r.options.map((o) => {
              const right = correctIds(r).includes(o.id);
              return (
                <div key={o.id} className={`option ${right ? 'correct' : ''} ${chosen.includes(o.id) && !right ? 'wrong' : ''}`}>
                  <span className="option-letter">{o.id}</span>
                  <span>
                    {o.text}
                    {right && <em className="topic-right"> (right answer)</em>}
                    {chosen.includes(o.id) && <em className="mock-you"> {m && !answers ? '(your last wrong answer)' : '(your answer)'}</em>}
                    {r.trapOption === o.id && <em className="trap-badge">TRAP</em>}
                    <small className="mock-why">{r.optionExplanations?.[o.id]}</small>
                  </span>
                </div>
              );
            })}
            {showAnswerLabel && !chosen.length && <p className="mock-expl"><strong>You did not answer this question.</strong></p>}
            <p className="mock-expl"><strong>Explanation:</strong> {r.explanation}</p>
            {r.whyNotOthers && <p className="mock-expl why-not"><strong>Why this answer and not the others:</strong> {r.whyNotOthers}</p>}
            {r.decode?.needs && (
              <div className="mock-expl drill-box decode-box">
                <strong>Decode the scenario:</strong> {r.decode.needs}
                {r.decode.clues?.length > 0 && <ul>{r.decode.clues.map((c) => <li key={c}>{c}</li>)}</ul>}
              </div>
            )}
          </div>
        );
      })}
    </>
  );
}

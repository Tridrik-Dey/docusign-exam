import React, { useMemo, useState } from 'react';
import { ArrowLeft, ArrowRight, ClipboardCheck, Search } from 'lucide-react';
import papers from './papers.json';
import questions from './questions.json';
import { SECTIONS } from './studyPlan.js';
import { ReviewList, isActiveMistake, loadMistakes } from './review.jsx';

const CHEAT = Object.fromEntries(SECTIONS.map((s) => [s.name, s.cheat]));
const byId = new Map([...questions, ...papers].map((q) => [String(q.id), q]));

// "My mistakes": one question at a time. The numbered boxes at the top, grouped by topic, open each mistake.
// A wrong answer leaves the list after two right answers in a row; an "unsure" one after one more right answer
// without a flag. Until then they come first in topic tests and drills.
export default function MistakesPage({ initialDomain = 'All', onPlan, onAction }) {
  const [domain, setDomain] = useState(initialDomain || 'All');
  const store = useMemo(() => loadMistakes(), []);

  // all open mistakes grouped by section, worst first inside each group
  const groups = useMemo(() => {
    const all = Object.entries(store)
      .filter(([, r]) => isActiveMistake(r))
      .map(([id, r]) => ({ q: byId.get(String(id)), r }))
      .filter(({ q }) => q);
    return SECTIONS.map((s) => ({
      name: s.name,
      items: all
        .filter(({ q }) => q.domain === s.name)
        .sort((a, b) => (b.r.wrong || 0) - (a.r.wrong || 0) || String(b.r.lastWrongAt || '').localeCompare(String(a.r.lastWrongAt || ''))),
    })).filter((g) => g.items.length);
  }, [store]);

  const shownGroups = groups.filter((g) => domain === 'All' || g.name === domain);
  const flat = shownGroups.flatMap((g) => g.items.map((it) => ({ ...it, section: g.name })));
  const [selected, setSelected] = useState(null);
  const current = flat.find((x) => x.q.id === selected) || flat[0];
  const index = current ? flat.indexOf(current) : -1;
  const cleared = Object.values(store).filter((r) => (r.wrong > 0 || r.unsure > 0) && (r.rightStreak || 0) >= 2).length;
  const total = groups.reduce((n, g) => n + g.items.length, 0);

  function pick(id) {
    setSelected(id);
    window.scrollTo(0, 0);
  }

  return (
    <div className="mock-shell">
      <section className="mock-card topic-results">
        <div className="mock-head">
          <Search size={28} />
          <div>
            <h1>My mistakes</h1>
            <p>Questions you got wrong or flagged as unsure. Click a number to open it. They come first in your topic tests and drills until you have answered them right again.</p>
          </div>
        </div>
        <div className="topic-setup">
          <label className="plan-date">Topic
            <select value={domain} onChange={(e) => { setDomain(e.target.value); setSelected(null); }}>
              <option value="All">All topics ({total})</option>
              {SECTIONS.map((s) => {
                const n = groups.find((g) => g.name === s.name)?.items.length || 0;
                return <option key={s.name} value={s.name}>{s.name} ({n})</option>;
              })}
            </select>
          </label>
          <div className="mock-paper-note mistakes-summary">{flat.length} open here &middot; {cleared} cleared so far</div>
        </div>
        <div className="mock-actions">
          <button className="nav-button" onClick={onPlan}><ArrowLeft size={18} /> Back to plan</button>
          {current && (
            <a className="nav-button concept-link" href={`/pdf/${CHEAT[current.section]}`} target="_blank" rel="noreferrer">{current.section} cheat sheet (PDF)</a>
          )}
          {domain !== 'All' && flat.length > 0 && (
            <button className="submit-button" onClick={() => onAction({ type: 'topic', domain, size: Math.min(15, Math.max(5, flat.length)) })}>
              <ClipboardCheck size={16} /> Retest these now
            </button>
          )}
        </div>

        {flat.length === 0 ? (
          <p className="plan-note">No open mistakes{domain !== 'All' ? ` in ${domain}` : ''}. Take a topic test or the decode drill; anything you get wrong or flag as unsure appears here.</p>
        ) : (
          <>
            <div className="mistake-groups">
              {shownGroups.map((g) => (
                <div key={g.name} className="mistake-group">
                  <div className="mistake-group-title">{g.name} <span>({g.items.length})</span></div>
                  <div className="mock-grid">
                    {g.items.map(({ q, r }) => {
                      const n = flat.findIndex((x) => x.q.id === q.id) + 1;
                      return (
                        <button
                          key={q.id}
                          className={`mock-cell ${r.wrong ? 'bad' : 'flag'} ${current?.q.id === q.id ? 'current' : ''}`}
                          onClick={() => pick(q.id)}
                          title={r.wrong ? `wrong ${r.wrong}x` : 'unsure'}
                        >
                          {n}
                        </button>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>
            <ReviewList questions={[current.q]} answers={null} showAnswerLabel={false} mistakes={store} hideBar numberFrom={index} />
            <div className="question-actions">
              <button className="nav-button" onClick={() => pick(flat[index - 1].q.id)} disabled={index <= 0}><ArrowLeft size={18} /> Previous</button>
              <button className="nav-button" onClick={() => pick(flat[index + 1].q.id)} disabled={index >= flat.length - 1}>Next <ArrowRight size={18} /></button>
            </div>
          </>
        )}
      </section>
    </div>
  );
}

import React, { useMemo, useState } from 'react';
import { ArrowLeft, ClipboardCheck, Search } from 'lucide-react';
import papers from './papers.json';
import { SECTIONS } from './studyPlan.js';
import { ReviewList, activeMistakesFor, loadMistakes } from './review.jsx';

// "My mistakes": every question you have answered wrong and not yet answered right twice in a row, worst first,
// with your last wrong answer, the right answer and the full explanation.
export default function MistakesPage({ initialDomain = 'All', onPlan, onAction }) {
  const [domain, setDomain] = useState(initialDomain || 'All');
  const store = useMemo(() => loadMistakes(), []);
  const list = useMemo(() => activeMistakesFor(domain, papers, store), [domain, store]);
  const counts = useMemo(() => {
    const out = {};
    SECTIONS.forEach((s) => { out[s.name] = activeMistakesFor(s.name, papers, store).length; });
    return out;
  }, [store]);
  const cleared = Object.values(store).filter((r) => r.wrong > 0 && (r.rightStreak || 0) >= 2).length;

  return (
    <div className="mock-shell">
      <section className="mock-card topic-results">
        <div className="mock-head">
          <Search size={28} />
          <div>
            <h1>My mistakes</h1>
            <p>Questions you got wrong (topic tests, decode drill, mock exams, papers), worst first. One leaves the list after you answer it right twice in a row; until then it comes first in topic tests and drills.</p>
          </div>
        </div>
        <div className="topic-setup">
          <label className="plan-date">Section
            <select value={domain} onChange={(e) => setDomain(e.target.value)}>
              <option value="All">All sections ({Object.values(counts).reduce((a, b) => a + b, 0)})</option>
              {SECTIONS.map((s) => <option key={s.name} value={s.name}>{s.name} ({counts[s.name]})</option>)}
            </select>
          </label>
          <div className="mock-paper-note mistakes-summary">{list.length} open mistakes here &middot; {cleared} cleared so far</div>
        </div>
        <div className="mock-actions">
          <button className="nav-button" onClick={onPlan}><ArrowLeft size={18} /> Back to plan</button>
          {domain !== 'All' && (
            <button className="submit-button" onClick={() => onAction({ type: 'topic', domain, size: Math.min(15, Math.max(5, list.length)) })}>
              <ClipboardCheck size={16} /> Retest these now (topic test, mistakes first)
            </button>
          )}
        </div>
        {list.length ? (
          <ReviewList questions={list} answers={null} showAnswerLabel={false} mistakes={store} />
        ) : (
          <p className="plan-note">No open mistakes{domain !== 'All' ? ` in ${domain}` : ''} yet. Take a topic test or the decode drill; anything you get wrong appears here.</p>
        )}
      </section>
    </div>
  );
}

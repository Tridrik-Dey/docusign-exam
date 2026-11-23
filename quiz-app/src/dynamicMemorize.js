// Dynamic "Memorize today": the concepts behind the questions you keep getting wrong (or flagged as unsure),
// today's sections first and repeat mistakes at the top. When there are few, it is topped up with the section's
// cheat-sheet must-know facts, rotating by day so each day shows different ones.
import papers from './papers.json';
import questions from './questions.json';
import facts from './facts.json';
import { SECTIONS } from './studyPlan.js';
import { isActiveMistake, loadMistakes } from './review.jsx';

const byId = new Map([...questions, ...papers].map((q) => [String(q.id), q]));
const MAX = 8;
const MIN = 5;

function conceptOf(q) {
  if (q.concept?.line) return q.concept.line;
  const first = String(q.explanation || '').split(/(?<=\.)\s/)[0];
  return first || q.answerText;
}

export function dynamicMemorize(day, dayIndex) {
  const focus = day.domains?.length ? day.domains : SECTIONS.map((s) => s.name);
  const store = loadMistakes();
  const seen = new Set();
  const mistakes = Object.entries(store)
    .filter(([, r]) => isActiveMistake(r))
    .map(([id, r]) => ({ q: byId.get(String(id)), r }))
    .filter(({ q }) => q)
    .sort((a, b) =>
      Number(focus.includes(b.q.domain)) - Number(focus.includes(a.q.domain)) ||
      (b.r.wrong || 0) - (a.r.wrong || 0) ||
      String(b.r.lastWrongAt || '').localeCompare(String(a.r.lastWrongAt || '')))
    .map(({ q, r }) => ({ kind: 'mistake', section: q.domain, text: conceptOf(q), wrong: r.wrong || 0, unsure: !r.wrong && r.unsure > 0, id: q.id }))
    .filter((m) => (seen.has(m.text) ? false : seen.add(m.text)))
    .slice(0, MAX);

  const out = [...mistakes];
  if (out.length < MIN) {
    const pool = focus.flatMap((s) => (facts[s] || []).map((t) => ({ kind: 'fact', section: s, text: t })));
    for (let i = 0; out.length < MIN && i < pool.length; i += 1) {
      const f = pool[(dayIndex * 3 + i) % pool.length];
      if (!seen.has(f.text)) {
        seen.add(f.text);
        out.push(f);
      }
    }
  }
  return { items: out, mistakeCount: mistakes.length };
}

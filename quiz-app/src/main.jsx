import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle2,
  CircleHelp,
  ListChecks,
  RotateCcw,
  Search,
  Shuffle,
  Timer,
  CalendarDays,
  XCircle,
} from 'lucide-react';
import questions from './questions.json';
import MockExam from './MockExam.jsx';
import StudyPlan from './StudyPlan.jsx';
import DecodeDrill from './DecodeDrill.jsx';
import TopicTest from './TopicTest.jsx';
import MistakesPage from './MistakesPage.jsx';
import EmbedLab from './EmbedLab.jsx';
import { ImportanceTag } from './importance.jsx';
import './styles.css';

// v4: fresh start for the 16-22 Nov 2026 study plan (older progress is ignored)
const STORAGE_KEY = 'docusign-iam-quiz-state-v4';
const MODE_KEY = 'docusign-iam-mode-v2';

function loadState() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    return {
      currentIndex: Number.isInteger(saved.currentIndex) ? saved.currentIndex : 0,
      answers: saved.answers || {},
      submitted: saved.submitted || {},
      showIncorrectOnly: Boolean(saved.showIncorrectOnly),
      domain: saved.domain || 'All',
      query: saved.query || '',
      importance: saved.importance || 'All',
    };
  } catch {
    return { currentIndex: 0, answers: {}, submitted: {}, showIncorrectOnly: false, domain: 'All', query: '', importance: 'All' };
  }
}


function saveState(state) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function classNames(...parts) {
  return parts.filter(Boolean).join(' ');
}

function getCorrectIds(question) {
  if (!question) return [];
  if (Array.isArray(question.correctAnswers)) return question.correctAnswers;
  return [question.correct];
}

function getSelectedIds(answer) {
  if (!answer) return [];
  return Array.isArray(answer) ? answer : [answer];
}

function answersEqual(answer, question) {
  const selectedIds = getSelectedIds(answer).slice().sort();
  const correctIds = getCorrectIds(question).slice().sort();
  return selectedIds.length === correctIds.length && selectedIds.every((id, index) => id === correctIds[index]);
}

function answerLabel(question) {
  const correctIds = getCorrectIds(question);
  return `${correctIds.join(', ')}. ${question.answerText}`;
}

function Root() {
  const [mode, setMode] = useState(() => {
    try {
      return localStorage.getItem(MODE_KEY) || 'plan';
    } catch {
      return 'plan';
    }
  });
  function switchMode(next) {
    setMode(next);
    try {
      localStorage.setItem(MODE_KEY, next);
    } catch {
      /* ignore */
    }
  }
  function handlePlanAction(action) {
    if (action.type === 'mock') {
      switchMode('mock');
      return;
    }
    if (action.type === 'embed') {
      switchMode('embed');
      return;
    }
    if (action.type === 'mistakes') {
      try {
        localStorage.setItem('docusign-iam-mistakes-domain', action.domain || 'All');
      } catch {
        /* ignore */
      }
      switchMode('mistakes');
      return;
    }
    if (action.type === 'topic') {
      try {
        localStorage.setItem('docusign-iam-topic-pick', JSON.stringify({ domain: action.domain || 'All', size: action.size || 15 }));
      } catch {
        /* ignore */
      }
      switchMode('topic');
      return;
    }
    if (action.type === 'drill') {
      try {
        localStorage.setItem('docusign-iam-drill-domain', action.domain || 'All');
      } catch {
        /* ignore */
      }
      switchMode('drill');
      return;
    }
    // practice / review: preset the practice filters, then open practice mode
    const state = loadState();
    try {
      saveState({
        ...state,
        domain: action.domain || 'All',
        query: '',
        currentIndex: 0,
        importance: action.importance || 'All',
        showIncorrectOnly: action.type === 'review',
      });
    } catch {
      /* ignore */
    }
    switchMode('practice');
  }
  if (mode === 'mock') return <MockExam onExit={() => switchMode('plan')} />;
  if (mode === 'embed') return <EmbedLab onPlan={() => switchMode('plan')} />;
  if (mode === 'mistakes') {
    let d = 'All';
    try {
      d = localStorage.getItem('docusign-iam-mistakes-domain') || 'All';
    } catch {
      /* ignore */
    }
    return <MistakesPage initialDomain={d} onPlan={() => switchMode('plan')} onAction={handlePlanAction} />;
  }
  if (mode === 'topic') {
    let pick = {};
    try {
      pick = JSON.parse(localStorage.getItem('docusign-iam-topic-pick') || '{}');
    } catch {
      /* ignore */
    }
    return <TopicTest initialDomain={pick.domain} initialSize={pick.size} onPlan={() => switchMode('plan')} />;
  }
  if (mode === 'drill') {
    let d = 'All';
    try {
      d = localStorage.getItem('docusign-iam-drill-domain') || 'All';
    } catch {
      /* ignore */
    }
    return <DecodeDrill initialDomain={d} onPlan={() => switchMode('plan')} />;
  }
  if (mode === 'practice') return <App onMockExam={() => switchMode('mock')} onPlan={() => switchMode('plan')} />;
  return <StudyPlan practiceState={loadState()} onAction={handlePlanAction} />;
}

function App({ onMockExam, onPlan }) {
  const initial = useMemo(loadState, []);
  const [answers, setAnswers] = useState(initial.answers);
  const [submitted, setSubmitted] = useState(initial.submitted);
  const [currentIndex, setCurrentIndex] = useState(Math.min(initial.currentIndex, questions.length - 1));
  const [domain, setDomain] = useState(initial.domain);
  const [query, setQuery] = useState(initial.query);
  const [showIncorrectOnly, setShowIncorrectOnly] = useState(initial.showIncorrectOnly);
  const [importance, setImportance] = useState(initial.importance);

  const domains = useMemo(() => ['All', ...Array.from(new Set(questions.map((q) => q.domain)))], []);

  const filteredQuestions = useMemo(() => {
    const q = query.trim().toLowerCase();
    return questions.filter((question) => {
      const matchesDomain = domain === 'All' || question.domain === domain;
      const matchesQuery =
        !q ||
        question.stem.toLowerCase().includes(q) ||
        question.topic.toLowerCase().includes(q) ||
        question.domain.toLowerCase().includes(q);
      const isIncorrect = submitted[question.id] && !answersEqual(answers[question.id], question);
      const matchesIncorrect = !showIncorrectOnly || isIncorrect;
      const matchesImportance = importance === 'All' || question.importance === importance;
      return matchesDomain && matchesQuery && matchesIncorrect && matchesImportance;
    });
  }, [answers, domain, query, showIncorrectOnly, submitted, importance]);

  const currentQuestion = filteredQuestions[Math.min(currentIndex, Math.max(filteredQuestions.length - 1, 0))];
  const selected = currentQuestion ? answers[currentQuestion.id] : null;
  const selectedIds = getSelectedIds(selected);
  const correctIds = getCorrectIds(currentQuestion);
  const isMultiAnswer = correctIds.length > 1;
  const hasSelection = currentQuestion ? (isMultiAnswer ? selectedIds.length === correctIds.length : selectedIds.length > 0) : false;
  const isSubmitted = currentQuestion ? submitted[currentQuestion.id] : false;
  const isCorrect = currentQuestion ? answersEqual(answers[currentQuestion.id], currentQuestion) : false;

  const stats = useMemo(() => {
    const answered = Object.keys(submitted).length;
    const correct = questions.filter((q) => submitted[q.id] && answersEqual(answers[q.id], q)).length;
    const incorrect = answered - correct;
    return {
      answered,
      correct,
      incorrect,
      percent: answered ? Math.round((correct / answered) * 100) : 0,
      progress: Math.round((answered / questions.length) * 100),
    };
  }, [answers, submitted]);

  function commit(next) {
    const state = {
      currentIndex,
      answers,
      submitted,
      showIncorrectOnly,
      domain,
      query,
      importance,
      ...next,
    };
    if (next.currentIndex === undefined) state.currentIndex = currentIndex;
    if (next.answers === undefined) state.answers = answers;
    if (next.submitted === undefined) state.submitted = submitted;
    if (next.showIncorrectOnly === undefined) state.showIncorrectOnly = showIncorrectOnly;
    if (next.domain === undefined) state.domain = domain;
    if (next.query === undefined) state.query = query;
    if (next.importance === undefined) state.importance = importance;
    saveState(state);
  }

  function selectAnswer(optionId) {
    if (!currentQuestion || isSubmitted) return;
    let nextAnswer = optionId;
    if (isMultiAnswer) {
      const existing = new Set(selectedIds);
      if (existing.has(optionId)) {
        existing.delete(optionId);
      } else if (existing.size < correctIds.length) {
        existing.add(optionId);
      }
      nextAnswer = Array.from(existing).sort();
    }
    const nextAnswers = { ...answers, [currentQuestion.id]: nextAnswer };
    setAnswers(nextAnswers);
    commit({ answers: nextAnswers });
  }

  function submitAnswer() {
    if (!currentQuestion || !hasSelection) return;
    const nextSubmitted = { ...submitted, [currentQuestion.id]: true };
    setSubmitted(nextSubmitted);
    commit({ submitted: nextSubmitted });
  }

  function goToIndex(nextIndex) {
    const bounded = Math.max(0, Math.min(nextIndex, filteredQuestions.length - 1));
    setCurrentIndex(bounded);
    commit({ currentIndex: bounded });
  }

  function updateDomain(value) {
    setDomain(value);
    setCurrentIndex(0);
    commit({ domain: value, currentIndex: 0 });
  }

  function updateImportance(value) {
    setImportance(value);
    setCurrentIndex(0);
    commit({ importance: value, currentIndex: 0 });
  }

  function updateQuery(value) {
    setQuery(value);
    setCurrentIndex(0);
    commit({ query: value, currentIndex: 0 });
  }

  function toggleIncorrect() {
    const next = !showIncorrectOnly;
    setShowIncorrectOnly(next);
    setCurrentIndex(0);
    commit({ showIncorrectOnly: next, currentIndex: 0 });
  }

  function resetAll() {
    setAnswers({});
    setSubmitted({});
    setCurrentIndex(0);
    setShowIncorrectOnly(false);
    setDomain('All');
    setQuery('');
    setImportance('All');
    saveState({ currentIndex: 0, answers: {}, submitted: {}, showIncorrectOnly: false, domain: 'All', query: '', importance: 'All' });
  }

  function jumpToRandom() {
    if (!filteredQuestions.length) return;
    goToIndex(Math.floor(Math.random() * filteredQuestions.length));
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="mark">DS</div>
          <div>
            <h1>Docusign IAM Quiz</h1>
            <p>{questions.length} practice questions</p>
          </div>
        </div>

        <div className="score-card">
          <div className="score-main">{stats.percent}%</div>
          <div className="score-label">current score</div>
          <div className="progress-track">
            <div style={{ width: `${stats.progress}%` }} />
          </div>
          <div className="score-grid">
            <span><strong>{stats.answered}</strong> answered</span>
            <span><strong>{stats.correct}</strong> correct</span>
            <span><strong>{stats.incorrect}</strong> missed</span>
            <span><strong>{questions.length - stats.answered}</strong> left</span>
          </div>
        </div>

        <label className="field-label" htmlFor="domain">Section</label>
        <select id="domain" className="select" value={domain} onChange={(event) => updateDomain(event.target.value)}>
          {domains.map((item) => (
            <option key={item} value={item}>{item}</option>
          ))}
        </select>

        <label className="field-label" htmlFor="importance">Importance</label>
        <select id="importance" className="select" value={importance} onChange={(event) => updateImportance(event.target.value)}>
          <option value="All">All</option>
          <option value="HIGH">Must know only</option>
          <option value="MEDIUM">Important only</option>
          <option value="LOW">Background only</option>
        </select>

        <label className="field-label" htmlFor="search">Search</label>
        <div className="search-box">
          <Search size={16} />
          <input id="search" value={query} onChange={(event) => updateQuery(event.target.value)} placeholder="topic, section, keyword" />
        </div>

        <button className="side-action plan-entry" onClick={onPlan}>
          <CalendarDays size={17} />
          Exam plan
        </button>
        <button className="side-action mock-entry" onClick={onMockExam}>
          <Timer size={17} />
          Mock exam (60 Q, 150 min)
        </button>
        <button className={classNames('side-action', showIncorrectOnly && 'active')} onClick={toggleIncorrect}>
          <ListChecks size={17} />
          Review incorrect
        </button>
        <button className="side-action" onClick={jumpToRandom}>
          <Shuffle size={17} />
          Random question
        </button>
        <button className="side-action danger" onClick={resetAll}>
          <RotateCcw size={17} />
          Reset session
        </button>
      </aside>

      <main className="question-area">
        {!currentQuestion ? (
          <section className="empty-state">
            <CircleHelp size={42} />
            <h2>No questions match this view</h2>
            <p>Clear the search or switch off incorrect-only review.</p>
          </section>
        ) : (
          <>
            <div className="topbar">
              <div>
                <span className="section-label">{currentQuestion.domain}</span>
                <h2>Question {currentQuestion.id}</h2>
              </div>
              <div className="question-counter">
                {Math.min(currentIndex + 1, filteredQuestions.length)} / {filteredQuestions.length}
              </div>
            </div>

            <section className="question-card">
              <div className="topic-row">
                <ImportanceTag level={currentQuestion.importance} />
                <div className="topic">{currentQuestion.topic}</div>
              </div>
              <p className="stem">{currentQuestion.stem}</p>
              {isMultiAnswer && (
                <div className="multi-note">
                  Select {correctIds.length} answers. Selected {selectedIds.length} / {correctIds.length}.
                </div>
              )}

              <div className="options">
                {currentQuestion.options.map((option) => {
                  const optionCorrect = correctIds.includes(option.id);
                  const optionSelected = selectedIds.includes(option.id);
                  return (
                    <button
                      key={option.id}
                      className={classNames(
                        'option',
                        optionSelected && 'selected',
                        isSubmitted && optionCorrect && 'correct',
                        isSubmitted && optionSelected && !optionCorrect && 'wrong'
                      )}
                      onClick={() => selectAnswer(option.id)}
                      aria-pressed={optionSelected}
                    >
                      <span className="option-letter">{option.id}</span>
                      <span>{option.text}</span>
                    </button>
                  );
                })}
              </div>

              <div className="question-actions">
                <button className="nav-button" onClick={() => goToIndex(currentIndex - 1)} disabled={currentIndex === 0}>
                  <ArrowLeft size={18} />
                  Previous
                </button>
                <button className="submit-button" onClick={submitAnswer} disabled={!hasSelection || isSubmitted}>
                  Check answer
                </button>
                <button className="nav-button" onClick={() => goToIndex(currentIndex + 1)} disabled={currentIndex >= filteredQuestions.length - 1}>
                  Next
                  <ArrowRight size={18} />
                </button>
              </div>
            </section>
          </>
        )}
      </main>

      <aside className="analysis-panel">
        <div className="analysis-header">
          <h2>Answer Review</h2>
          <p>Submit your answer to see the result and explanations.</p>
        </div>

        {currentQuestion && isSubmitted ? (
          <div className="result-stack">
            <div className={classNames('result-banner', isCorrect ? 'pass' : 'fail')}>
              {isCorrect ? <CheckCircle2 size={22} /> : <XCircle size={22} />}
              <div>
                <strong>{isCorrect ? 'Correct' : 'Incorrect'}</strong>
                <span>
                  Correct answer: {answerLabel(currentQuestion)}
                </span>
              </div>
            </div>

            <div className="explanation-block">
              <h3>Why the correct answer is right</h3>
              <p>{currentQuestion.explanation}</p>
            </div>

            {currentQuestion.whyNotOthers && (
              <div className="explanation-block why-not">
                <h3>Why this answer and not the others</h3>
                <p>{currentQuestion.whyNotOthers}</p>
              </div>
            )}

            <div className="explanation-block">
              <h3>Why each option fits or does not fit</h3>
              {currentQuestion.options.map((option) => (
                <div key={option.id} className={classNames('option-analysis', correctIds.includes(option.id) && 'right')}>
                  <div className="analysis-option-title">
                    <span>{option.id}</span>
                    <strong>{option.text}</strong>
                    {currentQuestion.trapOption === option.id && <em className="trap-badge">TRAP</em>}
                  </div>
                  <p>{currentQuestion.optionExplanations[option.id]}</p>
                </div>
              ))}
            </div>
          </div>
        ) : (
          <div className="pending-panel">
            <CircleHelp size={36} />
            <p>Select an option, then check your answer. The right panel will explain why the correct choice wins and why the other choices do not.</p>
          </div>
        )}
      </aside>
    </div>
  );
}

createRoot(document.getElementById('root')).render(<Root />);

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
  XCircle,
} from 'lucide-react';
import questions from './questions.json';
import './styles.css';

const STORAGE_KEY = 'docusign-iam-quiz-state-v3';

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
    };
  } catch {
    return { currentIndex: 0, answers: {}, submitted: {}, showIncorrectOnly: false, domain: 'All', query: '' };
  }
}

function saveState(state) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function classNames(...parts) {
  return parts.filter(Boolean).join(' ');
}

function App() {
  const initial = useMemo(loadState, []);
  const [answers, setAnswers] = useState(initial.answers);
  const [submitted, setSubmitted] = useState(initial.submitted);
  const [currentIndex, setCurrentIndex] = useState(Math.min(initial.currentIndex, questions.length - 1));
  const [domain, setDomain] = useState(initial.domain);
  const [query, setQuery] = useState(initial.query);
  const [showIncorrectOnly, setShowIncorrectOnly] = useState(initial.showIncorrectOnly);

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
      const isIncorrect = submitted[question.id] && answers[question.id] !== question.correct;
      const matchesIncorrect = !showIncorrectOnly || isIncorrect;
      return matchesDomain && matchesQuery && matchesIncorrect;
    });
  }, [answers, domain, query, showIncorrectOnly, submitted]);

  const currentQuestion = filteredQuestions[Math.min(currentIndex, Math.max(filteredQuestions.length - 1, 0))];
  const selected = currentQuestion ? answers[currentQuestion.id] : null;
  const isSubmitted = currentQuestion ? submitted[currentQuestion.id] : false;
  const isCorrect = currentQuestion ? answers[currentQuestion.id] === currentQuestion.correct : false;

  const stats = useMemo(() => {
    const answered = Object.keys(submitted).length;
    const correct = questions.filter((q) => submitted[q.id] && answers[q.id] === q.correct).length;
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
      ...next,
    };
    if (next.currentIndex === undefined) state.currentIndex = currentIndex;
    if (next.answers === undefined) state.answers = answers;
    if (next.submitted === undefined) state.submitted = submitted;
    if (next.showIncorrectOnly === undefined) state.showIncorrectOnly = showIncorrectOnly;
    if (next.domain === undefined) state.domain = domain;
    if (next.query === undefined) state.query = query;
    saveState(state);
  }

  function selectAnswer(optionId) {
    if (!currentQuestion || isSubmitted) return;
    const nextAnswers = { ...answers, [currentQuestion.id]: optionId };
    setAnswers(nextAnswers);
    commit({ answers: nextAnswers });
  }

  function submitAnswer() {
    if (!currentQuestion || !selected) return;
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
    saveState({ currentIndex: 0, answers: {}, submitted: {}, showIncorrectOnly: false, domain: 'All', query: '' });
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

        <label className="field-label" htmlFor="search">Search</label>
        <div className="search-box">
          <Search size={16} />
          <input id="search" value={query} onChange={(event) => updateQuery(event.target.value)} placeholder="topic, section, keyword" />
        </div>

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
              <div className="topic">{currentQuestion.topic}</div>
              <p className="stem">{currentQuestion.stem}</p>

              <div className="options">
                {currentQuestion.options.map((option) => {
                  const optionCorrect = option.id === currentQuestion.correct;
                  const optionSelected = selected === option.id;
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
                <button className="submit-button" onClick={submitAnswer} disabled={!selected || isSubmitted}>
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
                  Correct answer: {currentQuestion.correct}. {currentQuestion.answerText}
                </span>
              </div>
            </div>

            <div className="explanation-block">
              <h3>Why the correct answer is right</h3>
              <p>{currentQuestion.explanation}</p>
            </div>

            <div className="explanation-block">
              <h3>Why each option fits or does not fit</h3>
              {currentQuestion.options.map((option) => (
                <div key={option.id} className={classNames('option-analysis', option.id === currentQuestion.correct && 'right')}>
                  <div className="analysis-option-title">
                    <span>{option.id}</span>
                    <strong>{option.text}</strong>
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

createRoot(document.getElementById('root')).render(<App />);

import React, { useRef, useState } from 'react';
import { ArrowLeft, ExternalLink, FileText, Frame, Play } from 'lucide-react';

// Embedding tool (opened from the Try it step of Lab 1 ex 5-7, Lab 3 ex 7, Lab 5 ex 5): paste a URL you got from an API call and see it as a redirect, in a plain iframe, or through
// Docusign JS (focused view signing / embedded web form). Use a developer (demo) account only.
const ORIGIN = typeof window !== 'undefined' ? window.location.origin : 'http://127.0.0.1:5173';
const BUNDLE = { demo: 'https://js-d.docusign.com/bundle.js', prod: 'https://js.docusign.com/bundle.js' };
const APPS = { demo: 'https://apps-d.docusign.com', prod: 'https://apps.docusign.com' };
const KINDS = {
  signing: 'Signing (createRecipient)',
  sending: 'Sending (createSender)',
  webform: 'Web form (formUrl + token)',
  workflow: 'Workflow instance URL',
};
const EVENTS = ['ready', 'sessionEnd', 'submitted', 'signingReady', 'sessionTimeout', 'error'];

function loadBundle(env) {
  return new Promise((resolve, reject) => {
    if (window.DocuSign?.loadDocuSign && window.__dsBundle === env) return resolve(window.DocuSign);
    const s = document.createElement('script');
    s.src = BUNDLE[env];
    s.onload = () => { window.__dsBundle = env; resolve(window.DocuSign); };
    s.onerror = () => reject(new Error(`Could not load ${BUNDLE[env]}`));
    document.head.appendChild(s);
  });
}

export default function EmbedLab({ from = {}, onPlan }) {
  const [kind, setKind] = useState('signing');
  const [env, setEnv] = useState('demo');
  const [url, setUrl] = useState('');
  const [ik, setIk] = useState('');
  const [token, setToken] = useState('');
  const [mode, setMode] = useState(null);
  const [log, setLog] = useState([]);
  const mountRef = useRef(null);

  const add = (line) => setLog((l) => [`${new Date().toLocaleTimeString()}  ${line}`, ...l].slice(0, 40));

  function redirect() {
    if (!url) return;
    window.open(url, '_blank', 'noopener');
    add('Opened as a full-page redirect in a new tab (the classic, always-allowed pattern).');
    setMode('redirect');
  }

  function iframe() {
    if (!url) return;
    setMode('iframe');
    add('Loaded in a plain <iframe>. Observe: does it render, or does the browser refuse to frame it? Check the console.');
  }

  async function docusignJs() {
    if (!url || !ik) {
      add('Docusign JS needs the URL and your integration key.');
      return;
    }
    setMode('js');
    try {
      const DS = await loadBundle(env);
      const docusign = await DS.loadDocuSign(ik);
      if (mountRef.current) mountRef.current.innerHTML = '';
      const widget = kind === 'webform'
        ? docusign.webforms({ url, options: { instanceToken: token } })
        : docusign.signing({ url, displayFormat: 'focused', style: { branding: { primaryButton: { backgroundColor: '#155eef', color: '#fff' } } } });
      EVENTS.forEach((ev) => {
        try {
          widget.on(ev, (e) => add(`event "${ev}" ${e ? JSON.stringify(e).slice(0, 200) : ''}`));
        } catch {
          /* event not supported by this widget */
        }
      });
      widget.mount('#ds-embed-target');
      add(`Docusign JS mounted (${kind === 'webform' ? 'webforms' : 'signing, focused view'}) from ${BUNDLE[env]}.`);
    } catch (e) {
      add(`Docusign JS error: ${e.message || e}`);
    }
  }

  return (
    <div className="app-shell embed-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="mark"><Frame size={18} /></div>
          <div>
            <h1>Try it: embedding</h1>
            <p>{from.exercise ? `For: ${from.exercise}` : 'Redirect vs iframe vs Docusign JS'}</p>
          </div>
        </div>
        <label className="plan-date">What is the URL?
          <select value={kind} onChange={(e) => setKind(e.target.value)}>
            {Object.entries(KINDS).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
          </select>
        </label>
        <label className="plan-date">Environment
          <select value={env} onChange={(e) => setEnv(e.target.value)}>
            <option value="demo">Developer (demo)</option>
            <option value="prod">Production</option>
          </select>
        </label>
        <label className="plan-date">URL from the API response
          <textarea rows={3} value={url} onChange={(e) => setUrl(e.target.value.trim())} placeholder="https://demo.docusign.net/Signing/..." />
        </label>
        <label className="plan-date">Integration key (Docusign JS only)
          <input value={ik} onChange={(e) => setIk(e.target.value.trim())} placeholder="your demo integration key" />
        </label>
        {kind === 'webform' && (
          <label className="plan-date">instanceToken (web forms)
            <input value={token} onChange={(e) => setToken(e.target.value.trim())} />
          </label>
        )}
        <div className="embed-buttons">
          <button className="nav-button" onClick={redirect} disabled={!url}><ExternalLink size={16} /> 1. Redirect</button>
          <button className="nav-button" onClick={iframe} disabled={!url}><Frame size={16} /> 2. Plain iframe</button>
          <button className="submit-button" onClick={docusignJs} disabled={!url || kind === 'sending' || kind === 'workflow'}><Play size={16} /> 3. Docusign JS</button>
        </div>
        <p className="plan-note">URLs from createRecipient / createSender expire after 5 minutes and work once: create a fresh one for each try. Nothing you paste here is stored.</p>
        <button className="side-action" onClick={() => window.open(`/pdf/${from.lab || 'labs/lab_1_esignature_api.pdf'}`, '_blank', 'noopener')}><FileText size={17} /> Back to the lab guide (PDF)</button>
        <button className="side-action" onClick={onPlan}><ArrowLeft size={17} /> Back to plan</button>
      </aside>

      <main className="question-area">
        <div className="topbar">
          <div>
            <span className="section-label">{KINDS[kind]}</span>
            <h2>{mode === 'iframe' ? 'Plain iframe' : mode === 'js' ? 'Docusign JS' : mode === 'redirect' ? 'Opened as a redirect (new tab)' : 'Paste a URL and choose a method'}</h2>
          </div>
          <div className="embed-top-actions">
            <button className="nav-button" onClick={onPlan}><ArrowLeft size={18} /> Back to plan</button>
            <button className="nav-button" onClick={() => window.open(`/pdf/${from.lab || 'labs/lab_1_esignature_api.pdf'}`, '_blank', 'noopener')}><FileText size={16} /> Lab guide (PDF)</button>
          </div>
        </div>
        <section className="question-card embed-stage">
          {mode === 'iframe' && <iframe title="embedded" src={url} className="embed-frame" />}
          <div id="ds-embed-target" ref={mountRef} className={`embed-frame ${mode === 'js' ? '' : 'hidden'}`} />
          {!mode && <p className="plan-note">Use a developer account. Create the URL with your own API call (see the Try it step in your lab guide), paste it on the left, then try the three methods one after another with fresh URLs.</p>}
          {mode === 'redirect' && <p className="plan-note">The signing session opened in a new tab. After signing, Docusign redirects to your returnUrl with ?event=... (for example signing_complete, cancel, decline, ttl_expired). Treat it as a hint and confirm the status with Connect or a GET.</p>}
        </section>
      </main>

      <aside className="analysis-panel">
        <div className="analysis-header">
          <h2>Setup and what to observe</h2>
          <p>Add these to createRecipient for focused view:</p>
        </div>
        {ORIGIN.includes('127.0.0.1') && (
          <p className="embed-warn">Docusign accepts plain-http origins only for localhost. For focused view, open this app at <a href={ORIGIN.replace('127.0.0.1', 'localhost') + '/'}>{ORIGIN.replace('127.0.0.1', 'localhost')}</a> and use that origin below.</p>
        )}
        <pre className="embed-code">{`"frameAncestors": ["${ORIGIN.replace('127.0.0.1', 'localhost')}", "${APPS[env]}"],
"messageOrigins": ["${APPS[env]}"]`}</pre>
        <ul className="plan-rules">
          <li>Focused view needs frameAncestors + messageOrigins and Docusign JS; try it once without them and note what happens.</li>
          <li>Signer needs clientUserId (embedded, no email); the createRecipient values must match the recipient exactly.</li>
          <li>Classic view is required for payments, ID verification, some SBS providers and 21 CFR Part 11.</li>
          <li>Embedded sending = createSender on a draft (status created); it is shown by redirect or iframe, not Docusign JS signing.</li>
          <li>Web form: embedded instance needs clientUserId; render formUrl + instanceToken with Docusign JS webforms.</li>
          <li>Compare the returnUrl event (redirect) with the Docusign JS sessionEnd event; neither replaces Connect.</li>
        </ul>
        <h3 className="plan-h3">Event log</h3>
        <div className="embed-log">{log.length ? log.map((l) => <div key={l}>{l}</div>) : <span className="plan-note">Events appear here.</span>}</div>
      </aside>
    </div>
  );
}

import 'dotenv/config'
import express from 'express'

const {
  DS_CLIENT_ID,
  DS_CLIENT_SECRET,
  DS_REDIRECT_URI,
  DS_AUTH_BASE,
  DS_AGREEMENT_MANAGER_BASE,
  DS_SCOPES,
  PORT = 5173,
} = process.env

for (const [name, value] of Object.entries({ DS_CLIENT_ID, DS_CLIENT_SECRET, DS_REDIRECT_URI })) {
  if (!value) {
    console.error(`Missing ${name} - copy .env.example to .env and fill it in.`)
    process.exit(1)
  }
}

// Single-user local dev tool - no need for a real session store.
const session = { accessToken: null, refreshToken: null, accountId: null }

const app = express()

app.get('/', (_req, res) => {
  res.send('<a href="/auth">Connect to DocuSign</a>')
})

app.get('/auth', (_req, res) => {
  const url = new URL('/oauth/auth', DS_AUTH_BASE)
  url.searchParams.set('response_type', 'code')
  url.searchParams.set('scope', DS_SCOPES)
  url.searchParams.set('client_id', DS_CLIENT_ID)
  url.searchParams.set('redirect_uri', DS_REDIRECT_URI)
  res.redirect(url.toString())
})

app.get('/callback', async (req, res) => {
  const { code, error, error_description: errorDescription } = req.query
  if (error) {
    res.status(400).send(`DocuSign returned an error: ${error} - ${errorDescription ?? ''}`)
    return
  }

  const basicAuth = Buffer.from(`${DS_CLIENT_ID}:${DS_CLIENT_SECRET}`).toString('base64')
  const tokenResponse = await fetch(new URL('/oauth/token', DS_AUTH_BASE), {
    method: 'POST',
    headers: {
      Authorization: `Basic ${basicAuth}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({ grant_type: 'authorization_code', code }),
  })
  if (!tokenResponse.ok) {
    res.status(502).send(`Token exchange failed: ${tokenResponse.status} ${await tokenResponse.text()}`)
    return
  }
  const tokens = await tokenResponse.json()

  const userInfoResponse = await fetch(new URL('/oauth/userinfo', DS_AUTH_BASE), {
    headers: { Authorization: `Bearer ${tokens.access_token}` },
  })
  const userInfo = await userInfoResponse.json()
  const account = userInfo.accounts.find((a) => a.is_default) ?? userInfo.accounts[0]

  session.accessToken = tokens.access_token
  session.refreshToken = tokens.refresh_token
  session.accountId = account.account_id

  res.redirect('/agreements')
})

app.get('/agreements', async (_req, res) => {
  if (!session.accessToken) {
    res.redirect('/auth')
    return
  }

  const url = new URL(`/v1/accounts/${session.accountId}/agreements`, DS_AGREEMENT_MANAGER_BASE)
  const response = await fetch(url, {
    headers: { Authorization: `Bearer ${session.accessToken}` },
  })
  const body = await response.text()
  res.status(response.status).type('application/json').send(body)
})

app.listen(PORT, () => {
  console.log(`Listening on http://localhost:${PORT} - open it and click "Connect to DocuSign"`)
})

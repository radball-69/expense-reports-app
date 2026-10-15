# Slack Test Workspace Setup

Follow these steps to set up a dedicated Slack app/workspace for local testing.

## 1) Create the Slack app (in your new workspace)

1. Go to https://api.slack.com/apps
2. Click **Create New App** → **From scratch**
3. Name it (for example: `expense-reports-test-bot`)
4. Select your new test workspace

## 2) Configure bot permissions (OAuth scopes)

1. Open **OAuth & Permissions**
2. Under **Bot Token Scopes**, add:
   - `chat:write`
   - `files:read`
   - `commands`
   - `im:history`
   - `im:read`

## 3) Enable Socket Mode (for local dev)

1. Open **Socket Mode**
2. Turn it **On**
3. Create an **App-Level Token** with scope:
   - `connections:write`
4. Save this token (`xapp-...`) as `SLACK_TEST_APP_TOKEN`

## 4) Enable events so the bot can receive messages

1. Open **Event Subscriptions**
2. Enable events
3. Under **Subscribe to bot events**, add:
   - `message.im`
   - `file_shared`

## 5) Add slash command

1. Open **Slash Commands**
2. Create command: `/expense`
3. Use a placeholder request URL while in Socket Mode/local testing, for example:
   - `https://example.com/slack/commands`

## 6) Install app into workspace

1. Return to **OAuth & Permissions**
2. Click **Install to Workspace**
3. Authorize requested scopes

Collect and save:
- **Bot User OAuth Token** (`xoxb-...`)
- **Signing Secret** (from **Basic Information**)
- **App-Level Token** (`xapp-...`)

## 7) Put secrets into local env

Set these values in your local `.env`:

```bash
SLACK_TEST_BOT_TOKEN=xoxb-...
SLACK_TEST_SIGNING_SECRET=...
SLACK_TEST_APP_TOKEN=xapp-...
SLACK_ENV=local
```

`SLACK_TEST_APP_TOKEN` is the App-Level Token from **Socket Mode** in your Slack app settings.

## 8) Run a basic smoke test in Slack

1. Open a DM with your app in Slack
2. Send a simple message (e.g., `hello`)
3. Upload an image file in the DM
4. Run `/expense`

Expected result: bot receives events and can respond in the test workspace.

# expense-reports-app

Slack bot that accepts receipts and descriptions to automatically fill out expense reports in Unanet.

## Quick start

```bash
cp .env.example .env
./run.sh it
```

Scripts create `.venv` and install dependencies automatically when needed.
`./run.sh it` starts the Slack bot in Socket Mode and requires valid Slack env vars in `.env`.

## Scripts

- `./run.sh install-deps` — create/update local Python environment
- `./run.sh it` — start app
- `./run.sh tests` — run tests
- `./run.sh format-check` — run lint/format checks
- `./run.sh format` — auto-fix lint/format issues

Each command maps to `scripts/<name>.sh`.

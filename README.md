# expense-reports-app

Slack bot that accepts receipts and descriptions to automatically fill out expense reports in Unanet.

## Quick start

```bash
cp .env.example .env
./run.sh
```

Scripts create `.venv` and install dependencies automatically when needed.
`run.sh` starts the Slack bot in Socket Mode and requires valid Slack env vars in `.env`.

## Scripts

- `./install-deps.sh` — create/update local Python environment
- `./run.sh` — start app
- `./run-tests.sh` — run tests
- `./run-format-check.sh` — run lint/format checks

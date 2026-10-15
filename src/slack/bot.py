"""Slack bot entrypoint and handlers."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


@dataclass(frozen=True)
class SlackSettings:
    bot_token: str
    signing_secret: str
    app_token: str


def load_slack_settings() -> SlackSettings:
    slack_env = os.getenv("SLACK_ENV", "local").strip().lower()
    if slack_env == "local":
        prefix = "SLACK_TEST"
    elif slack_env in {"dev", "prod"}:
        prefix = "SLACK"
    else:
        raise ValueError("SLACK_ENV must be one of: local, dev, prod.")

    bot_token = os.getenv(f"{prefix}_BOT_TOKEN", "").strip()
    signing_secret = os.getenv(f"{prefix}_SIGNING_SECRET", "").strip()
    app_token = os.getenv(f"{prefix}_APP_TOKEN", "").strip()

    missing_vars = [
        key
        for key, value in {
            f"{prefix}_BOT_TOKEN": bot_token,
            f"{prefix}_SIGNING_SECRET": signing_secret,
            f"{prefix}_APP_TOKEN": app_token,
        }.items()
        if not value
    ]

    if missing_vars:
        missing = ", ".join(missing_vars)
        raise ValueError(f"Missing required Slack environment variables: {missing}")

    return SlackSettings(
        bot_token=bot_token, signing_secret=signing_secret, app_token=app_token
    )


def build_app(settings: SlackSettings) -> App:
    app = App(token=settings.bot_token, signing_secret=settings.signing_secret)

    @app.message(re.compile(r".+"))
    def handle_message(message: dict, say) -> None:
        if message.get("bot_id"):
            return
        text = str(message.get("text", "")).strip()
        if not text:
            say("I received your message.")
            return
        say(f"You said: {text}")

    @app.command("/expense")
    def handle_expense_command(ack, respond, command: dict) -> None:
        ack()
        command_text = str(command.get("text", "")).strip()
        if command_text:
            respond(
                f'Expense command received: "{command_text}". '
            )
            return
        respond(
            "Expense command received. Stub mode is active; "
            "no submission is happening yet."
        )

    return app


def run_slack_bot() -> None:
    settings = load_slack_settings()
    app = build_app(settings)
    handler = SocketModeHandler(app, settings.app_token)
    handler.start()

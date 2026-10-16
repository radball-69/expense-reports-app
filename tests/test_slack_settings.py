import pytest

from src.slack.bot import load_slack_settings


def test_load_slack_settings_local(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SLACK_ENV", "local")
    monkeypatch.setenv("SLACK_TEST_BOT_TOKEN", "xoxb-test")
    monkeypatch.setenv("SLACK_TEST_SIGNING_SECRET", "secret")
    monkeypatch.setenv("SLACK_TEST_APP_TOKEN", "xapp-test")

    settings = load_slack_settings()

    assert settings.bot_token
    assert settings.signing_secret
    assert settings.app_token


def test_load_slack_settings_requires_tokens(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SLACK_ENV", "local")
    monkeypatch.delenv("SLACK_TEST_BOT_TOKEN", raising=False)
    monkeypatch.delenv("SLACK_TEST_SIGNING_SECRET", raising=False)
    monkeypatch.delenv("SLACK_TEST_APP_TOKEN", raising=False)

    with pytest.raises(
        ValueError, match="Missing required Slack environment variables"
    ):
        load_slack_settings()

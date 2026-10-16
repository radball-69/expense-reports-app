"""Application entry point."""

from src.slack.bot import run_slack_bot


def get_app_name() -> str:
    return "expense-reports-app"


def main() -> None:
    print(f"Starting {get_app_name()} in Slack Socket Mode...")
    run_slack_bot()


if __name__ == "__main__":
    main()

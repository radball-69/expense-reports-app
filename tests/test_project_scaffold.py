from src.main import get_app_name


def test_app_name() -> None:
    assert get_app_name() == "expense-reports-app"

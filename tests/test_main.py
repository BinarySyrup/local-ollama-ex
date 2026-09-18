from app_template.main import run


def test_run_default_name() -> None:
    assert run("World") == "Hello, World!"


def test_run_custom_name() -> None:
    assert run("Coder") == "Hello, Coder!"

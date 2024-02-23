from app.app import foo


def test_foo() -> None:
    assert foo() == "bar"

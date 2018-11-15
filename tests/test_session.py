import pytest


def test_get_apps():
    assert pytest.session.get_apps() is not None


def test_get_app():
    assert pytest.session.get_app(name=pytest.app_name) is not None

def test_get_app_no_input():
    with pytest.raises(ValueError):
        pytest.session.get_app()

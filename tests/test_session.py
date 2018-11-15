import pytest


def test_get_apps():
    assert pytest.session.get_apps() is not None


def test_get_app():
    assert pytest.session.get_app(name=pytest.app_name) is not None

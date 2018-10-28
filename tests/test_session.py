import pytest

def test_get_apps():
    assert pytest.session.get_apps() != None

def test_get_app():
    assert pytest.session.get_app(name='Listening to Music :)') != None

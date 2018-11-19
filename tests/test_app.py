import pytest


def test_upload_and_delete_image():
    app = pytest.session.get_app(name=pytest.app_name)

    image_id = app.upload_image('tests/--!cat!--.jpg')
    assert image_id is not None
    app.delete_image(image_id)


def test_is_bot():
    app = pytest.session.get_app(name='Thonky')
    assert app.is_bot is True


def test_is_bot_false():
    app = pytest.session.get_app(name=pytest.app_name)
    assert app.is_bot is False


def test_bot_token():
    app = pytest.session.get_app(name='Thonky')
    assert app.bot_token is not None


def test_change_name():
    app = pytest.session.get_app(name='TestBot')
    app.name = 'testing'
    assert app.name == 'testing'
    app.name = 'TestBot'


def test_change_name_too_long():
    app = pytest.session.get_app(name=pytest.app_name)
    with pytest.raises(ValueError):
        app.name = 'ogdog' * 50


def test_change_name_too_short():
    app = pytest.session.get_app(name=pytest.app_name)
    with pytest.raises(ValueError):
        app.name = '1'

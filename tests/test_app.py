import pytest


def test_upload_and_delete_image():
    app = pytest.session.get_app(name=pytest.app_name)

    image_id = app.upload_image('tests/--!cat!--.jpg')
    assert image_id is not None
    app.delete_image(image_id)

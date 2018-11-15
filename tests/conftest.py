import os

from dam import login


def pytest_namespace():
    email = os.environ['LOGIN_EMAIL']
    password = os.environ['LOGIN_PASSWORD']
    app_name = os.environ['APP_NAME']
    session = login(email=email, password=password)
    return {'session': session, 'app_name': app_name}

import pytest
import os

from dam import login

def pytest_namespace():
    email = os.environ['LOGIN_EMAIL']
    password = os.environ['LOGIN_PASSWORD']
    session = login(email=email, password=password)
    return {'session': session}

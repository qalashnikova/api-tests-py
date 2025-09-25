import pytest


@pytest.fixture
def base_url():
    return "https://reqres.in/api"


@pytest.fixture
def headers():
    return {"Content-Type": "application/json", "x-api-key": "reqres-free-v1"}


@pytest.fixture
def user_login_data():
    return {"email": "eve.holt@reqres.in", "password": "cityslicka"}


@pytest.fixture
def user_login_data_invalid():
    return {"email": "eve.holt@reqres.in", "password": ""}

import requests


def test_login_success():
    user = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

    headers = {"x-api-key": "reqres-free-v1"}

    response = requests.post("https://reqres.in/api/login", json=user, headers=headers)
    data = response.json()

    assert response.status_code == 200
    assert "token" in data

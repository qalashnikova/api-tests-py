import requests


def test_register_valid():
    user = {"email": "eve.holt@reqres.in", "password": "pistol"}
    headers = {"x-api-key": "reqres-free-v1"}

    response = requests.post(
        "https://reqres.in/api/register", json=user, headers=headers
    )
    data = response.json()

    assert response.status_code == 200
    assert "token" in data


def test_register_missing_password():
    user = {"email": "sydney@fife"}
    headers = {"x-api-key": "reqres-free-v1"}

    response = requests.post(
        "https://reqres.in/api/register", json=user, headers=headers
    )
    data = response.json()

    assert response.status_code == 400
    assert data["error"] == "Missing password"


def test_register_missing_email():
    user = {"email": "", "password": "123456"}
    headers = {"x-api-key": "reqres-free-v1"}

    response = requests.post(
        "https://reqres.in/api/register", json=user, headers=headers
    )
    data = response.json()

    assert response.status_code == 400
    assert data["error"] == "Missing email or username"

import requests


def test_successful_login(base_url, headers, user_login_data):
    response = requests.post(f"{base_url}/login", headers=headers, json=user_login_data)

    assert response.status_code == 200
    assert "token" in response.json()


def test_failed_login_missing_password(base_url, headers, user_login_data_invalid):
    response = requests.post(
        f"{base_url}/login", headers=headers, json=user_login_data_invalid
    )

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


def test_failed_login_missing_api_key(base_url, user_login_data):
    response = requests.post(f"{base_url}/login", json=user_login_data)

    assert response.status_code == 401
    assert response.json()["error"] == "Missing API key"

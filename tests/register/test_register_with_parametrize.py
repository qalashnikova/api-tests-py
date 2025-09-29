import requests
import pytest


@pytest.mark.parametrize(
    ("email", "password", "expected_status", "expected_error"),
    [
        ("eve.holt@reqres.in", "pistol", 200, None),
        ("eve.holt@reqres.in", "", 400, "Missing password"),
        ("", "", 400, "Missing email or username"),
    ],
)
def test_register_with_various_data(
    base_url, headers, email, password, expected_status, expected_error
):
    data = {"email": email, "password": password}
    response = requests.post(f"{base_url}/register", headers=headers, json=data)

    assert response.status_code == expected_status

    if expected_error:
        response_data = response.json()
        assert response_data["error"] == expected_error

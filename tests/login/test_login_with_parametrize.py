import requests
import pytest


@pytest.mark.parametrize(
    ("email", "password", "expected_status"),
    [
        ("eve.holt@reqres.in", "cityslicka", 200),
        ("wrong.email@reqres.in", "cityslicka", 400),
        ("", "cityslicka", 400),
    ],
)
def test_login_with_various_data(base_url, headers, email, password, expected_status):
    data = {"email": email, "password": password}
    response = requests.post(f"{base_url}/login", headers=headers, json=data)

    assert response.status_code == expected_status

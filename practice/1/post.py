import requests

user = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

headers = {"x-api-key": "reqres-free-v1"}

response = requests.post("https://reqres.in/api/login", json=user, headers=headers)

print("Status code:", response.status_code)

data = response.json()
print("Response JSON:", data)

if response.status_code == 200:
    print("Token:", data["token"])
else:
    print("Ошибка:", data.get("error", "Неизвестная ошибка"))

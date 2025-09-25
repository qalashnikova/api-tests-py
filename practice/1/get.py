import requests

# GET-запрос на получение информации о пользователе
response = requests.get("https://reqres.in/api/users/2")

print("Status code:", response.status_code)

data = response.json()

# Выведи имя пользователя
print("User name:", data["data"]["first_name"], data["data"]["last_name"])

# Список:
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Добавление в список
fruits.append("orange")
print(fruits[3])

# Вывести список
for fruit in fruits:
    print(fruit)

# Словарь:
user = {"id": 1, "name": "Rita", "email": "rita@example.com"}

# Добавление в словарь:
user["role"] = "queen"

# Вложенный словарь:
response = {
    "user": {
        "id": 42,
        "name": "Rayan Gosling",
    },
    "status": "ok",
}

print(response["user"]["name"], response["status"])


# Функции:
def greet(name):
    print("Hello,", name)


greet("Rayan")


def add(a, b):
    return a + b


print(add(2, 3))

# Когда мы получаем ответ от API, это строка в формате JSON:
response_text = '{"token": "abc123"}'

# Чтобы превратить это в словарь:
import json

parsed = json.loads(response_text)
print(parsed["token"])  # 👉 abc123

# И наоборот — можно превратить Python-объект в строку:
user = {"email": "rita@example.com"}
json_string = json.dumps(user)
print(json_string)  # 👉 {"email": "rita@example.com"}

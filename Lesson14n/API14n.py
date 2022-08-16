import requests

response = requests.get("https://rickandmortyapi.com/api/character")
# print(response.text)

j = response.json()
names = []
characters = {}
# characters = []

for character in j['results']:
    name = character['name']
    status = character['status']
    match name, status:
        case _, "Dead":
            print(name)

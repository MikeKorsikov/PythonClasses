import requests

response = requests.get("https://rickandmortyapi.com/api/character")
# print(response.text)

j = response.json()
names = []

for character in j['results']:
    names.append(character['name'])
print(*names)

print((type(response.text)))

# post


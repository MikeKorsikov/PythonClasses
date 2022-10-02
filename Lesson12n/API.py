import requests
endpoint = "https://rickandmortyapi.com/api/character"
response = requests.get(endpoint)
# print(response.text)

j = response.json()
names = []

for character in j['results']:
    names.append(character['name'])
print(*names)

print((type(response.text)))

# post


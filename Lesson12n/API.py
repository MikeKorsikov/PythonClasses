import requests

response = requests.get("https://rickandmortyapi.com/api/character")
print(response.text)


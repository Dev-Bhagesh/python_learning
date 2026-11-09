import requests
import json

response = requests.get(
    "https://pokeapi.co/api/v2/pokemon/pikachu"
)

data = response.json()
print(response.status_code)
print(type(response))
print(type(data))
# print(json.dumps(data,indent=4)[:1000])
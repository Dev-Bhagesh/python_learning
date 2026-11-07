import requests
import json

response = requests.get(
    "https://pokeapi.co/api/v2/pokemon/pikachu"
)

# print(response.status_code)
# print(response.text)
# print(response.headers)
data = response.json()
print(json.dumps(data,indent=4))
import requests
import json

url = "https://httpbin.org/headers"

header = {
    "User-Agent": 'PokemonDataCollector',
    "Accept":'application/json',
    "X-App-Version":'1.0'
}

response = requests.get(
    url,
    headers=header
)

print(response.json())
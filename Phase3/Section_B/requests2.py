import requests
import json

url = "https://httpbin.org/headers"

header = {
    "Authorization" : 'Bearer demo-token-123',
    "User-Agent": 'PokemonDataCollector',
    "Accept":'application/json',
    "X-App-Version":'1.0'
}

response = requests.get(
    url,
    headers=header
)
data = response.json()
print(json.dumps(data,indent=4))


try:
    url2 = "https://pokeapi.co/api/v2/pokemon/unknownpokemon"
    PokeResponse = requests.get(
        url2
    )

    PokeResponse.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error {e}")
except requests.exceptions.RequestException as e:
    print(f'Request Exception {e}')
    
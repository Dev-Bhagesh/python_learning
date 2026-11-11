import requests

session = requests.Session()

session.headers.update({
    'User-Agent' : "PokemonCollector",
    "Accept" : "application/json"
}
)

response1 = session.get(
    "https://pokeapi.co/api/v2/pokemon/pikachu"
)

response2 = session.get(
    "https://pokeapi.co/api/v2/pokemon/charizard"
)


print(response1.json()['name'])
print(response2.json()['name'])
print(session.cookies)
print(session.headers)
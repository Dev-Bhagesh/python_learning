import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(
    url,
    params={
        'limit' : 5,
        'offset': 10
    }
)

data = response.json()
pokemons = data['results']
print(data)

for pokemon in pokemons:
    print(pokemon['name'])
    print(pokemon['url'])
    print('-'*75)

# print(response.headers.get('Content-type'))
# print(response.headers.get('Status-code'))
# print(response.headers.get('Content-ength'))

# print(response.status_code)
# print(type(response))
# print(type(data))
# print(json.dumps(data,indent=4)[:1000])
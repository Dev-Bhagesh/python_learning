import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"

lim = 0
params = {
    'limit' : 10,
    'offset':0
}
count = 1
while lim < 5:
    if lim <= 0:
        response = requests.get(
            url , 
            params
        )
    
    else:
        response = requests.get(
            url
        )
    
    data = response.json()
    url = data['next']

    for pokemon in data['results']:
        print(f'Pokemon ID {count}: {pokemon['name']}')
        count += 1

    lim += 1

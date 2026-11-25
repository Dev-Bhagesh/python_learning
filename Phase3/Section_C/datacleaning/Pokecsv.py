import csv
import json
import requests
from pathlib import Path

pokeApi = 'https://pokeapi.co/api/v2/pokemon'

params = {
    'limit' : 5,
    'offset' : 0
}

lim = 0
pokemon_fields = ['pokemon_id','pokemon_name','pokemon_type','pokemon_height','pokemon_weight']
pokemon_list = []
while lim <= 1:
    if lim < 1:
        response = requests.get(pokeApi,params=params)
    else:
        response = requests.get(pokeApi)
    lim += 1
    data = response.json()
    pokeApi = data['next']

    for item in data['results']:
        pokemon_detail_url = item['url']
        pokemon_response = requests.get(pokemon_detail_url)
        pokemon_data = pokemon_response.json()

        pokemon_type = ','.join(types['type']['name'] for types in pokemon_data['types'])
        pokemon_list.append({
            pokemon_fields[0]:pokemon_data['id'],
            pokemon_fields[1]:pokemon_data['name'],
            pokemon_fields[2]:pokemon_type,
            pokemon_fields[3]:pokemon_data['height'],
            pokemon_fields[4]:pokemon_data['weight'],
        }
        )

cwd = Path.cwd()
poke_file = Path(cwd/'pokemon.csv').resolve()

if not poke_file.exists() :
    poke_file.touch()

header = False
with open('pokemon.csv','r',newline='',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    if headers:
        header = True

with open('pokemon.csv','a',newline='',encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file,fieldnames=pokemon_fields)
    if header == False:
        writer.writeheader()

    writer.writerows(pokemon_list)
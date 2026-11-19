import json
import csv
from pathlib import Path

cwd = Path.cwd()
json_file = Path(cwd/'pokemon.json').resolve()

if not json_file.exists():
    json_file.touch()

pokemons_list = []

with open(f'poke2.csv','r') as file:
    reader = csv.DictReader(file)
    fieldNames = reader.fieldnames
    print(type(fieldNames))
    print(fieldNames)
    data = reader
    for pokemon in data:
        poke = {
            fieldNames[0]:int(pokemon['pokemon_id']),
            fieldNames[1]:pokemon['pokemon_name'],
            fieldNames[2]:int(pokemon['pokemon_height']),
            fieldNames[3]:int(pokemon['pokemon_weight']),
            fieldNames[4]:pokemon['pokemon_type']
        }

        pokemons_list.append(poke)


with open(f'{json_file}','w') as file:
    json.dump(pokemons_list,file,indent=4)
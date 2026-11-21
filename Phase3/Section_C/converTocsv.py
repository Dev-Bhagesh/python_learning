import json
import csv
from pathlib import Path

cwd = Path.cwd()
pokecsv_file = Path(cwd/'pokecsv.csv').resolve()

if not pokecsv_file.exists():
    pokecsv_file.touch()

pokemon_list = []

with open(f'pokemon.json','r') as file:
    data = json.load(file)
    fieldNames = list(data[0].keys())
    print(fieldNames)
    for pokemon in data:
        pokemon_list.append(pokemon)

    
with open(f'{pokecsv_file}','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fieldNames)
    writer.writeheader()
    for pokemon in pokemon_list:
        writer.writerow(pokemon)
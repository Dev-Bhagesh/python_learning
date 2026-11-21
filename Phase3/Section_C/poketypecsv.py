import csv
from pathlib import Path
from itertools import islice

cwd = Path.cwd()
folder_path = Path(cwd/'Pokemons_Types2').resolve()

if not folder_path.exists():
    folder_path.mkdir(parents=True)

with open('pokemon.csv','r') as file:
    reader = csv.DictReader(file)
    # print(reader.fieldnames)

    for pokemon in reader:
        pokemon_types = pokemon['pokemon_type'].split(',')
        fieldnames = reader.fieldnames
        # print(fieldnames)
        for type in pokemon_types:
            # print(type)
            header_exist = False
            file_path = Path(folder_path/f'{type}.csv').resolve()

            if not file_path.exists():
                file_path.touch()

            with open(f"{file_path}",'r') as file:
                readerrr = csv.DictReader(file)
                headers = readerrr.fieldnames
                if headers:
                    header_exist = True

            with open(f'{file_path}','a',newline='') as file:
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                if header_exist == False:
                    writer.writeheader()
                writer.writerow(pokemon)

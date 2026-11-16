import csv
from pathlib import Path

cwd = Path.cwd()
pokemon_folder = Path(cwd/'Pokemons_Types').resolve()

if not pokemon_folder.exists():
    pokemon_folder.mkdir(parents = True)


with open('pokemon.csv','r') as file:
    data = csv.DictReader(file)
    print(data)
    for pokemon in data:
        # if int(pokemon['pokemon_id']) > 10:
        #     print(f"Pokemon Name : {pokemon['pokemon_name']}")
        #     print(f"Pokemon ID   : {int(pokemon['pokemon_id'])}")
        #     print(f"Pokemon Type : {pokemon['pokemon_type']}")
        #     print('='*50)

        pokemon_type = pokemon['pokemon_type']
        pokemon_type = pokemon_type.split(',')
        headers = ['pokemon_id','pokemon_name','pokemon_type']

        #Grass Type
        if 'grass'in pokemon_type:
            file_path = Path(pokemon_folder/'grass_type.csv').resolve()
            if not file_path.exists() :
                file_path.touch()

            headerexists = False
            with open(f'{file_path}','r') as file:
                reader = csv.DictReader(file)
                if reader.fieldnames:
                    headerexists = True

            with open(f'{file_path}','a',newline='') as file:
                writer = csv.DictWriter(file,fieldnames=headers,extrasaction='ignore')
                if headerexists == False:
                    writer.writeheader()
                writer.writerow(pokemon)

        #Fire Type
        if 'fire' in pokemon_type:
            file_path = Path(pokemon_folder/'fire_type.csv').resolve()
            if not file_path.exists():
                file_path.touch()

            headerexists = False
            with open(f'{file_path}','r')as file:
                reader = csv.DictReader(file)
                if reader.fieldnames:
                    headerexists = True

            with open(f'{file_path}','a',newline='') as file:
                writer = csv.DictWriter(file,fieldnames=headers,extrasaction='ignore')
                if headerexists == False:
                    writer.writeheader()
                writer.writerow(pokemon)

        #Water Type
        if 'water' in pokemon_type:
            file_path = Path(pokemon_folder/'water_type.csv').resolve()
            if not file_path.exists():
                file_path.touch()

            headerexists = False
            with open(f'{file_path}','r') as file:
                reader = csv.DictReader(file)
                if reader.fieldnames :
                    headerexists = True

            with open(f'{file_path}','a', newline='') as file:
                writer = csv.DictWriter(file,fieldnames=headers,extrasaction='ignore')
                if headerexists == False:
                    writer.writeheader()
                writer.writerow(pokemon)
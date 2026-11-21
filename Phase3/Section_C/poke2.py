import csv

pokemon_list = []

with open('poke.csv','r') as file:
    reader = csv.DictReader(file)

    for pokemon in reader :
        if pokemon['pokemon_name'] == 'pikachu':
            pokemon['pokemon_type'] = 'electric,normal'
        
        pokemon_list.append(pokemon)


fields = ['pokemon_id','pokemon_name','pokemon_height','pokemon_weight','pokemon_type']
with open('poke2.csv','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    for pokemon in pokemon_list:
        writer.writerow(pokemon)
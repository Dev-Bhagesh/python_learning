import csv
import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/"

params = {
    'limit' : 5,
    'offset':0
}

count = 0
lim = 0


# pokemons = []
# response = requests.get(url,params=params)
# # data = response.json()
# # url = data['next']

# data = response.json()
# for items in data['results']:
#     pokemons.append(items)

# print(json.dumps(pokemons,indent=4))


pokemon_list = []
while lim<=3:
    if lim <= 0:
        response = requests.get(url,params=params)
    else:
        response = requests.get(url)
    lim += 1
    data = response.json()
    url = data['next']
    for item in data['results']:
        pokemon_detail_url = item['url']
        pokemon_detail_response = requests.get(pokemon_detail_url)
        pokemon_details = pokemon_detail_response.json()
        # print(json.dumps(pokemon_details,indent=4))
        # print(pokemon_details['id'])
        # print(pokemon_details['name'])
        # print(pokemon_details['height'])
        # print(pokemon_details['weight'])
        # print(json.dumps(pokemon_details['types'],indent=4))
        # print(json.dumps(pokemon_details['stats'],indent=4))
        # print('='*50)
        pokemon_type = ','.join(item['type']['name'] for item in pokemon_details['types'])
        pokemon_list.append({''
            'pokemon_id':pokemon_details['id'],
            'pokemon_name':pokemon_details['name'],
            'pokemon_height':pokemon_details['height'],
            'pokemon_weight':pokemon_details['weight'],
            # 'pokemon_type':pokemon_details['types'][0]['type']['name']
            'pokemon_type':pokemon_type
            })

        

with open('pokemon.csv','a',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=[
        'pokemon_id',
        'pokemon_name',
        'pokemon_height',
        'pokemon_weight',
        'pokemon_type'
    ])

    writer.writeheader()
    writer.writerows(pokemon_list)

print(json.dumps(pokemon_list,indent=4))
    
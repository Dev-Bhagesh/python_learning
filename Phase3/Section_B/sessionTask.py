import requests

session = requests.Session()
pokelist = ['Pikachu','Charizard','Gengar']

session.headers.update({
    "User-Agent":"Pokemon Collector",
    "Accept":"application/json",
    "X-App-Version":'1.0'
})

for poke in pokelist:
    response = session.get(
        f"https://pokeapi.co/api/v2/pokemon/{poke}"
    )

    print(response.json()['name'])

print(session.headers)
print(session.cookies)
session.close()
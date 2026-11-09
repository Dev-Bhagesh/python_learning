import json

pokemon = [
    {
        'name':'pikachu',
        'level':20,
        'type':'electric',
    },
    {
        'name':'charmander',
        'level':25,
        'type':'fire',
    },
    {
        'name':'squertal',
        'level':22,
        'type':'water',
    },
    {
        'name':'bulbasour',
        'level':24,
        'type':'grass',
    }
]

with open('json1.json','w')as file:
    json.dump(pokemon,file,indent=4)
data = []
with open('json1.json','r') as file:
    data = json.load(file)

for poke in data:
    print(poke['name'])
    print(poke['level'])
    print(poke['type'])
    print('-'*75)
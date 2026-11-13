import time
from fastapi import FastAPI,HTTPException,Header
from pydantic import BaseModel

app = FastAPI()

pokemon_db = []

class Pokemon(BaseModel):
    name:str
    level:int
    type:str

class Pokemonupdate(BaseModel):
    name:str | None=None
    level:int | None = None
    type:str | None = None

@app.get('/')
def home():
    return {'message ': 'Hello this is my first fast api server'}

@app.get('/pokemonName/{pokemonName}')
def GetPoke(pokemonName:str):
    return {
        'message':"Successfully fetching pokemon",
        'Pokemon':pokemon_db
    }

@app.get('/name/{name}')
def get_Name(name:str , type:str='electric' ,level:int = 20):
    return {
        'Name':name,
        'Level':level,
        'type':type
    }

@app.post('/pokemon')
# the body of request contains the data of pokemon
def post_Pokemon(pokemondata: Pokemon):
    pokemon_db.append(pokemondata.model_dump())
    return{
        'Message':'Pokemon saved successfully',
        'Pokemon':pokemondata
    }

@app.put('/pokemonChange/{pokemon_name}')
def update_pokemon(pokemon : Pokemon, pokemon_name : str):

    for index, pokeName in enumerate(pokemon_db):
        if pokeName['name'].lower() == pokemon_name.lower():
            pokeName.update(pokemon.model_dump())
        
        return{
            'Message':'Pokemon Updated',
        }

    # if pokemon_name.lower() != pokemon.name.lower():
    #     raise HTTPException(
    #         status_code=406,
    #         detail='The missmatch in query name and request body name'
    #     )
    # index = 0
    # for pokeName in pokemon_db:
    #     if pokeName['name'] == pokemon_name:
    #         pokemon_db[pokeName] = pokemon.model_dump()
    #         index = pokeName

@app.patch('/update/{pokemon_name}')
def PokeUpdate(pokemon : Pokemonupdate,pokemon_name :str):

    update_data = pokemon.model_dump(exclude_unset=True)

    for index,pokeName in enumerate(pokemon_db):
        if pokeName['name'].lower() == pokemon_name.lower():
            pokeName.update(update_data)

            return {
                    'message': 'Pokemon updated',
                    'Pokemon': pokemon_db[index]
                }

    # return {
    #     'message':'Pokemon updated',
    #     'Pokemon':pokemon_db[index]
    # }

keyran = 0
@app.get('/Get-key')
def GetKey():
    if keyran == 0:
        return({
            'message':'Successfully created Key',
            'key':rate_limits['abc123']
        })
    else:
        return({
            'message':'Successfully Created key',
            'key':rate_limits['xyz456']
        })


# current_window = time.time()
rate_limits = {
    "abc123":{
        "count":0,
        "window_start":0,
    },
    "xyz456":{
        "count":0,
        "window_start":0
    }
}

@app.get('/protected')
def Protected(x_api_key : str = Header()): 

    if x_api_key not in rate_limits:
        raise HTTPException(status_code=401,detail='Unautharised')

    key_data = rate_limits[x_api_key]
    current_time = time.monotonic()
    print("Current time:", current_time)
    print("Window start:", key_data['window_start'])
    print("Window expires:", key_data['window_start'] + 60)
    print("Request count:", key_data['count'])
    if key_data['window_start'] + 60 < current_time :
        key_data['window_start'] = current_time
        key_data['count'] = 0
        print('Window time reset complete and count reset done')
        print("After reset:", key_data)

    if key_data['count'] >= 5:
        raise HTTPException(status_code=429,detail='Too many requests')
    else:
        key_data['count'] += 1
        return('Welcome You Successfully Accessed The Protected Route')

pokemon_db = [
    {"id": 101, "name": "Pikachu"},
    {"id": 102, "name": "Eevee"},
    {"id": 103, "name": "Charmander"},
    {"id": 104, "name": "Bulbasaur"},
    {"id": 105, "name": "Squirtle"},
    {"id": 106, "name": "Snorlax"},
    {"id": 107, "name": "Mew"},
    {"id": 108, "name": "Gengar"},
    {"id": 109, "name": "Ditto"},
    {"id": 110, "name": "Dragonite"}
]

@app.get('/cursor')
def CursorTest(limit:int = 3,cursor:int | None = None):
    start_index = 0
    if cursor is not None:
        for index , pokemon in enumerate(pokemon_db):
            if pokemon['id'] == cursor:
                start_index = index + 1
                break

    end_index = start_index + limit
    batch = pokemon_db[start_index:end_index]

    if end_index<len(pokemon_db) and batch:
        next_cursor = batch[-1]["id"]
    else:
        next_cursor = None

    return{
        "result":batch,
        "next_cursor":next_cursor
    }
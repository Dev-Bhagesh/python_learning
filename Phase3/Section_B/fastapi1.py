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

key = 'hello'
@app.get('/Get-key')
def GetKey():

    return({
        'message':'Successfully created Key',
        'key':key
    })

@app.get('/protected')
def Protected(x_api_key : str = Header()): 
    if x_api_key == key:
        return({
            'message':'successfully accessing the protected route'
        })
    else:
        return({
            'message':'Not authoarized'
        })
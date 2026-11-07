from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message ': 'Hello this is my first fast api server'}

@app.get('/{name}')
def get_Name(name):
    return {'Name':name}
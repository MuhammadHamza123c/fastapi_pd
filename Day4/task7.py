
from fastapi import FastAPI 
app=FastAPI()
@app.get('/hello')
def check(name:str):
    return{
        'Greeting':f'Hello {name}'
    }
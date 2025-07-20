from fastapi import FastAPI 
app=FastAPI()
@app.get('/Greet/{name}')
def check(name:str):
    return{
        "Greet":f'Hello {name}'
    }
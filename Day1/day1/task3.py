from fastapi import FastAPI  
app=FastAPI()
@app.get('/hello/{name}')#path parameter
def check(name:str):
    return{
        f'Hello {name}!! how can i help you?'
    }
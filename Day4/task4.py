
from fastapi import FastAPI 
app=FastAPI()
@app.get('/length/{text}')
def check(text:str):
    return{
        'Word Length':f'Here is Length of word: {len(text)}'
    }

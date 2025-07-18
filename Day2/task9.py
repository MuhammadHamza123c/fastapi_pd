from fastapi import FastAPI 
app=FastAPI()
@app.get('/count')
def check(text:str):
    length_word=len(text.split())
    return{
        'Words Length':f'Here is total words in text: {length_word}'
    }
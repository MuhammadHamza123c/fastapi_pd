from fastapi import FastAPI 
app=FastAPI()
@app.get('/count_words')
def check(text:str):
    length_check=len(text)
    return{
        'Words Count':f'Here is Total numbers of words: {length_check}'
    }
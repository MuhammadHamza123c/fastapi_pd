from fastapi import FastAPI 
app=FastAPI()
@app.get('/square/{numb}')
def check(numb:int):
    return{
        'Square':f'Here is Square of givem number: {numb*numb}'
    }
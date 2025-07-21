
from fastapi import FastAPI 
app=FastAPI()
@app.get('/multiply')
def math(a:int,b:int):
    multiply_number=a*b
    return{
        'Product':f'Here is Product of both numbers: {multiply_number}'
    }
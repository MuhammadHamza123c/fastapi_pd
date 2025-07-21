from fastapi import FastAPI 
app=FastAPI()
@app.get('/power/{base}/{exp}')
def check(base:int,exp:int):
    power=base*exp
    return{
        'Power':f'Here is Power of given number: {power}'
    }

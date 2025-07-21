from fastapi import FastAPI 
app=FastAPI()
@app.get('/mix/{f}/{i}')
def check(f:float,i:int):
    return{
        'Mix Multiplication':f*i'
    }

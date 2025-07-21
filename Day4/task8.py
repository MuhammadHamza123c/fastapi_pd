from fastapi import FastAPI 
app=FastAPI()
@app.get('/add')
def math(a:int,b:int):
    total=a+b 
    return{'Total':f'Here is Sum of both numbers: {total}'}

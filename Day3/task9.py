from fastapi import FastAPI 
app=FastAPI()
@app.get('/even_odd/{number}')
def check(number:int):
    if number%2==0:
        result="Its an even"
    else:
        result="Its an odd"
    return {
        "Even or odd":result
    }


from fastapi import FastAPI 
app=FastAPI()
@app.get('/convert_to_month/{year}')
def check(year:int):
    month=year*12
    return{
        'Total Month':f'Here is total months: {month}'
    }

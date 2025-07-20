from fastapi import FastAPI 
app=FastAPI()
@app.get('/conversion/{celsius}')
def temperature(celsius:float):
    convert=(1.8*celsius)+32
    return{
        'Fahrenheit':f'Here is Temperature in Fahrenheit: {convert} Degree'
    }


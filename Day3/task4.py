
from fastapi import FastAPI 
app=FastAPI()
@app.get('/Convert_Km_to_mil/{km}')
def convert(km:float):
    mile=km* 0.621371
    return{
        'Miles':f'Here is Conversion of Kilometer into miles: {mile}'
    }
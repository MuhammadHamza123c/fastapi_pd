from fastapi import FastAPI 
from pydantic import BaseModel 
class Info(BaseModel):
    name:str
    age:int
    email:str

app=FastAPI()
@app.post('/info')
def check(i:Info):
    return{
        'Name':i.name,
        'Age':i.age,
        'Email':i.email
    }
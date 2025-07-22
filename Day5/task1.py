from fastapi import FastAPI 
from pydantic import BaseModel,Field
class info(BaseModel):
    name:str=Field(...,min_length=3)
app=FastAPI()
@app.post('/info')
def check(i:info):
    return{
        'Name':i.name
    }
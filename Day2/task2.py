from fastapi import FastAPI
from pydantic import BaseModel,Field
class info(BaseModel):
    name:str=Field(..., min_length=3)
    age:int=Field(...,ge=18)

app=FastAPI()
@app.post('/Info')
def check(i:info):
    return {
        'Message':f'Hello {i.name}'
    }

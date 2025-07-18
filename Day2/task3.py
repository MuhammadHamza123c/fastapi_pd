from fastapi import FastAPI 
from typing import Optional 
from pydantic import BaseModel 

class Info(BaseModel):
    name:str
    age:int
    bio:Optional[str]=None

app=FastAPI()
@app.post('/info')
def check(i:Info):
    if i.bio:
        result={
            'Bio':i.bio
        }
    else:
        result={
            'Bio':"Sorry bio not provided!"
        }
    return result
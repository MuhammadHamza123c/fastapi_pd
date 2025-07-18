from fastapi import FastAPI 
from pydantic import BaseModel
from typing import List
class college(BaseModel):
    country_name:str
    city_name:str
    state:str
    coll_location:str

class Info(BaseModel):
    name:str
    age:str
    bio:str
    skills:List[str]
    college:college

app=FastAPI()
@app.post('/Form')
def check(i:Info):
    return{
        'Name':i.name,
        'Age':i.age,
        'Bio':i.bio,
        'Skills':i.skills,
        'College Info':i.college
    }

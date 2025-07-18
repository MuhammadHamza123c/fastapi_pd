from fastapi import FastAPI 
from typing import List
from pydantic import BaseModel 
class info(BaseModel):
    name:str
    age:int
    bio:str
    skills:list[str]
app=FastAPI()
@app.post('/info')
def check(i:info):
    if i.skills:
     top_skills=i.skills[0]
    else:
       top_skills='No Skills Provided'
    return top_skills
    

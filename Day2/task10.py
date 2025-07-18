from fastapi import FastAPI 
from pydantic import BaseModel 
info_list=[]
class Info(BaseModel):
    name:str
    age:int
    bio:str

app=FastAPI()
@app.post('/info')
def check(i:Info):
    info_list.append(i.dict())
    return{'Message':"Thank you for Info!!!"}

@app.get('/get_info')
def check_info():
    return {'Info List':info_list}

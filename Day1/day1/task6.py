from fastapi import FastAPI
from pydantic import BaseModel 
class get_feedback(BaseModel):
    username:str
    message:str

app=FastAPI()
@app.post('/feedback')
def check(g1:get_feedback):
    return{
        'User name':g1.username,
        'Message':g1.message
    }
from fastapi import FastAPI 
from pydantic import BaseModel 
class auth(BaseModel):
    username:str
    password:str

app=FastAPI()
@app.post('/login')
def check(a:auth):
    result=''
    if a.username=="admin" and a.password=='123':
        result='Login Successful'
    else:
        result="Try Again"
    return result
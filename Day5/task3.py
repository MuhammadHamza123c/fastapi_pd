from fastapi import FastAPI 
from pydantic import BaseModel,EmailStr
class Login(BaseModel):
    email:EmailStr

app=FastAPI()
@app.post('/login')
def check(l:Login):
    return{
        'Email':l.email
    }
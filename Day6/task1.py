from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

class Login(BaseModel):
    username: str = Field(..., min_length=3)
    emai: EmailStr
    password: str = Field(..., min_length=6)

app = FastAPI()

@app.post('/Login')
def check(l: Login):
    return {'Message': f'Hello {l.username}'}'''
    }
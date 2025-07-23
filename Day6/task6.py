from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

class Register(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(..., min_length=6)

app = FastAPI()

@app.post('/register')
def register_user(user: Register):
    return {'Message': f'Registered user: {user.full_name}'}
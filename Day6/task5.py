from fastapi import FastAPI 
from pydantic import BaseModel, Field, EmailStr

class Contact(BaseModel):
    name: str
    email: EmailStr
    message: str = Field(..., max_length=500)

app = FastAPI()

@app.post('/Contact')
def check(c: Contact):
    return {'Message': f'Contact: {c.name}'}'''
    }
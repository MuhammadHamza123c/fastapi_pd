from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class Register(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

@app.post("/register")
def register_user(r: Register):
    return {"Email": r.email}

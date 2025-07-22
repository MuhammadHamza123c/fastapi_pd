from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class FullInfo(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.post("/full-info")
def get_full_info(info: FullInfo):
    return info

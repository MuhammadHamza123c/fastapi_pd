from fastapi import FastAPI  
from pydantic import BaseModel, Field

class Info(BaseModel):
    name: str
    age: int = Field(..., gt=18, lt=100)

app = FastAPI()

@app.post('/info')
def check(i: Info):
    return {'Message': f'Welcome {i.name}'}'''
    }
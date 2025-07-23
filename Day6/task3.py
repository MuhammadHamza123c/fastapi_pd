
from fastapi import FastAPI 
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str
    tags: str
    date: str

app = FastAPI()

@app.post('/Blog')
def check():
    return {'Message': 'Thank you for posting blog!'}'''
    }
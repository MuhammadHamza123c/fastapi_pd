from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class Subscription(BaseModel):
    name: str
    email: EmailStr

app = FastAPI()

@app.post('/subscribe')
def subscribe(sub: Subscription):
    return {'Message': f'Subscribed {sub.name} successfully!'}
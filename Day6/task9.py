from fastapi import FastAPI
from pydantic import BaseModel

class Event(BaseModel):
    event_name: str
    location: str
    date: str

app = FastAPI()

@app.post('/event')
def create_event(e: Event):
    return {'Event Created': e.event_name}
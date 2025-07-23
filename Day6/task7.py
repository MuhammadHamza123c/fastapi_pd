from fastapi import FastAPI
from pydantic import BaseModel, Field

class Feedback(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comments: str

app = FastAPI()

@app.post('/feedback')
def get_feedback(f: Feedback):
    return {'Rating': f.rating, 'Comments': f.comments}
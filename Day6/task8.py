from fastapi import FastAPI
from pydantic import BaseModel

class JobApplication(BaseModel):
    name: str
    cv_link: str
    skills: list[str]

app = FastAPI()

@app.post('/apply')
def apply(job: JobApplication):
    return {'Applicant': job.name, 'Skills': job.skills}
from fastapi import FastAPI
from pydantic import BaseModel, Field
import re

app = FastAPI()

class RegexUser(BaseModel):
    name: str = Field(..., regex="^[A-Za-z ]+$")

@app.post("/regex-user")
def get_regex_user(u: RegexUser):
    return {"Validated Name": u.name}

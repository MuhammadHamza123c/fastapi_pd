from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import Optional

class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"


class Info(BaseModel):
    name: str
    age: int
    bio: Optional[str] = None
    gender: GenderEnum

app = FastAPI()


@app.post('/info')
def check(i: Info):
    return {
        "Name": i.name,
        "Age": i.age,
        "Gender": i.gender,
        "Bio": i.bio if i.bio else "No bio provided"
    }

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class UserInfo(BaseModel):
    name: str
    age: int = Field(..., ge=18)

@app.post("/user")
def get_user(user: UserInfo):
    return {"Name": user.name, "Age": user.age}

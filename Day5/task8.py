from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Role(str, Enum):
    admin = "admin"
    user = "user"

class LoginWithRole(BaseModel):
    email: str
    role: Role

@app.post("/login-role")
def login_role(data: LoginWithRole):
    return {"Email": data.email, "Role": data.role}

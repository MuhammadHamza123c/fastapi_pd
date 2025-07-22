from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class MobileData(BaseModel):
    mobile: str = Field(..., min_length=11, max_length=11)

@app.post("/mobile")
def validate_mobile(m: MobileData):
    return {"Mobile Number": m.mobile}

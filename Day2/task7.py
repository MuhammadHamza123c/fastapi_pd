from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/custom-message")
def custom_message():
    message = {"message": "This is a custom JSON response"}
    return JSONResponse(content=message, status_code=200)

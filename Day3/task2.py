from fastapi import FastAPI 
app=FastAPI()
@app.get('/about')
def info():
    return{
        'Info Message':f"Hello, Hamza. So you are a data scientist!"
    }
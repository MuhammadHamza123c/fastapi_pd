from fastapi import FastAPI 
app=FastAPI()
@app.get('/hello')
def check():
    return{
        'Message':'Welcome Sir'
    }
from fastapi import FastAPI 
app=FastAPI()
@app.get('/about')
def check():
    return{
        'Name':"Hamza",
        'Role':"Data Scientist"
    }
from fastapi import FastAPI 
app=FastAPI()
@app.get('/time/{hours}')
def check(hours:float):
    mints=hours*60
    return{
        'Total Mints':mints
    }
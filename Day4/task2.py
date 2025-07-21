from fastapi import FastAPI 
app=FastAPI()
@app.get('/seconds/{days}')
def check(days:int):
    count_seconds=days*24*60*60
    return{'Total Seconds':f'Here is Total Seconds: {count_seconds}'}




from fastapi import FastAPI 
app=FastAPI()
@app.get('/search')
def check(name:str):
    if name=="Ali":
        result={'Message':"Hello Ali"}
    else:
        result={"Message":"Sorry invalid query"}
    return result
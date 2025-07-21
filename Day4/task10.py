from fastapi import FastAPI 
app=FastAPI()
@app.get('/fullname')
def check(first_name:str,last_name:str):
    full_name=first_name + " " + last_name
    return{
        'Full name':f'Here is Full name: {full_name}'
    }
from fastapi import FastAPI 
app=FastAPI()
@app.get('/fullname/{first_name}/{second_name}')
def full_name(first_name:str,second_name:str):
    name=first_name + ' ' + second_name
    return{
        'Full name':f"Here is Full name: {name}"
    }  
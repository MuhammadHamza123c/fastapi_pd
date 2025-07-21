from fastapi import FastAPI 
app=FastAPI()
@app.get('Check_uppercase/{text}')
def check(text:str):
    return{
        'Upper case_not':text.isupper()
    }

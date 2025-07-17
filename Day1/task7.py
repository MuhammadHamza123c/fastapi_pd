from fastapi import FastAPI 
from pydantic import BaseModel
class Addition(BaseModel):
    value_one:int
    value_two:int

app=FastAPI()
@app.post('/sum')
def check(add:Addition):
    sum_values=add.value_one+add.value_two
    return{'Sum':f'Here is Sum of both numbers: {sum_values}'}
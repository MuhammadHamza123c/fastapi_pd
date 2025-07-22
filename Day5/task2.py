from fastapi import FastAPI 
from pydantic import BaseModel,Field
class Product(BaseModel):
    name:str=Field(...,min_length=3,max_length=20)
app=FastAPI()
@app.post('/Product')
def check(p:Product):
    return{
        'Product Name':p.name
    }
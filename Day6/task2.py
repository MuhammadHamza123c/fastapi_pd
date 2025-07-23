from fastapi import FastAPI 
from pydantic import BaseModel

class Product(BaseModel):
    product_name: str
    price: float
    availability: bool

app = FastAPI()

@app.post('/Product_Info')
def check(p: Product):
    return {
        'Product Name': p.product_name,
        'Product Price': p.price,
        'Product Availability': p.availability
    }
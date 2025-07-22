from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class ProductDetails(BaseModel):
    name: str
    description: Optional[str] = None

@app.post("/product-details")
def get_product_info(p: ProductDetails):
    return p

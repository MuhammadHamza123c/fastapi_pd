from fastapi import FastAPI 
category_items = {
    "electronics": ["Laptop", "Smartphone", "Headphones", "Tablet", "Smartwatch"],
    "books": ["Python Crash Course", "Deep Learning with PyTorch", "FastAPI Guide", "Clean Code"],
    "clothing": ["T-shirt", "Jeans", "Jacket", "Sneakers", "Cap"],
    "groceries": ["Milk", "Bread", "Eggs", "Apples", "Rice"],
    "furniture": ["Chair", "Table", "Sofa", "Bookshelf", "Bed"],
    "stationery": ["Pen", "Notebook", "Eraser", "Highlighter", "Stapler"]
}

app=FastAPI()
@app.get('/items')
def check(category_:str):
    get_item=' ,'.join(category_items[category_])
    return{'ITEM':f'Here is Category Items: {get_item}'}
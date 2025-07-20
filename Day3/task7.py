from fastapi import FastAPI 
app=FastAPI()
@app.get('/multiply/{number}/{number1}')
def math(number:int,number1:int):
    return{
        'Multiplication':f'Here is Multiply of both numbers: {number*number1}'
    }
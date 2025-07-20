from fastapi import FastAPI 
app=FastAPI()
@app.get('/contact')
def contact_num():
    return{
        'Contact Number':'Here is your contact number: +923091792065'
    }
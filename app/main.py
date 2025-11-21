from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def get():
    return {"data":"server running on the port 8000"}
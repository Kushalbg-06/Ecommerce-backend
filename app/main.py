from fastapi import FastAPI,Depends, HTTPException,status
from . import models,schemas,hashing
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
app=FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])
def home():
    return {'message': 'server is running'}

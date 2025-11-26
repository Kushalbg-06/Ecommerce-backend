from fastapi import FastAPI,Depends, HTTPException,status
from . import models,schemas,hashing
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from .routers import user_router,order_router,product_router,cart_router
app=FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])
def home():
    return {'message': 'server is running'}
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)

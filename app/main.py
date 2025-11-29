from fastapi import FastAPI
from . import models
from .database import engine
from .routers import order_router,product_router,cart_router
from .authentication import auth_router

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])
def home():
    return {'message': 'server is running'}


app.include_router(auth_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)

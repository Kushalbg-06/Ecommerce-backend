from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from ..database import get_db
from typing import List
from .. import models,schemas,database

router=APIRouter(
    prefix="/product",
    tags=["Products"]
)

#add products
@router.post("/",response_model=schemas.ProductResponse,status_code=status.HTTP_202_ACCEPTED)
def add(product:schemas.ProductCreate,db:session=Depends(get_db)):
    new_product=models.Product(
    name=product.name,
    price=product.price,
    stock=product.stock,
    discription=product.discription
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

#get all products
@router.get("/",response_model=List[schemas.ProductResponse],status_code=200)
def get_products(db:session=Depends(get_db)):
    new_products=db.query(models.Product).all()
    return new_products

#get product by id
@router.get("/{id}",response_model=schemas.ProductResponse,status_code=200)
def get_product(id:int,db:session=Depends(get_db)):
    new_product=db.query(models.Product).filter(models.Product.id==id).first()
    if not new_product:
        raise HTTPException(404,detail="the product is not found")
    return new_product

@router.delete("/{id}",response_model=schemas.ProductResponse,status_code=200)
def get_product(id:int,db:session=Depends(get_db)):
    product=db.query(models.Product).filter(models.Product.id==id).first()
    if not product:
        raise HTTPException(404,detail="the product is not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}

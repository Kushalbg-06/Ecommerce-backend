from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from ..database import get_db
from .. import models,schemas,database
from typing import List

router=APIRouter(
   prefix="/cart",
   tags=["Carts"] 
)

@router.post('/add',response_model=schemas.CartResponse,status_code=status.HTTP_201_CREATED)
def additem_cart(item:schemas.CratCreate,db:session=Depends(get_db)):
    new_item=db.query(models.Product).filter(models.Product.id==item.product_id).first()
    if not new_item:
        raise HTTPException(404,detail="product not found")
    new_item=models.Cart(
        user_id=1,
        product_id=item.product_id,
        quantity=item.quantity
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/",response_model=List[schemas.CartResponse],status_code=status.HTTP_200_OK)
def get_all(db:session=Depends(get_db)):
    items=db.query(models.Cart).filter(models.Cart.user_id==1).all()
    return items

@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_items(id:int,db:session=Depends(get_db)):
    cart_items=db.query(models.Cart).filter(models.Cart.id==id).first()
    if not cart_items:
        raise HTTPException(404,detail="cart items not found")
    db.delete(cart_items)
    db.commit()
    return {"message":"cart item is Removed Succesfully"}

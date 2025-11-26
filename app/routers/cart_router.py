from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from ..database import get_db
from .. import models,schemas,database

router=APIRouter(
   prefix="/cart",
   tags=["Carts"] 
)

@router.post('/',response_model=schemas.CartResponse,status_code=status.HTTP_201_CREATED)
def additem_cart(item:schemas.CratCreate,db:session=Depends(get_db)):
    new_item=db.query(models.Cart).filter(models.Cart.id==item.product_id).first()
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


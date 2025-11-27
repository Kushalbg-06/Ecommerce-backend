from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from ..database import get_db
from .. import models,schemas,database

router=APIRouter(
    prefix="/order",
    tags=["Order"]
)

@router.post("/place",response_model=schemas.OrderResponse)
def place_order(db:session=Depends(get_db)):
        cart_items=db.query(models.Cart).filter(models.Cart.user_id==1).all()
        if not cart_items:
                raise HTTPException(404,detail="cart not found")
        total=0
        for items in cart_items:
                total +=items.quantity*items.product.price
        order=models.Order(
                user_id=1,
                total_amount=total
        )
        db.add(order)
        db.commit()
        db.refresh(order)
        
        for item in cart_items:
                order_item=models.OrderItem(
                        order_id = order.id,
                        product_id=item.product_id,
                        quantity=item.quantity,
                        price=item.product.price
                )
                db.add(order_item)

                for i in cart_items:
                        db.delete(i)
        db.commit()
        db.refresh(order)
        return order
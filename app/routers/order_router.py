from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])


# PLACE ORDER
@router.post("/place", response_model=schemas.OrderResponse)
def place_order(db: Session = Depends(get_db)):
    cart_items = db.query(models.Cart).filter(models.Cart.user_id == 1).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")
    total = sum(i.quantity * i.product.price for i in cart_items)
    order = models.Order(user_id=1, total_amount=total)
    db.add(order)
    db.commit()
    db.refresh(order)
    # Add order items
    for item in cart_items:
        order_item = models.OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )
        db.add(order_item)
    # Clear cart
    for item in cart_items:
        db.delete(item)
    db.commit()
    return order


# GET ALL ORDERS
@router.get("/", response_model=list[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

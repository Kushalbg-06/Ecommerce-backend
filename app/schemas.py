from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

    model_config = {
        "from_attributes": True
    }

class ProductCreate(BaseModel):
    name:str
    price:float
    stock:int
    discription:str

class ProductResponse(BaseModel):
    id:int
    name:str
    price:float
    stock:int
    discription:Optional[str]

    model_config = {
        "from_attributes": True
    }

class CratCreate(BaseModel):
    product_id:int
    quantity:int

class CartResponse(BaseModel):
    id:int
    user_id:int
    product_id:int
    quantity:int

    model_config = {
        "from_attributes": True
    }

class OrderItemResponse(BaseModel):
    id:int
    product_id:int
    quantity:int
    price:float

    model_config = {
        "from_attributes": True
    }
class OrderResponse(BaseModel):
    id:int
    total_amount:float
    create_at:datetime
    items:List[OrderItemResponse]

    model_config = {
        "from_attributes": True
    }    
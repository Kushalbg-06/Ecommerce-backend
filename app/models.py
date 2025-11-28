from sqlalchemy import Column,Integer,Float,ForeignKey,DateTime,String
from datetime import datetime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
     __tablename__="users"
     id=Column(Integer,primary_key=True,index=True)
     name=Column(String,nullable=False)
     email=Column(String,unique=True,nullable=False)
     password=Column(String,nullable=False)
     #relationship
     cart=relationship("Cart",back_populates="user")
     order=relationship("Order",back_populates="user")

class Product(Base):
     __tablename__="products"
     id=Column(Integer,primary_key=True,index=True)
     name=Column(String)
     price=Column(Float)
     stock=Column(Integer)
     discription=Column(String)
     #relationship
     cart=relationship("Cart",back_populates="product")
     order_items=relationship("OrderItem",back_populates="product")

class Cart(Base):
     __tablename__="carts"
     id=Column(Integer,primary_key=True,index=True)
     user_id=Column(Integer,ForeignKey("users.id"))
     product_id=Column(Integer,ForeignKey("products.id"))
     quantity=Column(Integer,default=1)
     #relationship
     user=relationship("User",back_populates="cart")
     product=relationship("Product",back_populates="cart")


class Order(Base):
     __tablename__="orders"
     id=Column(Integer,primary_key=True,index=True)
     user_id=Column(Integer,ForeignKey("users.id"))
     total_amount=Column(Float)
     create_at=Column(DateTime,default=datetime.utcnow)
     #relationship
     user=relationship("User",back_populates="order")
     items=relationship("OrderItem",back_populates="order")



class OrderItem(Base):
     __tablename__="orderitem"
     id=Column(Integer,primary_key=True,index=True)
     order_id = Column(Integer, ForeignKey("orders.id"))
     product_id = Column(Integer, ForeignKey("products.id"))
     quantity = Column(Integer, default=1)
     price = Column(Float)
     #relationship
     order=relationship("Order",back_populates="items")
     product=relationship("Product",back_populates="order_items")
from sqlalchemy import Column,Integer,Float,ForeignKey,DateTime,String
from datetime import datetime
from sqlalchemy.orm import relationship
from .database import Base

class user(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)

class product(Base):
     __tablename__="products"
     id=Column(Integer,primary_key=True,index=True)
     name=Column(String)
     price=Column(Float)
     stock=Column(Integer)
     discription=Column(String)

class cart(Base):
     __tablename__="carts"
     id=Column(Integer,primary_key=True,index=True)
     user_id=Column(Integer,ForeignKey("users.id"))
     product_id=Column(Integer,ForeignKey("products.id"))
     quantity=Column(Integer,default=1)


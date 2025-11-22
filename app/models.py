from sqlalchemy import  Column, Integer, String,Boolean
from sqlalchemy.orm import relationship
from .database import Base

class product(Base):
     __tablename__ = "products" 
    
     id=Column(Integer,primary_key=True,index=True)

     name = Column(String)
     price=Column(Integer,nullable=False)
     discription =Column(String)
     is_stock=Column(Boolean,default=True)
    
class user(Base):
     __tablename__="users"
     id=Column(Integer,primary_key=True,index=True)
     name=Column(String)
     email=Column(String)
     password=Column(String)

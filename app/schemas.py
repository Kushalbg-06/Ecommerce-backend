from pydantic import BaseModel

class productcreate(BaseModel):
    name:str
    price:int
    discription:str
    is_stock:bool=True

class productout(BaseModel):
    id:int
    name:str
    price:int
    discription:str
    is_stock:bool

    class Config:
        from_attributes = True
class user(BaseModel):
    name:str
    email:str
    password:str

class showuser(BaseModel):
     id:int
     name:str
     email:str
     password:str

     class Config:
         from_attributes=True

class login(BaseModel):
    username:str
    password:str

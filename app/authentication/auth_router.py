from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,hashing
from . import token
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post('/register',response_model=schemas.UserResponse)
def register(request:schemas.UserCreate,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.email).first()
    if user:
        raise HTTPException(404,detail="email is already register")
    
    hash_pwd=hashing.hash_password(request.password)
    new_user=models.User(
        name=request.name,
        email=request.email,
        password=hash_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post('/login',response_model=schemas.Token)
def login(request:schemas.Login,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.email).first()
    if not user:
        raise HTTPException(404,detail="invalid email")
   
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(404,detail="invalid password")
     
    access_token = token.create_access_token(data={"sub": str(user.id)}) 
    return {"access_token": access_token, "token_type": "bearer"}





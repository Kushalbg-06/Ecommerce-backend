from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from ..database import get_db
from .. import models,schemas,database

router=APIRouter(
    prefix="/user",
    tags=["Users"]
)
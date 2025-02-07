from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.user as UserCrud
import config.db
from schemas.user import User, UserCreate
import models.user
from typing import List

user = APIRouter()

def get_db():
    db = config.db.SesionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get('/users/', response_model=List[User], tags=['Usuarios'])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users = UserCrud.get_users(db = db, skip = skip, limit = limit)
    return db_users

@user.get("/users/{user_id}", response_model=User, tags=["Usuarios"])
async def get_user(user_id: str, db: Session = Depends(get_db)):
    user = UserCrud.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@user.post("/usersCreate/", response_model=User, tags=["Usuarios"])
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #existing_user = User.get_user_by_id(db=db, correoElectronico=user.correoElectronico)
    #if existing_user:
        #raise HTTPException(status_code=400, detail="El usuario ya existe")    
    new_user = UserCrud.create_user(db=db, user=user)
    return new_user
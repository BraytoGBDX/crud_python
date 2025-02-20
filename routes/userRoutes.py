from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.user as UserCrud
import config.db
from schemas.user import User, UserCreate, UserUpdate, UserLogin, Token
import models.user
from typing import List

from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer



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
    new_user = UserCrud.create_user(db=db, user=user)
    return new_user

@user.put("/usersUpdate/{user_id}", response_model=User, tags=["Usuarios"])
async def update_user(user_id: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = UserCrud.update_user(db=db, user_id=user_id, user=user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o no se pudo actualizar")
    return updated_user

@user.delete("/usersDelete/{user_id}", tags=["Usuarios"])
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    deleted = UserCrud.delete_user(db=db, user_id=user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o no se pudo eliminar")
    return {"message": "Prestamo eliminado correctamente"}


SECRET_KEY = "secret_key_123"  # Cambia esto por una clave segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@user.post("/users/login", response_model=Token, tags=["Usuarios"])
async def login_for_access_token(user: UserLogin, db: Session = Depends(get_db)):
    user_db = UserCrud.get_user_by_email(db, email=user.correoElectronico)
    if not user_db or user_db.contrasena != user.contrasena:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    access_token = create_access_token(data={"sub": user_db.correoElectronico})
    print("Token generado:", access_token)
    return {"message": "Bienvenido al sistema"}



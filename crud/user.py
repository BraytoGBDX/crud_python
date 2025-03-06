from models.user import User as UserModel
from schemas.user import User, UserCreate, UserUpdate
from sqlalchemy.orm import Session
from datetime import datetime

def get_users(db: Session, skip: int = 0, limit: int =0):
    return db.query(UserModel).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: str):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        tipoUsuario=user.tipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,  
        numeroTelefono=user.numeroTelefono,
        estatus=user.estatus
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = get_user_by_id(db,user_id)
    if db_user is None:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: str):
    db_user = get_user_by_id(db, user_id)
    if db_user is None:
        return False
    db.delete(db_user)
    db.commit()
    return True

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.correoElectronico == email).first()
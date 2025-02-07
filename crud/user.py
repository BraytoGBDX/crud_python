from models.user import User as UserModel
from schemas.user import User, UserCreate
from sqlalchemy.orm import Session
from datetime import datetime

def get_users(db: Session, skip: int = 0, limit: int =0):
    return db.query(UserModel).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: str):
    return db.query(UserModel).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        tipoUsuario=user.tipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,  # Considera encriptar la contraseña antes de guardarla
        numeroTelefono=user.numeroTelefono,
        estatus=user.estatus,
        fechaRegistro=user.fechaRegistro or datetime.utcnow(),  # Asigna la fecha actual si no se pasa
        fechaActualizacion=user.fechaActualizacion or datetime.utcnow(),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
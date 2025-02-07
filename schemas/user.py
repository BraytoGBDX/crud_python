from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: str
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: str
    fechaRegistro: Optional[datetime] = None
    fechaActualizacion: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass
    

        
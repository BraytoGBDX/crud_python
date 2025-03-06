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
    
    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    nombre: Optional[str] = None
    primerApellido: Optional[str] = None
    segundoApellido: Optional[str] = None
    tipoUsuario: Optional[str] = None
    nombreUsuario: Optional[str] = None
    correoElectronico: Optional[str] = None
    contrasena: Optional[str] = None
    numeroTelefono: Optional[str] = None
    estatus: Optional[str] = None
    class Config:
        from_attributes = True

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass
    

class UserLogin(BaseModel):
    correoElectronico: str
    contrasena: str

class Token(BaseModel):
    access_token: str
    token_type: str
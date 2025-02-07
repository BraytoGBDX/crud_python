from pydantic import BaseModel
from datetime import datetime
from models.materiales import EstadoMaterial
from typing import Optional

class MaterialBase(BaseModel):
    tipo_material: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    estado: EstadoMaterial

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    cantidad: Optional[int] = None

class Material(MaterialBase):
    id: int
    fechaRegistro: Optional[datetime] = None
    fechaActualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True

from pydantic import BaseModel
from datetime import datetime
from models.materiales import EstadoMaterial
from typing import Optional

class MaterialBase(BaseModel):
    tipo_material: str
    marca: Optional[str]
    modelo: Optional[str]
    estado: EstadoMaterial

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    nombre: Optional[str]
    descripcion: Optional[str]
    cantidad: Optional[int]

class Material(MaterialBase):
    id: int
    fechaRegistro: datetime
    fechaActualizacion: datetime

    class Config:
        from_attributes = True

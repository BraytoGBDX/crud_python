from pydantic import BaseModel
from datetime import datetime
from models.prestamos import Prestamo
from typing import Optional

class PrestamoBase(BaseModel):
    id_material: int
    id_usuario: int
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime]
    estado_prestamo: str  

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(PrestamoBase):
    id_material: Optional[int]
    id_usuario: Optional[int]
    fecha_prestamo: Optional[datetime]
    fecha_devolucion: Optional[datetime]
    estado_prestamo: Optional[str]

class Prestamo(PrestamoBase):
    id: int

    class Config:
        from_attributes = True

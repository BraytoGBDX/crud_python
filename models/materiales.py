from sqlalchemy import Column, Integer, String, Enum, DateTime
from config.db import Base
from sqlalchemy.orm import relationship
import enum

class TipoMaterial(str, enum.Enum):
    Proyector = "Proyector"
    Extencion = "Extencion"
    Computadora = "Computadora"
    HDMI = "HDMI"

class EstadoMaterial(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    En_Mantenimiento = "En Mantenimiento"
    Otro = "Otro"

class Material(Base):
    __tablename__ = "tbb_material"

    id_material = Column(Integer, primary_key=True, autoincrement=True)
    tipo_material = Column(Enum(TipoMaterial), nullable=False)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    estado = Column(Enum(EstadoMaterial), nullable=False)

    prestamos = relationship("Prestamo", back_populates="material")
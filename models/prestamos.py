from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class EstadoPrestamo(str, enum.Enum):
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    __tablename__ = "tbb_prestamo"
    
    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    id_material = Column(Integer, ForeignKey("tbb_material.id_material"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("tbb_usuario.id"), nullable=False)
    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)  
    estado_prestamo = Column(Enum(EstadoPrestamo), nullable=False)
    material = relationship("Material", back_populates="prestamos")
    usuario = relationship("User", back_populates="prestamos")

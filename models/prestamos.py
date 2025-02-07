from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class EstadoPrestamo(str, enum.Enum):
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    __tablename__ = "tbb_prestamo"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_material = Column(Integer)
    id_usuario = Column(Integer)

    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)  
    estado_prestamo = Column(Enum(EstadoPrestamo), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_material'], ['tbb_material.id']),
        ForeignKeyConstraint(['id_usuario'], ['tbb_usuarios.id']),
    )

    material = relationship("Material", back_populates="prestamo")
    usuario = relationship("User", back_populates="prestamo")

from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
from sqlalchemy.orm import relationship


import enum

class TipoUsuario(str, enum.Enum):
	Alumno = "Alumno"
	Profesor = "Profesor"
	Secretaria = "Secretaria"
	Laboratorista = "Laboratorista"
	Directivo = "Directivo"
	Administratvo = "Administrativo"

class Estatus(str, enum.Enum):
	Activo = "Activo"
	Inactivo = "Inactivo"
	Bloqueado = "Bloqueado"
	Suspendido = "Suspendido"

class User(Base):
    __tablename__ = "tbb_usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primerApellido = Column(String(60))
    segundoApellido = Column(String(60))
    tipoUsuario = Column(Enum(TipoUsuario))
    nombreUsuario = Column(String(60))
    correoElectronico = Column(String(100))
    contrasena = Column(String(60))
    numeroTelefono = Column(String(20))
    estatus = Column(Enum(Estatus))
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)
    prestamo = relationship("Prestamo", back_populates="usuario")
    

import models.prestamos
import schemas.prestamos
from sqlalchemy.orm import Session
from datetime import datetime

def get_prestamos(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.prestamos.Prestamo).offset(skip).limit(limit).all()

def get_prestamo(db: Session, id: int):
    return db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id == id).first()

def create_prestamo(db: Session, prestamo: schemas.prestamos.PrestamoCreate):
    db_prestamo = models.prestamos.Prestamo(
        id_material=prestamo.id_material,
        id_usuario=prestamo.id_usuario,
        fecha_prestamo=datetime.utcnow(),
        fecha_devolucion=prestamo.fecha_devolucion,
        estado_prestamo=prestamo.estado_prestamo
    )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db: Session, id: int, prestamo: schemas.prestamos.PrestamoUpdate):
    db_prestamo = db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id == id).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            setattr(db_prestamo, var, value) if value else None
            db.commit()
            db.refresh(db_prestamo)
        return db_prestamo

def delete_prestamo(db: Session, id: int):
    db_prestamo = db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id == id).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo

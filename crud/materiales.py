import models.materiales
import schemas.materiales
from sqlalchemy.orm import Session

def get_materials(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.materiales.Material).offset(skip).limit(limit).all()

def get_material(db: Session, id: int):
    return db.query(models.materiales.Material).filter(models.materiales.Material.id == id).first()

def create_material(db: Session, material: schemas.materiales.MaterialCreate):
    db_material = models.materiales.Material(
        tipo_material=material.tipo_material, 
        marca=material.marca,  
        modelo=material.modelo,  
        estado=material.estado,  

    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, id: int, material: schemas.materiales.MaterialUpdate):
    db_material = db.query(models.materiales.Material).filter(models.materiales.Material.id == id).first()
    if db_material:
        for var, value in vars(material).items():
            setattr(db_material, var, value) if value else None
            db.commit()
            db.refresh(db_material)
        return db_material

def delete_material(db: Session, id: int):
    db_material = db.query(models.materiales.Material).filter(models.materiales.Material.id == id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.materiales
import schemas.materiales
import models.materiales
from typing import List
from routes.userRoutes import verify_token_simple

material = APIRouter(dependencies=[Depends(verify_token_simple)])

models.materiales.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SesionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener materiales
@material.get("/materials/", response_model=List[schemas.materiales.Material], tags=["Materiales"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_materials = crud.materiales.get_materials(db=db, skip=skip, limit=limit)
    return db_materials

# Crear material
@material.post("/materialsCreate/", response_model=schemas.materiales.Material, tags=["Materiales"])
async def create_material(material: schemas.materiales.MaterialCreate, db: Session = Depends(get_db)):
    return crud.materiales.create_material(db=db, material=material)

# Ver un material por ID
@material.get("/materials/{id_material}", response_model=schemas.materiales.Material, tags=["Materiales"])
async def read_material(id_material: int, db: Session = Depends(get_db)):
    db_material = crud.materiales.get_material(db=db, id=id_material)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return db_material

# Actualizar material
@material.put("/materialsUpdate/{id_material}", response_model=schemas.materiales.Material, tags=["Materiales"])
async def update_material(id_material: int, material: schemas.materiales.MaterialUpdate, db: Session = Depends(get_db)):
    db_material = crud.materiales.update_material(db=db, id=id_material, material=material)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no existente, no actualizado")
    return db_material

# Eliminar material
@material.delete("/materialsDelete/{id_material}", tags=["Materiales"])
async def delete_material(id_material: int, db: Session = Depends(get_db)):
    db_material = crud.materiales.delete_material(db=db, id=id_material)
    if not db_material:
        raise HTTPException(status_code=400, detail="Material no existente, no eliminado")
    return {"message": "Prestamo eliminado correctamente"}


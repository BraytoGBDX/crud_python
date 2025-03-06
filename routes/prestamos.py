from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.prestamos
import schemas.prestamos
import models.prestamos
from typing import List
from routes.userRoutes import verify_token_simple

prestamo = APIRouter(dependencies=[Depends(verify_token_simple)]) 


models.prestamos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SesionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener préstamos
@prestamo.get("/prestamos/", response_model=List[schemas.prestamos.Prestamo], tags=["Préstamos"])
async def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_prestamos = crud.prestamos.get_prestamos(db=db, skip=skip, limit=limit)
    return db_prestamos

# Crear préstamo
@prestamo.post("/prestamosCreate/", response_model=schemas.prestamos.Prestamo, tags=["Préstamos"])
async def create_prestamo(prestamo: schemas.prestamos.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.prestamos.create_prestamo(db=db, prestamo=prestamo)

# Ver un préstamo por ID
@prestamo.get("/prestamos/{id_prestamo}", response_model=schemas.prestamos.Prestamo, tags=["Préstamos"])
async def read_prestamo(id_prestamo: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id_prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return db_prestamo

# Actualizar préstamo
@prestamo.put("/prestamosUpdate/{id_prestamo}", response_model=schemas.prestamos.Prestamo, tags=["Préstamos"])
async def update_prestamo(id_prestamo: int, prestamo: schemas.prestamos.PrestamoUpdate, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.update_prestamo(db=db, id=id_prestamo, prestamo=prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Préstamo no existente, no actualizado")
    return db_prestamo

# Eliminar préstamo
@prestamo.delete("/prestamosDelete/{id_prestamo}", tags=["Préstamos"])
async def delete_prestamo(id_prestamo: str, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.delete_prestamo(db=db, id=id_prestamo)
    if not db_prestamo:
        raise HTTPException(status_code=400, detail="Préstamo no existente, no eliminado")
    return {"message": "Prestamo eliminado correctamente"}

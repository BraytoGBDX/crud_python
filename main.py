from fastapi import FastAPI
from routes.userRoutes import user
from routes.prestamos import prestamo
from routes.materiales import material


app = FastAPI(
    title="Example S.A de C.V",
    description="API de prueba para almacenar usuarios"
)

app.include_router(user)
app.include_router(prestamo)
app.include_router(material)

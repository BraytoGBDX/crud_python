from fastapi import FastAPI
from routes.userRoutes import user
from routes.prestamos import prestamo
from routes.materiales import material
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Example S.A de C.V",
    description="API de prueba para almacenar usuarios"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(prestamo)
app.include_router(material)

from fastapi import FastAPI
from routes.userRoutes import user

app = FastAPI(
    tittle="Example S.A de C.V",
    description="api de prueba para amacenar usuarios"
)

app.include_router(user)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.interfaces.controllers.order_controller import router

app = FastAPI(
    title="Exercie number #2",
    description="Implementa un endpoint en python para obtener el estado de la orden",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Origen permitido (tu frontend)
    allow_credentials=True,  # Permitir envío de cookies o credenciales
    allow_methods=["*"],  # Métodos HTTP permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Encabezados permitidos (Content-Type, etc.)
)

app.include_router(router)
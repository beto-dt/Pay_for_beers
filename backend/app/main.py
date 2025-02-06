from fastapi import FastAPI
from backend.app.interfaces.controllers.order_controller import router

app = FastAPI(
    title="Exercie number #2",
    description="Implementa un endpoint en python para obtener el estado de la orden",
    version="1.0.0",
)

app.include_router(router)
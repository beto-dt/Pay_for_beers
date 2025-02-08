from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.interfaces.controllers.order_controller import router

app = FastAPI(
    title="Exercie number #2",
    description="Exercie number #2",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
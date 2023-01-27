from fastapi import FastAPI
from src.routers import rota


app = FastAPI()

app.include_router(router=rota.router)

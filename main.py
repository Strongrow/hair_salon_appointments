import sys
from app.src.Logica import Logica 
from fastapi import FastAPI
from app.routers.peluqueros import router as router_peluqueros
from app.routers.clientes import router as router_clientes

app = FastAPI()

app.include_router(router_peluqueros, prefix="/peluqueros")
app.include_router(router_clientes, prefix="/clientes")
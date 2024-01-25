import sys
from app.src.Logica import Logica 
from fastapi import FastAPI
from app.routers.peluqueros import router as router_peluqueros
from app.routers.clientes import router as router_clientes
from app.routers.citas import router as router_citas
from app.routers.servicios import router as router_servicios

app = FastAPI()

app.include_router(router_peluqueros, prefix="/peluqueros")
app.include_router(router_clientes, prefix="/clientes")
app.include_router(router_citas, prefix="/citas")
app.include_router(router_servicios, prefix="/servicios")
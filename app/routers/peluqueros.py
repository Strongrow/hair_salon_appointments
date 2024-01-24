from fastapi import APIRouter
from app.src.Logica import Logica
from app.model.models import Peluquero
from typing import Optional

router = APIRouter()
logica = Logica()

@router.get("/")
def get_peluqueros():
    return logica.dar_peluqueros()

@router.post("/")
def crear_peluquero(peluquero: Peluquero):
    return logica.crear_peluquero(peluquero.nombre, peluquero.apellido)

@router.get("/{peluquero_id}")
def get_peluquero(peluquero_id: int):
    return logica.dar_peluquero(peluquero_id)

@router.put("/{peluquero_id}")
def actualizar_peluquero(peluquero_id: int,  peluquero: Peluquero):
    return logica.actualizar_peluquero(peluquero_id, peluquero.nombre, peluquero.apellido)

@router.delete("/{peluquero_id}")
def eliminar_peluquero(peluquero_id: int):
    return logica.eliminar_peluquero(peluquero_id)
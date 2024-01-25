from fastapi import APIRouter
from app.src.peluquero import LogicaPeluquero
from app.model.models import Peluquero

router = APIRouter()
peluqueros = LogicaPeluquero()

@router.get("/")
def get_peluqueros():
    return peluqueros.dar_peluqueros()

@router.post("/")
def crear_peluquero(peluquero: Peluquero):
    return peluqueros.crear_peluquero(peluquero.nombre, peluquero.apellido)

@router.get("/{peluquero_id}")
def get_peluquero(peluquero_id: int):
    return peluqueros.dar_peluquero(peluquero_id)

@router.put("/{peluquero_id}")
def actualizar_peluquero(peluquero_id: int,  peluquero: Peluquero):
    return peluqueros.actualizar_peluquero(peluquero_id, peluquero.nombre, peluquero.apellido)

@router.delete("/{peluquero_id}")
def eliminar_peluquero(peluquero_id: int):
    return peluqueros.eliminar_peluquero(peluquero_id)
from fastapi import APIRouter, HTTPException, Depends
from app.src.servicio import LogicaServicios
from app.model.models import Servicio


router = APIRouter()
servicios = LogicaServicios()

@router.get("/")
def get_servicios():
    return servicios.dar_servicios()

@router.post("/")
def crear_servicio(servicio: Servicio):
    try:
        return servicios.crear_servicio(servicio.descripcion, servicio.duracion, servicio.costo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{servicio_id}")
def get_servicio(servicio_id: int):
    return servicios.dar_servicio(servicio_id)

@router.put("/{servicio_id}")
def actualizar_servicio(servicio_id: int, servicio: Servicio):
        try:
            return servicios.actualizar_servicio(servicio_id, servicio.descripcion, servicio.duracion, servicio.costo)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int):
    return servicios.eliminar_servicio(servicio_id)
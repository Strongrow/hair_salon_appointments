from fastapi import APIRouter, HTTPException, Depends
from app.src.Logica import Logica
from app.model.models import Servicio


router = APIRouter()
logica = Logica()

@router.get("/")
def get_servicios():
    return logica.dar_servicios()

@router.post("/")
def crear_servicio(servicio: Servicio):
    try:
        return logica.crear_servicio(servicio.descripcion, servicio.duracion, servicio.costo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{servicio_id}")
def get_servicio(servicio_id: int):
    return logica.dar_servicio(servicio_id)

@router.put("/{servicio_id}")
def actualizar_servicio(servicio_id: int, servicio: Servicio):
        try:
            return logica.actualizar_servicio(servicio_id, servicio.descripcion, servicio.duracion, servicio.costo)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int):
    return logica.eliminar_servicio(servicio_id)
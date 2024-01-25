from fastapi import APIRouter, HTTPException, Depends
from app.src.Logica import Logica
from app.model.models import CitaBase


router = APIRouter()
logica = Logica()

@router.get("/")
def get_citas():
    return logica.dar_citas()

@router.post("/")
def crear_cita(cita: CitaBase):
    try:
        return logica.crear_cita(fecha_inicio=cita.fecha_inicio,peluquero_id=cita.peluquero_id, cliente_id=cita.cliente_id, servicio_id=cita.servicio_id, estado=cita.estado)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{cita_id}")
def get_cita(cita_id: int):
    return logica.dar_cita(cita_id)

@router.put("/{cita_id}")
def actualizar_cita(cita_id: int, cita: CitaBase):
        try:
            return logica.actualizar_cita(cita_id, cita.peluquero_id, cita.cliente_id, cita.fecha_inicio, cita.fecha_fin, cita.duracion, cita.estado)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cita_id}")
def eliminar_cita(cita_id: int):
    return logica.eliminar_cita(cita_id)
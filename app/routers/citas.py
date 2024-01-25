from fastapi import APIRouter, HTTPException, Depends
from app.model.models import CitaBase
from app.src.citas import LogicaCitas


router = APIRouter()
citas = LogicaCitas()

@router.get("/")
def get_citas():
    return citas.dar_citas()

@router.post("/")
def crear_cita(cita: CitaBase):
    try:
        return citas.crear_cita(fecha_inicio=cita.fecha_inicio,peluquero_id=cita.peluquero_id, cliente_id=cita.cliente_id, servicio_id=cita.servicio_id, estado=cita.estado)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{cita_id}")
def get_cita(cita_id: int):
    return citas.dar_cita(cita_id)

@router.put("/{cita_id}")
def actualizar_cita(cita_id: int, cita: CitaBase):
        try:
            return citas.actualizar_cita(cita_id, cita.peluquero_id, cita.cliente_id, cita.fecha_inicio, cita.fecha_fin, cita.duracion, cita.estado)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.put("/{cita_id}/estado")
def actualizar_estado_cita(cita_id: int, cita: CitaBase):
        try:
            return citas.actualizar_estado_cita(cita_id, cita.estado)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cita_id}")
def eliminar_cita(cita_id: int):
    return citas.eliminar_cita(cita_id)
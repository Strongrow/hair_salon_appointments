from fastapi import APIRouter, HTTPException
from app.src.Logica import Logica
from app.model.models import Cliente

router = APIRouter()
logica = Logica()

@router.get("/")
def get_clientes():
    return logica.dar_clientes()

@router.post("/")
def crear_cliente(cliente: Cliente):
    try:
        return logica.crear_cliente(cliente.nombre, cliente.apellido, cliente.telefono, cliente.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{cliente_id}")
def get_cliente(cliente_id: int):
    return logica.dar_cliente(cliente_id)

@router.put("/{cliente_id}")
def actualizar_cliente(cliente_id: int, cliente: Cliente):
        try:
            return logica.actualizar_cliente(cliente_id, cliente.nombre, cliente.apellido, cliente.telefono, cliente.email)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    return logica.eliminar_cliente(cliente_id)
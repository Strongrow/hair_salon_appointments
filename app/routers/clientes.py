from fastapi import APIRouter, HTTPException
from app.model.models import Cliente
from app.src.cliente import LogicaCliente

router = APIRouter()
clientes= LogicaCliente()

@router.get("/")
def get_clientes():
    return clientes.dar_clientes()

@router.post("/")
def crear_cliente(cliente: Cliente):
    try:
        return clientes.crear_cliente(cliente.nombre, cliente.apellido, cliente.telefono, cliente.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{cliente_id}")
def get_cliente(cliente_id: int):
    return clientes.dar_cliente(cliente_id)

@router.put("/{cliente_id}")
def actualizar_cliente(cliente_id: int, cliente: Cliente):
        try:
            return clientes.actualizar_cliente(cliente_id, cliente.nombre, cliente.apellido, cliente.telefono, cliente.email)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    return clientes.eliminar_cliente(cliente_id)
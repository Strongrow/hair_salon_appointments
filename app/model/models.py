from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cliente(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[int] = None
    email: Optional[str] = None

class Peluquero(BaseModel):
    nombre: str
    apellido: str

class Servicio(BaseModel):
    nombre: str
    descripcion: str
    costo: float

class Cita(BaseModel):
    cliente_id: int
    peluquero_id: int
    servicio_id: int
    fecha_hora: datetime

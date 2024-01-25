from pydantic import BaseModel
from typing import Optional
from datetime import datetime, time
from enum import Enum

class Cliente(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[int] = None
    email: Optional[str] = None

class Peluquero(BaseModel):
    nombre:Optional[str] = None
    apellido: Optional[str] = None

class Servicio(BaseModel):
    descripcion: Optional[str] = None
    duracion: Optional[time] = None
    costo: Optional[float] = None

class EstadoCita(Enum):
    APARTADA: str = "apartada"
    CONFIRMADA: str = "confirmada"
    EN_PROGRESO: str = "en progreso"
    FINALIZADA: str = "finalizada"
    CANCELADA: str = "cancelada"

class CitaBase(BaseModel):
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    duracion: Optional[time] = None
    peluquero_id: Optional[int] = None
    cliente_id: Optional[int] = None
    servicio_id: Optional[int] = None
    estado: Optional[str] = EstadoCita.APARTADA.value

    class Config:
        orm_mode = True

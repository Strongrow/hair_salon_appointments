from sqlalchemy import Column, Integer, DateTime, ForeignKey, Time, String
from sqlalchemy.orm import relationship
from app.dataBase.declarative_base import Base

class Cita(Base):
    __tablename__ = 'citas'

    ESTADOS_POSIBLES = ["apartada","confirmada", "en progreso", "finalizada", "cancelada"]


    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    duracion = Column(Time, nullable=False)
    peluquero_id = Column(Integer, ForeignKey('peluqueros.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    servicio_id = Column(Integer, ForeignKey('servicios.id'), nullable=False)
    estado = Column(String, default="apartada")
    peluquero = relationship("Peluquero", back_populates="cita")
    cliente = relationship("Cliente", back_populates="cita")
    servicio = relationship("Servicio", back_populates="cita")
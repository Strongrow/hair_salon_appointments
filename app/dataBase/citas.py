from sqlalchemy import Column, Integer, DateTime, ForeignKey, Time, String
from app.dataBase.declarative_base import Base

# Definimos la clase Cita que hereda de Base
class Cita(Base):
    # Especificamos el nombre de la tabla en la base de datos
    __tablename__ = 'citas'
    # Definimos los posibles estados de una cita
    ESTADOS_POSIBLES = ["apartada","confirmada", "en progreso", "finalizada", "cancelada"]

    
    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    duracion = Column(Time, nullable=False)
    peluquero_id = Column(Integer, ForeignKey('peluqueros.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    servicio_id = Column(Integer, ForeignKey('servicios.id'), nullable=False)
    estado = Column(String, default="apartada")

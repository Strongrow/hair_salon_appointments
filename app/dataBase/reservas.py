from sqlalchemy import Column, Integer, String, CheckConstraint,DateTime
from .declarative_base import Base

class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_peluquero = Column(String(50), nullable=False)
    nombre_cliente = Column(String(50), nullable=False)
    id_servicio = Column(Integer, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)

    __table_args__ = (
        CheckConstraint ('fecha_fin >= fecha_inicio' ,name='check_fecha_fin_inicio'),
    )


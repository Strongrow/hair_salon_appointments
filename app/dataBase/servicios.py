from sqlalchemy import Column, Integer, String, Time, Float
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Servicio(Base):
    __tablename__ = 'servicios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(50), nullable=False)
    duracion = Column(Time(), nullable=False)
    costo = Column(Float, nullable=False)
    


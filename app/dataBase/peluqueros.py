from sqlalchemy import Column, Integer, String, CheckConstraint
from .declarative_base import Base
from sqlalchemy.orm import relationship


class Peluquero(Base):
    __tablename__ = 'peluqueros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)




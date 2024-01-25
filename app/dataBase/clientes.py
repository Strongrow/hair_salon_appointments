from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy_utils import EmailType
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    telefono = Column(Integer, nullable=False)
    email = Column(EmailType, nullable=False, unique=True)

    cita = relationship("Cita", back_populates="cliente")


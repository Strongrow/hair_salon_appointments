from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy_utils import EmailType
from .declarative_base import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    telefono = Column(Integer, nullable=False)
    email = Column(EmailType, nullable=False, unique=True)


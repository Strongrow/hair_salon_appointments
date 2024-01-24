from sqlalchemy import Column, Integer, String, CheckConstraint, Time
from .declarative_base import Base

class Servicio(Base):
    __tablename__ = 'servicios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    service = Column(String(50), nullable=False)
    duration = Column(Time(), nullable=False)
    price = Column(Integer, nullable=False)


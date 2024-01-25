
from app.dataBase.declarative_base import Session, engine, Base
from app.dataBase.peluqueros import Peluquero
from typing import Optional
from pydantic import ValidationError


class LogicaPeluquero():
    Base.metadata.create_all(engine)

    def crear_peluquero(self, nombre: str, apellido:str):
        if nombre is None or apellido is None:
            raise ValueError("Error: nombre y apellido son requeridos para crear un peluquero")
        try:
            with Session() as session:
                peluquero = Peluquero(nombre=nombre, apellido=apellido)
                session.add(peluquero)
                session.commit()
                peluquero_copy = Peluquero(nombre=peluquero.nombre, apellido=peluquero.apellido)
                return peluquero
        except ValidationError as e:
            raise ValueError(f"Error al crear peluquero: {e}")
        
    def dar_peluqueros(self):
        with Session() as session:
            return session.query(Peluquero).all()

    def dar_peluquero(self, peluquero_id: int):
        with Session() as session:
            return session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
    
    def dar_ids_peluqueros(self):
        with Session() as session:
            return [peluquero.id for peluquero in session.query(Peluquero).all()]

    def actualizar_peluquero(self, peluquero_id: int, nombre: Optional[str] = None, apellido:Optional[str] = None):
        with Session() as session:
            peluquero = session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
            if peluquero is None:
                raise ValueError(f"No se encontró un peluquero con el id {peluquero_id}")
            if nombre is not None:
                peluquero.nombre = nombre
            if apellido is not None:
                peluquero.apellido = apellido
            session.commit()
        # Crear una copia del objeto peluquero con los atributos ya cargados
            peluquero_copy = Peluquero(id=peluquero.id, nombre=peluquero.nombre, apellido=peluquero.apellido)
    # Devolver la copia después de que la sesión se ha cerrado
        return peluquero_copy

    def eliminar_peluquero(self, peluquero_id: int):
        with Session() as session:
            peluquero = session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
            if peluquero is None:
                raise ValueError(f"No se encontró un peluquero con el id {peluquero_id}")
            session.delete(peluquero)
            session.commit()
            return {"message": "Peluquero eliminado con éxito"}

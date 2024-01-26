
from app.dataBase.declarative_base import Session, engine, Base
from app.dataBase.peluqueros import Peluquero
from typing import Optional
from pydantic import ValidationError


class LogicaPeluquero():
    # Creamos todas las tablas definidas en el modelo de datos
    Base.metadata.create_all(engine)

    # Método para crear un nuevo peluquero
    def crear_peluquero(self, nombre: str, apellido:str):
        # Verificamos que todos los parámetros requeridos estén presentes
        if nombre is None or apellido is None:
            raise ValueError("Error: nombre y apellido son requeridos para crear un peluquero")
        try:
            # Abrimos una nueva sesión de base de datos
            with Session() as session:
                # Creamos el nuevo peluquero
                peluquero = Peluquero(nombre=nombre, apellido=apellido)
                # Agregamos el nuevo peluquero a la sesión y hacemos commit
                session.add(peluquero)
                session.commit()
                # Devolvemos el nuevo peluquero
                peluquero_copy = Peluquero(nombre=peluquero.nombre, apellido=peluquero.apellido)
                return peluquero
        except ValidationError as e:
        # Manejamos cualquier error de validación
            raise ValueError(f"Error al crear peluquero: {e}")
    
    # Método para obtener todos los peluqueros
    def dar_peluqueros(self):
        with Session() as session:
            return session.query(Peluquero).all()

    # Método para obtener un peluquero específico
    def dar_peluquero(self, peluquero_id: int):
        with Session() as session:
            return session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
    
    # Método para obtener los ids de todos los peluqueros
    def dar_ids_peluqueros(self):
        with Session() as session:
            return [peluquero.id for peluquero in session.query(Peluquero).all()]

    # Método para actualizar un peluquero
    def actualizar_peluquero(self, peluquero_id: int, nombre: Optional[str] = None, apellido:Optional[str] = None):
        with Session() as session:
            # Obtenemos el peluquero a actualizar
            peluquero = session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
            if peluquero is None:
                raise ValueError(f"No se encontró un peluquero con el id {peluquero_id}")
            # Actualizamos los campos del peluquero
            if nombre is not None:
                peluquero.nombre = nombre
            if apellido is not None:
                peluquero.apellido = apellido
            
            # Hacemos commit de los cambios
            session.commit()
        # Crear una copia del objeto peluquero con los atributos ya cargados
            peluquero_copy = Peluquero(id=peluquero.id, nombre=peluquero.nombre, apellido=peluquero.apellido)
        # Devolver la copia después de que la sesión se ha cerrado
        return peluquero_copy

    # Método para eliminar un peluquero
    def eliminar_peluquero(self, peluquero_id: int):
        with Session() as session:
            # Obtenemos el peluquero a eliminar
            peluquero = session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
            if peluquero is None:
                raise ValueError(f"No se encontró un peluquero con el id {peluquero_id}")
            # Eliminamos el peluquero de la sesión y hacemos commit
            session.delete(peluquero)
            session.commit()
            # Devolvemos un mensaje de éxito
            return {"message": "Peluquero eliminado con éxito"}

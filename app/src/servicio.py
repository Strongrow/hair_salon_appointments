from app.dataBase.declarative_base import Session, engine, Base
from app.dataBase.servicios import Servicio
from datetime import time
from pydantic import ValidationError

class LogicaServicios():
    # Creamos todas las tablas definidas en el modelo de datos
    Base.metadata.create_all(engine)
    # Método para crear un nuevo servicio
    def crear_servicio(self, descripcion: str, duracion: time, costo: float):
        # Verificamos que todos los parámetros requeridos estén presentes
        if descripcion is None or duracion is None or costo is None:
            return "Error: nombre del servicio, duración del servicio y costo son requeridos para crear un servicio"
        try:
            # Abrimos una nueva sesión de base de datos
            with Session() as session:
                # Verificamos si el servicio ya existe
                servicio_existente = session.query(Servicio).filter(Servicio.descripcion == descripcion).first()
                if servicio_existente is not None:
                    raise ValueError("El servicio ya existe")
                # Creamos el nuevo servicio
                nuevo_servicio = Servicio(descripcion=descripcion, duracion=duracion, costo=costo)
                # Agregamos el nuevo servicio a la sesión y hacemos commit
                session.add(nuevo_servicio)
                session.commit()
                return nuevo_servicio
        except ValidationError as e:
            # Manejamos cualquier error de validación
            print(f"Error al crear servicio: {e}")
            return None
        
    # Método para obtener todos los servicios
    def dar_servicios(self):
        with Session() as session:
            return session.query(Servicio).all()
        
    # Método para obtener un servicio específico
    def dar_servicio(self, servicio_id: int):
        with Session() as session:
            return session.query(Servicio).filter(Servicio.id == servicio_id).first()

    # Método para actualizar un servicio
    def actualizar_servicio(self, servicio_id: int, descripcion: str = None, duracion: time = None, costo: float = None):
        with Session() as session:
            # Obtenemos el servicio a actualizar
            servicio_obj = session.query(Servicio).filter(Servicio.id == servicio_id).first()
            if servicio_obj is None:
                raise ValueError("Servicio no encontrado")
            # Actualizamos los campos del servicio
            if descripcion is not None:
                servicio_obj.descripcion = descripcion
            if duracion is not None:
                servicio_obj.duracion = duracion
            if costo is not None:
                servicio_obj.costo = costo
            session.commit()
            return servicio_obj

    # Método para eliminar un servicio
    def eliminar_servicio(self, servicio_id: int):
        with Session() as session:
            servicio = session.query(Servicio).filter(Servicio.id == servicio_id).first()
            session.delete(servicio)
            session.commit()
            return {"message": "Servicio eliminado con éxito"}

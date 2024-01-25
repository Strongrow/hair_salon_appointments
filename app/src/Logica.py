from app.dataBase.clientes import Cliente
from app.dataBase.declarative_base import Session, engine, Base
from app.dataBase.peluqueros import Peluquero
from typing import Optional
from app.dataBase.reservas import Reserva
from app.dataBase.servicios import Servicio
from app.dataBase.citas import Cita
from sqlalchemy import asc, Integer
from datetime import datetime, time, timedelta
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func , cast
from sqlalchemy.exc import IntegrityError
from .envioMail import enviar_email_confirmacion

class Logica():
    Base.metadata.create_all(engine)

    def crear_peluquero(self, nombre: str, apellido:str):
        with Session() as session:
            peluquero = Peluquero(nombre=nombre, apellido=apellido)
            session.add(peluquero)
            session.commit()
            peluquero_copy = Peluquero(nombre=peluquero.nombre, apellido=peluquero.apellido)
            return peluquero

    def dar_peluqueros(self):
        with Session() as session:
            return session.query(Peluquero).all()

    def dar_peluquero(self, peluquero_id: int):
        with Session() as session:
            return session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()

    def actualizar_peluquero(self, peluquero_id: int, nombre: Optional[str] = None, apellido:Optional[str] = None):
        with Session() as session:
            peluquero = session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
            if nombre is not None:
                peluquero.nombre = nombre
            if apellido is not None:
                peluquero.apellido = apellido
            session.commit()
            return peluquero

    def eliminar_peluquero(self, peluquero_id: int):
        with Session() as session:
            peluquero = session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
            session.delete(peluquero)
            session.commit()
            return {"message": "Peluquero eliminado con éxito"}

    def crear_cliente(self, nombre: str, apellido:str, telefono: int, email: str):
        with Session() as session:
            cliente_existente = session.query(Cliente).filter(Cliente.email == email).first()
            if cliente_existente is not None:
                raise ValueError("El email ya está en uso")
            cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            session.add(cliente)
            session.commit()
            return cliente

    def dar_clientes(self):
        with Session() as session:
            return session.query(Cliente).all()

    def dar_cliente(self, cliente_id: int):
        with Session() as session:
            return session.query(Cliente).filter(Cliente.id == cliente_id).first()

    def actualizar_cliente(self, cliente_id: int, nombre: str = None, apellido: str = None, telefono: int = None, email: str = None):
        with Session() as session:
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            if cliente is None:
                raise ValueError("Cliente no encontrado")
            if email is not None:
                cliente_existente = session.query(Cliente).filter(Cliente.email == email).first()
                if cliente_existente is not None:
                    raise ValueError("El email ya está en uso")
            if nombre is not None:
                cliente.nombre = nombre
            if apellido is not None:
                cliente.apellido = apellido
            if telefono is not None:
                cliente.telefono = telefono
            if email is not None:
                cliente.email = email
            session.commit()
            return cliente

    def eliminar_cliente(self, cliente_id: int):
        with Session() as session:
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            session.delete(cliente)
            session.commit()
            return {"message": "Cliente eliminado con éxito"}
    
    def crear_servicio(self, descripcion: str, duracion: time, costo: float):
        with Session() as session:
            servicio_existente = session.query(Servicio).filter(Servicio.descripcion == descripcion).first()
            if servicio_existente is not None:
                raise ValueError("El servicio ya existe")
            nuevo_servicio = Servicio(descripcion=descripcion, duracion=duracion, costo=costo)
            session.add(nuevo_servicio)
            session.commit()
            return nuevo_servicio

    def dar_servicios(self):
        with Session() as session:
            return session.query(Servicio).all()

    def dar_servicio(self, servicio_id: int):
        with Session() as session:
            return session.query(Servicio).filter(Servicio.id == servicio_id).first()

    def actualizar_servicio(self, servicio_id: int, descripcion: str = None, duracion: time = None, costo: float = None):
        with Session() as session:
            servicio_obj = session.query(Servicio).filter(Servicio.id == servicio_id).first()
            if servicio_obj is None:
                raise ValueError("Servicio no encontrado")
            if descripcion is not None:
                servicio_obj.descripcion = descripcion
            if duracion is not None:
                servicio_obj.duracion = duracion
            if costo is not None:
                servicio_obj.costo = costo
            session.commit()
            return servicio_obj

    def eliminar_servicio(self, servicio_id: int):
        with Session() as session:
            servicio = session.query(Servicio).filter(Servicio.id == servicio_id).first()
            session.delete(servicio)
            session.commit()
            return {"message": "Servicio eliminado con éxito"}

    def crear_cita(self, fecha_inicio: datetime, peluquero_id: int, cliente_id: int, servicio_id: int, estado: str = None):
        with Session() as session:
            try:
                # Buscar el servicio en la base de datos
                servicio = session.query(Servicio).get(servicio_id)
                if servicio is None:
                    return (f"Error: No se encontró el servicio con id {servicio_id}")

                # Calcular la fecha_fin a partir de la fecha_inicio y la duración del servicio
                duracion = timedelta(hours=servicio.duracion.hour, minutes=servicio.duracion.minute, seconds=servicio.duracion.second)
                fecha_fin = fecha_inicio + duracion

                # Verificar si el peluquero ya tiene una cita en el mismo horario
                cita_existente = session.query(Cita).filter(Cita.peluquero_id == peluquero_id, Cita.fecha_inicio < fecha_fin, Cita.fecha_fin > fecha_inicio).first()
                if cita_existente is not None:
                    return (f"Error: El peluquero ya tiene una cita en este horario")
            
                # Usar la duración del servicio al crear la cita
                nueva_cita = Cita(fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, duracion=servicio.duracion, peluquero_id=peluquero_id, cliente_id=cliente_id, servicio_id=servicio_id, estado=estado)
                session.add(nueva_cita)
                session.commit()

                enviar_email_confirmacion(nueva_cita)
                return nueva_cita
            except Exception as e:
            # Manejar el error de integridad de la base de datos
                return print(f"Error al crear cita: {e}")

    def dar_citas(self):
        with Session() as session:
            return session.query(Cita).all()

    def dar_cita(self, cita_id: int):
        with Session() as session:
            return session.query(Cita).filter(Cita.id == cita_id).first()

    def actualizar_cita(self, cita_id: int, fecha_inicio: datetime = None, fecha_fin: datetime = None, duracion: time = None, peluquero_id: int = None, cliente_id: int = None, servicio_id: int = None, estado: str = None):
        with Session() as session:
            cita_obj = session.query(Cita).filter(Cita.id == cita_id).first()
            if cita_obj is None:
                raise ValueError("Cita no encontrada")
            if fecha_inicio is not None:
                cita_obj.fecha_inicio = fecha_inicio
            if fecha_fin is not None:
                cita_obj.fecha_fin = fecha_fin
            if duracion is not None:
                cita_obj.duracion = duracion
            if peluquero_id is not None:
                peluquero_obj = session.query(Peluquero).filter(Peluquero.id == peluquero_id).first()
                if peluquero_obj is None:
                    raise ValueError("Peluquero no encontrado")
                cita_obj.peluquero_id = peluquero_id
            if cliente_id is not None:
                cliente_obj = session.query(Cliente).filter(Cliente.id == cliente_id).first()
                if cliente_obj is None:
                    raise ValueError("Cliente no encontrado")
                cita_obj.cliente_id = cliente_id
            if servicio_id is not None:
                servicio_obj = session.query(Servicio).filter(Servicio.id == servicio_id).first()
                if servicio_obj is None:
                    raise ValueError("Servicio no encontrado")
                cita_obj.servicio_id = servicio_id
            if estado is not None:
                if estado not in Cita.ESTADOS_POSIBLES:
                    raise ValueError("Estado no válido")
                cita_obj.estado = estado
            session.commit()
            return cita_obj

    def eliminar_cita(self, cita_id: int):
        with Session() as session:
            cita = session.query(Cita).filter(Cita.id == cita_id).first()
            session.delete(cita)
            session.commit()
            return {"message": "Cita eliminada con éxito"}
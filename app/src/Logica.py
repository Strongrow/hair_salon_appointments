from app.dataBase.clientes import Cliente
from app.dataBase.declarative_base import Session, engine, Base
from app.dataBase.peluqueros import Peluquero
from typing import Optional
from app.dataBase.reservas import Reserva
from app.dataBase.servicios import Servicio
from sqlalchemy import asc, Integer
from datetime import datetime, time
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func , cast
from sqlalchemy.exc import IntegrityError

class Logica():
    Base.metadata.create_all(engine)

    def crear_peluquero(self, nombre: str, apellido:str):
        with Session() as session:
            peluquero = Peluquero(nombre=nombre, apellido=apellido)
            session.add(peluquero)
            session.commit()
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

from app.dataBase.clientes import Cliente
from app.dataBase.declarative_base import Session, engine, Base
from app.dataBase.peluqueros import Peluquero
from app.dataBase.servicios import Servicio
from app.dataBase.citas import Cita
from datetime import datetime, time, timedelta
from .envioMail import enviar_email_confirmacion

class LogicaCitas():
    Base.metadata.create_all(engine)

    def crear_cita(self, fecha_inicio: datetime, peluquero_id: int, cliente_id: int, servicio_id: int, estado: str = None):
        with Session() as session:
            try:
                # Buscar el servicio en la base de datos
                servicio = session.query(Servicio).get(servicio_id)
                if servicio is None:
                    return (f"Error: No se encontró el servicio con id {servicio_id}")
                if fecha_inicio.hour == 24:
                    fecha_inicio = fecha_inicio.replace(hour=0) + timedelta(days=1)

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
            try:
                return session.query(Cita).filter(Cita.id == cita_id).first()
            except Exception as e:
                # Manejar el error de integridad de la base de datos
                return print(f"Excepción: {e}")

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
    
    def actualizar_estado_cita(self, cita_id: int, estado: str):
        with Session() as session:
            cita_obj = session.query(Cita).filter(Cita.id == cita_id).first()
            if cita_obj is None:
                raise ValueError("Cita no encontrada")
            if estado is not None:
                if estado not in [e for e in Cita.ESTADOS_POSIBLES]:
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
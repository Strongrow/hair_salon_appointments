from app.dataBase.clientes import Cliente
from app.dataBase.declarative_base import Session, engine, Base


class LogicaCliente():
    Base.metadata.create_all(engine)

    def crear_cliente(self, nombre: str, apellido:str, telefono: int, email: str):
        with Session() as session:
            cliente_existente = session.query(Cliente).filter(Cliente.email == email).first()
            if cliente_existente is not None:
                raise ValueError("El email ya está en uso")
            cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            session.add(cliente)
            session.commit()
            return {"id": cliente.id, "nombre": cliente.nombre, "apellido": cliente.apellido, "telefono": cliente.telefono, "email": cliente.email}

    def dar_clientes(self):
        with Session() as session:
            return session.query(Cliente).all()

    def dar_cliente(self, cliente_id: int):
        with Session() as session:
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            if cliente is None:
                raise ValueError("El cliente no existe")
            return cliente

    def actualizar_cliente(self, cliente_id: int, nombre: str = None, apellido: str = None, telefono: int = None, email: str = None):
        with Session() as session:
            #Se inicia la sesión del API
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            #
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
    
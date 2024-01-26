from app.dataBase.clientes import Cliente
from app.dataBase.declarative_base import Session, engine, Base


class LogicaCliente():
    Base.metadata.create_all(engine)

    # Método para crear un nuevo cliente
    def crear_cliente(self, nombre: str, apellido:str, telefono: int, email: str):
        # Iniciamos una nueva sesión de base de datos
        with Session() as session:
            # Verificamos si ya existe un cliente con el mismo email
            cliente_existente = session.query(Cliente).filter(Cliente.email == email).first()
            if cliente_existente is not None:
                # Si existe, lanzamos un error
                raise ValueError("El email ya está en uso")
            # Creamos un nuevo cliente
            cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            # Añadimos el nuevo cliente a la sesión y hacemos commit
            session.add(cliente)
            session.commit()
            # Devolvemos los datos del nuevo cliente
            return {"id": cliente.id, "nombre": cliente.nombre, "apellido": cliente.apellido, "telefono": cliente.telefono, "email": cliente.email}

    # Método para obtener todos los clientes
    def dar_clientes(self):
        with Session() as session:
            # Devolvemos todos los clientes
            return session.query(Cliente).all()

    # Método para obtener un cliente específico
    def dar_cliente(self, cliente_id: int):
        with Session() as session:
            # Buscamos el cliente por su id
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            if cliente is None:
                # Si no existe, lanzamos un error
                raise ValueError("El cliente no existe")
            return cliente

    # Método para actualizar los datos de un cliente
    def actualizar_cliente(self, cliente_id: int, nombre: str = None, apellido: str = None, telefono: int = None, email: str = None):
        with Session() as session:
            # Buscamos el cliente por su id
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            if cliente is None:
                # Si no existe, lanzamos un error
                raise ValueError("Cliente no encontrado")
            # Si se proporciona un nuevo email, verificamos que no esté en uso
            if email is not None:
                cliente_existente = session.query(Cliente).filter(Cliente.email == email).first()
                if cliente_existente is not None:
                    # Si el email ya está en uso, lanzamos un error
                    raise ValueError("El email ya está en uso")
            # Actualizamos los datos del cliente
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

    # Método para eliminar un cliente
    def eliminar_cliente(self, cliente_id: int):
        with Session() as session:
            # Buscamos el cliente por su id
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            # Eliminamos el cliente de la sesión
            session.delete(cliente)
            session.commit()
            return {"message": "Cliente eliminado con éxito"}
    
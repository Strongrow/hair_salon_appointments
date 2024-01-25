import unittest
from faker import Faker
from app.dataBase.declarative_base import Session
from app.src.cliente import LogicaCliente
from app.dataBase.clientes import Cliente

class TestLogicaCliente(unittest.TestCase):

    def setUp(self):
        self.cliente_service = LogicaCliente()
        fake = Faker()
        self.nombre = fake.first_name()
        self.apellido = fake.last_name()
        self.telefono = fake.random_int(min=1000000000, max=9999999999)  # Genera un número de teléfono aleatorio
        self.email = fake.email()

    def test_crear_cliente(self):
        cliente = self.cliente_service.crear_cliente(self.nombre, self.apellido, self.telefono, self.email)
        self.assertEqual(cliente["nombre"], self.nombre)
        self.assertEqual(cliente["apellido"], self.apellido)
        self.assertEqual(cliente["telefono"], self.telefono)
        self.assertEqual(cliente["email"], self.email)

    def test_dar_clientes(self):
        clientes = self.cliente_service.dar_clientes()
        self.assertIsInstance(clientes, list)

    def test_dar_cliente(self):
        cliente = self.cliente_service.crear_cliente(self.nombre, self.apellido, self.telefono, self.email)
        cliente_obtenido = self.cliente_service.dar_cliente(cliente['id'])
        self.assertEqual(cliente['id'], cliente_obtenido.id)

    def test_actualizar_cliente(self):
        cliente = self.cliente_service.crear_cliente(self.nombre, self.apellido, self.telefono, self.email)
        nuevo_nombre = Faker().first_name()
        cliente_actualizado = self.cliente_service.actualizar_cliente(cliente['id'], nombre=nuevo_nombre)
        self.assertEqual(cliente_actualizado.nombre, nuevo_nombre)

    def test_eliminar_cliente(self):
        cliente = self.cliente_service.crear_cliente(self.nombre, self.apellido, self.telefono, self.email)
        cliente_id = cliente['id']
        response = self.cliente_service.eliminar_cliente(cliente_id)
        self.assertEqual(response, {"message": "Cliente eliminado con éxito"})
        with self.assertRaises(ValueError):
            self.cliente_service.dar_cliente(cliente_id)  # El cliente ya no debería existir

if __name__ == '__main__':
    unittest.main()
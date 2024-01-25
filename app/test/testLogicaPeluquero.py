import unittest
import random
from faker import Faker
from app.dataBase.declarative_base import Session
from app.src.peluquero import LogicaPeluquero
from app.dataBase.peluqueros import Peluquero

class TestLogica(unittest.TestCase):

    def setUp(self):
        self.peluquero_service = LogicaPeluquero()
        fake = Faker()
        self.nombre = fake.first_name()
        self.apellido = fake.last_name()

    def test_crear_peluquero(self):
        self.session = Session()
        logica = LogicaPeluquero()
        peluquero = logica.crear_peluquero(self.nombre, self.apellido)
        self.assertEqual(peluquero.nombre, self.nombre)
        self.assertEqual(peluquero.apellido, self.apellido)

        # Prueba con nombre None
        with self.assertRaises(ValueError):
            self.peluquero_service.crear_peluquero(None, self.apellido)

        # Prueba con apellido None
        with self.assertRaises(ValueError):
            self.peluquero_service.crear_peluquero(self.nombre, None)

        # Prueba con nombre y apellido None
        with self.assertRaises(ValueError):
            self.peluquero_service.crear_peluquero(None, None)

    def test_dar_peluqueros(self):
        # Prueba que se devuelva una lista
        peluqueros = self.peluquero_service.dar_peluqueros()
        self.assertIsInstance(peluqueros, list)

        # Prueba que cada elemento en la lista sea una instancia de Peluquero
        for peluquero in peluqueros:
            self.assertIsInstance(peluquero, Peluquero)

    def test_dar_peluquero(self):
        # Prueba con un id válido
        ids_peluqueros = self.peluquero_service.dar_ids_peluqueros()
        id_peluquero = random.choice(ids_peluqueros)
        peluquero = self.peluquero_service.dar_peluquero(id_peluquero)
        self.assertIsInstance(peluquero, Peluquero)

        # Prueba con un id inválido
        id_invalido = random.randint(1, 10000)  # Genera un número aleatorio entre 1 y 10000
        while id_invalido in ids_peluqueros:  # Si el número aleatorio está en la lista de ids, genera otro
            id_invalido = random.randint(1, 10000)
        peluquero = self.peluquero_service.dar_peluquero(id_invalido)
        self.assertIsNone(peluquero)

    def test_actualizar_peluquero(self):
        # Prueba con un id válido y cambios válidos
        id_peluqueros = self.peluquero_service.dar_ids_peluqueros()
        if not id_peluqueros:  # Si la lista está vacía
        # Crea un nuevo peluquero y obtén su ID
            nuevo_peluquero = self.peluquero_service.crear_peluquero("Nombre", "Apellido")
            id_peluquero = nuevo_peluquero.id
        else:
            id_peluquero = random.choice(id_peluqueros)
        peluquero = self.peluquero_service.actualizar_peluquero(id_peluquero, self.nombre, self.apellido)
        self.assertIsInstance(peluquero, Peluquero)
        self.assertEqual(peluquero.nombre, self.nombre)
        self.assertEqual(peluquero.apellido, self.apellido)

        # Prueba con un id inválido
        with self.assertRaises(ValueError):
            id_invalido = random.randint(1, 10000)  # Genera un número aleatorio entre 1 y 10000
            while id_invalido in id_peluqueros:  # Si el número aleatorio está en la lista de ids, genera otro
                id_invalido = random.randint(1, 10000)
            self.peluquero_service.actualizar_peluquero(id_invalido, self.nombre, self.apellido)

    def test_eliminar_peluquero(self):
        # Prueba con un id válido
        id_peluqueros = self.peluquero_service.dar_ids_peluqueros()
        id_peluquero = random.choice(id_peluqueros)
        response = self.peluquero_service.eliminar_peluquero(id_peluquero)  # Asegúrate de que este id exista en tu base de datos
        self.assertEqual(response, {"message": "Peluquero eliminado con éxito"})

        # Generar un id inválido aleatorio
        id_invalido = random.randint(1, 10000)
        while id_invalido in id_peluqueros:
            id_invalido = random.randint(1, 10000)

        # Prueba con un id inválido
        with self.assertRaises(ValueError):  # Asegúrate de que tu función lanza una excepción cuando no se encuentra el peluquero
            self.peluquero_service.eliminar_peluquero(id_invalido)  # Asegúrate de que este id no exista en tu base de datos


if __name__ == '__main__':
    unittest.main()
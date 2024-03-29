import unittest
from datetime import time
from app.src.servicio import LogicaServicios
from app.dataBase.servicios import Servicio
from sqlalchemy.orm import Session
from faker import Faker
import random

class TestServicioService(unittest.TestCase):
    def setUp(self):
        self.servicio_service = LogicaServicios()
        self.session = Session()
        self.faker = Faker()

    def test_crear_servicio(self):
        descripcion = self.faker.sentence(nb_words=3)
        duracion = time(hour=random.randint(1, 3), minute=random.randint(0, 59))
        costo = round(random.uniform(50.0, 200.0), 2)
        with self.session as session:
            #self.servicio_service.crear_servicio(session)
            servicio = self.servicio_service.crear_servicio(session,descripcion, duracion, costo)
            session.flush()
            self.assertEqual(servicio.descripcion, descripcion)
            self.assertEqual(servicio.duracion, duracion)
            self.assertEqual(servicio.costo, costo)
            
            

    def test_dar_servicios(self):
        servicios = self.servicio_service.dar_servicios()
        self.assertIsInstance(servicios, list)
        self.assertTrue(all(isinstance(s, Servicio) for s in servicios))

    def test_dar_servicio(self):
        servicio_id = 1  # Asegúrate de que este ID exista en la base de datos
        servicio = self.servicio_service.dar_servicio(servicio_id)
        if servicio is None:
            self.assertIsNone(servicio)
        else:
            self.assertIsInstance(servicio, Servicio)

    def test_actualizar_servicio(self):
        with self.session as session:
        # Obtén el primer servicio de la base de datos
            servicio = session.query(Servicio).first()
            if servicio is None:
                self.fail("No hay servicios en la base de datos para probar")

            # Genera un costo aleatorio
            nuevo_costo = round(random.uniform(50.0, 200.0), 2)

            # Actualiza el servicio
            servicio_actualizado = self.servicio_service.actualizar_servicio(servicio.id, costo=nuevo_costo)

            # Comprueba que el costo se ha actualizado correctamente
            self.assertEqual(servicio_actualizado.costo, nuevo_costo)

    def eliminar_servicio(self, servicio_id: int):
        with Session() as session:
            servicio = session.query(Servicio).filter(Servicio.id == servicio_id).first()
            if servicio is not None:
                session.delete(servicio)
                session.commit()
                return True
            else:
                return False


if __name__ == "__main__":
    unittest.main()
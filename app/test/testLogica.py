import unittest
import random
from faker import Faker
from sqlalchemy import desc , asc
from app.dataBase.declarative_base import Session
from app.src.Logica import Logica
from app.dataBase.clientes import Cliente
from app.dataBase.peluqueros import Peluquero
from app.dataBase.citas import Cita
from app.dataBase.servicios import Servicio
from datetime import datetime, time, timedelta

class TestLogica(unittest.TestCase):

    def test_crear_peluquero(self):
        self.session = Session()
        logica = Logica()
        fake = Faker()
        nombre = fake.first_name()
        apellido = fake.last_name()
        peluquero = logica.crear_peluquero(nombre, apellido)
        self.assertEqual(peluquero.nombre, nombre)
        self.assertEqual(peluquero.apellido, apellido)
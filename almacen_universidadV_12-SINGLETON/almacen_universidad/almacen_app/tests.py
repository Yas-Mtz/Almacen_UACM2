from django.test import TestCase
import unittest
from almacen_app.models import Singleton
# Create your tests here.

# PRUEBAS DE SINGLETON -> métodos de prueba
# se define la clase de prueba "TestSingleton" que hereda de "unisttest.TestCase"


class TestSingleton(unittest.TestCase):  # Define una clase de prueba "TestSingleton"
    # definicion de método "test_singleton_instance" verifica si 2 instancias de la clase singleton son la misma instancia
    def test_singleton_instance(self):
        instance1 = Singleton()  # creacion de instancias
        instance2 = Singleton()

        # se usa "assertIs"para verificar que instance1 e instance2 son la misma instancia
        self.assertIs(instance1, instance2)


if __name__ == '__main__':  # Verifica si el script está siendo ejecutado directamente
    unittest.main()  # Ejecución de pruebas unitarias

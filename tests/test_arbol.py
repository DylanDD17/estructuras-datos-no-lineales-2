import unittest
from src.arbol_nario import OrganizacionNode


class TestArbol(unittest.TestCase):

    def test_iteracion(self):
        raiz = OrganizacionNode("Rectoría")
        hijo = OrganizacionNode("Ingeniería")

        raiz.agregar_hijo(hijo)

        resultado = list(raiz)

        self.assertIn("Rectoría", resultado)
        self.assertIn("Ingeniería", resultado)


if __name__ == "__main__":
    unittest.main()
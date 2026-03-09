import unittest
from src.hash_table import HashTable


class TestHash(unittest.TestCase):

    def test_insertar(self):

        tabla = HashTable()

        tabla[10] = "Carlos"

        self.assertEqual(tabla[10], "Carlos")


if __name__ == "__main__":
    unittest.main()
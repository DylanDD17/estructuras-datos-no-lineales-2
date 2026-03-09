import unittest
from src.trie import Trie


class TestTrie(unittest.TestCase):

    def test_sugerencias(self):

        trie = Trie()

        trie.insertar("gato")
        trie.insertar("gafas")

        resultados = list(trie.sugerir("ga"))

        self.assertIn("gato", resultados)
        self.assertIn("gafas", resultados)


if __name__ == "__main__":
    unittest.main()
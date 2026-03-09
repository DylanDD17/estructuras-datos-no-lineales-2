from typing import Dict, Generator


class TrieNode:
    """
    Nodo del Trie.
    """

    def __init__(self) -> None:
        self.hijos: Dict[str, "TrieNode"] = {}
        self.fin_palabra: bool = False


class Trie:
    """
    Implementación de un Trie para autocompletado.
    """

    def __init__(self) -> None:
        self.raiz = TrieNode()

    def insertar(self, palabra: str) -> None:
        """
        Inserta una palabra en el Trie.

        Args:
            palabra (str): palabra a insertar
        """
        nodo = self.raiz

        for letra in palabra:
            nodo = nodo.hijos.setdefault(letra, TrieNode())

        nodo.fin_palabra = True

    def sugerir(self, prefijo: str) -> Generator[str, None, None]:
        """
        Sugiere palabras que comiencen con un prefijo.

        Args:
            prefijo (str): prefijo buscado

        Yields:
            str: palabras sugeridas
        """
        nodo = self.raiz

        for letra in prefijo:
            if letra not in nodo.hijos:
                return
            nodo = nodo.hijos[letra]

        yield from self._dfs(nodo, prefijo)

    def _dfs(self, nodo: TrieNode, palabra: str) -> Generator[str, None, None]:

        if nodo.fin_palabra:
            yield palabra

        for letra, hijo in nodo.hijos.items():
            yield from self._dfs(hijo, palabra + letra)


if __name__ == "__main__":

    trie = Trie()

    trie.insertar("git")
    trie.insertar("github")
    trie.insertar("girar")

    for palabra in trie.sugerir("gi"):
        print(palabra)
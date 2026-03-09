from typing import Any, List, Tuple


class HashTable:
    """
    Implementación simple de una tabla hash con encadenamiento.
    """

    def __init__(self, tamaño: int = 10) -> None:
        self.tamaño = tamaño
        self.tabla: List[List[Tuple[Any, Any]]] = [[] for _ in range(tamaño)]

    def _hash(self, clave: Any) -> int:
        """
        Calcula el índice hash.

        Args:
            clave (Any): clave a hashear

        Returns:
            int: índice de la tabla
        """
        return hash(clave) % self.tamaño

    def __setitem__(self, clave: Any, valor: Any) -> None:
        """
        Inserta un elemento en la tabla.

        Args:
            clave (Any): clave
            valor (Any): valor
        """
        indice = self._hash(clave)
        bucket = self.tabla[indice]

        for i, (k, v) in enumerate(bucket):
            if k == clave:
                bucket[i] = (clave, valor)
                return

        bucket.append((clave, valor))

    def __getitem__(self, clave: Any) -> Any:
        """
        Obtiene un valor por clave.

        Args:
            clave (Any): clave buscada

        Raises:
            KeyError: si la clave no existe

        Returns:
            Any: valor asociado
        """
        indice = self._hash(clave)
        bucket = self.tabla[indice]

        for k, v in bucket:
            if k == clave:
                return v

        raise KeyError("Clave no encontrada")


if __name__ == "__main__":

    tabla = HashTable()

    tabla[1] = "Juan"
    tabla[2] = "Ana"

    print(tabla[1])
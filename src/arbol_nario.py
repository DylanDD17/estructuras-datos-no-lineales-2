from __future__ import annotations
from typing import Dict, Iterator


class OrganizacionNode:
    """
    Nodo de una estructura organizacional representada como árbol N-ario.
    """

    def __init__(self, nombre: str) -> None:
        """
        Args:
            nombre (str): Nombre de la unidad organizacional.
        """
        self.nombre: str = nombre
        self.hijos: Dict[str, "OrganizacionNode"] = {}

    def agregar_hijo(self, nodo: "OrganizacionNode") -> None:
        """
        Agrega un hijo al nodo actual.

        Args:
            nodo (OrganizacionNode): Nodo hijo a agregar.
        """
        self.hijos[nodo.nombre] = nodo

    def __iter__(self) -> Iterator[str]:
        """
        Permite iterar sobre el árbol.

        Yields:
            str: Nombre de cada nodo.
        """
        yield self.nombre
        for hijo in self.hijos.values():
            yield from hijo


if __name__ == "__main__":
    rectoria = OrganizacionNode("Rectoría")
    ingenieria = OrganizacionNode("Facultad Ingeniería")
    sistemas = OrganizacionNode("Programa Sistemas")

    rectoria.agregar_hijo(ingenieria)
    ingenieria.agregar_hijo(sistemas)

    for unidad in rectoria:
        print(unidad)
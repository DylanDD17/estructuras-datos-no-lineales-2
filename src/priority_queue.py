import heapq
import time


class Tarea:
    """
    Representa una tarea con prioridad.
    """

    def __init__(self, prioridad: int, descripcion: str) -> None:
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.timestamp = time.time()

    def __lt__(self, other: "Tarea") -> bool:
        """
        Define el orden de las tareas para el heap.

        Args:
            other (Tarea): otra tarea

        Returns:
            bool
        """
        if self.prioridad == other.prioridad:
            return self.timestamp < other.timestamp
        return self.prioridad < other.prioridad


class Planificador:

    def __init__(self) -> None:
        self.cola = []

    def agregar_tarea(self, tarea: Tarea) -> None:
        heapq.heappush(self.cola, tarea)

    def ejecutar(self) -> Tarea:
        return heapq.heappop(self.cola)


if __name__ == "__main__":

    plan = Planificador()

    plan.agregar_tarea(Tarea(1, "Proceso crítico"))
    plan.agregar_tarea(Tarea(3, "Actualizar sistema"))
    plan.agregar_tarea(Tarea(2, "Enviar datos"))

    print(plan.ejecutar().descripcion)
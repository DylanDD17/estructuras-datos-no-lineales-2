import unittest
from src.priority_queue import Planificador, Tarea


class TestHeap(unittest.TestCase):

    def test_prioridad(self):

        plan = Planificador()

        plan.agregar_tarea(Tarea(2, "Normal"))
        plan.agregar_tarea(Tarea(1, "Urgente"))

        tarea = plan.ejecutar()

        self.assertEqual(tarea.descripcion, "Urgente")


if __name__ == "__main__":
    unittest.main()
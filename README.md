# Parcial - Estructuras de Datos No Lineales


# Estructura del proyecto

```
src/
  arbol_nario.py
  trie.py
  hash_table.py
  priority_queue.py

tests/
  test_arbol.py
  test_trie.py
  test_hash.py
  test_heap.py

requirements.txt
README.md
```

---

# Ejercicios implementados

## 1. Árbol N-ario (Estructura Organizacional)

Se implementa una estructura de árbol N-ario para representar una jerarquía organizacional.

Ejemplo de jerarquía:

Rectoría → Facultades → Programas

Características:

* Los hijos se almacenan en `dict[str, OrganizacionNode]`
* Permite acceso O(1) por nombre
* Implementación del método mágico `__iter__` para recorrer el árbol

Complejidad:

* Inserción: **O(1)**
* Recorrido: **O(n)**

---

## 2. Trie (Autocompletado)

Se implementa un **Trie** para sugerencias de palabras basado en prefijos.

Características:

* Cada nodo usa un diccionario para almacenar las letras
* Uso de generadores (`yield`) para devolver sugerencias
* Búsqueda eficiente por prefijo

Complejidad:

* Inserción: **O(k)**
* Búsqueda por prefijo: **O(k)**
* Generación de sugerencias: **O(n)**

Donde **k** es la longitud del prefijo.

---

## 3. Hash Table

Se implementa una tabla hash desde cero, sin usar `dict` para la lógica interna.

Características:

* Manejo de colisiones mediante **encadenamiento (chaining)**
* Implementación de métodos mágicos:

```
tabla[clave] = valor
valor = tabla[clave]
```

Complejidad promedio:

* Inserción: **O(1)**
* Búsqueda: **O(1)**

Peor caso:

* **O(n)**

---

## 4. Cola de Prioridad (Heap)

Se implementa un planificador de tareas utilizando el módulo `heapq`.

Características:

* Clase `Tarea` con atributos:

  * prioridad
  * timestamp
* Sobrecarga del operador `__lt__` para permitir ordenamiento automático
* Simulación de una cola de prioridad similar a la de un sistema operativo

Complejidad:

* Inserción: **O(log n)**
* Eliminación: **O(log n)**

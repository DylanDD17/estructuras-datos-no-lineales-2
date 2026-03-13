# Parcial - Estructuras de Datos No Lineales

# Abstract

En este trabajo se desarrolla la implementación y el análisis de distintas estructuras de datos no lineales cuyo objetivo es la adecuada y óptima organización, localización y gestión de la información en sistemas computacionales a lo largo del curso. En este marco del parcial se implementan árboles N-arios, estructuras Trie, tablas hash y colas de prioridad mediante heaps, cada una de las cuales es adecuada para llegar a resolver un tipo y problema concreto relacionado con el almacenamiento y el procesamiento de los datos. Los árboles N-arios permiten representar estructuras jerárquicas con multiplicidad de hijos por nodo de forma que resulta idónea para poder modelar un conjunto de sistemas organizados como, entre otros, directorios o clasificaciones. Las estructuras Trie permiten optimizar la búsqueda de cadenas y prefijos siendo ideales para sistemas de autocompletado y motores de búsqueda. Las tablas hash implementan un acceso rápido a los datos mediante el uso de funciones hash siendo sus operaciones de inserción y búsqueda de complejidad promedio constante. Por último, los heaps permiten gestionar prioridades dentro de un conjunto de elementos siendo base de distintos algoritmos de planificación y de procesamiento de tareas. En definitiva, estas estructuras no dejan de demostrar cómo diferentes formas de organizar datos pueden ser integradas dentro de un mismo sistema y al mismo tiempo mejorar la eficiencia computacional, lo cual pone de manifiesto la importancia de éstas en aplicaciones reales como los sistemas de información, las redes o las plataformas de inteligencia artificial.


























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

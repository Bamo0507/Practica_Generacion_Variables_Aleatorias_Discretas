## **Ejercicio 6**

Suponga que cada elemento de una lista de n elementos tiene un valor asociado, y sea v(i) el
valor asociado al i-ésimo elemento de la lista. Suponga que n es muy grande, y que además cada
elemento puede aparecer en muchos lugares distintos de la lista. Explique cómo se pueden usar
números aleatorios para estimar la suma de los valores de los distintos elementos de la lista (donde
el valor de cada elemento debe contarse una sola vez, sin importar cuántas veces aparezca en la
lista).

---

Para poder estimar la suma de los valores distintos de una lista muy grande donde los elementos pueden repetirse, se busca generar posiciones aleatorias dentro de la lista, es decir, tomar un número aleatorio uniforme entre 1 y n para elegir una posición al azar. Cada valor v(Xi) obtenido se divide entre m(Xi), el número de veces que se repite ese elemento específico en la lista, de tal forma que su contribución al promedio sea siempre v(Xi) sin importar cuantas veces aparezca. Finalmente, se multiplica el promedio de estos valores corregidos por n, obteniendo así una estimación de la suma S de los valores distintos.

---

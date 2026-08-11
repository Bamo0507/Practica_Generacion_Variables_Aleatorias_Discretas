"""
Practica 2 - Generacion de Variables Aleatorias Discretas
Lanzamiento de 2 dados hasta completar todas las sumas posibles
"""

import random
import statistics

# Parametros del problema
random.seed(123)

numero_simulaciones = 100000
sumas_posibles = set(range(2, 13))


def simular_lanzamientos_hasta_completar():
    sumas_faltantes = set(sumas_posibles)
    numero_lanzamientos = 0

    while sumas_faltantes:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        numero_lanzamientos += 1

        if suma in sumas_faltantes:
            sumas_faltantes.remove(suma)

    return numero_lanzamientos


lanzamientos_por_simulacion = [simular_lanzamientos_hasta_completar() for _ in range(numero_simulaciones)]

promedio_lanzamientos = statistics.mean(lanzamientos_por_simulacion)
desviacion_lanzamientos = statistics.stdev(lanzamientos_por_simulacion)

print("=" * 60)
print(f"Simulacion con {numero_simulaciones} corridas")
print("=" * 60)
print(f"Numero esperado de lanzamientos: {promedio_lanzamientos:.2f}")
print(f"Minimo observado: {min(lanzamientos_por_simulacion)}")
print(f"Maximo observado: {max(lanzamientos_por_simulacion)}")
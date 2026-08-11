"""
Practica 2 - Generacion de Variables Aleatorias Discretas
Baraja de cartas enumeradas
"""

import random
import statistics

# Parametros del problema
random.seed(123)

numero_cartas = 100
numero_simulaciones = 15000

resultados_por_corrida = []

for _ in range(numero_simulaciones):
    mazo = list(range(1, numero_cartas + 1))
    random.shuffle(mazo)

    aciertos = 0
    for posicion, carta in enumerate(mazo, start=1):
        if carta == posicion:
            aciertos += 1

    resultados_por_corrida.append(aciertos)

esperanza_estimada = statistics.mean(resultados_por_corrida)
varianza_estimada = statistics.variance(resultados_por_corrida)

esperanza_exacta = 1.0
varianza_exacta = 1.0

print("=" * 60)
print(f"Simulacion con {numero_simulaciones} corridas, mazo de {numero_cartas} cartas")
print("=" * 60)
print(f"Esperanza estimada : {esperanza_estimada:.4f}")
print(f"Esperanza exacta   : {esperanza_exacta:.4f}")
print(f"Varianza estimada  : {varianza_estimada:.4f}")
print(f"Varianza exacta    : {varianza_exacta:.4f}")
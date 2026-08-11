"""
Practica 2 - Generacion de Variables Aleatorias Discretas
Algoritmo eficiente para simular valor de una variable aleatoria X
"""

import random

# Parametros del problema
random.seed(123)

valores_ordenados = [3, 1, 2, 4]
probabilidades_ordenadas = [0.35, 0.30, 0.20, 0.15]

acumuladas = []
acumulado = 0.0
for probabilidad in probabilidades_ordenadas:
    acumulado += probabilidad
    acumuladas.append(acumulado)


def generar_variable_aleatoria():
    numero_aleatorio = random.random()
    for valor, acumulada in zip(valores_ordenados, acumuladas):
        if numero_aleatorio < acumulada:
            return numero_aleatorio, valor
    return numero_aleatorio, valores_ordenados[-1]


numero_simulaciones = 10000
conteo_valores = {1: 0, 2: 0, 3: 0, 4: 0}

for _ in range(numero_simulaciones):
    numero_aleatorio, valor_generado = generar_variable_aleatoria()
    conteo_valores[valor_generado] += 1

print("=" * 50)
print(f"Simulacion de X con {numero_simulaciones} corridas")
print("=" * 50)
for valor in [1, 2, 3, 4]:
    print(f"X = {valor} -> frecuencia = {conteo_valores[valor]}")
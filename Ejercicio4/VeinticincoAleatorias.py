"""
Practica 2 - Generacion de Variables Aleatorias Discretas
Generacion de una secuencia de 25 Bernoulli con p=0.8
"""

import random
import math

# Parametros del problema
random.seed(123)

numero_bernoulli = 25
probabilidad_exito = 0.8

valores_generados = []
numeros_aleatorios_usados = 0
posiciones_restantes = numero_bernoulli

while posiciones_restantes > 0:
    numero_aleatorio = random.random()
    numeros_aleatorios_usados += 1

    posicion_fracaso = int(math.log(numero_aleatorio) / math.log(probabilidad_exito)) + 1

    if posicion_fracaso >= posiciones_restantes:
        for _ in range(posiciones_restantes):
            valores_generados.append(1)
        posiciones_restantes = 0
    else:
        for _ in range(posicion_fracaso - 1):
            valores_generados.append(1)
        valores_generados.append(0)
        posiciones_restantes -= posicion_fracaso

print("=" * 60)
print(f"Secuencia de {numero_bernoulli} Bernoulli con p={probabilidad_exito}")
print("=" * 60)
print(f"Valores generados: {valores_generados}")
print(f"Numeros aleatorios utilizados: {numeros_aleatorios_usados}")
print(f"Total de exitos: {sum(valores_generados)}")
print(f"Total de fracasos: {numero_bernoulli - sum(valores_generados)}")
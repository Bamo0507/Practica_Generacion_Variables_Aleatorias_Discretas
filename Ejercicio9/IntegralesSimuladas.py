"""
Practica 2 - Generacion de Variables Aleatorias Discretas
Simulacion de integrales
"""

import numpy as np
import pandas as pd
from scipy import integrate

# Parametros del problema
generador_numeros = np.random.default_rng(123)
numero_muestras = 200000

resultados = []


def registrar_resultado(nombre, estimado, exacto):
    resultados.append({
        "Ejercicio": nombre,
        "Estimado (Monte Carlo)": estimado,
        "Valor exacto": exacto,
        "Diferencia absoluta": abs(estimado - exacto),
    })


# Ejercicio 3: integral de 0 a 1 de exp(e^x) dx
numeros_uniformes = generador_numeros.uniform(0, 1, numero_muestras)
estimado_3 = np.mean(np.exp(np.exp(numeros_uniformes)))
exacto_3, _ = integrate.quad(lambda x: np.exp(np.exp(x)), 0, 1)
registrar_resultado("3. Integral de exp(e^x) en [0,1]", estimado_3, exacto_3)

# Ejercicio 4: integral de 0 a 1 de (1-x^2)^(3/2) dx
numeros_uniformes = generador_numeros.uniform(0, 1, numero_muestras)
estimado_4 = np.mean((1 - numeros_uniformes ** 2) ** 1.5)
exacto_4, _ = integrate.quad(lambda x: (1 - x ** 2) ** 1.5, 0, 1)
registrar_resultado("4. Integral de (1-x^2)^(3/2) en [0,1]", estimado_4, exacto_4)

# Ejercicio 5: integral de -2 a 2 de e^(x+x^2) dx
limite_inferior, limite_superior = -2, 2
ancho_intervalo = limite_superior - limite_inferior
numeros_uniformes = generador_numeros.uniform(0, 1, numero_muestras)
valores_transformados = limite_inferior + ancho_intervalo * numeros_uniformes
estimado_5 = ancho_intervalo * np.mean(np.exp(valores_transformados + valores_transformados ** 2))
exacto_5, _ = integrate.quad(lambda x: np.exp(x + x ** 2), limite_inferior, limite_superior)
registrar_resultado("5. Integral de e^(x+x^2) en [-2,2]", estimado_5, exacto_5)

# Ejercicio 6: integral de 0 a infinito de x*(1+x^2)^(-2) dx
numeros_uniformes = generador_numeros.uniform(0, 1, numero_muestras)
x_transformada = (1 - numeros_uniformes) / numeros_uniformes
integrando_transformado = x_transformada * (1 + x_transformada ** 2) ** (-2)
estimado_6 = np.mean(integrando_transformado / numeros_uniformes ** 2)
exacto_6, _ = integrate.quad(lambda x: x * (1 + x ** 2) ** (-2), 0, np.inf)
registrar_resultado("6. Integral de x/(1+x^2)^2 en [0,inf)", estimado_6, exacto_6)

# Ejercicio 7: integral de -infinito a infinito de e^(-x^2) dx
numeros_uniformes = generador_numeros.uniform(0, 1, numero_muestras)
x_transformada = (1 - numeros_uniformes) / numeros_uniformes
integrando_transformado = np.exp(-x_transformada ** 2)
estimado_7 = 2 * np.mean(integrando_transformado / numeros_uniformes ** 2)
exacto_7, _ = integrate.quad(lambda x: np.exp(-x ** 2), -np.inf, np.inf)
registrar_resultado("7. Integral de e^(-x^2) en (-inf,inf)", estimado_7, exacto_7)

# Ejercicio 8: integral doble de 0 a 1 en x y y de e^((x+y)^2) dy dx
numeros_uniformes_x = generador_numeros.uniform(0, 1, numero_muestras)
numeros_uniformes_y = generador_numeros.uniform(0, 1, numero_muestras)
estimado_8 = np.mean(np.exp((numeros_uniformes_x + numeros_uniformes_y) ** 2))
exacto_8, _ = integrate.dblquad(lambda y, x: np.exp((x + y) ** 2), 0, 1, 0, 1)
registrar_resultado("8. Integral doble de e^((x+y)^2) en [0,1]x[0,1]", estimado_8, exacto_8)

# Ejercicio 9: integral doble de 0 a infinito en x, de 0 a x en y, de e^(-(x+y)) dy dx
numeros_uniformes_x = generador_numeros.uniform(0, 1, numero_muestras)
numeros_uniformes_y = generador_numeros.uniform(0, 1, numero_muestras)
x_transformada = (1 - numeros_uniformes_x) / numeros_uniformes_x
y_transformada = (1 - numeros_uniformes_y) / numeros_uniformes_y
indicador = (y_transformada < x_transformada).astype(float)
integrando_transformado = np.exp(-(x_transformada + y_transformada)) * indicador
jacobiano = 1 / (numeros_uniformes_x ** 2 * numeros_uniformes_y ** 2)
estimado_9 = np.mean(integrando_transformado * jacobiano)
exacto_9, _ = integrate.dblquad(lambda y, x: np.exp(-(x + y)), 0, np.inf, 0, lambda x: x)
registrar_resultado("9. Integral doble de e^-(x+y) con y<x", estimado_9, exacto_9)

# Tabla resumen 
tabla_resultados = pd.DataFrame(resultados)
pd.set_option("display.float_format", lambda valor: f"{valor:.6f}")
print(tabla_resultados.to_string(index=False))
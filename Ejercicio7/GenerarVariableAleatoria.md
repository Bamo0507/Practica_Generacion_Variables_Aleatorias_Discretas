## **Ejercicio 7**

**(a) ¿Cuál es la distribución de Y en el Paso 2?**

- Se trata de una variable aleatoria Geométrica con parámetro p=lambda. Y representa el número de intentos hasta el primer éxito. La función de masa de probabilidad sería: P{Y=k}=λ(1-λ)^(k-1)

**(b) Explique qué está haciendo el algoritmo.**

El algoritmo prueba, uno por uno, los posibles valores que podría tomar X, pero en vez de revisarlos en orden estricto, avanza dando saltos, ya que muchos valores pequeños difícilmente serán el resultado final.

- Se arranca en S=0.
- Se genera un salto aleatorio Y (distribución geométrica) y se suma a S. Este nuevo S es el candidato actual para ser el valor final de X.
- Se genera un nuevo valor aleatorio entre 0 y 1, y se compara contra $\lambda_S/\lambda$, es decir, qué tan probable es realmente que X valga S, en proporción a la tasa de riesgo máxima $\lambda$.
- Si el valor aleatorio cae por debajo de ese umbral, se acepta el candidato: X=S y el algoritmo se detiene. De lo contrario se genera otro candidato y se repite. 


**(c) Argumente que X es una variable aleatoria con tasas de riesgo discretas {λn}**

En ningún momento el algoritmo se casa con un valor de S desde que lo genera, ya que hay aleatoriedad involucrada en cada decisión: cada vez que llega a un candidato, se genera un nuevo valor aleatorio entre 0 y 1 y se compara contra $\lambda_S/\lambda$, aceptando ese candidato solo si se cumple la condición, o descartándolo y generando nuevos valores hasta que uno sí la cumpla. Esto equivale a que, para cada entero n, existe una probabilidad $\lambda$ de ser visitado como candidato (gracias a los saltos geométricos) y, una vez visitado, una probabilidad independiente $\lambda_n/\lambda$ de ser aceptado, de tal forma que la probabilidad de que X termine aceptado exactamente en n es $\lambda \times (\lambda_n/\lambda) = \lambda_n$; y como cada decisión se toma con un valor aleatorio nuevo, sin arrastrar información de los candidatos rechazados previamente, la probabilidad de aceptación en n no depende del pasado, lo cual corresponde exactamente a la definición de tasa de riesgo $P\{X=n \mid X \ge n\} = \lambda_n$.
"""
Practica 2 - Generacion de Variables Aleatorias Discretas
Simulacion de inventario de botellas de agua (15 dias)
"""
import random

random.seed(123)

INVENTARIO_DIARIO = 3
N_DIAS = 15

PRECIO_VENTA = 10.00
COSTO_BOTELLA = 3.50
MARGEN = PRECIO_VENTA - COSTO_BOTELLA

# Distribucion de demanda diaria: valor -> probabilidad
demanda_valores = [0, 1, 2, 3, 4, 5]
probabilidades  = [0.05, 0.15, 0.30, 0.30, 0.15, 0.05]

# Probabilidades acumuladas F(x)
acumuladas = []
acum = 0.0
for p in probabilidades:
    acum += p
    acumuladas.append(acum)

def generar_demanda():
    # Genera un numero aleatorio U y devuelve (U, demanda)
    U = random.random()
    for valor, F in zip(demanda_valores, acumuladas):
        if U < F:
            return U, valor
    return U, demanda_valores[-1]

# Simulacion dia a dia
resultados = []

for dia in range(1, N_DIAS + 1):
    U, demanda = generar_demanda()

    ventas    = min(demanda, INVENTARIO_DIARIO)
    faltante  = max(demanda - INVENTARIO_DIARIO, 0)
    sobrante  = max(INVENTARIO_DIARIO - demanda, 0)

    resultados.append({
        "dia": dia,
        "U": U,
        "demanda": demanda,
        "ventas": ventas,
        "faltante": faltante,
        "sobrante": sobrante,
    })

# Tabla de resultados por dia
print("=" * 78)
print("SIMULACION DE 15 DIAS - INVENTARIO FIJO DE 3 BOTELLAS/DIA")
print("=" * 78)
print(f"{'Dia':>4} {'U':>8} {'Demanda':>8} {'Ventas':>8} {'Faltante':>9} {'Sobrante':>9}")
print("-" * 78)
for r in resultados:
    print(f"{r['dia']:>4} {r['U']:>8.4f} {r['demanda']:>8} "
          f"{r['ventas']:>8} {r['faltante']:>9} {r['sobrante']:>9}")
print("-" * 78)

# Metricas operativas
demanda_total = sum(r["demanda"] for r in resultados)
demanda_prom = demanda_total / N_DIAS
ventas_total = sum(r["ventas"] for r in resultados)
faltante_total = sum(r["faltante"] for r in resultados)
sobrante_total = sum(r["sobrante"] for r in resultados)
dias_con_faltante = sum(1 for r in resultados if r["faltante"] > 0)
dias_con_sobrante = sum(1 for r in resultados if r["sobrante"] > 0)
dias_exactos = sum(1 for r in resultados if r["faltante"] == 0 and r["sobrante"] == 0)

# Metricas financieras
ingreso_real = ventas_total * PRECIO_VENTA
ganancia_perdida = faltante_total * MARGEN
capital_atrapado = sobrante_total * COSTO_BOTELLA
costo_compra_total = INVENTARIO_DIARIO * N_DIAS * COSTO_BOTELLA
ganancia_neta_real = ingreso_real - costo_compra_total
ganancia_neta_ideal = ganancia_neta_real + ganancia_perdida

print("\n" + "=" * 78)
print("RESUMEN OPERATIVO (15 dias)")
print("=" * 78)
print(f"Demanda total                 : {demanda_total} botellas")
print(f"Demanda promedio diaria       : {demanda_prom:.2f} botellas/dia")
print(f"Ventas totales                : {ventas_total} botellas")
print(f"Botellas faltantes (perdidas) : {faltante_total} botellas")
print(f"Botellas sobrantes            : {sobrante_total} botellas")
print(f"Dias con quiebre de stock     : {dias_con_faltante} de {N_DIAS}")
print(f"Dias con sobrante             : {dias_con_sobrante} de {N_DIAS}")
print(f"Dias con inventario exacto    : {dias_exactos} de {N_DIAS}")

print("\n" + "=" * 78)
print("RESUMEN FINANCIERO (15 dias)")
print("=" * 78)
print(f"Precio de venta por botella   : Q{PRECIO_VENTA:.2f}")
print(f"Costo por botella             : Q{COSTO_BOTELLA:.2f}")
print(f"Margen por botella vendida    : Q{MARGEN:.2f}")
print("-" * 78)
print(f"Ingreso real por ventas       : Q{ingreso_real:,.2f}")
print(f"Costo total de compra (3/dia) : Q{costo_compra_total:,.2f}")
print(f"Ganancia neta real            : Q{ganancia_neta_real:,.2f}")
print(f"Ganancia perdida (faltantes)  : Q{ganancia_perdida:,.2f}")
print(f"Capital atrapado en sobrante  : Q{capital_atrapado:,.2f}")
print(f"Ganancia neta ideal (sin      :")
print(f"  quiebres de stock)          : Q{ganancia_neta_ideal:,.2f}")

# Comparar lo que hubiera pasado con otros inventarios
demandas_simuladas = [r["demanda"] for r in resultados]

def evaluar_inventario(inv):
    """Recalcula ventas/faltante/sobrante/ganancia neta para un nivel
    de inventario 'inv', usando las mismas demandas ya simuladas."""
    ventas_t = faltante_t = sobrante_t = 0
    for d in demandas_simuladas:
        ventas_t += min(d, inv)
        faltante_t += max(d - inv, 0)
        sobrante_t += max(inv - d, 0)
    ingreso = ventas_t * PRECIO_VENTA
    costo_compra = inv * N_DIAS * COSTO_BOTELLA
    ganancia_neta = ingreso - costo_compra
    return {
        "inventario": inv,
        "ventas": ventas_t,
        "faltante": faltante_t,
        "sobrante": sobrante_t,
        "ganancia_neta": ganancia_neta,
    }

niveles_a_comparar = [2, 3, 4, 5]
comparacion = [evaluar_inventario(inv) for inv in niveles_a_comparar]

print("\n" + "=" * 78)
print("COMPARACION: MISMA DEMANDA, DISTINTOS NIVELES DE INVENTARIO FIJO")
print("=" * 78)
print(f"{'Inventario':>10} {'Ventas':>8} {'Faltante':>9} {'Sobrante':>9} {'Ganancia neta':>15}")
print("-" * 78)
for c in comparacion:
    marca = "  <-- politica actual" if c["inventario"] == INVENTARIO_DIARIO else ""
    print(f"{c['inventario']:>10} {c['ventas']:>8} {c['faltante']:>9} "
          f"{c['sobrante']:>9} Q{c['ganancia_neta']:>13,.2f}{marca}")

mejor = max(comparacion, key=lambda c: c["ganancia_neta"])
actual = next(c for c in comparacion if c["inventario"] == INVENTARIO_DIARIO)

print("\n" + "=" * 78)
print("CONCLUSION")
print("=" * 78)

RATIO_UMBRAL = 2.0 

if capital_atrapado >= RATIO_UMBRAL * max(ganancia_perdida, 0.01):
    diagnostico = "sobrante"
elif ganancia_perdida >= RATIO_UMBRAL * max(capital_atrapado, 0.01):
    diagnostico = "faltante"
else:
    diagnostico = "balanceado"

conclusion = (
    f"Con la politica actual de {INVENTARIO_DIARIO} botellas diarias, en los "
    f"{N_DIAS} dias simulados se vendieron {ventas_total} botellas, se "
    f"perdieron {faltante_total} ventas por falta de stock y sobraron "
    f"{sobrante_total} botellas sin vender. Esto genero una ganancia neta de "
    f"Q{ganancia_neta_real:,.2f}, frente a Q{ganancia_perdida:,.2f} en "
    f"ganancias perdidas por quiebres de stock y Q{capital_atrapado:,.2f} "
    f"de capital inmovilizado en botellas sobrantes.\n\n"
)

if diagnostico == "sobrante":
    conclusion += (
        f"El capital atrapado en sobrante (Q{capital_atrapado:,.2f}) es al "
        f"menos el doble de la ganancia perdida por faltante "
        f"(Q{ganancia_perdida:,.2f}), lo que indica que el inventario de "
        f"{INVENTARIO_DIARIO} botellas es DEMASIADO ALTO para la demanda "
        f"real observada. La mayor parte del dinero invertido en inventario "
        f"se esta quedando sin vender en vez de generar ganancia.\n\n"
        f"Se recomienda REDUCIR el inventario diario."
    )
elif diagnostico == "faltante":
    conclusion += (
        f"La ganancia perdida por faltante (Q{ganancia_perdida:,.2f}) es al "
        f"menos el doble del capital atrapado en sobrante "
        f"(Q{capital_atrapado:,.2f}), lo que indica que el inventario de "
        f"{INVENTARIO_DIARIO} botellas es INSUFICIENTE para la demanda real "
        f"observada. Se estan perdiendo clientes y ganancias por no tener "
        f"suficiente stock.\n\n"
        f"Se recomienda AUMENTAR el inventario diario."
    )
else:
    conclusion += (
        f"La ganancia perdida por faltante (Q{ganancia_perdida:,.2f}) y el "
        f"capital atrapado en sobrante (Q{capital_atrapado:,.2f}) estan "
        f"relativamente balanceados, lo que sugiere que la politica actual "
        f"de {INVENTARIO_DIARIO} botellas diarias es razonable y no requiere "
        f"un ajuste drastico."
    )

diferencia_mejor = mejor["ganancia_neta"] - actual["ganancia_neta"]

if mejor["inventario"] == INVENTARIO_DIARIO:
    texto_comparacion = (
        f"con {mejor['inventario']} botellas diarias, generando una ganancia "
        f"neta de Q{mejor['ganancia_neta']:,.2f} (igual a la politica actual, "
        f"que ya es la optima entre las opciones evaluadas)."
    )
else:
    texto_comparacion = (
        f"con {mejor['inventario']} botellas diarias, generando una ganancia "
        f"neta de Q{mejor['ganancia_neta']:,.2f}, es decir "
        f"Q{diferencia_mejor:,.2f} MAS que la politica actual de "
        f"{INVENTARIO_DIARIO} botellas."
    )

conclusion += (
    f"\n\nAl recalcular la ganancia neta con la misma demanda observada pero "
    f"variando el inventario fijo, el mejor resultado se habria obtenido "
    f"{texto_comparacion}"
)

print(conclusion)
import math
import matplotlib.pyplot as plt
import numpy as np


def resolver_eoq(D, S, H, C, dias_laborables, lead_time):
    # Cálculos del modelo EOQ
    Q_optimo = math.sqrt((2 * D * S) / H)
    N_pedidos = D / Q_optimo
    tiempo_entre_pedidos = dias_laborables / N_pedidos
    demanda_diaria = D / dias_laborables
    rop = demanda_diaria * lead_time

    # Cálculos de costos
    costo_compra = D * C
    costo_ordenar = (D / Q_optimo) * S
    costo_mantener = (Q_optimo / 2) * H
    costo_total = costo_compra + costo_ordenar + costo_mantener

    # Salida de resultados en consola
    print("=== Universidad Cuauhtémoc - Ejercicio 3.4 ===")
    print(f"Lote Óptimo de Pedido (EOQ): {Q_optimo:.2f} unidades")
    print(f"Número de pedidos al año: {N_pedidos:.2f} órdenes")
    print(f"Tiempo entre pedidos: {tiempo_entre_pedidos:.2f} días laborables")
    print(f"Punto de Reorden (ROP): {rop:.2f} unidades")
    print("-" * 45)
    print(f"Costo Anual de Ordenar: ${costo_ordenar:,.2f} USD")
    print(f"Costo Anual de Mantener: ${costo_mantener:,.2f} USD")
    print(f"Costo Total Anual (con compra): ${costo_total:,.2f} USD")

    return Q_optimo, rop, tiempo_entre_pedidos


D = 12000       # Demanda anual (tarjetas NIC/año)
S = 200         # Costo de ordenar (USD/pedido)
H = 4           # Costo de mantener inventario (USD/unidad/año)
C = 50          # Costo unitario del producto (USD/tarjeta)
dias_lab = 240  # Días laborables al año
L = 6           # Tiempo de entrega / Lead Time (días)


# Ejecutar la función con los datos del ejercicio
Q_opt, rop_val, t_ciclo = resolver_eoq(
    D, S, H, C, dias_lab, L
)


num_ciclos = 3

tiempo = np.linspace(
    0,
    num_ciclos * t_ciclo,
    500
)

inventario = []

for t in tiempo:
    tiempo_en_ciclo = t % t_ciclo

    # Inventario que va disminuyendo durante cada ciclo
    inv = Q_opt - (
        (D / dias_lab) * tiempo_en_ciclo
    )

    inventario.append(inv)

plt.figure(figsize=(10, 5))

plt.plot(
    tiempo,
    inventario,
    color="navy",
    linewidth=2,
    label="Nivel de Inventario"
)

plt.axhline(
    y=rop_val,
    color="red",
    linestyle="--",
    label=f"Punto de Reorden (ROP = {rop_val:.0f} u)"
)

plt.axhline(
    y=0,
    color="black",
    linewidth=0.8
)

plt.title(
    "Simulación de Inventario: Modelo EOQ - Ejercicio 3.4"
)

plt.xlabel("Días Laborables")
plt.ylabel("Unidades en Almacén")

plt.grid(
    True,
    linestyle=":",
    alpha=0.6
)

plt.legend()
plt.tight_layout()

plt.show()
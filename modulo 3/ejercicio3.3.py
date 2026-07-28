import math
import matplotlib.pyplot as plt
import numpy as np

def resolver_eoq(D, S, H, C, dias_laborables, lead_time):
    Q_optimo = math.sqrt((2 * D * S) / H)
    N_pedidos = D / Q_optimo
    tiempo_entre_pedidos = dias_laborables / N_pedidos
    demanda_diaria = D / dias_laborables
    rop = demanda_diaria * lead_time
    
    costo_compra = D * C
    costo_ordenar = (D / Q_optimo) * S
    costo_mantener = (Q_optimo / 2) * H
    costo_total = costo_compra + costo_ordenar + costo_mantener
    
    print("=== RESULTADOS DEL MODELO EOQ ===")
    print(f"Lote Óptimo de Pedido (EOQ): {Q_optimo:.2f} unidades")
    print(f"Número de pedidos al año: {N_pedidos:.2f} órdenes")
    print(f"Tiempo entre pedidos: {tiempo_entre_pedidos:.2f} días laborables")
    print(f"Punto de Reorden (ROP): {rop:.2f} unidades")
    print("-" * 35)
    print(f"Costo Anual de Ordenar: ${costo_ordenar:,.2f} USD")
    print(f"Costo Anual de Mantener: ${costo_mantener:,.2f} USD")
    print(f"Costo Total Anual (con compra): ${costo_total:,.2f} USD")
    
    return Q_optimo, rop, tiempo_entre_pedidos


# Datos del ejercicio 3.3
D = 10000              # Demanda anual
S = 150                # Costo por realizar un pedido
H = 3                  # Costo de mantener una unidad al año
C = 25                 # Costo por unidad
dias_lab = 250         # Días laborables al año
L = 5                  # Tiempo de espera del proveedor

Q_opt, rop_val, t_ciclo = resolver_eoq(
    D, S, H, C, dias_lab, L
)

num_ciclos = 3
tiempo = np.linspace(0, num_ciclos * t_ciclo, 500)
inventario = []

for t in tiempo:
    tiempo_en_ciclo = t % t_ciclo
    demanda_diaria = D / dias_lab
    inv = Q_opt - (demanda_diaria * tiempo_en_ciclo)
    inventario.append(inv)

plt.figure(figsize=(10, 5))
plt.plot(tiempo, inventario, color="navy", linewidth=2)
plt.axhline(
    y=rop_val,
    color="red",
    linestyle="--",
    label=f"Punto de reorden: {rop_val:.0f} unidades"
)
plt.axhline(y=0, color="black", linewidth=0.8)

plt.title("Simulación de Inventario: Modelo EOQ")
plt.xlabel("Días laborables")
plt.ylabel("Unidades en almacén")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
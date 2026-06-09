import pulp

problema = pulp.LpProblem("Minimizar_Costo_Almacenamiento", pulp.LpMinimize)

x = pulp.LpVariable("Almacenamiento_Estandar", lowBound=0)
y = pulp.LpVariable("Almacenamiento_Premium", lowBound=0)


problema += 20*x + 60*y, "Costo_Total"

problema += x + 3*y >= 15, "Velocidad_Minima"
problema += 2*x + 2*y >= 14, "Retencion_Minima"

problema.solve()

print("Estado:", pulp.LpStatus[problema.status])
print("TB de almacenamiento Estándar:", x.varValue)
print("TB de almacenamiento Premium:", y.varValue)
print("Costo mínimo mensual:", pulp.value(problema.objective))
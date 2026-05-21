import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Firewall_Optimization", pulp.LpMaximize)

# 2. Variables de decisión
x = pulp.LpVariable("Inspeccion_Basica", lowBound=0, cat='Continuous')
y = pulp.LpVariable("Inspeccion_Profunda", lowBound=0, cat='Continuous')

# 3. Función objetivo
model += 2 * x + 5 * y, "Seguridad_Total"

# 4. Restricciones

# CPU disponible
model += x + 3 * y <= 18, "CPU_Limit"

# RAM disponible
model += x + y <= 8, "RAM_Limit"

# 5. Resolver
model.solve()

# 6. Resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"GB con Inspección Básica: {x.varValue}")
print(f"GB con Inspección Profunda: {y.varValue}")
print(f"Puntos máximos de seguridad: {pulp.value(model.objective)}")
import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Computer_Assembly_Optimization", pulp.LpMaximize)

# 2. Definir Variables
# Son enteras porque no se pueden ensamblar medias computadoras
x = pulp.LpVariable("Escritorios", lowBound=0, cat='Integer')
y = pulp.LpVariable("Laptops", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 2000 * x + 4000 * y, "Ganancia_Total"

# 4. Restricciones

# Restricción de microprocesadores
model += x + y <= 60, "Procesadores_Disponibles"

# Restricción de horas de trabajo
model += x + 3 * y <= 100, "Horas_Trabajo"

# 5. Resolver el modelo
model.solve()

# 6. Mostrar resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Computadoras de Escritorio: {x.varValue}")
print(f"Laptops: {y.varValue}")
print(f"Ganancia Máxima: ${pulp.value(model.objective)} MXN")
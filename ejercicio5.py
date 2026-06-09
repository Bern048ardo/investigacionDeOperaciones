import pulp

model = pulp.LpProblem("Cluster_Optimization", pulp.LpMaximize)

x = pulp.LpVariable("Backend", lowBound=0, upBound=6, cat='Integer')
y = pulp.LpVariable("Data_Workers", lowBound=0, upBound=7, cat='Integer')

model += 300 * x + 250 * y, "Rendimiento_Total"

model += 2 * x + y <= 16, "RAM_Limit"

model += x + 2 * y <= 17, "SSD_Limit"

model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Contenedores Backend: {x.varValue}")
print(f"Contenedores Data Workers: {y.varValue}")
print(f"Rendimiento Máximo: ${pulp.value(model.objective)} USD/hora")
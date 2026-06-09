import pulp

model = pulp.LpProblem("VideoGame_Assets", pulp.LpMaximize)

x = pulp.LpVariable("Personajes", lowBound=0)
y = pulp.LpVariable("Escenarios", lowBound=0)

model += 80*x + 60*y

model += 2*x + y <= 12
model += x + 2*y <= 14

model.solve()

print("Estado:", pulp.LpStatus[model.status])
print("Personajes:", x.varValue)
print("Escenarios:", y.varValue)
print("Valor máximo: $", pulp.value(model.objective))
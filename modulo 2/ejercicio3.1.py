from scipy.optimize import minimize

def costo(v):
    x, y = v
    return x**2 + y**2 + x*y + 3000*x + 4500*y + 6000
limites=[(0,None),(0,None)]
iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    print(f"Iteración {iteracion[0]}: x={v[0]:.4f}, y={v[1]:.4f}, costo={costo(v):.4f}")

resultado = minimize(
    costo,
    x0=[0, 0],
    method='BFGS',
    callback=mostrar_avance
)

print("\nResultado final:")
print("x =", resultado.x[0])
print("y =", resultado.x[1])
print("Costo mínimo =", resultado.fun)

# Actividad en clase:
# resultado.x representa la combinación de producción (x, y) que minimiza el costo.
# resultado.fun representa el costo mínimo alcanzado.
#
# Comparar con otros métodos de optimización.
#
# Probar cambiando el valor inicial a [1000, 1000] y observar el comportamiento.
#
# Probar cambiando el valor inicial a [0.1, 0.1] y observar el comportamiento.
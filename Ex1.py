import numpy as np

# Función que define f(x)
def f(x):
    return x * np.exp(-x**2)

# Límite superior para la integral
R = 10000

# Número de muestras
N = 10000000

# Paso 1: Encuentra la constante de normalización c
c = 1 / np.trapz(f(np.linspace(-R, R, 1000)), np.linspace(-R, R, 1000))

# Paso 2: Genera valores aleatorios utilizando el método de transformada inversa
u_values = np.random.rand(N)
x_values = np.sqrt(-np.log(1 - u_values) / 2)

# Paso 3: Estima la integral
integral_estimate = np.mean(f(x_values) / c)

# Paso 4: Toma el límite cuando R tiende a infinito
integral_estimate *= 2  # Multiplicamos por 2 porque la integral es simétrica

print("Estimación de la integral:", integral_estimate)
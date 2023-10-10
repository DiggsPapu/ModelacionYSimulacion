import matplotlib.pyplot as plt
import numpy as np
import random

# Define las funciones afines
def f1(x, y):
    return (0.5 * (x - y), 0.5 * (x + y))

def f2(x, y):
    return (0.5 * (-x - y) + 1, 0.5 * (x - y))

# Punto inicial
x, y = 0, 0

# Número de iteraciones
num_iteraciones = 1000000

# Listas para almacenar los puntos generados
x_vals = []
y_vals = []

for _ in range(num_iteraciones):
    # Elige una función al azar con probabilidades iguales
    random_choice = random.choice([f1, f2])

    # Aplica la función seleccionada al punto actual
    x, y = random_choice(x, y)

    # Agrega el punto a las listas
    x_vals.append(x)
    y_vals.append(y)

# Grafica los puntos generados
plt.scatter(x_vals, y_vals, s=1, c='blue', marker='.')
plt.title('Fractal IFS')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Ex1.jpg', format='jpg')
plt.show()

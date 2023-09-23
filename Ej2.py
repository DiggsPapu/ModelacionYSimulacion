import numpy as np
import matplotlib.pyplot as plt

def rk4(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(n):
        k1x = h * f(x_values[-1], y_values[-1])[0]
        k1y = h * f(x_values[-1], y_values[-1])[1]
        
        k2x = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k1y)[0]
        k2y = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k1y)[1]
        
        k3x = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k2y)[0]
        k3y = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k2y)[1]
        
        k4x = h * f(x_values[-1] + h, y_values[-1] + k3y)[0]
        k4y = h * f(x_values[-1] + h, y_values[-1] + k3y)[1]
        
        x_new = x_values[-1] + (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        y_new = y_values[-1] + (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        
        x_values.append(x_new)
        y_values.append(y_new)
    
    return x_values, y_values

# Inciso a)
def f_a(x, y):
    dxdt = -x + y
    dydt = 4 * x - y
    return dxdt, dydt

x0_a, y0_a = -1, 1
h_a = 0.1
n_a = 100

x_values_a, y_values_a = rk4(f_a, x0_a, y0_a, h_a, n_a)

# Imprimir los valores de x y y para el inciso a)
print("Inciso a)")
for i, (x, y) in enumerate(zip(x_values_a, y_values_a)):
    print(f"n={i}, x={x}, y={y}")


# Campo vectorial para el inciso a)
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
dx, dy = f_a(X, Y)

plt.figure()
plt.quiver(X, Y, dx, dy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo Vectorial para el Sistema a)')
plt.show()

# Inciso b)
def f_b(x, y):
    dxdt = -x + y
    dydt = -y
    return dxdt, dydt

x0_b, y0_b = 1, 1
h_b = 0.1
n_b = 100

x_values_b, y_values_b = rk4(f_b, x0_b, y0_b, h_b, n_b)

# Imprimir los valores de x y y para el inciso b)
print("\nInciso b)")
for i, (x, y) in enumerate(zip(x_values_b, y_values_b)):
    print(f"n={i}, x={x}, y={y}")


# Campo vectorial para el inciso b)
dx, dy = f_b(X, Y)

plt.figure()
plt.quiver(X, Y, dx, dy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo Vectorial para el Sistema b)')
plt.show()

# Inciso c)
def f_c(x, y):
    dxdt = -x + y
    dydt = -9 * x - y
    return dxdt, dydt

x0_c, y0_c = 1, 1
h_c = 0.1
n_c = 100

x_values_c, y_values_c = rk4(f_c, x0_c, y0_c, h_c, n_c)

# Imprimir los valores de x y y para el inciso c)
print("\nInciso c)")
for i, (x, y) in enumerate(zip(x_values_c, y_values_c)):
    print(f"n={i}, x={x}, y={y}")


# Campo vectorial para el inciso c)
dx, dy = f_c(X, Y)

plt.figure()
plt.quiver(X, Y, dx, dy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo Vectorial para el Sistema c)')
plt.show()

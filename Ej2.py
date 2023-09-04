import numpy as np
import matplotlib.pyplot as plt

# Función para generar variables aleatorias de una distribución discreta (Poisson) utilizando transformada inversa
def generate_discrete_random_variable(lambda_value, n):
    u = np.random.uniform(0, 1, n)
    poisson_values = -np.log(u) / lambda_value
    return np.floor(poisson_values).astype(int)

# Función para generar variables aleatorias de una distribución continua (Exponencial) utilizando aceptación y rechazo
def generate_continuous_random_variable(scale, n):
    result = []
    while len(result) < n:
        x = np.random.exponential(scale)
        u = np.random.uniform(0, 1)
        if u < np.exp(-x / scale):
            result.append(x)
    return np.array(result)

# Función para calcular las medias aritméticas parciales
def calculate_partial_means(data):
    n = len(data)
    partial_means = np.cumsum(data) / np.arange(1, n + 1)
    return partial_means

# Configuración de parámetros
n_simulations = 1000000  # Número de simulaciones
lambda_value = 3.0  # Parámetro lambda para la distribución Poisson
scale_value = 2.0  # Parámetro de escala para la distribución Exponencial

# Generar variables aleatorias y calcular las medias parciales
discrete_data = generate_discrete_random_variable(lambda_value, n_simulations)
continuous_data = generate_continuous_random_variable(scale_value, n_simulations)

partial_means_discrete = calculate_partial_means(discrete_data)
partial_means_continuous = calculate_partial_means(continuous_data)

# Calcular la media verdadera para comparar
true_mean_discrete = np.mean(discrete_data)
true_mean_continuous = np.mean(continuous_data)


# Graficar los resultados
plt.figure(figsize=(12, 6))

# Distribución discreta
plt.subplot(1, 2, 1)
plt.plot(range(1, n_simulations + 1), partial_means_discrete, label='Medias Parciales')
plt.axhline(y=true_mean_discrete, color='r', linestyle='--', label='Media Verdadera')
plt.title('Distribución Discreta (Poisson)')
plt.xlabel('n')
plt.ylabel('Media Parcial')
plt.legend()

# Distribución continua
plt.subplot(1, 2, 2)
plt.plot(range(1, n_simulations + 1), partial_means_continuous, label='Medias Parciales')
plt.axhline(y=true_mean_continuous, color='r', linestyle='--', label='Media Verdadera')
plt.title('Distribución Continua (Exponencial)')
plt.xlabel('n')
plt.ylabel('Media Parcial')
plt.legend()

plt.tight_layout()
plt.show()

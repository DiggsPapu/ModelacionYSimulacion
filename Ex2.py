import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros
mu = 0.5
sigma = np.sqrt(1/12)  # Varianza de la distribución uniforme en (0,1)

# n y N
n_values = [20, 40, 60, 80, 100]
N_values = [50, 100, 1000, 10000]

# Función valores de la distribución uniforme
def generate_uniform(n):
    return np.random.uniform(0, 1, n)

# Simulación para cada combinación de n y N
for n in n_values:
    for N in N_values:
        sample_means = []
        for _ in range(N):
            sample = generate_uniform(n)
            sample_mean = np.mean(sample)
            sample_means.append((sample_mean - mu) / (sigma / np.sqrt(n)))

        # Gráficas de densidad normal estándar
        plt.figure()
        plt.hist(sample_means, bins=20, density=True, alpha=0.6, label="Histograma de valores simulados")
        x = np.linspace(-5, 5, 100)
        plt.plot(x, stats.norm.pdf(x, 0, 1), color='r', label="Densidad normal estándar")
        plt.title(f"n={n}, N={N}")
        plt.legend()
        plt.xlabel("Valores")
        plt.ylabel("Densidad")
        plt.show()

        # Función de distribución empírica y acumulada de N(0,1)
        plt.figure()
        x_sorted = np.sort(sample_means)
        y = np.arange(1, N+1) / N
        plt.plot(x_sorted, y, label="Distribución empírica")
        plt.plot(x, stats.norm.cdf(x, 0, 1), color='r', label="Distribución acumulada N(0,1)")
        plt.title(f"Función de distribución empírica vs N(0,1) - n={n}, N={N}")
        plt.legend()
        plt.xlabel("Valores")
        plt.ylabel("Probabilidad acumulada")
        plt.show()

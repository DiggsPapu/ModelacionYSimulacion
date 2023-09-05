import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Para la versión discreta (inciso IV.a)
def geom_pmf(k, p):
    return (1 - p)**(k - 1) * p

# Genera muestras de la distribución geométrica utilizando el método de aceptación y rechazo
def geom_accept_reject(N, p):
    samples = []
    max_val = p  
    while len(samples) < N:
        x_proposed = np.random.randint(1, 50)
        u = np.random.uniform(0, max_val)
        if u <= geom_pmf(x_proposed, p):
            samples.append(x_proposed)
    return samples


def exp_pdf(x, lam):
    return lam * np.exp(-lam * x)

def exp_inverse_transform_sampling(N, lam):
    u = np.random.uniform(0, 1, N)
    x = -np.log(1 - u) / lam
    return x

# Realiza un experimento dado n, N, y p
def perform_experiment(n, N, dist_type, param):
    # Inicializa las variables para almacenar los resultados
    means = []
    centered_means = []
    
    # Elige la distribución y establece las propiedades como la media y varianza
    if dist_type == 'discrete':
        # Media y varianza para la distribución geométrica
        mu = 1 / param
        sigma2 = (1 - param) / (param ** 2)
        sample_func = lambda N, p: geom_accept_reject(N, p)
    elif dist_type == 'continuous':
        # Media y varianza para la distribución exponencial
        mu = 1 / param
        sigma2 = 1 / (param ** 2)
        sample_func = lambda N, lam: exp_inverse_transform_sampling(N, lam)
    else:
        print("Tipo de distribución desconocido.")
        return
    
    sigma = np.sqrt(sigma2)
    
    # Genera las muestras y calcula las medias y medias centradas
    for _ in range(N):
        samples = sample_func(n, param)
        mean_sample = np.mean(samples)
        means.append(mean_sample)
        centered_mean = (mean_sample - mu) / (sigma / np.sqrt(n))
        centered_means.append(centered_mean)
    
    # Genera el histograma
    plt.figure()
    plt.hist(centered_means, bins=30, density=True, alpha=0.75, label="Muestras")
    x = np.linspace(-4, 4, 100)
    plt.plot(x, norm.pdf(x, 0, 1), 'r', label="N(0,1)")
    plt.title(f"Histograma para n = {n} y N = {N} ({dist_type})")
    plt.legend()
    plt.show()
    
    # Genera la gráfica de la función de distribución empírica
    plt.figure()
    sorted_data = np.sort(centered_means)
    yvals = np.arange(len(sorted_data)) / float(len(sorted_data))
    plt.plot(sorted_data, yvals, label="Función de distribución empírica")
    plt.plot(x, norm.cdf(x, 0, 1), 'r', label="CDF de N(0,1)")
    plt.title(f"Función de distribución empírica para n = {n} y N = {N} ({dist_type})")
    plt.legend()
    plt.show()
    
def main():
    # Ejecución para el inciso IV.a (distribución discreta)
    n_values = [20, 40, 60, 80, 100]
    N_values = [50, 100, 1000, 10000]
    p = 0.3
    for n in n_values:
        for N in N_values:
            perform_experiment(n, N, 'discrete', p)

    # Ejecución para el inciso IV.b (distribución continua)
    lam = 0.5
    for n in n_values:
        for N in N_values:
            perform_experiment(n, N, 'continuous', lam)

if __name__ == "__main__":
    main()

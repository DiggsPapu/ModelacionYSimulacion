import random
import math

#1. Calcular el valor esperado de una variable aleatoria exponencial con λ =1, utilizando el uso de variables antitéticas.

def exponential_rv(lmbda):
    return -1 / lmbda * math.log(1 - random.random())

def monte_carlo_antithetic(num_samples):
    total = 0
    for _ in range(num_samples // 2):
        u1 = random.random()
        u2 = 1 - u1
        x1 = exponential_rv(1)
        x2 = exponential_rv(1)
        total += (x1 + x2)
    return total / num_samples

num_samples = 10000
expected_value = monte_carlo_antithetic(num_samples)
print("Valor esperado (variables antitéticas):", expected_value)

#2. Calcular el valor esperado de una variable aleatoria exponencial con λ =1, utilizando el uso de variables de control.

def exponential_rv(lmbda):
    return -1 / lmbda * math.log(1 - random.random())

def control_variates(num_samples):
    total = 0
    for _ in range(num_samples):
        x = exponential_rv(1)
        y = x - 1  # Control variate
        total += x - 0.5 * y  # Adjusted value
    return total / num_samples

num_samples = 10000
expected_value = control_variates(num_samples)
print("Valor esperado (variables de control):", expected_value)

#3. Calcular el valor esperado de una variable aleatoria exponencial con λ = 1, utilizando el método estratificado. Se escogen tres estratos (intervalos) de 0 a 1, de 1 a 3 y de 3 a ∞.

def exponential_rv(lmbda):
    return -1 / lmbda * math.log(1 - random.random())

def stratified_sampling(num_strata):
    total = 0
    for i in range(num_strata):
        a = i / num_strata
        b = (i + 1) / num_strata
        u = random.uniform(a, b)
        x = exponential_rv(1)
        total += x / num_strata
    return total

num_strata = 3
expected_value = stratified_sampling(num_strata)
print("Valor esperado (método estratificado):", expected_value)

#4. Sea X variable aleatoria exponencial con media 1;y dado X=x, Y es una variable aleatoria exponencial con media x (X y Y son variables aleatorias dependientes). Dé una forma eficiente para estimar P(XY ≤ 3).

def exponential_rv(lmbda):
    return -1 / lmbda * math.log(1 - random.random())

def monte_carlo_probability(num_samples):
    count = 0
    for _ in range(num_samples):
        x = exponential_rv(1)
        y = exponential_rv(1/x)
        if x * y <= 3:
            count += 1
    probability = count / num_samples
    return probability

num_samples = 10000
estimated_probability = monte_carlo_probability(num_samples)
print("Estimación de P(XY ≤ 3):", estimated_probability)

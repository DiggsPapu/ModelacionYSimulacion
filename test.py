import numpy as np

# Función objetivo
def objective_function(x1, x2):
    return 3*x1 + 5*x2

# Restricción
def constraint1(x1, x2):
    return 3*x1 + 2*x2 - 18

# Algoritmo genético
def genetic_algorithm(population_size, num_generations, mutation_rate):
    # Rango de valores para x1 y x2
    x1_min, x1_max = 0, 6  # Asumiendo que x1 está en el rango [0, 6] para cumplir con la restricción
    x2_min, x2_max = 0, 9  # Asumiendo que x2 está en el rango [0, 9] para cumplir con la restricción

    # Inicialización de la población
    population = np.random.uniform(low=(x1_min, x2_min), high=(x1_max, x2_max), size=(population_size, 2))

    for generation in range(num_generations):
        # Evaluación de la aptitud de la población
        fitness = [objective_function(ind[0], ind[1]) for ind in population]

        # Selección de padres
        # Utilizaremos selección por torneo
        parents = []
        for _ in range(population_size):
            tournament_indices = np.random.choice(population_size, size=5)
            tournament_fitness = [fitness[i] for i in tournament_indices]
            parent_index = tournament_indices[np.argmax(tournament_fitness)]
            parents.append(population[parent_index])

        # Cruce (crossover)
        offspring = []
        for i in range(0, population_size, 2):
            parent1, parent2 = parents[i], parents[i+1]
            offspring.append([(parent1[0] + parent2[0]) / 2, (parent1[1] + parent2[1]) / 2])
            offspring.append([(parent1[0] + parent2[0]) / 2, (parent1[1] + parent2[1]) / 2])

        # Mutación
        for i in range(population_size):
            if np.random.random() < mutation_rate:
                offspring[i][0] += np.random.uniform(-0.1, 0.1)
                offspring[i][1] += np.random.uniform(-0.1, 0.1)
                offspring[i][0] = np.clip(offspring[i][0], x1_min, x1_max)
                offspring[i][1] = np.clip(offspring[i][1], x2_min, x2_max)

        # Evaluación de la aptitud de la descendencia
        offspring_fitness = [objective_function(ind[0], ind[1]) for ind in offspring]

        # Reemplazo de la población
        for i in range(population_size):
            if offspring_fitness[i] > fitness[i] and constraint1(offspring[i][0], offspring[i][1]) <= 0:
                population[i] = offspring[i]

        # Mostrar el mejor individuo de esta generación
        best_individual_index = np.argmax(fitness)
        best_fitness = fitness[best_individual_index]
        best_individual = population[best_individual_index]
        print(f"Generación {generation + 1}: Mejor fitness = {best_fitness}, Mejor individuo = {best_individual}")

    return best_individual

# Parámetros del algoritmo
population_size = 5000
num_generations = 100
mutation_rate = 0.4

# Ejecutar el algoritmo genético
best_solution = genetic_algorithm(population_size, num_generations, mutation_rate)
print("\nMejor solución encontrada:")
print("x1 =", best_solution[0])
print("x2 =", best_solution[1])
print("Valor de la función objetivo:", objective_function(best_solution[0], best_solution[1]))

import random


# Función de inicialización de individuos
def initialize_individual():
		x1 = random.uniform(0, 0)  # x1 está en el rango [0, 15]
		x2 = random.uniform(0, 0)  # x2 está en el rango [0, 15]
		return x1, x2

# Función de selección de padres (selección de torneo)
def select_parents(population, fitness_scores):
		idx1 = random.randint(0, len(population) - 1)
		idx2 = random.randint(0, len(population) - 1)
		if fitness_scores[idx1] > fitness_scores[idx2]:
				return population[idx1]
		else:
				return population[idx2]

# Función de cruce (cruce en un punto)
def crossover(parent1, parent2):
		crossover_point = random.randint(0, 1)
		child1 = (parent1[0], parent2[crossover_point])
		child2 = (parent2[0], parent1[crossover_point])
		return child1, child2

# Función de mutación (mutación por cambio aleatorio)
def mutate(individual, mutation_prob):
		if random.random() < mutation_prob:
				index = random.randint(0, 1)
				if index == 0:
						individual = (random.uniform(0, 15), individual[1])
				else:
						individual = (individual[0], random.uniform(0, 15))
		return individual


def genetic_algorithm(population_size, num_generations, mutation_probability, is_valid, fitness_function):
	# Inicializar la población inicial
	population = [initialize_individual() for _ in range(population_size)]
	while len(population) < 0:
		population = [initialize_individual() for _ in range(population_size)]

	# Bucle principal del algoritmo genético
	for generation in range(num_generations):
			# Calcular los valores de fitness para cada individuo y filtrar los inválidos
			valid_population = [ind for ind in population if is_valid(ind[0], ind[1])]
			fitness_scores = [fitness_function(ind[0], ind[1]) for ind in valid_population]

			# Seleccionar y crear una nueva población
			new_population = []
			for _ in range(population_size // 2):
					parent1 = select_parents(valid_population, fitness_scores)
					parent2 = select_parents(valid_population, fitness_scores)
					child1, child2 = crossover(parent1, parent2)
					child1 = mutate(child1, mutation_probability)
					child2 = mutate(child2, mutation_probability)
					new_population.extend([child1, child2])

			# Reemplazar la población anterior con la nueva población
			population = new_population

	# Encontrar el individuo con el mayor valor de fitness
	best_individual = max(population, key=lambda ind: fitness_function(ind[0], ind[1]))
	return best_individual



# Parámetros del algoritmo genético
population_size = 50
num_generations = 1000
mutation_probability = 0.1



# Ejercicio A
# Función que queremos maximizar: 15x1 + 30x2 + 4x1x2 - 2x1^2 - 4x2^2
def fitness_function(x1, x2):
    return 15*x1 + 30*x2 + 4*x1*x2 - 2*x1**2 - 4*x2**2

# Restricción: x1 + 2x2 <= 30
def is_valid(x1, x2):
    return x1 + 2 * x2 <= 30

best_individual = genetic_algorithm(population_size, num_generations, mutation_probability, is_valid, fitness_function)
print("Mejor solución encontrada A:")
print("x1 =", best_individual[0])
print("x2 =", best_individual[1])
print("Valor de la función objetivo:", fitness_function(best_individual[0], best_individual[1]))


# Ejercicio B
# Función que queremos maximizar: 3x + 5y
def fitness_function_b(x1, x2):
		return 3*x1 + 5*x2

# Restricciones: 3x1 + 2x2 <= 18, x1 >=0, x2 >= 0
def is_valid_b(x1, x2):
		return (((3*x1) + (2*x2)) <= 18) and x1 >= 0 and x2 >= 0

num_generations = 10000
population_size = 100
best_individual = genetic_algorithm(population_size, num_generations, mutation_probability, is_valid_b, fitness_function_b)
print("Mejor solución encontrada B:")
print("x1 =", best_individual[0])
print("x2 =", best_individual[1])
print("Valor de la función objetivo:", fitness_function_b(best_individual[0], best_individual[1]))

# # Ejercicio C
# Función que queremos maximizar: 5x1-x1^2+8x2-2x2^2
def fitness_function(x1, x2):
		return 5*x1 - x1**2 + 8*x2 - 2*x2**2

# Restricciones: 3x1 + 2x2 <= 6
def is_valid(x1, x2):
		return 3*x1 + 2*x2 <= 6 and x1 >=0 and x2 >= 0

num_generations = 100
population_size = 100
best_individual = genetic_algorithm(population_size, num_generations, mutation_probability, is_valid, fitness_function)
print("Mejor solución encontrada C:")
print("x1 =", best_individual[0])
print("x2 =", best_individual[1])
print("Valor de la función objetivo:", fitness_function(best_individual[0], best_individual[1]))


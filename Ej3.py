from pulp import *

def maximizar(variables, funcion_objetivo_coeficientes, restricciones_coeficientes, valores_restricciones):
    # Definir el problema
    problema = LpProblem("Problema_Primal", LpMaximize)
    # Crear variables
    var_dict = {var: LpVariable(var, lowBound=0) for var in variables}
    # Definir la función objetivo
    funcion_objetivo = sum(coef * var_dict[var] for coef, var in zip(funcion_objetivo_coeficientes, variables))
    problema += funcion_objetivo
    # Crear restricciones
    for i, coeficientes in enumerate(restricciones_coeficientes):
        restriccion = sum(coef * var_dict[var] for coef, var in zip(coeficientes, variables))
        operador = "<=" if valores_restricciones[i] >= 0 else ">="  # Cambiar a ">=" si el valor es negativo
        problema += restriccion <= valores_restricciones[i], f'Restriccion_{i} ({operador} {valores_restricciones[i]})'
    # Mostrar el problema
    print(problema)
    # Resolver el problema
    solution = problema.solve()
    # Generar el optimo
    assert solution == LpStatusOptimal
    # Imprimir los valores optimos
    for var in var_dict:
        print('Valores optimos {}={}'.format(var_dict[var].name, var_dict[var].value()))    
    # Devolver el valor óptimo de la maximización
    print("Maximizacion: "+str(value(problema.objective)))

# Ejercicio 3.a
variables = ['x1', 'x2', 'x3']
funcion_objetivo_coeficientes = [1, -1, 1]
restricciones_coeficientes = [
    [1, 1, 2],
    [2, 1, 1],
    [2, -1, 3],
    [1, 2, 5]
]
valores_restricciones = [5, 7, 8, 9]
maximizar(variables, funcion_objetivo_coeficientes, restricciones_coeficientes, valores_restricciones)


# Ejercicio 3.b
variables = ['x1', 'x2', 'x3', 'x4']
funcion_objetivo_coeficientes = [5, 7, 15, 6]
restricciones_coeficientes = [
    [1, 2, 0, 1],
    [1, 3, 1, 0],
    [1, 4, 3, 2],
    [1, 0, 5, 3]
]
valores_restricciones = [1, 2, 3, 4]
maximizar(variables, funcion_objetivo_coeficientes, restricciones_coeficientes, valores_restricciones)


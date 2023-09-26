import numpy as np
from scipy.optimize import linprog


def problemaMaximizacion(funcionObjetivo=[1,1,1], 
                         restriccionesIzquierdo =[
                        [1,1,1],
                        [1,1,1],
                        [1,1,1]
                        ],
                        restriccionesDerecho=[1,1,1],
                        limites=[0,0,0]):
    
    # Coeficientes de la función objetivo
    c = np.array(funcionObjetivo)
    # Coeficientes de las restricciones (matriz A), de manera que da las ecuaciones de forma: x1+x2+x3<=
    A = np.array(restriccionesIzquierdo)
    # Lados derecho de las restricciones son la otra parte de la desigualdad es el <=n
    b = np.array(restriccionesDerecho)
    # Definir los límites de las variables (x >= 0, y >= 0, z>=0)
    limites = [(i,None) for i in limites]
    # Resolver el problema primal
    result_primal = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')
    # Imprimir resultados
    print("Problema Primal maximizar x1-x2+x3:")
    print("Status:", result_primal.message)
    print("x1 =", result_primal.x[0])
    print("x2 =", result_primal.x[1])
    print("x3 =", result_primal.x[2])
    print("Valor óptimo =", -result_primal.fun)
    
c = np.array([1,-1,1])


A = np.array([
    [1,1,2],
    [2,1,1],
    [2,-1,3],
    [1,2,5]
    
])


b = np.array([5,7,8,9])

x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)

# Resolver el problema primal
result_primal = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='highs')

# Imprimir resultados
print("Problema Primal maximizar x1-x2+x3:")
print("Status:", result_primal.message)
print("x1 =", result_primal.x[0])
print("x2 =", result_primal.x[1])
print("x3 =", result_primal.x[2])
print("Valor óptimo =", -result_primal.fun)

problemaMaximizacion([1,-1,1],[
    [1,1,2],
    [2,1,1],
    [2,-1,3],
    [1,2,5]
    ],[5,7,8,9],[0,0,0])
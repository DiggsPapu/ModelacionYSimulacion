import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def diamond_square(n, roughness):
    size = 2 ** n + 1
    terrain = np.zeros((size, size), dtype=float)  # Inciso a
    
    # Inciso b: Inicializa las esquinas con valores aleatorios
    terrain[0, 0] = np.random.rand()
    terrain[0, size - 1] = np.random.rand()
    terrain[size - 1, 0] = np.random.rand()
    terrain[size - 1, size - 1] = np.random.rand()
    
    step_size = size - 1
    scale = roughness
    
    #  C pasos aleternados 
    while step_size > 1:
        half_step = step_size // 2
        
        # Inciso D: Paso Diamond
        for y in range(half_step, size - 1, step_size):
            for x in range(half_step, size - 1, step_size):
                avg = (
                    terrain[y - half_step, x - half_step] +
                    terrain[y - half_step, x + half_step] +
                    terrain[y + half_step, x - half_step] +
                    terrain[y + half_step, x + half_step]
                ) / 4.0
                terrain[y, x] = avg + np.random.uniform(-scale, scale)
        
        # Inciso e: Paso Square
        for y in range(0, size, half_step):
            for x in range((y + half_step) % step_size, size, step_size):
                total = 0
                count = 0
                
                if y >= half_step:
                    total += terrain[y - half_step, x]
                    count += 1
                if y < size - half_step:
                    total += terrain[y + half_step, x]
                    count += 1
                if x >= half_step:
                    total += terrain[y, x - half_step]
                    count += 1
                if x < size - half_step:
                    total += terrain[y, x + half_step]
                    count += 1
                
                avg = total / count
                terrain[y, x] = avg + np.random.uniform(-scale, scale)
        
        # Inciso f: Reduce la magnitud del valor aleatorio
        scale *= roughness
        step_size //= 2
    
    return terrain

n = 8  # Ajustar el valor de n para la resolución del terreno
roughness = 0.6  # Ajustar el valor de roughness para controlar la rugosidad

terrain = diamond_square(n, roughness)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(0, terrain.shape[0] - 1, terrain.shape[0])
y = np.linspace(0, terrain.shape[1] - 1, terrain.shape[1])
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, terrain, cmap='viridis')

plt.show()

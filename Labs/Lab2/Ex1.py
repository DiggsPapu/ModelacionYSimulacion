# Guillermo Santos 191517
# Diego Alonzo 20172
from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np
# Generate an array of 1*10^6 random variates from the uniform distribution [0, 1]
y = uniform.rvs(loc=0, scale=1  , size=1000000)
# Calculate the partial arithmetic mean of each one of the values, it means it will do an acumulative sum. Acumulative sum of probability divided by a million to get the partial.
y = np.cumsum(y)/np.arange(1, 1000000 + 1)
# Graph Partial Mean
plt.plot(np.arange(1, 1000000 + 1), y, label = "Medias Parciales" )
# Graph Real mean
plt.plot(np.arange(1, 1000000 + 1), np.full(1000000,0.5), label ="Media Real")
plt.xlabel("Muestra (n)")
plt.ylabel("Media")
plt.title("Ley debil de los grandes numeros")
plt.legend()
plt.show()

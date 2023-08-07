# Diego Andres Alonzo Medinilla 20172
# Guillermo
import numpy as np
import matplotlib.pyplot as plt
sum = 0
probs = []
rang = []
for x in range(0,1000000):
    probs.append(np.random.random_sample())
    rang.append(x)
    sum+= probs[x]
print("Promedio: "+str(sum))
plt.plot(rang, probs)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Ley debil de los grandes numeros')
plt.show()
# for x in probs:
#     print(x)
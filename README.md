# Lab 4 

## Autores

- Guillermo Santos
- Kenneth Galvez
- Diego Alonzo
- Luis Pedro Gonzalez 

## Simulaciones 


### I. Simulación de selección de estudiantes
Problema:

En una clase de modelación y simulación hay 1,000,000 estudiantes distribuidos de la siguiente manera:

- 400,000 son mujeres
- 300,000 personas usan lentes
- 150,000 varones usan lentes

#### Preguntas

- Si se selecciona al azar un estudiante, ¿cuál es la probabilidad de que sea mujer y use gafas?
- Si se selecciona a alguien que no usa lentes, ¿cuál es la probabilidad de que sea varón?


Nota: La generación de variables aleatorias debe realizarse con los procedimientos vistos en clase. Es decir, utilizar el método de transformada inversa o aceptación y rechazo.


### II. Simulación con distribuciones de probabilidad
#### a) Distribución discreta

Seleccione una distribución de probabilidad discreta de su preferencia, especificando valores numéricos para sus parámetros. Genere $n=1,000,000$ valores independientesal azar $x_1, ..., x_n$ de esta distribución y calcule las medias aritméticas parciales $s_n = \frac{1}{n}\sum_{i=1}^n{x_i}, n=1, 2, ..., 1000000$


Grafique la función $n\rightarrow s_n$ uniendo los valores con una línea recta. Sea $\mu$ la media de la distribución. Trace en la misma gráfica la función constante $\mu$ y verifique graficamente que la función $n\rightarrow s_n$ oscila y se aproxima al valor $\mu$ conforme crece. 

#### b)Realice lo mismo que el inciso a), pero con una distribución continua de su preferencia.

Nota: La generación de variables aleatorias debe realizarse con los procedimientos vistos en clase. Es decir, utilizar el método de transformada inversa o aceptación y rechazo. En el caso II.b), favor no utilizar la distribución uniforme.

### III. Estime el valor de la integral, realizando una simulación

$$\int_{-\infty}^{\infty}{xe^{-x^2}dx}$$

Nota: La generación de variables aleatorias debe realizarse con los procedimientos vistos en clase. Es decir, utilizar el método de transformada inversa o aceptación y rechazo.


### IV. Realice la siguiente simulación

#### a) Selecciona una distribución de probabilidad discreta diferente del inciso II.a).

Sea $\mu$ la media de la distribución y sesa $\sigma^2$ su varianza. Lleve a cabo las indicaciones de los siguientes incisos para: 

- $n=20, 40, 60, 80, 100$
- $N = 50, 100, 1000, 10000$

1. Genere n valores independientes al azar $x_1, ..., x_n$ y calcule la media aritmética $s_n = \frac{1}{n}b)\sum_{i=1}^nx_i$ 
2. Repita N veces el inciso anterior calculando los promedios centrados $\frac{s_n - \mu}{\sigma / \sqrt{n}}$
3. Elabore un histograma de estos N valores, trazando en la misma gráfica, la función de densidad normal estándar N(0,1). Utilice un tamaño adecuado para la base de los rectángulos.
4. Elabore una gráfica de la frecuencia relativa acumulada (función de distribución empírica) de los N valores uniendo los puntos con una línea recta y en la misma gráfica dibuje la función de distribución acumulada de N(0,1).

#### b)elecciona una distribución de probabilidad continua diferente del inciso II.b) y diferente la distribución uniforme.

Sea $\mu$ la media de la distribución y sea $\sigma^2$ su varianza. Lleve a cabo las indicaciones de los siguientes incisos para: 

- $n = n=20, 40, 60, 80, 100$
- $N=50, 100, 1000, 10000$


1. Genere n valores independientes al azar $x_1, ..., x_n$ y calcule la media aritmética $s_n = \frac{1}{n}b)\sum_{i=1}^nx_i$.
2. Repita N veces el inciso anterior calculando los promedios centrados $\frac{s_n - \mu}{\sigma / \sqrt{n}}$
3. Elabore un histograma de estos N valores, trazando en la misma gráfica, la función de densidad normal estándar N(0,1). Utilice un tamaño adecuado para la base de los rectángulos.
4. Elabore una gráfica de la frecuencia relativa acumulada (función de distribución empírica) de los N valores uniendo los puntos con una línea recta y en la misma gráfica dibuje la función de distribución acumulada de N(0,1).

Nota: La generación de variables aleatorias debe realizarse con los procedimientos vistos en clase. Es decir, utilizar el método de transformada inversa o aceptación y rechazo.

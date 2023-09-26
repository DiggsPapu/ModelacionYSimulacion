import numpy as np
from sympy import symbols, diff, lambdify



def adam_optimizer_minimize(objective_grad, lr=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8, max_iter=1000):
    x = np.array([0.0, 0.0])
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    t = 0
    
    for _ in range(max_iter):
        t += 1
        grad = objective_grad(x)
        m = beta1 * m + (1 - beta1) * grad
        v = beta2 * v + (1 - beta2) * grad ** 2
        m_hat = m / (1 - beta1 ** t)
        v_hat = v / (1 - beta2 ** t)
        x = x - lr * m_hat / (np.sqrt(v_hat) + epsilon)
        
    return x


def adam_optimizer_maximize(objective_grad, lr=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8, max_iter=1000):
    x = np.array([0.0, 0.0])
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    t = 0
    
    for _ in range(max_iter):
        t += 1
        grad = -objective_grad(x)  # Cambiamos el signo del gradiente para maximizar
        m = beta1 * m + (1 - beta1) * grad
        v = beta2 * v + (1 - beta2) * grad ** 2
        m_hat = m / (1 - beta1 ** t)
        v_hat = v / (1 - beta2 ** t)
        x = x - lr * m_hat / (np.sqrt(v_hat) + epsilon)
        
    return x

########################################################
########################################################
###############         INCISO A         ###############
########################################################
########################################################
def gradient_function_a():
    x1, x2 = symbols("x1 x2")
    polynomial = ((x1-10)**2/25) + ((x2-20)**2/16)

    gradient_expr = [diff(polynomial, var) for var in (x1, x2)]

    gradient_func = lambdify((x1, x2), gradient_expr, 'numpy')

    return gradient_func
    

def inciso_a():
    grad_func = gradient_function_a()

    objective_grad = lambda x: np.array(grad_func(x[0], x[1]))

    x_opt = adam_optimizer_minimize(objective_grad)
    print("Inciso A")
    print(x_opt)

########################################################
########################################################
###############         INCISO B         ###############
########################################################
########################################################
def gradient_function_b():
    x1, x2 = symbols("x1 x2")
    polynomial = 5* x1 - x1**2 + 8*x2**2 - 2* x2**2

    gradient_expr = [diff(polynomial, var) for var in (x1, x2)]

    gradient_func = lambdify((x1, x2), gradient_expr, 'numpy')

    return gradient_func

def inciso_b():
    grad_func = gradient_function_b()

    objective_grad = lambda x: np.array(grad_func(x[0], x[1]))

    x_opt = adam_optimizer_maximize(objective_grad)
    print("Inciso B")
    print(x_opt)
########################################################
########################################################
###############         INCISO C         ###############
########################################################
########################################################
def gradient_function_c():
    x1, x2 = symbols("x1 x2")
    polynomial = 15*x1 + 30 * x2 + 4*x1 * x2  - 2 * x1**2 - 4 * x2 ** 2

    gradient_expr = [diff(polynomial, var) for var in (x1, x2)]

    gradient_func = lambdify((x1, x2), gradient_expr, 'numpy')

    return gradient_func

def inciso_c():
    grad_func = gradient_function_c()

    objective_grad = lambda x: np.array(grad_func(x[0], x[1]))

    x_opt = adam_optimizer_maximize(objective_grad)
    print("Inciso C")
    print(x_opt)

def main():

    inciso_a()
    inciso_b()
    inciso_c()


if __name__ == "__main__":
    main()
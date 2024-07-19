import numpy as np
import matplotlib.pyplot as plt

# Função f(x, y)
def f(x, y):
    return -y + x + 2

# Solução exata
def y_exact(x):
    return np.exp(-x) + x + 1

# Método de Euler
def euler(f, x0, y0, h, x_end):
    n = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
    return x, y

# Método de Runge-Kutta de 2ª ordem
def rk2(f, x0, y0, h, x_end):
    n = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h, y[i] + k1)
        y[i+1] = y[i] + 0.5 * (k1 + k2)
    return x, y

# Método de Runge-Kutta de 3ª ordem
def rk3(f, x0, y0, h, x_end):
    n = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1)
        k3 = h * f(x[i] + h, y[i] - k1 + 2*k2)
        y[i+1] = y[i] + (k1 + 4*k2 + k3) / 6
    return x, y

# Método de Runge-Kutta de 4ª ordem
def rk4(f, x0, y0, h, x_end):
    n = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1)
        k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return x, y

# Parâmetros
x0, y0 = 0, 2
h = 0.1
x_end = 1.0

# Solução numérica
x_euler, y_euler = euler(f, x0, y0, h, x_end)
x_rk2, y_rk2 = rk2(f, x0, y0, h, x_end)
x_rk3, y_rk3 = rk3(f, x0, y0, h, x_end)
x_rk4, y_rk4 = rk4(f, x0, y0, h, x_end)
x_exact = np.linspace(x0, x_end, 100)
y_exact_vals = y_exact(x_exact)

# Plot
plt.plot(x_exact, y_exact_vals, label='Solução Exata', color='black', linestyle='dashed')
plt.plot(x_euler, y_euler, label='Euler', marker='o')
plt.plot(x_rk2, y_rk2, label='Runge-Kutta 2ª ordem', marker='x')
plt.plot(x_rk3, y_rk3, label='Runge-Kutta 3ª ordem', marker='s')
plt.plot(x_rk4, y_rk4, label='Runge-Kutta 4ª ordem', marker='d')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Comparação dos Métodos Numéricos')
plt.grid()
plt.show()

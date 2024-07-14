import numpy as np

# Definindo as funções
def f1(x):
    return x * np.exp(x**2)

def f2(t):
    return 1 / (1 + t)

def f3(x):
    return x**2

# Método dos Trapézios Composta
def trapezoidal_comp(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Regra de Simpson 1/3
def simpson_1_3(f, a, b, n):
    if n % 2 == 1:
        n += 1  # n needs to be even
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * h)
    integral *= h / 3
    return integral

# Regra de Simpson 3/8
def simpson_3_8(f, a, b, n):
    if n % 3 != 0:
        n += 3 - (n % 3)  # n needs to be multiple of 3
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 3 * f(a + i * h)
    integral *= 3 * h / 8
    return integral

# Integral 1: \int_1^4 xe^{x^2} dx com 30 subintervalos
a1, b1, n1 = 1, 4, 30
I1_trapezoidal = trapezoidal_comp(f1, a1, b1, n1)
I1_simpson_1_3 = simpson_1_3(f1, a1, b1, n1)
I1_simpson_3_8 = simpson_3_8(f1, a1, b1, n1)

# Integral 2: \int_2^4 \frac{1}{1+t} dt com 300 subintervalos
a2, b2, n2 = 2, 4, 300
I2_trapezoidal = trapezoidal_comp(f2, a2, b2, n2)
I2_simpson_1_3 = simpson_1_3(f2, a2, b2, n2)
I2_simpson_3_8 = simpson_3_8(f2, a2, b2, n2)

# Quantidade de subintervalos necessários para \int_0^1 x^2 dx com quatro casas decimais corretas
a3, b3, true_value = 0, 1, 1/3
error_tolerance = 0.00005

n3 = 1
while True:
    I3_trapezoidal = trapezoidal_comp(f3, a3, b3, n3)
    error = abs(I3_trapezoidal - true_value)
    if error < error_tolerance:
        break
    n3 += 1

I1_trapezoidal, I1_simpson_1_3, I1_simpson_3_8, I2_trapezoidal, I2_simpson_1_3, I2_simpson_3_8, n3

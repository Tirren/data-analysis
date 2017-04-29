import matplotlib.pyplot as plt
import numpy as np

def f_x(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

A_1 = np.array([[1, 1], [1, 15]])
b_1 = np.array([f_x(1), f_x(15)])
np.linalg.solve(A_1, b_1)

poly_rank = 2
A_2 = np.array([[1**n for n in range(poly_rank + 1)],
                [8**n for n in range(poly_rank + 1)],
                [15**n for n in range(poly_rank + 1)]])
b_2 = np.array([f_x(1), f_x(8), f_x(15)])
np.linalg.solve(A_2, b_2)

poly_rank = 3
A_3 = np.array([[1**n for n in range(poly_rank + 1)],
                [4**n for n in range(poly_rank + 1)],
                [10**n for n in range(poly_rank + 1)],
                [15**n for n in range(poly_rank + 1)]])
b_3 = np.array([f_x(1), f_x(4), f_x(10), f_x(15)])
np.linalg.solve(A_3, b_3).round(2)


def f(x, c):
    return c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

c = [4.36264154, -1.29552587,  0.19333685, -0.00823565]
x = np.arange(0, 16, 0.5)
plt.plot(x, f_x(x), x, f(x, c))
plt.xlabel(r'$x$'), plt.ylabel(r'%f(x)$')
plt.grid(True)
plt.show()

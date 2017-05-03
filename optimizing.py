import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt

def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

x_min2 = optimize.minimize(f, [2], method='BFGS')
#print("{:.2f}".format(*x_min2.x))

x_min30 = optimize.minimize(f, [30], method='BFGS')
#print("{:.2f}".format(*x_min30.x))

x_devol = optimize.differential_evolution(f, [(1, 30)])
#print("{:.2f}".format(*x_devol.x))

def h(x):
    return np.trunc(f(x)) #h(x) = int(f(x))

x_min30_h = optimize.minimize(h, [30], method='BFGS')
#print("{:.2f}".format(*x_min30_h.x))

x_devol_h = optimize.differential_evolution(h, [(1, 30)])
#print("{:.2f}".format(*x_devol_h.x))

x = np.arange(1, 30, 0.4)
plt.plot(x, f(x), x, h(x))
plt.xlabel(r'$x$'), plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()

import numpy as np
​
def f(x, y):
    return y + 2 * x - x**2
​
x0 = 0
y0 = 1
​
x, h = np.linspace(x0, 1.5, 50, retstep=True)  # Note the optional argument to get the stepsize.
print(f'h = {h}')  #return h
​
y = np.zeros(x.shape)
y[0] = y0  #initial condition corresponding to x[0]
​
# Implementation of Euler's method
for n in range(0, len(x) - 1):
    y[n + 1] = y[n] + f(x[n], y[n]) * h #calculate via Euler
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(x, y, label='Euler')
plt.plot(x, x**2 + np.exp(x), 'r--', label='Analytical') #the ODE result using for comparsion
plt.xlabel('x')
plt.ylabel('y')
plt.legend() 

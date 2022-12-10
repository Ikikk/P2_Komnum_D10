import numpy as np
from sciPy import integrate
Gaussian = lambda x: np.exp(-x**2)

Romberg = integrate.romberg(Iter, 0, 3, show = True)
  
print(Romberg)
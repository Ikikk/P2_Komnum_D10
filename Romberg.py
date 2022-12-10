import numpy as np
from scipy import integrate
Gaussian = lambda x: np.exp(-x**2)

Romberg = integrate.romberg(Gaussian, 0, 3, show = True)
  
print(Romberg)
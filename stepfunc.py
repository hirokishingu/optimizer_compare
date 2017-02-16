import numpy as np
import matplotlib.pyplot as plt

def reluy(x):
  return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = reluy(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
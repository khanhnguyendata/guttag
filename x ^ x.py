from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, 2.1, 0.01)
y = [math.sqrt(n) for n in np.arange(0, 2.1, 0.01)]

plt.plot(x, y)
plt.show()
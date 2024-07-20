import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-3, 3, 0.1)


lines = plt.plot(t, np.sqrt(t), t, -np.sqrt(t))
plt.setp(lines, color='r', linewidth=3.5)
plt.show()

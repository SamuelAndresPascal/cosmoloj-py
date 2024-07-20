import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-3, 3, 0.1)

plt.plot(t)

plt.plot(t ** 2, linewidth=2.5)

line1, = plt.plot(t ** 3, '-')
line1.set_antialiased(False)

line2, = plt.plot(-t ** 3, '-')
line2.set_antialiased(True)

plt.show()

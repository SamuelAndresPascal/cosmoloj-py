import numpy as np
import matplotlib.pyplot as plt


a = np.arange(start=10, stop=30, step=5)
print(a)

# floating point step allowed but NOT RECOMMENDED
b = np.arange(start=0, stop=2, step=0.3)  # it accepts float arguments
print(b)

# use linspace instead of arange using floating point step !!
c = np.linspace(start=0, stop=2, num=9)
print(c)

x = np.linspace(start=0, stop=2 * np.pi, num=100)        # useful to evaluate function at lots of points

f = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x + 10, f)

plt.show()

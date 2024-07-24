import numpy as np
import matplotlib.pyplot as plt

rg = np.random.default_rng(1)

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2

mu, sigma = 2, 0.5

v = rg.normal(loc=mu, scale=sigma, size=10000)

# Plot a normalized histogram with 50 bins

fig, ax = plt.subplots()

ax.hist(v, bins=50, density=True)       # matplotlib version (plot)

# Compute the histogram with numpy and then plot it

(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)

ax.plot(.5 * (bins[1:] + bins[:-1]), n)

plt.show()

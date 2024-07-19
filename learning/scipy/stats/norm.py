from scipy import stats
import numpy as np

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = stats.norm.stats(moments='mvsk')

x = np.linspace(stats.norm.ppf(0.01), stats.norm.ppf(0.99), 100)
ax.plot(x, stats.norm.pdf(x), '-', lw=2, label='norm pdf', color='green')
ax.plot(x, stats.norm.cdf(x), '--', lw=2, label='norm cdf', color='green')
print(stats.norm.stats(moments='mvsk'))

x = np.linspace(stats.norm.ppf(0.01, loc=0.3, scale=2), stats.norm.ppf(0.99, loc=0.3, scale=2), 100)
ax.plot(x, stats.norm.pdf(x, loc=0.3, scale=2), '-', lw=2, label='norm pdf', color='blue')
ax.plot(x, stats.norm.cdf(x, loc=0.3, scale=2), '--', lw=2, label='norm cdf', color='blue')
print(stats.norm.stats(moments='mvsk', loc=0.3, scale=2))

x = np.linspace(stats.norm.ppf(0.01, loc=2.3, scale=0.5), stats.norm.ppf(0.99, loc=2.3, scale=0.5), 100)
ax.plot(x, stats.norm.pdf(x, loc=2.3, scale=0.5), '-', lw=2, label='norm pdf', color='red')
ax.plot(x, stats.norm.cdf(x, loc=2.3, scale=0.5), '--', lw=2, label='norm cdf', color='red')
print(stats.norm.stats(moments='mvsk', loc=2.3, scale=0.5))

plt.show()

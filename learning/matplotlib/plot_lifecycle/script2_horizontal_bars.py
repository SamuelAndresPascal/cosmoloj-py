import matplotlib.pyplot as plt

from learning.matplotlib.plot_lifecycle.data import group_data, group_names

fig, ax = plt.subplots()
ax.barh(group_names, group_data)

plt.show()

import matplotlib.pyplot as plt

from learning.matplotlib.plot_lifecycle.data import group_data, group_names

print(plt.style.available)

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.barh(group_names, group_data)


plt.show()

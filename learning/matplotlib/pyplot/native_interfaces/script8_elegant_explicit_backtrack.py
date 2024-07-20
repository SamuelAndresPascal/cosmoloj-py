import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].plot([1, 2, 3], [0, 0.5, 0.2])
axs[1].plot([3, 2, 1], [0, 0.5, 0.2])
fig.suptitle('Explicit Interface')
for i in range(2):
    axs[i].set_xlabel(f'Boo {i + 1}')

plt.show()

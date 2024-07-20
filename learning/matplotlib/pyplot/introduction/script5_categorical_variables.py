import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 6))

plt.subplot(141)
plt.bar(names, values)
plt.subplot(143)
plt.scatter(names, values)
plt.subplot(244)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

import numpy as np

time = np.linspace(start=20, stop=145, num=5)  # time scale

data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series

print(time)

print(data)

# index of the maxima for each series
ind = data.argmax(axis=0)

print(ind)

# times corresponding to the maxima
time_max = time[ind]

data_max = data[ind, range(data.shape[1])]  # => data[ind[0], 0], data[ind[1], 1]...

print(time_max)

print(data_max)

np.all(data_max == data.max(axis=0))

import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(year=2023, month=1, day=1)
end = datetime.datetime(year=2026, month=1, day=1)
date = start

yearlies = {}
while date != end:
    print(date)
    if date.year not in yearlies.keys():
        yearlies[date.year] = []
    yearlies[date.year].append(date)
    date += datetime.timedelta(days=1)

plt.plot(yearlies[2023], [x.day for x in yearlies[2023]])
plt.plot(yearlies[2024], [x.day * 3 for x in yearlies[2024]])
plt.plot(yearlies[2023], [x.day * 2 for x in yearlies[2025]])
plt.show()
print("toto")

import numpy as np
import matplotlib.pyplot as plt

pop = [45, 35, 25, 15]

year = [1987, 1988, 1989, 1990]
names = ['Jabu', 'Sthe', 'Dani', 'Deli']
xLab = 'Year'
yLab = 'Names'
title = 'Birthday Projections'
tickVal = [1975, 1980, 1985, 1990, 1995, 2000]
tickLab = ["'75", "'80", "'85", "'90", "'95", "'00"]

plt.scatter(year, names, s=np.array(pop) * 2, c='black')

plt.xlabel(xLab)
plt.ylabel(yLab)
plt.title(title)
plt.xticks(tickVal, tickLab)

plt.grid(True)

plt.show()
plt.savefig('scatter.png')
plt.clf()

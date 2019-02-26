import matplotlib.pyplot as plt

year = [1987, 1988, 1989, 1990]
year = [1960, 1970, 1980] + year

names = ['Jabu', 'Sthe', 'Dani', 'Deli']
names = ['Gogos', 'Aunts', 'Uncles'] + names

# print(year[-1])
# print(names[-1])
plt.plot(year, names)
plt.xlabel('Year')
plt.ylabel('Names')
plt.title('Birthday Projections')
# plt.yticks([])
plt.show()
plt.savefig('lineplot.png')
plt.clf()

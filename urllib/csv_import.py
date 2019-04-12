from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
urlretrieve(url, '../data-files/winequality-red.csv')

df = pd.read_csv('../data-files/winequality-red.csv', sep=';')
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

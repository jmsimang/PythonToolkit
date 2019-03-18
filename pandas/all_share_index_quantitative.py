import math
import matplotlib.pyplot as plt
import pandas as pd

cols = [
    'Subsidiary Sector Index',
    'No. of shares in subsidiary index',
    'Percentage weighting in All-Share Index',
    'Major sector index'
]

rows = [
    ['Coal', 2, 0.82, 'Coal'],
    ['Diamonds', 1, 8.27, 'Diamonds'],
    ['Gold - Rand and others', 5, 1.39, 'All-Gold'],
    ['Gold - Evander', 2, 0.89, 'All-Gold'],
    ['Gold - Klerksdorp', 3, 5.45, 'All-Gold'],
    ['Gold - OFS', 4, 3.99, 'All-Gold'],
    ['Gold - West Wits', 3, 7.27, 'All-Gold'],
    ['Copper', 1, 0.55, 'Metal & minerals'],
    ['Manganese', 1, 0.91, 'Metal & minerals'],
    ['Platinum', 2, 5.00, 'Metal & minerals'],
    ['Tin', 1, 0.01, 'Metal & minerals'],
    ['Other metals & minerals', 3, 0.26, 'Metal & minerals'],
    ['Mining houses', 3, 16.79, 'Mining financial'],
    ['Mining holding', 3, 7.13, 'Mining financial'],
    ['Banks & financial services', 5, 2.80, 'Financial'],
    ['Insurance', 4, 2.15, 'Financial'],
    ['Investment trusts', 3, 1.02, 'Financial'],
    ['Property', 12, 0.47, 'Financial'],
    ['Property trusts', 11, 0.97, 'Financial'],
    ['Industrial holdings', 6, 9.94, 'Industrial'],
    ['Beverages & hotels', 2, 3.43, 'Industrial'],
    ['Building & construction', 6, 0.92, 'Industrial'],
    ['Chemicals', 2, 3.46, 'Industrial'],
    ['Clothing, footwear & textiles', 10, 0.62, 'Industrial'],
    ['Electronics, electr. & battery', 7, 1.39, 'Industrial'],
    ['Engineering', 7, 0.95, 'Industrial'],
    ['Fishing', 1, 0.08, 'Industrial'],
    ['Food', 4, 2.14, 'Industrial'],
    ['Furniture & household goods', 5, 0.30, 'Industrial'],
    ['Motors', 6, 0.43, 'Industrial'],
    ['Paper & packaging', 3, 2.26, 'Industrial'],
    ['Pharmaceutical & medical', 3, 0.48, 'Industrial'],
    ['Printing & publishing', 3, 0.18, 'Industrial'],
    ['Steel & allied', 2, 1.99, 'Industrial'],
    ['Stores', 10, 2.16, 'Industrial'],
    ['Sugar', 1, 0.43, 'Industrial'],
    ['Tobacco & match', 1, 2.48, 'Industrial'],
    ['Transportation', 3, 0.22, 'Industrial']
]

indices = pd.DataFrame(data=rows, columns=cols)
indices.set_index('Subsidiary Sector Index', inplace=True)

print(indices.head())

# Visual displays of qualitative data...
# 1. Construct a bar chart showing number of shares in each of the 7 major sector indices
indices.groupby('Major sector index').sum()['No. of shares in subsidiary index'] \
    .sort_values(ascending=True) \
    .plot(kind='barh', title='No. of shares in each major sector', figsize=(10, 6))
plt.show()

# 2. Construct a bar chart showing the relative weightings of each of the 7 major sectors
#  as percentage of the All-Share Index
indices.groupby('Major sector index').sum()['Percentage weighting in All-Share Index'] \
    .sort_values(ascending=True) \
    .plot(kind='barh', title='% of All-Share Index', figsize=(10, 6))
plt.show()

# 3. Construct a pie chart showing number of shares in each of the 7 major sector indices
indices.groupby('Major sector index').sum()['Percentage weighting in All-Share Index'] \
    .sort_values(ascending=False) \
    .plot(kind='pie', title='% of All-Share Index', figsize=(10, 6))
plt.show()

# 4. Construct a bar chart showing the relative weightings of each of the 7 major sectors
#  as percentage of the All-Share Index
indices.groupby('Major sector index').sum()['Percentage weighting in All-Share Index'] \
    .sort_values(ascending=False) \
    .plot(kind='pie', title='% of All-Share Index', figsize=(10, 6))
plt.show()

# Visual displays of quantitative data
# Histograms - a timely and familiar way of displaying quantitative data
# Step 1 - Determine sample size as n, min and max value on our observation (No.of shares)
n = indices.count()[0]
x_min = indices.min()['No. of shares in subsidiary index']
x_max = indices.max()['No. of shares in subsidiary index']

# Step 2 - Choose class intervals that cover range x_min to x_max
# Guideline 1 - Mr Sturge
s_len = round((x_max - x_min) / (1 + 1.44 * math.log(n, math.e)), 1)

# Guideline 2 - GENSTAT
genstat_len = round((x_max - x_min) / math.sqrt(n), 1)

print(indices.count()[0])

# Stem-and-leaf plot
import numpy as np

# returns 10 evenly spaced samples from 0.1 to 2*PI
x = np.linspace(0.1, 2 * np.pi, 10)
markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')

# setting property of baseline with color red and linewidth 2
plt.setp(baseline, color='r', linewidth=2)
plt.show()

x = [2, 3, 4, 5, 6, 7]
y = [
    [9], [], [1, 8],
    [0, 0, 0, 1, 1, 1, 2, 3, 7, 9],
    [0, 0, 1, 3],
    [1, 1, 3, 4, 9]
]
plt.stem(x, x, linefmt='-.', markerfmt=None, basefmt=None)
# plt.setp(baseline, color='r', linewidth=2)
plt.show()

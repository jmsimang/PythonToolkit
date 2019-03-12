import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyodbc


#
# def connect_to_db():
#     server = '172.17.0.2,1433'
#     db = 'WaterCrisisDB'
#     user = 'sa'
#     pw = 'edsa@2019'
#
#     # Specify the ODBC driver, server name, database, etc. directly
#     con = pyodbc.connect(
#         r'DRIVER={ODBC Driver 17 for SQL Server};' +
#         'SERVER={};database={};UID={};PWD={};'.format(server, db, user, pw))
#
#     return con
#
#
# def close_db_connection(conn):
#     try:
#         conn.close()
#     except Exception as e:
#         print(str(e))


def load_dam_data(file):
    df = pd.read_csv(file, encoding='latin-1')
    # drop unnecessary columns - dam_stats_key
    df = df.drop('dam_stats_key', axis=1)
    return df


dam_csv = '../data-files/dam_levels-a-346.csv'
dam_levels = load_dam_data(dam_csv)

# inspect dam_levels DataFrame
print(dam_levels.head())

# display summary stats of current DataFrame
print(dam_levels.describe())

# display missing values found in the DataFrame
print(dam_levels.info())

# Data cleanup
# Ideally, the percentage_capacity should range between 0 and 1, from 0 to 112+
dam_levels['percentage_capacity'] = dam_levels['percentage_capacity'].apply(lambda x: x / 100).round(3)
print(dam_levels['percentage_capacity'].head())

"""
The data is now loaded and clean to work with, we can start finding and exploring into the
problem areas. We start by finding the latest data in the data, then look at total dam capacity
and storage for that date. The following steps hold:
1. Group by date,
2. Use sum() to add all values (max dam capacity and storage) for that date,
3. Sort newest to oldest using date,
4. Use iloc to show top entry (newest date)
"""
var = dam_levels.groupby('t_date').sum()[['Max_dam_capacity_ML', 'storage_ml']] \
    .reset_index().sort_values(by='t_date', ascending=False).iloc[0]
print(var.head())

# Number of different dams
print(dam_levels['dam_name'].nunique())

"""
We now look at the average height, capacity, storage and percentage capacity of each dam.
1. Group by dam name,
2. Use the mean() method
"""
d = dam_levels.groupby('dam_name').mean()[
    ['height_m', 'Max_dam_capacity_ML', 'storage_ml', 'percentage_capacity']]
print(d)

# Plot dam capacity on a bar chart, by dam name, and use the mean()
dam_levels.groupby('dam_name').mean()['Max_dam_capacity_ML'] \
    .sort_values(ascending=False) \
    .plot(kind='bar', title='Capacity by Dam in ML', figsize=(10, 6))
plt.show()

# Large variation in dam total capacity. So let's group by dam class.
print(dam_levels.groupby('dam_class')['dam_name'].nunique())

# Showing difference in the stats for Major Dams vs Minor Dams
# Group by dam class
dc = dam_levels.groupby('dam_class').mean()[['height_m', 'Max_dam_capacity_ML', 'storage_ml', 'percentage_capacity']]
print(dc)

dam_levels[dam_levels['dam_class'] == 'Major Dam'].groupby('dam_name').mean()['Max_dam_capacity_ML'] \
    .sort_values(ascending=True) \
    .plot(kind='barh', title='Capacity by Dam in ML', figsize=(10, 6))
plt.show()

# For future charting - Store Major Dam names order
major_dam_order = list(dam_levels[dam_levels['dam_class'] == 'Major Dam']
                       .groupby('dam_name')
                       .mean()['Max_dam_capacity_ML']
                       .sort_values(ascending=True))

# Dam levels over time.
# Filter dam class on Major Dam, group by Year, then look at averages over time.
dcot = dam_levels[dam_levels['dam_class'] == 'Major Dam']\
    .groupby('t_year')\
    .mean()[['height_m', 'Max_dam_capacity_ML', 'storage_ml', 'percentage_capacity']]
print(dcot)

# Dam levels over time using line plot
dam_levels[dam_levels['dam_class'] == 'Major Dam']\
    .groupby('t_year')\
    .mean()['percentage_capacity']\
    .plot(kind='line', title='Average % Capacity for Major Dams over time', figsize=(10, 6), ylim=(0, 1))
plt.show()

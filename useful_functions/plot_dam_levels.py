import pandas as pd
import matplotlib.pyplot as plt
import pyodbc


def connect_to_db():
    server = '172.17.0.2,1433'
    db = 'WaterCrisisDB'
    user = 'sa'
    pw = 'edsa@2019'

    # Specify the ODBC driver, server name, database, etc. directly
    con = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};' +
        'SERVER={};database={};UID={};PWD={};'.format(server, db, user, pw))

    return con


def close_db_connection(conn):
    try:
        conn.close()
    except Exception as e:
        print(str(e))


conn = connect_to_db()
sql_query = 'SELECT * FROM RainfallMeasurements'
df = pd.read_sql(sql_query, conn)
print(df.head())

tdf = df[df['rain station name'] == 'ASSEGAAIBOS']
print(tdf.head())

plt.plot(tdf['rain precipitation'])
plt.show()

query = 'SELECT * FROM  DamsWaterLevelMeasurement'
water_df = pd.read_sql(query, conn)
print(water_df.head())

wdf = water_df[water_df['dam name'] == 'THEEWATERSKLOOF']
print(wdf.head())

plt.plot(wdf['height in metres'])
plt.show()

conn.close()

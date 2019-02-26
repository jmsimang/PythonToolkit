import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import pyodbc as pyodbc


def connect_to_db():
    # Driver={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.3.so.1.1}
    server = '172.17.0.2,1433'
    db = 'WaterCrisisDB'
    user = 'sa'
    pw = 'edsa@2019'
    # Specify the ODBC driver, server name, database, etc. directly
    con = pyodbc.connect(r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
                         ';database=' + db + ';UID=' + user + ';PWD=' + pw + ';')
    # Create a cursor from the connection
    #   cursor = con.cursor()
    return con


def plot_population(tablename):
    # cursor = connect_to_db()
    # Select statement to retrieve all data from a specified table
    # cursor.execute('SELECT YEAR([population review date]) AS Year, population AS Population FROM ' + tablename)
    # rows = cursor.fetchall()
    # print(rows)
    # Create a connection to the database
    connection = connect_to_db()
    data = pd.read_sql_query('SELECT YEAR([population review date]) AS Year, population AS Population FROM ' +
                             tablename, connection)
    print(data)
    # query = 'SELECT YEAR([population review date]) AS Year, population AS Population FROM ' + tablename
    # population_reader = pd.read_sql(query, cursor)
    # print(population_reader)
    # data = pd.DataFrame()
    # for df_population in population_reader:
    #     data = data.append(df_population)
    # print(data)
    data.plot(kind='scatter', x='Year', y='Population')
    plt.show()
    connection.close()


plot_population('PopulationDataAsPerWorldReview')

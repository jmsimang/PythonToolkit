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


def plot_world_bank_data():
    # Create a connection to the database
    connection = connect_to_db()

    data = pd.read_sql_query('SELECT YEAR([population review date]) AS Year, population AS Population FROM ' +
                             'PopulationDataAsPerWorldReview', connection)
    print(data)

    data.plot(kind='scatter', x='Year', y='Population')
    plt.show()

    # Close db connection
    close_db_connection(connection)


def plot_census_data():
    # Create a connection to the database
    connection = connect_to_db()

    query = 'SELECT Year([population review date]) AS Year, population AS Population FROM PopulationDataAsPerCensus'
    data_2 = pd.read_sql(query, connection)

    print(data_2)

    data_2.plot(kind='scatter', x='Year', y='Population')
    plt.show()

    # Close db connection
    close_db_connection(connection)


plot_world_bank_data()
plot_census_data()

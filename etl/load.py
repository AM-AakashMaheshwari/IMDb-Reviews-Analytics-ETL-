import pyodbc
from config.dbConfigs import conn_str 

def load_to_mssql(df, table_name, conn_str):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    for index, row in df.iterrows():
        placeholders = ', '.join(['?'] * len(row))
        columns = ', '.join(row.index)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(row))
    conn.commit()
    cursor.close()
    conn.close()

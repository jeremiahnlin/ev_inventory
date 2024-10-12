import pandas as pd

def pull_data(table):
    return """SELECT * FROM """ + str(table)

def pull_data(table):
    return f"SELECT * FROM {table};"

def pull_data_with_column_values(table, column, value):
    return f"SELECT * FROM {table} WHERE {column} = '{value}';"

def pull_specific_columns(table, columns):
    columns_str = ", ".join(columns)
    return f"SELECT {columns_str} FROM {table};"

def pull_data_with_conditions(table, conditions):
    conditions_str = " AND ".join(conditions)
    return f"SELECT * FROM {table} WHERE {conditions_str};"

def count_rows(table):
    return f"SELECT COUNT(*) FROM {table};"

def pull_data_ordered(table, order_by, ascending=True):
    order = "ASC" if ascending else "DESC"
    return f"SELECT * FROM {table} ORDER BY {order_by} {order};"

def create_table(table_name, columns):
    columns_str = ", ".join([f"{col_name} {data_type}" for col_name, data_type in columns.items()])
    return f"CREATE TABLE {table_name} ({columns_str});"

def delete_table(table_name):
    return f"DROP TABLE IF EXISTS {table_name};"

def generate_insert_queries(csv_file_path, table_name):
    df = pd.read_csv(csv_file_path)
    queries = []
    for _, row in df.iterrows():
        values = ', '.join(f"'{str(value)}'" if isinstance(value, str) else str(value) for value in row)
        query = f"INSERT INTO {table_name} VALUES ({values});"
        queries.append(query)
    return '\n'.join(queries)
def pull_data(table):
    return """SELECT * FROM """ + str(table)

def pull_data(table):
    return f"SELECT * FROM {table};"

# Pull data examples --> user permissions
#ALLOWED_TABLES = {'users', 'products', 'orders'}  # Example allowed tables

# def pull_data(connection, table):
#     if table not in ALLOWED_TABLES:
#         raise ValueError("Invalid table name")
#     query = f"SELECT * FROM {table};"
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         return cursor.fetchall()

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


def pull_data(table):
    return """SELECT * FROM """ + str(table)

print(pull_data("help"))

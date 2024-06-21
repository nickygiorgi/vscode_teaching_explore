# I had to install pyodbc
# In Thonny this is Tools -> Manage Packages -> install pyodbc using PyPi

import pyodbc

# function to read SQL from a separate script file
def execute_scripts_from_file(filepath):
    # file reading
    f = open(filepath, 'r')
    file_content = f.read()
    f.close()

    # separate different SQL commands in script
    # eliminate any empty commands and save to variable
    sql_commands = list(filter(None, file_content.split(';')))

    return sql_commands

# Define the path to your Access database
database_path = 'C:/Users/nicol/Downloads/TestDatabase.accdb'

# Create a connection string
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=' + database_path + ';'
)

# Connect to the Access database
conn = pyodbc.connect(conn_str)

# Create a cursor from the connection
cursor = conn.cursor()

# Example query
#query = 'SELECT * FROM TestTable WHERE BooleanField = True'
# Execute the query
#cursor.execute(query)

# Read and execute SQL code from a separate script
sql_script_path = 'C:/Users/nicol/Downloads/script.sql'
sql_commands = execute_scripts_from_file(sql_script_path)
for command in sql_commands:
    cursor.execute(command)
    # If the command is not a query, commit it
    if command.find("SELECT") == -1:
        cursor.commit()
    # Else, fetch and print the query's results
    else:
        rows = cursor.fetchall()
        for row in rows:
            print(row)

# Close the cursor and DB connection
cursor.close()
conn.close()

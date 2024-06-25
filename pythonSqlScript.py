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

class AccessInterface:
    def __init__(self, database_path):
        # Create a connection string
        self.connection_string = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + database_path + ';'
        )

    def execute_sql_script(self, sql_script_path):
        # Connect to the Access database
        connection = pyodbc.connect(self.connection_string)

        # Create a cursor from the connection
        cursor = connection.cursor()

        # Read and execute SQL code from a separate script
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
        connection.close()


# Create an AccessInterface object and use it to execute SQL on an MS Access database
access_interface = AccessInterface('C:/Users/nicol/Downloads/TestDatabase.accdb')
access_interface.execute_sql_script('C:/Users/nicol/Downloads/script.sql')

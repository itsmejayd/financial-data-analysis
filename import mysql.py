import sqlite3

# Connect to the SQLite database (this will create a new file if it doesn't exist)
connection = sqlite3.connect('test_database.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Example: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Example: Insert data into the table
cursor.execute('''
    INSERT INTO users (username, email) VALUES
    ('john_doe', 'john.doe@example.com'),
    ('jane_doe', 'jane.doe@example.com')
''')

# Commit the changes and close the connection
connection.commit()
connection.close()
import sqlite3

def create_database():
    # Connect to SQLite database (creates a new file if it doesn't exist)
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Create Employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date DATE NOT NULL
    )
    ''')

    # Create Departments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
    ''')

    # Insert sample data into Employees table
    employees_data = [
        (1, 'Alice', 'Sales', 50000, '2021-01-15'),
        (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
        (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
    ]

    cursor.execute('DELETE FROM Employees')  # Clear existing data
    cursor.executemany('INSERT INTO Employees VALUES (?, ?, ?, ?, ?)', employees_data)

    # Insert sample data into Departments table
    departments_data = [
        (1, 'Sales', 'Alice'),
        (2, 'Engineering', 'Bob'),
        (3, 'Marketing', 'Charlie')
    ]

    cursor.execute('DELETE FROM Departments')  # Clear existing data
    cursor.executemany('INSERT INTO Departments VALUES (?, ?, ?)', departments_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

def verify_database():
    """Verify the database was created correctly by printing the contents of both tables."""
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    print("Employees table:")
    cursor.execute('SELECT * FROM Employees')
    print(cursor.fetchall())

    print("\nDepartments table:")
    cursor.execute('SELECT * FROM Departments')
    print(cursor.fetchall())

    conn.close()

if __name__ == "__main__":
    create_database()
    verify_database()

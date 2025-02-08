import sqlite3
import re
from datetime import datetime

class DatabaseChatAssistant:
    def __init__(self, db_path='company.db'):
        self.db_path = db_path
        # Define query patterns and their corresponding SQL templates
        self.query_patterns = [
            {
                'pattern': r'Show me all employees in the (\w+) department',
                'sql': '''
                    SELECT Name, Salary, Hire_Date 
                    FROM Employees 
                    WHERE LOWER(Department) = LOWER(?)
                ''',
                'params': lambda matches: [matches[0]],
                'format': lambda rows: "\n".join([f"- {row[0]}: ${row[1]}, hired on {row[2]}" for row in rows])
            },
            {
                'pattern': r'Who is the manager of the (\w+) department',
                'sql': '''
                    SELECT Manager 
                    FROM Departments 
                    WHERE LOWER(Name) = LOWER(?)
                ''',
                'params': lambda matches: [matches[0]],
                'format': lambda rows: f"The manager of this department is {rows[0][0]}" if rows else "No manager found."
            },
            {
                'pattern': r'List all employees hired after (\d{4}-\d{2}-\d{2})',
                'sql': '''
                    SELECT Name, Department, Hire_Date 
                    FROM Employees 
                    WHERE Hire_Date > ?
                    ORDER BY Hire_Date
                ''',
                'params': lambda matches: [matches[0]],
                'format': lambda rows: "\n".join([f"- {row[0]} ({row[1]}) hired on {row[2]}" for row in rows])
            },
            {
                'pattern': r'What is the total salary expense for the (\w+) department',
                'sql': '''
                    SELECT SUM(Salary) 
                    FROM Employees 
                    WHERE LOWER(Department) = LOWER(?)
                ''',
                'params': lambda matches: [matches[0]],
                'format': lambda rows: f"Total salary expense: ${rows[0][0]:,}" if rows[0][0] else "No salary data found."
            },
            {
                'pattern': r'List all departments',
                'sql': '''
                    SELECT Name, Manager 
                    FROM Departments
                ''',
                'params': lambda matches: [],
                'format': lambda rows: "\n".join([f"- {row[0]} (Manager: {row[1]})" for row in rows])
            },
            {
                'pattern': r'What is (\w+)\'s salary',
                'sql': '''
                    SELECT Salary 
                    FROM Employees 
                    WHERE LOWER(Name) = LOWER(?)
                ''',
                'params': lambda matches: [matches[0]],
                'format': lambda rows: f"Salary: ${rows[0][0]:,}" if rows and rows[0][0] else "Employee not found."
            }
        ]

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def execute_query(self, sql, params):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(sql, params)
            results = cursor.fetchall()
            conn.close()
            return results
        except sqlite3.Error as e:
            return f"Database error: {str(e)}"

    def process_query(self, user_input):
        try:
            # Check for empty input
            if not user_input.strip():
                return "Please provide a valid query."

            # Try to match the input against known patterns
            for pattern in self.query_patterns:
                matches = re.search(pattern['pattern'], user_input, re.IGNORECASE)
                if matches:
                    # Extract matched groups (excluding the full match)
                    params = pattern['params'](matches.groups())
                    
                    # For date queries, validate the date format
                    if 'hired after' in user_input.lower() and not self.validate_date(params[0]):
                        return "Please provide a valid date in YYYY-MM-DD format."

                    # Execute the query
                    results = self.execute_query(pattern['sql'], params)
                    
                    # Check for database errors
                    if isinstance(results, str):
                        return results
                    
                    # Format and return results
                    if not results:
                        return "No results found for your query."
                    
                    return pattern['format'](results)

            return "I don't understand that query. Please try rephrasing or use one of the supported query formats."

        except Exception as e:
            return f"An error occurred: {str(e)}"

def main():
    assistant = DatabaseChatAssistant()
    print("Welcome to the Database Chat Assistant!")
    print("You can ask questions about employees and departments.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nWhat would you like to know? ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        response = assistant.process_query(user_input)
        print("\nResponse:", response)

if __name__ == "__main__":
    main()


# Database Chat Assistant

A natural language interface for querying employee and department information from a SQLite database. This chat assistant allows users to ask questions about employee data, department statistics, and organizational structure in plain English.

## Features

### Query Capabilities
- Employee lookups by department
- Department manager information
- Salary analysis and comparisons
- Hiring trend visualization
- Detailed employee reports
- Department statistics and analytics

### Visualizations
- Salary distribution charts
- Hiring trend graphs
- Department comparisons
- Statistical analysis plots

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/database-chat-assistant.git
cd database-chat-assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python setup_database.py
```

4. Run the chat assistant:
```bash
python chat_assistant.py
```

## Usage Examples

Here are some example queries you can try:

```
# Basic Queries
Show me all employees in the Sales department
Who is the manager of the Engineering department
List all employees hired after 2021-01-01

# Analytics
Show salary distribution
Show department statistics for Engineering
Compare salaries between departments
Show hiring trends

# Detailed Reports
Generate employee report for Alice
```

## Project Structure

```
database-chat-assistant/
├── README.md
├── requirements.txt
├── setup_database.py
├── chat_assistant.py
templates/
   index.html
├── company.db
```

## Technical Implementation

### Database Schema

#### Employees Table
```sql
CREATE TABLE Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Hire_Date DATE NOT NULL
)
```

#### Departments Table
```sql
CREATE TABLE Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Manager TEXT NOT NULL
)
```

### Key Components

1. **Natural Language Processing**
   - Regular expression patterns for query matching
   - Parameter extraction from natural language
   - Query type classification

2. **Database Interface**
   - SQLite connection management
   - Parameterized queries for security
   - Error handling and validation

3. **Data Visualization**
   - Matplotlib for generating charts
   - Multiple visualization types
   - Dynamic data representation

4. **Output Formatting**
   - Tabulated data presentation
   - Formatted currency and dates
   - Clear, readable responses

## Known Limitations

1. **Query Understanding**
   - Limited to predefined query patterns
   - No fuzzy matching for similar queries
   - Cannot handle complex, multi-part questions

2. **Data Visualization**
   - Static image generation only
   - No interactive visualizations
   - Limited customization options

3. **Database**
   - Single SQLite file
   - No real-time updates
   - Limited to employee/department domain

## Future Improvements

1. **Natural Language Processing**
   - Implement machine learning for query understanding
   - Add support for more complex queries
   - Enable conversational context

2. **Visualization**
   - Add interactive charts using Plotly
   - Enable custom visualization parameters
   - Implement real-time data updates

3. **Features**
   - Add data export capabilities (CSV, PDF)
   - Implement user authentication
   - Add data modification capabilities
   - Enable custom query creation

4. **Performance**
   - Implement query caching
   - Optimize database indexes
   - Add connection pooling

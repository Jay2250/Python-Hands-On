import sqlite3 as sql
import pandas as pd

try:
    conn = sql.connect('company.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INTEGER PRIMARY KEY,
        dept_name TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        emp_name TEXT NOT NULL,
        dept_id INTEGER,
        FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
    )
    ''')
    # create index
    cursor.execute("CREATE INDEX idx_emp_name ON employees (emp_name)")
    cursor.execute("CREATE INDEX idx_dept_name ON departments (dept_name)")

    cursor.execute("INSERT INTO departments (dept_name) VALUES ('HR')")
    cursor.execute("INSERT INTO departments (dept_name) VALUES ('IT')")
    cursor.execute("INSERT INTO departments (dept_name) VALUES ('Finance')")

    cursor.execute(
        "INSERT INTO employees (emp_name, dept_id) VALUES ('John Doe', 1)")
    cursor.execute(
        "INSERT INTO employees (emp_name, dept_id) VALUES ('Jane Smith', 2)")
    cursor.execute(
        "INSERT INTO employees (emp_name, dept_id) VALUES ('Mike Johnson', 1)")
    cursor.execute(
        "INSERT INTO employees (emp_name, dept_id) VALUES ('Emily Brown', 3)")

    conn.commit()

    cursor.execute("SELECT * FROM departments")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM employees")
    print(cursor.fetchall())

    print("Employees and their departments:")
    cursor.execute(
        "SELECT employees.emp_name, departments.dept_name FROM employees JOIN departments ON employees.dept_id = departments.dept_id")
    print(cursor.fetchall())

    cursor.execute('''SELECT emp_id, emp_name, dept_id FROM employees''')
    print(cursor.fetchall())

    cursor.execute(
        '''SELECT employees.emp_name, departsments.dept_name from employees JOIN departments ON employees.dept_id = departments.dept_id''')
    print(cursor.fetchall())


except Exception as e:
    print(e)

# ---------------------------------------------------------------

conn = sql.connect('college.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects(
    id INTEGER PRIMARY KEY ,
    name TEXT)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL,
    subject_id INTEGER,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)
''')

cursor.execute("INSERT INTO subjects VALUES (1, 'Maths')")
cursor.execute("INSERT INTO subjects VALUES (2, 'English')")
cursor.execute("INSERT INTO subjects VALUES (3, 'Science')")


cursor.execute(
    "INSERT INTO students (id, name, marks,subject_id) VALUES (1, 'Jay',99,2)")
cursor.execute(
    "INSERT INTO students (id, name, marks,subject_id) VALUES (2, 'Bapat', 89,2)")
cursor.execute(
    "INSERT INTO students (id, name, marks,subject_id) VALUES (3, 'Sammak', 29,1)")
cursor.execute(
    "INSERT INTO students (id, name, marks,subject_id) VALUES (4, 'Abhishek', 98,3)")
cursor.execute(
    "INSERT INTO students (id, name, marks,subject_id) VALUES (5, 'Yash', 79,3)")
cursor.execute(
    "INSERT INTO students (id, name, marks,subject_id) VALUES (6, 'Chammak', 69,3)")
conn.commit()
cursor.execute("Select * from students")
print(cursor.fetchall())


# -----------------------------------------------------------------


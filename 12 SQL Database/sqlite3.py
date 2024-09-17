import sqlite3 as sql

# Establishing a connection
conn = sql.connect('DAIBatch2024.db')

# Creating a cursor object
cursor = conn.cursor()

# cursor.execute('''DROP TABLE IF EXISTS users''')

# create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

cursor.execute('''INSERT INTO users (name, age) VALUES ('Mayura', 30)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('Mayuresh', 25)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('Charlie', 35)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('David', 28)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('Eve', 32)''')

# Commit the changes
conn.commit()

# query with order by
cursor.execute('SELECT * FROM users ORDER BY age DESC')
result = cursor.fetchall()
for row in result:
    print(row)

while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

#  query with group by
cursor.execute('SELECT age, COUNT(*) as count FROM users GROUP BY age')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute('UPDATE users SET age = 31 WHERE name = "Mayura"')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT * FROM users where name LIKE 'Mayura'")
result = cursor.fetchall()
for row in result:
    print(row)
print(result)
cursor.close()
conn.close()

# ------------------------------------------------------------------

# Assignment 1
conn = sql.connect('school.db')

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor TEXT
)
''')

# -------------------------------------------------------------------

cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES ('Alice', 18, 'A')")
cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES ('Bob', 17, 'B')")
cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES ('Charlie', 19, 'A')")
cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES ('David', 18, 'B')")
cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES ('Eve', 17, 'A')")

cursor.execute(
    "INSERT INTO courses (course_name, instructor) VALUES ('Math', 'Dr. Smith')")
cursor.execute(
    "INSERT INTO courses (course_name, instructor) VALUES ('Science', 'Prof. Johnson')")
cursor.execute(
    "INSERT INTO courses (course_name, instructor) VALUES ('History', 'Dr. Brown')")

conn.commit()

print(cursor.fetchall())

# -------------------------------------------------------------------

cursor.execute("SELECT * FROM students WHERE grade = 'A'")

cursor.execute("SELECT * FROM courses order by course_name")

# -------------------------------------------------------------------

cursor.execute("UPDATE students SET grade = 'A' WHERE name = 'David'")

cursor.execute(
    "UPDATE courses SET instructor = 'Dr. Johnson' WHERE course_id = 2")

# -------------------------------------------------------------------

cursor.execute("DELETE FROM students WHERE id = 4")
conn.commit()

# -------------------------------------------------------------------

cursor.execute("DROP TABLE courses")
cursor.execute("DROP TABLE students")
cursor.close()
conn.close()

# -------------------------------------------------------------------

# Exception Handling

try:
    conn = sql.connect('school1.db')

    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        instructor TEXT
    )
    ''')
    # cursor.execute("DROP TABLE courses")
    # cursor.execute("DROP TABLE students")
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES ('Alice', 18, 'A')")
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES ('Bob', 17, 'B')")
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES ('Charlie', 19, 'A')")
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES ('David', 18, 'B')")
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES ('Eve', 17, 'A')")

    cursor.execute(
        "INSERT INTO courses (course_name, instructor) VALUES ('Math', 'Dr. Smith')")
    cursor.execute(
        "INSERT INTO courses (course_name, instructor) VALUES ('Science', 'Prof. Johnson')")
    cursor.execute(
        "INSERT INTO courses (course_name, instructor) VALUES ('History', 'Dr. Brown')")

    conn.commit()
    cursor.execute("SELECT * FROM students WHERE grade = 'A'")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM courses order by course_name")
    print(cursor.fetchall())
except Exception as e:
    print(e)
else:
    print()
finally:
    cursor.close()
    conn.close()

# -------------------------------------------------------------------------


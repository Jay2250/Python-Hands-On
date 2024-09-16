import sqlite3 as sql
conn = sql.connect('college4.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()
# cursor.execute("DROP TABLE subjects")
# cursor.execute("DROP TABLE students")
# conn.commit()
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


cursor.execute("INSERT INTO students (id, name, marks,subject_id) VALUES (1, 'Jay',99,2)")
cursor.execute("INSERT INTO students (id, name, marks,subject_id) VALUES (2, 'Bapat', 89,2)")
cursor.execute("INSERT INTO students (id, name, marks,subject_id) VALUES (3, 'Sammak', 29,1)")
cursor.execute("INSERT INTO students (id, name, marks,subject_id) VALUES (4, 'Abhishek', 98,3)")
cursor.execute("INSERT INTO students (id, name, marks,subject_id) VALUES (5, 'Yash', 79,3)")
cursor.execute("INSERT INTO students (id, name, marks,subject_id) VALUES (6, 'Chammak', 69,3)")
conn.commit()


cursor.execute("Select students.name, students.marks, students.subject_id, subjects.name from students JOIN subjects on subjects.id = students.subject_id")
print(cursor.fetchall())
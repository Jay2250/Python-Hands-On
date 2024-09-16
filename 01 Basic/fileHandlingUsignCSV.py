import csv
students = [
    {'ID': 1, 'Name': 'Abhishek', 'Age': 23, 'Grade': 'A'},
    {'ID': 2, 'Name': 'Jayesh', 'Age': 23, 'Grade': 'B'},
    {'ID': 3, 'Name': 'Bapat', 'Age': 22, 'Grade': 'A'},
    {'ID': 4, 'Name': 'Sammak', 'Age': 47, 'Grade': 'F'}
]
fieldnames = ['ID', 'Name', 'Age', 'Grade']

with open('student.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
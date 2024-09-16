# Write Data to CSV file
# create a list of dictionaries where each dictionary rpresents students record with the following field: ID, Name, Age, Grade
# use csv module to write the list of dictionaries to csv file named as student.csv

import csv

# Create a list of dictionaries representing student records
students = [
    {'ID': 1, 'Name': 'Alice', 'Age': 18, 'Grade': 'A'},
    {'ID': 2, 'Name': 'Bob', 'Age': 17, 'Grade': 'B'},
    {'ID': 3, 'Name': 'Charlie', 'Age': 19, 'Grade': 'A'}
]

# Define the fieldnames for the CSV file
fieldnames = ['ID', 'Name', 'Age', 'Grade']

# Write the data to the CSV file
with open('student.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)


grades_input = input("Enter a list of grades separated by commas: ")

try:

    grades_list = grades_input.split(',')

    grades = [int(grade.strip()) for grade in grades_list]

    print("Grades as integers:", grades)

except ValueError:

    print("One or more values you entered cannot be converted to an integer.")

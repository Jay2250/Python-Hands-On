import pandas as pd

# Lists for employee details

employee_names = ["John Doe", "Jane Smith",
                  "Alice Johnson", "Robert Brown", "Charlie Davis"]

employee_ids = ["E001", "E002", "E003", "E004", "E005"]

company_names = ["Company A", "Company B",
                 "Company A", "Company C", "Company B"]

employee_salaries = [50000, 60000, 55000, 65000, 62000]

# Create the first DataFrame with employee name, ID, and company name

df_employee = pd.DataFrame({

    "Employee_ID": employee_ids,

    "Employee_Name": employee_names,

    "Company_Name": company_names

})

# Create the second DataFrame with employee ID and salary

df_salary = pd.DataFrame({

    "Employee_ID": employee_ids,

    "Salary": employee_salaries

})

# Merge the two DataFrames on Employee_ID

df_final = pd.merge(df_employee, df_salary, on="Employee_ID")

# Print the final DataFrame with employee details and salary

print(df_final)

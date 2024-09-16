# Radius= float(input("Enter the radius of circle"))
# PI=3.142
# Area= PI*(Radius**2)
# print("Area of circle is : ",Area)

Income = float(input("Enter the Income"))
Expenses = float(input("Enter Total Monthly Expenses"))

totalSaving= Income-Expenses
percentSaving= (totalSaving/Income)*100

print("Total savings is : ",totalSaving)
print("Percentage Saving is : ",percentSaving,"%")
print("Percentage Expense is : ",100-percentSaving,"%")
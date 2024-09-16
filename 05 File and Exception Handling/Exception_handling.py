try:
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  result = num1 / num2
  print("Result:", result)
except ZeroDivisionError:
  print("Error: Division by zero!")
except ValueError:
  print("Error: Invalid input. Please enter numbers only.")
except Exception as e:
  print("An unexpected error occurred:", e)

#----------------------------------------------------------------



try:
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  result = num1 / num2
except ZeroDivisionError:
  print("Error: Division by zero!")
except ValueError:
  print("Error: Invalid input. Please enter numbers only.")
else:
  print("Result:", result)
finally:
  print("This block will always execute.")


#------------------------------------------------------------------

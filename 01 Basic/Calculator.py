number1= int(input("Enter Number 1"))
number2= int(input("Enter Number 2"))

choice=int(input("Enter Operation to perform \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division"))
if choice==1:
    print(number1+number2)
elif choice==2:
    print(number1-number2)
elif choice==3:
    print(number1*number2)
elif choice==4:
    print(number1/number2)
else:
    print("Invalid Choice")

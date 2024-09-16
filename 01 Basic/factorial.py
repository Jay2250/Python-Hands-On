fact = int(input("Enter the number"))
number=fact
result=1
while fact>1:
    result*=fact
    fact-=1
print("Factorial of {} is {} ".format(number,result))

for i in range(1,fact+1):
    result*=i
print("Factorial of {} is {}".format(number,result))
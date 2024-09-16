for i in range(1,4):
  for j in range(1,4):

    print("i=",i ,"j=",j)
    
    
#----------------------------------------------------------------

#Sum of digits

number = int(input("Enter the number"))
result=0
while number>0:
  x=number%10
  number=number//10
  result += x
print("Sum of digits is : ",result)

#----------------------------------------------------------------

# table of number

number = int(input("Enter the Number"))
for i in range(1,13):
  print(f"{number} X {i} = {number*i}")   # f string, variables writte in {}  will be printes as value and the remaining is printed as string
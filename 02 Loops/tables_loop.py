for i in range(1,11):
  for j in range(1,6):
    print(f"{j} x {i} = {i*j} \t",end="  ")
  print()
  
#----------------------------------------------------------------

# Triangular pattern
num = int(input("Enter number of rows"))
last = 1
for i in range(0,num):
  for j in range(0,last):
    print(last,end='')
  print()
  last += 1

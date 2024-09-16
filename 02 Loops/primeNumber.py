#prime number using list
num = int(input("Enter the number "))
my_list = []

for i in range(1,num):
  count=0
  for j in range(1,i+1):
      if i % j == 0:
        count += 1
  if count == 2:
     my_list.append(i)
print(my_list)
print("Total prime number are : ",len(my_list))
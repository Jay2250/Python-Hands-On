# list rotation operation
lengthList = int(input("Enter the length of the list"))
list1 = [int(input("Enter the elements of the list ")) for i in range(0,lengthList)]
print(list1)
rotation = int(input("Enter the rotation count"))
for i in range(0,rotation):
  temp = list1[-1]
  for j in range(-1,-lengthList,-1):   #iterating reversely in the list
      list1[j] = list1[j-1]
  list1[0]=temp
print()
print(list1)



# Assignment 01 Day 3

listStudents = []
i =0
while i < 3:
  listStudents.append((input("Enter Name : "), int(input("Enter age : ")), int(input("Score 1 : ")), int(input("Score 2 : ")), int(input("Score 3 : "))))
  i+=1
print(listStudents)
newList = []
avgList= []
for i in listStudents:
  avg = sum(i[2:]) / 3
  avgList.append(avg)
  name, age, score1, score2, score3 = i    # packing and unpacking concept
  new_tuple=(name, age, score1, score2, score3,round(avg, 2))
  newList.append(new_tuple)
print(newList)
x = max(avgList)
for i in newList:
  if i[5]==x:
    print(i[0],"Has the higest avg , and that is : ",i[5])

avgMin=float(input("Enter minimum avg score "))
for i in newList:
  if i[5]>=avgMin:
    print(i[0]," has exceeds the minimum avg score ", avgMin, " has avg score ", i[5])

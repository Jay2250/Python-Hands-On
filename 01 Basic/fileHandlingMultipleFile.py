with open("C:\\Users\\DAI.STUDENTSDC\\Desktop\\document.rtf",'r') as file1:
    global list1
    list1 = file1.readlines()

with open("C:\\Users\\DAI.STUDENTSDC\\Desktop\\Document1.rtf",'r') as file2:
    global list2
    list2 = file2.readlines()

newlist = list1 + list2
newSet = set(newlist)
newSet = sorted(newSet)
with open("C:\\Users\\DAI.STUDENTSDC\\Desktop\\DocumentNew.rtf",'w') as file3:
    for i in newSet:
        file3.writelines(i)
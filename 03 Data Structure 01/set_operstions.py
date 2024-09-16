#Set assignments
newTuple1= tuple(int(i) for i in input("Enter numbers separated by comma ").split(','))
newTuple2=tuple(int(i) for i in input("Enter numbers separated by comma ").split(','))

newSet1, newSet2= set(newTuple1), set(newTuple2)
commonSet= newSet1 & newSet2
print(commonSet)


#----------------------------------------------------------------

para = [i for i in input("Enter a paragraph").split(' ')]
print(para)
list_of_set = []
for i in para:
  list_of_set.append(sorted(set(i))) # for sorting inner words alphabets

print(sorted(list_of_set))  # for sorting whole word alphabetically




# set convert whole string into single single alphabets
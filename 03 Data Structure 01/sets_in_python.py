set1 = {'apple', 'banana', 'baigan', 'wheat', 'rice','pineapple'}
set2 = {'mango', 'rice', 'spinach','jawar'}
set3 = {'apple', 'rice', 'wheat', 'baigan', 'spinach','bittergod'}
print(set1 & set2 & set3)
print((set1 | set2 | set3) - (set1 & set2 & set3))
print((set1 | set2) & set3)
print("Unique items in set 1 : ",set1 - set2 - set3)
print("Unique items in set 2 : ",set2 - set1 - set3)
print("Unique items in set 3 : ",set3 - set1 - set2)

print(set1.symmetric_difference(set2 | set3))

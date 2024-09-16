# Assignment 01
rangeInput = int(input("Enter number of elements : "))
list_of_tuple = []
for i in range(0,rangeInput):
    list_of_tuple.append(tuple(input(f"Enter the {i}'th key value seperated by colon : ").split(':')))     #if there is a duplicate key, the system uses the last occurence of the key
print(list_of_tuple)                                                                               #Input --- [('1', 'hello'), ('2', 'bhai'), ('1', 'sahab')]
list_to_dict = dict(list_of_tuple)                                                                 #Output --- {'1': 'sahab', '2': 'bhai'}
print(list_to_dict)
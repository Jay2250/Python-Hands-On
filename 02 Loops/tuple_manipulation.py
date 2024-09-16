# Tuple manipulation

userInput = input("Enter the list of ele seperarted by space")
element_list = userInput.split(' ')
my_tuple= tuple(element_list)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:-1])
print(my_tuple[::2])
print(my_tuple[::-1])
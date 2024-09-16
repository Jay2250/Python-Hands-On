# packng and unpacking of tuple
Age = int(input("Enter age"))
name = input("Enter name")
city, Country = (input("Enter City"), input("Enter Country"))
people = (name, Age, (city, Country))  # packing of tuple
print(people)
name1, age1, (city1, country) = people
print("Name = ",name1)
print("Age = ",age1)
print("City = ",city1)
print("Country = ",country)


#----------------------------------------------------------------

#Tuple Statistics
tup =  tuple(int(i) for i in input("Enter numbers separated by comma ").split(','))
print("Sum of elements = ",sum(tup))
print('Avg of ele = ', sum(tup)/len(tup))
x = int(input("Enter threshold value"))
filt= tuple(i for i in tup if (i >x))
print(i for i in filt)
print(sorted(tup))
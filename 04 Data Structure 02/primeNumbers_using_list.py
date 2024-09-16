#prime number using list comprehensions
# this does not work
# prime_list = [i for i in range(2,50) if i%j == 0 else continue for j in range(2,i)  ]
# print(prime_list)


#----------------------------------------------------------------

# prime number using list comprehensions

prime_list = [i for i in range(2, 50) if all(i % j != 0 for j in range(2, i))]
print(prime_list)


#----------------------------------------------------------------

# prime number using list comprehensions without using all

prime_list = [i for i in range(2, 50) if not any(i % j == 0 for j in range(2, i))]
print(prime_list)

#----------------------------------------------------------------

prime_list = [i for i in range(2, 51) if all(i % j != 0 for j in range(2, i))]
print(prime_list)

#----------------------------------------------------------------

#list comprehension assignment 5  even number then square else cube
newList= [i**2 if i %2 ==0 else i**3 for i in range(1, 11)]
print(newList)
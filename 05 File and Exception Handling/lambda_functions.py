# lambda function
numbers = (int(i) for i in input("Enter numbers separated by comma ").split(','))
integer = lambda x : 'positive' if x > 0 else 'negative' if x < 0 else 'zero'
print(list(map(integer, numbers)))
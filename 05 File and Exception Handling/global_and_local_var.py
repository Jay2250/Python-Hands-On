#global and local variable
x =(int(i) for i in input("Enter numbers separated by comma ").split(','))
global summation
summation = sum(x)
print(summation)
def sumOfNumbers(x):
    s = sum(x)
    print(f"local variable summation inside function {s}")
    print(f"Global variable summation inside function before assigning s {summation}")
    summation = s
    print(f"Global variable summation inside function {summation}")
    return s
sum = sumOfNumbers(int(i) for i in input("Enter numbers separated by comma ").split(','))
print(f"Global variable summation outside function {summation}")
print(f"Global variable summation inside function {summation}")
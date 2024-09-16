Year = int(input("Enter the Year"))

if(Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("Year ", Year, " Is a Leap Year")
else:
    print("Year ", Year, " Is Not a Leap Year")
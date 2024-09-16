password = str(input("Enter the Password"))

length= len(password)
specialChar= set("!@#$%&")
flagLength= False
flagUpper=False
flagLower=False
flagNumber=False
flagSpecial=False
if length>=8:
    flagLength=True
for char in password:
    if  char.isupper():
        flagUpper=True
    elif char.islower():
        flagLower=True
    elif char.isnumeric():
        flagNumber=True
    elif char in specialChar:
        flagSpecial=True

strength=0
if flagLength:
    strength+=1
if flagSpecial:
    strength+=1
if flagNumber:
    strength+=1
if flagLower:
    strength+=1
if flagUpper:
    strength+=1

if strength<=2:
    print("Password is Weak")
elif strength<=4:
    print("Password is Moderate")
else:
    print("Password is Strong")
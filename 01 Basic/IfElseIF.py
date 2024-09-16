# Even Odd Number

number = 18
if number % 2 == 0:
    print("Even number")
else:
    print("Odd Number")

#If Else If

marks = 65
if marks>=90:
    print("Grade A ")
elif marks>=80:
    print("Grade B ")
elif marks>=70:
    print("Grade C ")
else:
    print("Fail")

#Nested if else

marks=92
attendance = 95

if marks>=90:
    if attendance>=90:
        print("Grade A , Honors")
    else:
        print("Grade A ")
elif marks>=80:
    if attendance>=90:
        print("Grade B , Honors")
    else:
        print("Grade B")
else:
    print("Fail")

# Assignment String Slicing Formatting
messag = "Hello Abhishek@From PG-DAI"


def slice_String(s):
    # Printing first 5 elements
    print("First 5 Ele : ", s[:5])
    # Extraxting last 5 elements
    print("Last 5 Ele : ", s[-5:])
    # Extrecting middle characters
    if (len(s) % 2 == 0):
        mid = len(s)//2
        print("Middle 3 ele : ", s[mid-1:mid+2])
    else:
        mid = len(s)//2
        print("Middle 2 ele : ", s[mid-1:mid+1])

    # Extracting and returning every second char from the string
    for i in range(0, len(s), 2):
        print(s[i], end=' ')


slice_String(messag)

#-------------------------------------------------------------

messag = "Hello Abhishek From PG-DAI"
print(len(messag))
print(len(messag)/2)

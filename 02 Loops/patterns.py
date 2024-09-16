# Pyramid pattern
number=int(input("Enter number of rows: "))
i=0
while i<number:
    j=0
    while j<number-i-1:
         print(' ', end='')
         j+=1
    k=0
    while k<=i:
         print('*', end='')
         k+=1
    m=0
    while m<i:
         print('*',end='')
         m+=1
    print()
    i+=1
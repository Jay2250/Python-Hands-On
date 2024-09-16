customerAge = int(input("Enter the Age of Passenger"))

if customerAge<5:
    print("Free..!")
elif customerAge<=12:
    print("Ticket is Rs 5 ")
elif customerAge<=60:
    print("Ticket is Rs 10 ")
else:
    print("Ticket is Rs 7 ")
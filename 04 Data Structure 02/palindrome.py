# palindrome
a = input("Enter a String : ")
print("Palindrome" if a[:] == a[::-1] else "Not Palindrome")   #reverse slicing
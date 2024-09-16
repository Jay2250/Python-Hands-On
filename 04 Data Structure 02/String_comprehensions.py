string = input("Enter a String : ")
print(string.strip(" "))
charter = input("Character to strip from string : ")
print(string.strip(charter))
print(string.lstrip(charter))
print(string.rstrip(charter))


#----------------------------------------------------------------

string = input("Enter a String : ")
print(string.split(" "))
print(string.split("&"))
stringList = ["i am from India...! ", "As if"]
print(" ".join(stringList))


#----------------------------------------------------------------

string1 = "Hello my name is abhi my country is India my love"
subString = "my"
print("First occurence ",string1.find(subString))
print("Last occurence ",string1.rfind(subString))


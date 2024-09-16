# anagram String
string1 = input("Enter the 1st String : ")
string2 = input("Enter the 2nd String : ")
string1Dict = {i: string1.count(i) for i in string1}
string2Dict = {i: string2.count(i) for i in string2}
print(string1Dict)
print(string2Dict)
print("Anagram" if string1Dict==string2Dict else "Not Anagram")
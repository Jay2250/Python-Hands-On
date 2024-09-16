dict1 ={i:i*i*i for i in range(1, 6)}
print(dict1)


#----------------------------------------------------------------
dict2 = {chr(97+i):97+i for i in range(0, 5)}
dict3 = {chr(65+i):65+i for i in range(0, 5)}
print(dict2)
print(dict3)

#-------------------------------------

String1='abcde'
dict4={i:ord(i) for i in String1} #ord is used to find the ascii values of alphabets
print(dict4)
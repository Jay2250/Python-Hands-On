print([x for x in range(11) if x % 2 ==0])

#----------------------------------------------------------------

String1 = "quick brown fox jumps over the lazy dog"
list_of_vowels = [i for i in String1 if i in ['a','e','i','o','u']]
print(list_of_vowels)

#----------------------------------------------------------------

dic = {'a' : 1 , 'b' : 2, 'c': 3}
inv_dic = {value: key for key, value in dic.items()}
print(inv_dic)


#----------------------------------------------------------------

dic = {'a' : 1 , 'b' : 2, 'c': 3}
print(dic)
print(dic.items())
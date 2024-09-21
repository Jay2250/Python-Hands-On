# Assignmnet : Masking PII personal identification info
info_type = (input("Enter type of info : ")).lower()
info = input("Enter the info : ")


def mask_sensitive_info(info, info_type):
    if info_type == "email":
        index = info.find('@')
        if index == -1:
            raise ValueError(
                "Incorrect formating of info pls insert '@' in email ")
        else:
            new_string = info[0]+"*"*len(info[1:index-1])+info[index-1:]
            print(new_string)

    elif info_type == "credit card":
        if len(info) == 16:
            new_number = "*"*len(info[:-4])+info[-4:]
            print(new_number)
        else:
            raise ValueError("Incorrect info")
    else:
        raise ValueError("Invalid info type")


mask_sensitive_info(info, info_type)


mesa = "1234 5678 9876 3214"
list1 = mesa.split(" ")
print(list1)
crd = "*"*(len(list1[0]))+" "+"*"*(len(list1[1])) + \
    " "+"*"*(len(list1[2]))+" "+list1[3]
ll = ' '.join('*'*(len(list1[i]) for i in range(0, 3)))
print(crd)

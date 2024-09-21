# hands on assignment

message = "A A B A S F R S S R V d a"
print(set(message.split(" ")))


def remove_dupliactes(string):
    list2 = message.split(" ")
    list1 = []
    for ele in list2:
        if ele not in list1:
            list1.append(ele)
    print(list1)


remove_dupliactes(message)

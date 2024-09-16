#kwargs with key value pair

def displayInfo(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

displayInfo(name="Alice", age= 30)
displayInfo(city = "NewYork" , country = "USA")


#----------------------------------------------------------------


def display_info(*args, **kwargs):
    print(args)
    print(kwargs)

def display_infos(name,city, **kwargs):
    print(city, name)
    print(kwargs)

display_info(10,20, name = "Alie " , city="New Delhi")
display_infos(10,20,name1 = "Alie " , city1="New Delhi")

#----------------------------------------------------------------


# Assignment 10

def translate():
    message = "This is fun"
    new_str = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in message:
        if char not in vowels:
            new_str += char
        else:
            new_str += 'abc'
    print(new_str)


translate()

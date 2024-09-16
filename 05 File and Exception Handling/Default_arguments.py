# default arguments

def greet(name, message="Hello" ):
    print(f"{message}, {name}")

greet("Alice")
greet("bob","Hi")
greet(name = "Abhi", message = "Hiiii")
greet(message = "Hellllo", name = "Jay")
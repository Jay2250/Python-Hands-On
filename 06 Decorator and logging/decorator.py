def simple_longer(func):
    def wrapper(*args,**kwargs):
        print(f'starting {func.__name__}...')
        result = func(*args, **kwargs) # Calls the original Function
        print(result)
        print(f'Finished {func.__name__}')
        return result
    return wrapper

# Not a wrapper function if wraaper function is not defined
# def simple_longer(func, *args,**kwargs):

#         print(f'starting {func.__name__}...')
#         result= func(*args, **kwargs)
#         print(f'Finished {func.__name__}')
#         return result

@simple_longer
def greet(name):
    print(f'hello .. {name}')

greet("Abhishek")
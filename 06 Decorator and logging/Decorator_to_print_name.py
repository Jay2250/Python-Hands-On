#assignment 1 decorator to print name

def decoratorFunc(func):
    def abhi(*args,**kwargs):
        print(f"First {func.__name__}..")
        result = func(*args,**kwargs)
        print(result)
        print(f'Last {func.__name__}...')
        return result
    return abhi

@decoratorFunc
def greet(name):
    print(f'Hello {name}...!')
greet('Jay')

# ----------------------------------------------------------------

import time
def log_func_name(func):
    def wrapper(*args,**kwargs):
        print(f'starting {func.__name__}...')
        func(*args,**kwargs)
    return wrapper
def log_execution_time(func):
    def wrapper(*args,**kwargs):
        print(f'starting {time.time():2.4f}\n')
        func(*args, **kwargs)
        print(f'\nending {time.time():2.4f}')
    return wrapper

@log_execution_time
@log_func_name
def greet(name):
    print(f'Hello {name}...!')
    for i in range(1000):
        print(i, end=" " )
greet('Jay')
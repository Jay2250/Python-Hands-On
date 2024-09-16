def get_integer_input():
    """THis is doc string"""
    try:
        num = int(input("Enter an integer: "))
        print(f"The entered integer is: {num}")
    except ValueError:
        print("ValueError: Input is not a valid integer.")
    finally:
        print("Operation completed.")

def get_element_from_list(lst, index):
    try:
        element = lst[index]
    except IndexError:
        print("IndexError: Index is out of bounds.")
    except TypeError:
        print("TypeError: Index must be an integer.")
    else:
        print(f"The element at index {index} is: {element}")
    finally:
        print("Operation completed.")

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")
    else:
        print(f"The result of {a} divided by {b} is: {result}")
    finally:
        print("Operation completed.")

# Example usage:
get_integer_input()
get_element_from_list([1, 2, 3], 2)
divide_numbers(10, 2)
divide_numbers(10, 0)

get_integer_input()
print(get_integer_input.__doc__)

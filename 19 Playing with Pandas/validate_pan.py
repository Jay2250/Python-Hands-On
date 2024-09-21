# Assignment Validate if the string is a valid PAN number using regex
import re


def validate_pan_number(pan_number):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    if re.match(pattern, pan_number):
        return f'PAN Number{pan_number} is a Valid PAN Number'
    else:
        return f'PAN Number {pan_number} is not a Valid PAN Number'


pan_number = input("Enter the PAN Number : ")
print(validate_pan_number(pan_number))

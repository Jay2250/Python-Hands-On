#  create a file which has multiple urls along with other text data. Extract only urls from the file

import re


def extract_urls(filename):
  urls = []
  with open(urlFile, 'r') as file:
    for line in file:
      # Use regular expression to find URLs
      found_urls = re.findall(r'https?://[^\s]+', line)
      if found_urls:
        urls.append(found_urls)
  return urls


# Example usage
urlFile = '/content/sample_data/urls.txt'  # Replace with your file name
extracted_urls = extract_urls(urlFile)
print(extracted_urls)


# ---------------------------------------------------------------

# # Regular expression in python
# uses re library
# re.search():searches for the firsst match
# re.match(): checks for a match only at


# use of meta-characters

# -----------------------------------------------------------------
string = "Hello my birth date is 08/09/2024 and today is 16/09/2024 and 12312/04/200a21 "
pattern = r'[0-3][0-9]/[0-1][0-9]/\d{2,4}'
# pattern = r'^(:0[1-9]|1[0-9]|2[0-9]|3[0-1])/(:0[1-9]|1[0-2])/(:2[0-9][0-9][0-9])'
# pattern = r'^(?:19|20)\d\d/(?:0[1-9]|1[0-2])/(?:0[1-9]|[12][0-9]|3[01])$'
pattern = r'\s[\d][\d]/[\d][\d]/[\d][\d][\d][\d]\s'
print(re.findall(pattern, string))


# -----------------------------------------------------------------

string = 'plsaskmeanything'
pattern = r'ask'
print(re.sub(pattern, 'tell', string))

# -----------------------------------------------------------------

String = "The cat is on the catlog. The cat is also in the category"
pattern = r'\scat\s'
print(re.findall(pattern, String))

# -----------------------------------------------------------------

String = "My phone 123 number 456 is 123-456-7890123454321 124 "
pattern = r'\d'
digit = re.findall(pattern, String)
set1 = set(digit)
dict1 = {i: digit.count(i) for i in set1}
print(dict1)
# print(tuple(i for i in dict1.items() if dict1.values()==3))
pattern1 = r'\s[\d][\d][\d]\s'
print(re.findall(pattern1, String))

# ----------------------------------------------------------------

string1 = "Error: File not founs.\n Warning:Low disk space \nError: Access Denied."
pattern = r'^Error.*\.$'
print(re.findall(pattern, string1, re.MULTILINE))

# ---------------------------------------------------------------

password = "Abhishek@123"
pattern = r'^[a-zA-Z]\S{4,10}\d$'
if re.search(pattern, password):
    print("Valid")
else:
    print("Invalid")

# ----------------------------------------------------------------


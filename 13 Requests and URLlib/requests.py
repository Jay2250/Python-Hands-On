import requests

# FTP File Transfer Protocol
# SMTP Simple Mail Transfer
# DNS Domain Name System
# SSH Secure Shell
# SOAP Simple Object Access
# HTTP Hyper Text Transfer
# HTTPS Hyper Text Transfer Secure

# HTTP Methods
# GET
# POST
# DELETE
# PUT
# PATCH
# HEAD

#
response = requests.get('https://restcountries.com/v3.1/all')

# check the status code
if response.status_code == 200:
    print("Resposnse recevied")
    print(response)
else:
    print("Failed to retrieve data", response.status_code)

countries = response.json()

for country in countries:
    name = country.get('name', {}).get('common', 'N/A')
    capital = country.get('capital', ['N/A'])[0]
    area = country.get('area', 'N/A')
    if name == 'India':
        print(f'Country: {name}')
        print(f'Capital: {capital}')
        print(f'Area: {area} sq km ')
        print(f"courency code : {country.get('currencies', 'N/A')}")
        print(f"region : {country.get('region')}")

# ------------------------------------------------------------

# Hands on GET Method
try:
    # count = 0
    userRegion = input("Enter Region : ").capitalize()
    userCode = input("Enter Currency code : ").upper()
    response = requests.get('https://restcountries.com/v3.1/all')
    countries = response.json()
    for country in countries:
        region = country.get('region', {})
        currency_code = country.get('currencies', {})

        if region == userRegion and tuple(currency_code.keys())[0] == userCode:
            # count += 1
            # print(country)
            print(f"Country : {country.get('name', {}).get('common', 'N/A')}")
            print(f"Capital : {country.get('capital', ['N/A'])[0]}")
            print(f"Area : {country.get('area', 'N/A')} sq km")
            print(f'Currency Code : {tuple(currency_code.keys())[0]}')
            print(f'Region : {region}')
            break
    else:
        raise Exception("Not found")
except Exception as e:
    print(e)

# --------------------------------------------------------------------

# Hands on POST request
# API endpoint for creating a new user
post_url = "https://regres.in/api/users"
# Data to be sent in the post request
post_data = {
    "name": "Abhishek",
    "job": "Software Dev"
}
response = requests.post(post_url, json=post_data)

# --------------------------------------------------------------------

post_url = "https://jsonplaceholder.typicode.com/posts"

weather_data = {
    "city": "Newyork",
    "temperature": 28,
    "humidity": 60,
    "condition": "sunny"
}


def post_data(url, data):
    response = requests.post(url, json=data)
    print(response.json())


# Deleting data using id
try:
    post_data(post_url, weather_data)
    id = 111
    delete_url = f"https://reqres.in/api/users/{id}"

    def delete_data(url):
        response = requests.delete(delete_url)
        if response.status_code == 204:
            print("User deleted successfully")
        else:
            print("Failed to delete user")
    delete_data(delete_url)
except Exception as e:
    print(e)

# -----------------------------------------------------------------


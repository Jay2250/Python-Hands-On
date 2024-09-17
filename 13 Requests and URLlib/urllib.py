# URL library : Standard library in python used for working with urls
# provides modeules and functions to
# Fetch data from urls
# Handle url encoding
# Decode urls
# Manage requests and response over http and https protocols

from urllib.parse import urlparse, parse_qs, urlencode

# Extracting the domain name fro a full url to identify which website is being accessed
url = "https://www.example.com/search?query=python&sort=recent"
parsed_url = urlparse(url)
domain_name = parsed_url.netloc
print(f'Domain :{domain_name}')
print(f'Path : {parsed_url.path}')
print(f'Query : {parsed_url.query}')

# Extracting or modifying query parameters in a url, at runtime
url = "https://www.example.com/search?query=python&sort=recent"
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)
print(f'Query Params : {query_params}')

# Adding or removing query parameters from an existing url
base_url = 'https://www.example.com/search'
query_params = {
    'query': 'python',
    'sort': 'recent'
}
updated_url = base_url + '?' + urlencode(query_params)
print(f'Updated URL : {updated_url}')

# ---------------------------------------------------------------
# list of urls

urls = [
    "https://www.example.com/search?query=python&sort=recent",
    "https://www.bing.com/search?q=google+translate+english+to+marathi&qs=LS&pq=google+t&sk=HS1&sc=10-8&cvid=1B597EF3A0034C869145627317E098DA&FORM=QBRE&sp=2&ghc=1&lq=0",
    "https://www.flipkart.com/apple-iphone-15-pro-natural-titanium-128-gb/p/itm7ffb1e9990edd?pid=MOBGTAGP38MFPN6Q&lid=LSTMOBGTAGP38MFPN6QBVS1LF&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_5&otracker=CLP_Filters&fm=organic&iid=a1ef72e4-6072-404c-adcf-985d246bbd13.MOBGTAGP38MFPN6Q.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=xzsx4ashps0000001726470286089"
]
for url in urls:
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    print(f'Domain :{domain_name}')
    print(f'Path : {parsed_url.path}')
    print(f'Query : {parsed_url.query}')

# ----------------------------------------------------------------


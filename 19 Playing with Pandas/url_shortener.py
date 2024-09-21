class URLShortener:
    def __init__(self):
        self.url_dict = {}
        self.base_url = "http://short.url/"
        self.index = 1

    def add_url(self, original_url):
        # Checking URL already exists in the dictionary
        if original_url in self.url_dict:
            print(f"{original_url} URL already exists as :")

        else:
            # Creating New short URL
            shortened_url = self.base_url + str(self.index)

            # Adding the new short URL to the dictionary
            self.url_dict[original_url] = shortened_url
            self.index += 1

            # Display the new shortened URL
            print(f"{original_url} -> {shortened_url}")

        return self.url_dict[original_url]


# Example usage
url = URLShortener()
url.add_url("https://www.example.com")
url.add_url("https://www.python.com")
url.add_url("https://www.pandas.com")
url.add_url("https://www.example.com")

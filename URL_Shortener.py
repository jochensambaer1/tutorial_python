import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, original_url):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        self.url_map[short_url] = original_url
        return short_url

    def get_original_url(self, short_url):
        return self.url_map.get(short_url)

# Usage example
shortener = URLShortener()
original_url = "https://www.example.com"
short_url = shortener.shorten_url(original_url)
print(f"Short URL: {short_url}")
print(f"Original URL: {shortener.get_original_url(short_url)}")

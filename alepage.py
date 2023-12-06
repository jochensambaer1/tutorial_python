import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_paths(url):
    paths = set()  # Use a set to store unique paths

    # Make an HTTP request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract paths from anchor tags
    for a_tag in soup.find_all('a', href=True):
        absolute_path = urljoin(url, a_tag['href'])
        paths.add(absolute_path)

    return paths

def main():
    website_url = 'http://www.pleasurebonbon.com/'
    all_paths = get_all_paths(website_url)

    print("All Paths:")
    for path in all_paths:
        print(path)

if __name__ == "__main__":
    main()

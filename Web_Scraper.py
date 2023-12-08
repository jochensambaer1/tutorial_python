import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://example.com"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the desired data from the parsed HTML
# Example: Extract all the links on the page
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

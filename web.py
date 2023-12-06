import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request  # Import urllib module for urlretrieve

def save_photos_from_link(link):
    try:
        response = requests.get(link)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        img_tags = soup.find_all('img')

        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                img_url = urljoin(link, img_url)
                print(f"Downloading image from: {img_url}")
                
                filename = os.path.basename(img_url)
                filename = ''.join(c if c.isalnum() or c in ['.', '_'] else '_' for c in filename)
                
                urllib.request.urlretrieve(img_url, filename)
                
                print(f"Image downloaded and saved as: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")

# Example usage
link = "https://tabledho.squarespace.com/welcome"
save_photos_from_link(link)


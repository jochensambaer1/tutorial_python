import requests

def brute_force_urls(start_url):
    # Add your logic here to generate all possible URLs
    
    # Example: Generate URLs by appending numbers to the start URL
    for i in range(1, 100):
        url = start_url + str(i)
        
        # Send a request to the URL
        response = requests.get(url)
        
        # Add your logic here to process the response
        
        # Example: Print the URL and response status code
        print(f"URL: {url}, Status Code: {response.status_code}")

# Usage example
start_url = "https://example.com/"
brute_force_urls(start_url)

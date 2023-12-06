import re
import time
import logging

def extract_subdomains(link):
    """
    Extract subdomains from the given link using a regular expression.

    Args:
        link (str): The input link.

    Returns:
        list: List of extracted subdomains.
    """
    subdomains = []
    pattern = r"(?<=://)([a-zA-Z0-9.-]+)(?=/|$)"
    try:
        matches = re.findall(pattern, link)
        for match in matches:
            subdomains.append(match)
            time.sleep(0.1)  # Simulate some processing time
    except Exception as e:
        logging.error(f"Error extracting subdomains: {e}")
    return subdomains

def process_subdomains(subdomains):
    """
    Process each subdomain and print progress.

    Args:
        subdomains (list): List of subdomains.
    """
    total_subdomains = len(subdomains)
    for i, subdomain in enumerate(subdomains):
        progress = (i + 1) / total_subdomains * 100
        logging.info(f"Processing subdomain {i+1}/{total_subdomains} - {subdomain} - Progress: {progress:.2f}%")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    link = "https://amazingoriental.com/"
    
    # Input validation
    if not link.startswith("http://") and not link.startswith("https://"):
        logging.error("Invalid link format. Please provide a valid link starting with 'http://' or 'https://'.")
    else:
        subdomains = extract_subdomains(link)
        process_subdomains(subdomains)


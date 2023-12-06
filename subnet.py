import socket
import ipaddress

def get_subnets(url):
    try:
        # Remove the "https://" prefix and any path information
        domain = url.replace("https://", "").split("/")[0]
        ip_address = socket.gethostbyname(domain)
        network = ipaddress.ip_network(ip_address)
        subnets = list(network.subnets())
        return subnets
    except socket.gaierror as e:
        print(f"Error: {e}")
        return []

url = input("Enter a URL: ")
subnets = get_subnets(url)

if subnets:
    for subnet in subnets:
        print(subnet)
else:
    print("Subnet information not available due to an error.")

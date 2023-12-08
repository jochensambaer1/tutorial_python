import random
import string

passwords = {}

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(service, password):
    passwords[service] = password

def get_password(service):
    return passwords.get(service)

def delete_password(service):
    if service in passwords:
        del passwords[service]

# Example usage
password = generate_password(10)
save_password("GitHub", password)
retrieved_password = get_password("GitHub")
print(retrieved_password)

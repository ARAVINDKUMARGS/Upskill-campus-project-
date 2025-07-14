
# Password Generator
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(characters, length))

length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))

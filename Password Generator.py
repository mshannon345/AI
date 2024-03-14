#Programmer: Miles shannon
#Date 3/13/2024
#Program: Password Generator
#Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import os
import getpass

def hash_password(password, salt):
    # Concatenate password and salt
    salted_password = password + salt
    # Hash the concatenated string using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password

def main():
    # Get user input for password (hidden)
    password = getpass.getpass("Enter your password: ")

    # Generate a random salt
    salt = os.urandom(16).hex()

    # Hash the password with the generated salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()

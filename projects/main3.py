# Random Password Challenge

# Lesson 26: Python Challenges
# Write a Python program to generate a random password consisting of lower case and upper case characters along with numbers. You can also use random module for shuffling the password generated.

import random

def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.choices(characters, k=length))
    return password

password_length = int(input("Enter password length: "))
print("Generated Password:", generate_password(password_length))

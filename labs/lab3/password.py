# File: filename.py
# Author: Student name
# Date: 01/01/2022
# Section: Student section number
# E-mail: email@tamu.edu
# Description:

length = False
space = False
digits = False
letters = False
vowels = False
uppercase = False
lowercase = False
special_characters = False
consecutive_letters = False
valid = False

while not valid:
    password = input('Enter a password: ')

    if password == "quit":
        break

    # The password must be at least 9 characters long and at most 18 characters long
    length = 9 <= len(password) <= 18

    # The password should contain no spaces
    space = " " not in password

    # The password must contain at least 2 digits.
    digits_count = sum(char.isdigit() for char in password)
    digits = digits_count >= 2

    # The password must contain at least 4 letters.
    letters = sum(char.isalpha() for char in password)
    letters = letters >= 4

    # The password must contain at least 2 vowels
    vowels_count = sum(char.lower() in ["a", "e", "i", "o", "u"] for char in password)
    vowels = vowels_count >= 2

    # The password must contain at least one uppercase letter.
    uppercase_count = sum(char.isupper() for char in password)
    uppercase = bool(uppercase_count)

    # The password must contain at least one lowercase letter.
    lowercase_count = sum(char.islower() for char in password)
    lowercase = bool(lowercase_count)

    # The password must contain at least two special characters from [‘$’,’#’,’@’]
    special_characters_count = sum(char in ["$", "#", "@", "&"] for char in password)
    special_characters = special_characters_count >= 2

    # The password must not contain two consecutive identical characters
    consecutive_letters = False
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            consecutive_letters = True
            break

    print(f"\nPassword validation")
    print(f"9 to 18 characters: {length}")
    print(f"No spaces: {space}")
    print(f"At least 2 digits: {digits}")
    print(f"At least 4 letters: {letters}")
    print(f"At least 2 vowels: {vowels}")
    print(f"At least one uppercase letter: {uppercase}")
    print(f"At least one lowercase letter: {lowercase}")
    print(f"At least two special characters from ['$', '#', '@', '&']: {special_characters}")
    print(f"No two consecutive identical characters: {not consecutive_letters}")

    valid = length and space and digits and letters and vowels and uppercase and lowercase and special_characters and not consecutive_letters

    if not valid:
        print(f"Password {password} is invalid. Try again.\n")

if valid:
    print(f"\nPassword {password} is valid!")
    print(f"Number of digits: {digits_count}")
    print(f"Number of vowels: {vowels_count}")
    print(f"Number of uppercase letters: {uppercase_count}")
    print(f"Number of lowercase letters: {lowercase_count}")
    print(f"Number of special characters: {special_characters_count}")

"""Write a Python module password.py that performs the following operations:
Ask the user to enter a password.
Verify that the password meets some predefined requirements.
The password requirements are the following:

The password must be at least 9 characters long and at most 18 characters long (included).
The password must end with a letter.
The ending letter must be uppercase.
The password must contain `979`.
The password must not start with `@`."""

password = input('Enter password: ')
length = 9 <= len(password) <= 18
end_letter = password[-1].isalpha()
end_letter_uppercase = password[-1].isupper()
contains = '979' in password # Membership
start = password[0] == '@'

valid = length and end_letter_uppercase and contains and not start

print(f"9 to 18 characters: {length}")
print(f"Ends with letter: {end_letter}")
print(f"Ends with uppercase letter: {end_letter_uppercase}")
print(f"Contains 979: {contains}")
print(f"Does not start with @: {start}")
print(f"Valid password: {valid}")
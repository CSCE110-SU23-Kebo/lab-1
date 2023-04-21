# File: filename.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

print("Welcome to the Library Management App.")
print("Member registration")
first_name = input("Enter the member's first name: ")
middle_name = input("Enter the member's middle name: ")
last_name = input("Enter the member's last name: ")
phone = input("Enter the member's phone number: ")
mailing_address = input("Enter the member's mailing address: ")

name = first_name.capitalize() + " " + middle_name.capitalize() + " " + last_name.capitalize()
international_format = "+1-" + phone[0:3] + "-" + phone[4:7] + "-" + phone[8:]
north_american_format = "(" + phone[0:3] + ") " + phone[4:7] + "-" + phone[8:]
local_format = phone[4:7] + "." + phone[8:]
street, city, state_zip = mailing_address.split(',')

street_number = street[0:3]
street_name = street[4:].upper()
city = city[1:].upper()
state = state_zip[1:3].upper()
zip_code = state_zip[4:].upper()

print(f"\nMember name: {name}")
print(f"Phone number (International format): {international_format}")
print(f"Phone number (North American format): {north_american_format}")
print(f"Phone number (Local format): {local_format}")
print(f"Street number: {street_number}")
print(f"Street name: {street_name}")
print(f"City: {city}")
print(f"State: {state}")
print(f"Zip: {zip_code}")

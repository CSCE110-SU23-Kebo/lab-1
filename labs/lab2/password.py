# File: filename.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

print("Welcome to the Library Management App.")
print("Password generation")
l_name = input("Enter the member's last name: ")
phone = input("Enter the member's phone number: ")
mail = input("Enter the member's mailing address: ")

l_name = l_name.lower()
password_1 = str(l_name.count("a") + l_name.count("e") + l_name.count("i") + l_name.count("o") + l_name.count("u"))
password_2 = phone.replace(phone[0], l_name.upper()[-1])
password_3 = mail[:-5:-1]
password_4 = str(int(mail[0]) % 2) + str(int(mail[1]) % 2) + str(int(mail[2]) % 2)
print(f"\nGenerated password: {password_1 + password_2 + password_3 + password_4}")

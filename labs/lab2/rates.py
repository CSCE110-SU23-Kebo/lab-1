# File: filename.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

import math

print("Welcome to the Library Management App.")
print("Membership rates\n")
days = int(input("Enter the membership number of days: "))
week = math.ceil(days / 7)
month = math.ceil(days / 30)
quarter = math.ceil(days / 90)

weekly_membership = round(week * 10 * 1.0825, 2)
monthly_membership = round(month * 30 * 1.0825, 2)
quarterly_membership = round(quarter * 80 * 1.0825, 2)

print(f"Weekly membership: {week} weeks at ${weekly_membership}")
print(f"Monthly membership: {month} months at ${monthly_membership}")
print(f"Quarterly membership: {quarter} quarters at ${quarterly_membership}")
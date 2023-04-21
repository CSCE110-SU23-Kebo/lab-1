# File: filename.py
# Author: Student name
# Date: xx/xx/2021
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g. This program asks for ...

amount = float(input('Please enter the dollar amount: '))
halves = amount/0.5
quarters = amount/.25
dimes = amount*100/10
print()
print(f'For ${amount}, you can get {int(halves)} halves, or {int(quarters)} quarters, or {int(dimes)} dimes.')
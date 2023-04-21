# File: filename.py
# Author: Student name
# Date: xx/xx/2021
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g. This program asks for ...

name = input('What is your first name? ')
last_name = input('What is your last name? ')
title = input('Which title do you prefer? Mr., Mrs., Miss, Ms., Dr.: ')
year = int(input('In what year were you born? '))

print()
print(f'Welcome, {title} {name} {last_name}.')
print(f'You will be {(2022-year) + 5} years old in five years.')
# File: filename.py
# Author: Student name
# Date: xx/xx/2021
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g. This program asks for ...

x1 = float(input('x coordinate of the first point: '))
y1 = float(input('y coordinate of the first point: '))
x2 = float(input('\nx coordinate of the second point: '))
y2 = float(input('y coordinate of the second point: '))

x = (x1 - x2) ** 2
y = (y1 - y2) ** 2
distance = round((x + y) ** (1/2), 2)

print()
print(f'The distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance}')
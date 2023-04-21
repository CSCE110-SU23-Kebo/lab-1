# File: filename.py
# Author: Student name
# Date: xx/xx/2021
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g. This program asks for ...

amount = int(input('Please enter the dollar amount: '))
hundreds = amount // 100
remainder = amount % 100

fifties = remainder // 50
remainder = remainder % 50

twenties = remainder // 20
remainder = remainder % 20

tens = remainder // 10
remainder = remainder % 10

fives = remainder // 5
remainder = remainder % 5

ones = remainder

print(f"\nCash withdrawal for ${amount}\n")
print(f"{'Denomination':<15}{'Number of bills':^20}")
print(f"{'$100':<15}{hundreds:^20}")
print(f"{'$50':<15}{fifties:^20}")
print(f"{'$20':<15}{twenties:^20}")
print(f"{'$10':<15}{tens:^20}")
print(f"{'$5':<15}{fives:^20}")
print(f"{'$1':<15}{ones:^20}")

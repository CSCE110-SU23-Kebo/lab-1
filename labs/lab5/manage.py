# File: filename.py
# Author: Student name
# Date: 10/14/2019
# Section: Student section number
# E-mail: email@tamu.edu
# Description:
from datetime import date
books = {}

while True:
    type = input('Enter book type: ').title()
    if type.lower() == 'done':
        break
    if type not in books:
        books[type] = {}
    title = input('Enter book\'s title: ').title()
    year = input('Enter book\'s publication year: ')
    author = input('Enter book\'s first author\'s name: ').title()
    publisher = input('Enter book\'s publisher name: ').title()
    publisher = publisher.title()
    if year not in books[type]:
        books[type][year] = [[title, author, publisher]]
    else:
        books[type][year] += [[title, author, publisher]]
    print()
print()
if books:
    for types, values in books.items():
        print(f"===={types}")
        for year, ti_au_pub in values.items():
            print(f'Published in {year}:')
            print(f"{'Title':<15}|{'Author':<15}|{'Publisher':<15}|")
            for items in ti_au_pub:
                for item in items:
                    print(f'{item:<15}', end='|')
                print()
            print()
else:
    print('Information not found!')

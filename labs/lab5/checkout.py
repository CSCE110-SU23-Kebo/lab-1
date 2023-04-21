# File: filename.py
# Author: Student name
# Date: 10/14/2019
# Section: Student section number
# E-mail: email@tamu.edu
# Description:
cart = {}
while True:
    print('1. Add a book to the cart\n2. Remove book(s) from the cart\n3. View cart\n4. Sort cart\n5. Quit\n')
    option = input('Select from the menu: ')
    if option == '1':
        title = input('Book title: ').title()
        if title in cart:
            print(f'This book is in your cart.')
        else:
            author = input('Book author\'s name: ').title()
            period = input('How many days: ')
            #cart[title] = [author, period]
            book = {title:[author,period]}
            cart.update(book)
    elif option == '2':
        choice = input('Remove all or an item? (Enter \'all\' or \'book title\'): ').title()
        if choice == 'All':
            cart.clear()
        else:
            if choice in cart.keys():
                del cart[choice]
            else:
                print(f'{choice} is not in your cart.')
    elif option == '3':
        if cart.keys():
            print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
            for key, value in cart.items():
                print(f"{key:<20}", end='')
                for item in value:
                    print(f"{item:<20}", end='')
                print()
        else:
            print('Cart is empty.')

    elif option == '4':
        asc_des = input('Enter \'A\' for Ascending and \'D\' for Descending: ').upper()
        if asc_des == 'A':
            asc_des = False
        else:
            asc_des = True
        print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
        for key,value in sorted(cart.items(), reverse = asc_des):
            print(f"{key:<20}", end='')
            for item in value:
                print(f"{item:<20}", end='')
            print()

    elif option == '5':
        break
    print()

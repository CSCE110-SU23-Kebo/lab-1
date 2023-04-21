# File: book_library.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...


import math


def main():
    """Driver function"""
    library = {}
    while True:
        print_menu()
        option = input('Choose a menu option: ')
        if option == '1':
            add_books(library)
        elif option == '2':
            print_books(library)
        elif option == '3':
            create_collections(library)
        elif option == '4':
            sort_collections(library)
        elif option == '5':
            delete_collection(library)
        elif option == '6':
            print("End", end='')
            break
        else:
            print('\nInvalid entry\n')


def print_menu():
    """Prints the menu of options to the librarian"""
    print("*******************Main Menu*******************")
    print('1. Add books to the library')
    print('2. Print available books in the library')
    print('3. Create book collections')
    print('4. Sort books in the collections')
    print('5. Delete a collection')
    print('6. Quit')
    print('***********************************************\n')


def check_isbn(isbn):
    """Checks the format of an ISBN"""
    return isbn.isdigit() and len(isbn) == 10


def add_books(library):
    """Adds unique books to the library
    library = {isbn1: [title1, collectionNum or -1], isbn2: [title2, collectionNum or -1]}"""
    number_of_books = int(input('How many books would you like to enter: '))
    print()
    for i in range(number_of_books):
        while True:
            book = input(f"Enter book {i + 1}: ")
            if len(book) <= 10:
                print('Invalid entry')
            else:
                isbn = book[-10:]
                title = book[:-11].strip()
                if check_isbn(isbn) and title and (isbn not in library):
                    library[isbn] = [title, -1]  # Initial entry in Library
                    break
                else:
                    print('Invalid entry')
    print()


def print_books(library):
    """Prints available books in the library"""
    print('\nBooks available in the library: ')
    for isbn in library.keys():
        if library[isbn][1] == -1: # If the book is not assigned to a collection
            print(f'{library[isbn][0]:<20}{isbn:<20}')
        print()


def create_collections(library):
    """Creates book collections"""
    if [library[isbn][1] for isbn in library.keys() if library[isbn][1] == -1]:
        curr_collections = [library[isbn][1] for isbn in library.keys()]
        library_size = curr_collections.count(-1)
        start_collections = max(curr_collections) + 1
        collection_size = int(input("What is the size of the collection? "))
        collections = start_collections + math.ceil(library_size / collection_size)

        total = 0
        for i in range(start_collections, collections):
            print(f"\nEnter the book ISBNs for collection {i + 1}: ")
            while [library[isbn][1] for isbn in library.keys()].count(i) < collection_size and total < library_size:
                isbn = input()
                if check_isbn(isbn) and isbn in library and library[isbn][1] == -1:
                    library[isbn][1] = i
                    total += 1
                else:
                    print('Invalid entry')

        print_collections(library)
    else:
        print('\nInvalid entry\n')


def sort_collections(library):
    """Prints sorted books in each collection"""
    if [library[isbn][1] for isbn in library.keys() if library[isbn][1] != -1]:
        while True:
            order = input("Sort books in ascending or descending order of isbn: ")
            if order == 'ascending' or order == 'descending':
                break
            else:
                print('Invalid entry')
        print('\nCurrent book collections: ')
        collections = max([library[isbn][1] for isbn in library.keys()]) + 1

        for i in range(collections):
            print(f'Collection {i + 1}')
            current_collection = {isbn: [library[isbn][0], library[isbn][1]] for isbn in library if
                                 library[isbn][1] == i}
            for isbn in sorted(current_collection.keys(), reverse=(order == 'descending')):
                print(f"{library[isbn][0]:<20}{isbn:<20}")
            print()
    else:
        print('\nInvalid entry\n')


def delete_collection(library):
    """Deletes a collection from the list of collections and adds it back to the library"""
    collection = int(input('Which collection would you like to delete? '))
    if 0 < collection <= (max([library[isbn][1] for isbn in library.keys()]) + 1):
        for isbn in library.keys():
            if library[isbn][1] == collection - 1:
                library[isbn][1] = -1
            if library[isbn][1] > collection - 1:
                library[isbn][1] -= 1
        print_collections(library)
    else:
        print('Invalid entry\n')


def print_collections(library):
    collections = max([library[isbn][1] for isbn in library.keys()]) + 1
    print('\nCurrent book collections: ')
    for i in range(collections):
        print(f'Collection {i + 1}')
        current_collection = {isbn: [library[isbn][0], library[isbn][1]] for isbn in library if library[isbn][1] == i}
        for isbn in current_collection.keys():
            print(f"{library[isbn][0]:<20}{isbn:<20}")
        print()


main()

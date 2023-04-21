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
    # to do
    pass


def check_isbn(isbn):
    """Checks the format of an ISBN"""
    # to do
    pass


def add_books(library):
    """Adds unique books to the library"""
    # to do
    pass


def print_books(library):
    """Prints available books in the library"""
    # to do
    pass


def create_collections(library):
    """Creates book collections"""
    # to do
    pass


def sort_collections(library):
    """Sort books in the collections"""
    # to do
    pass


def delete_collection(library):
    """Deletes a collection"""
    # to do
    pass


main()

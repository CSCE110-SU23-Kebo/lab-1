# File: textstats.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...



def main():
    """Gets a block of text from the user and prints some statistics about the text."""
    text = input("Enter text: ").lower()
    print(f"Number of sentences: {get_sentences(text)}")
    print(f"Number of words: {get_words(text)}")
    print(f"Number of punctuations: {get_punctuations(text)}")
    print_letters(text)
    print_palindromes(text)


def get_sentences(text):
    """Returns the number of sentences in the text. """
    pass


def get_words(text):
    """Returns the number of words in the text."""
    pass


def get_punctuations(text):
    """Returns the number of punctuations in the text."""
    pass


def print_letters(text):
    """Prints the number of occurrences of case-insensitive letters in the text. """
    pass


def print_palindromes(text):
    """Prints the number of occurrences of case-insensitive palindrome numbers and palindrome words and letters in
    the text. """
    pass


main()

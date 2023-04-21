# File: textstats.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

import string
import re


def main():
    """Gets a block of text from the user and prints some statistics about the text."""
    text = input("Enter text: ").lower()
    print(f"Number of sentences: {get_sentences(text)}")
    print(f"Number of words: {get_words(text)}")
    print(f"Number of punctuations: {get_punctuations(text)}")
    print_letters(text)
    print_palindromes(text)


def get_sentences(text):
    """Returns the number of sentences in the text."""
    return len(re.findall(r'\.', text))


def get_words(text):
    """Returns the number of words in the text."""
    #print(re.findall(r'\w+', text))
    return len(re.findall(r'\w+', text))


def get_punctuations(text):
    """Returns the number of punctuations in the text."""
    punctuations = 0
    for character in text:
        if character in string.punctuation:
            punctuations += 1
    return punctuations


def print_letters(text):
    """Prints the number of occurrences of case-insensitive letters in the text. Case-insensitive means that a letter
    is the same whether it is uppercase or lowercase. The function should print the letters in decreasing order of
    the number of occurrences. If multiple letters have the same number of occurrences, print the letters in
    alphabetical order. Separate groups of letters with the same number of occurrences by a blank line.
    """
    letters = {}
    for char in text:
        if char.isalpha():
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

    letters_count = {}
    for char, count in letters.items():
        letters_count[count] = letters_count.get(count, []) + [char]
    #print(letters_count)

    print("\nLetter statistics:")
    for i in sorted(letters_count, reverse=True):
        chars = letters_count[i]
        for char in sorted(chars):
            print(f"{char} found {i} {'times' if i > 1 else 'time'}.")
        print()


def print_palindromes(text):
    """Prints the number of occurrences of case-insensitive palindrome numbers and palindrome words in the text. The
    function should print the palindromes sorted alphanumerically with their number of occurrences. Numbers must be
    printed first, and words must be printed next. """
    text = re.findall(r'\w+', text)
    palindrome_numbers = {}
    palindrome_words = {}

    for word in text:
        if word == word[::-1] and word.isnumeric():
            if word not in palindrome_numbers:
                palindrome_numbers[word] = 1
            else:
                palindrome_numbers[word] += 1
        elif word == word[::-1] and not word.isnumeric():
            if word not in palindrome_words:
                palindrome_words[word] = 1
            else:
                palindrome_words[word] += 1

    print("Palindrome numbers:")
    for number, count in sorted(palindrome_numbers.items()):
        print(f"{number}: {count}")

    print("\nPalindrome words and letters:")
    for word, count in sorted(palindrome_words.items()):
        print(f"{word}: {count}")


main()

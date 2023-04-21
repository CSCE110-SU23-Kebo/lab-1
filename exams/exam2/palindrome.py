# palindrome.py

def main():
    """Driver function"""
    text = input(" Enter words: ")
    print(f"Palindrome booleans: {find_palindromes(text)}")
    print(f"Number of palindromes: {count_palindromes(text)}")


def find_palindromes(text):
    """Returns a list of booleans representing if each entry is a palindrome or not."""
    words = text.split()
    palindromes = [word == word[::-1] for word in words] # Create a list of booleans
    return palindromes


def count_palindromes(text):
    """Returns the number of palindromes in the string."""
    words = text.split()
    palindromes = [word == word[::-1] for word in words]
    return palindromes.count(True) # Count the TRUE values in the list


if __name__ == "__main__":
    main()

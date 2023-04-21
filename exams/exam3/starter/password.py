def validate(password):
    """
    This function validates a password and returns a boolean that determines if the password is valid of invalid.
    """
    is_valid = False
    # todo

    return is_valid


def main():
    """
    This function prompts for a file of passwords.
    Next, it opens the file.
    Next, it checks for the validity of every password in the file using the function validate() and prints the validity of the password.
    """
    filename = input("Enter the password file name: ")
    print()
    with open(filename, 'r') as content:
        pass
        # todo


main()

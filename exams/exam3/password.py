def validate(password):
    """
    This function validates a password and returns a boolean that determines if the password is valid of invalid.
    """

    length = 9 <= len(password) <= 18
    end_letter_uppercase = password[-1].isupper()
    contains = '62' in password  # Membership
    start = password[0] != '@'
    digits = [character.isdigit() for character in password]
    digits = sum(digits) >= 4

    # print(f"length: {length}, end_letter: {end_letter_uppercase}, contains: {contains}, start: {start},
    # digits: {digits}")

    is_valid = length and end_letter_uppercase and contains and start and digits
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
        passwords = content.readlines()
        for password in passwords:
            password = password.strip()
            if validate(password):
                print(f'{password} is valid')
            else:
                print(f'{password} is invalid')

if __name__ == '__main__':
    main()

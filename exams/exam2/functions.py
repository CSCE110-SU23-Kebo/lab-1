def shuffle(numbers, word):
    count = len(numbers)
    letters = list(word)
    mixed = []
    for i in range(count):
        char = letters[i].upper()
        mixed.insert(i, char)
        mixed.append(numbers[i])
    return mixed


def main():
    numbers = ''
    while numbers != 'quit':
        numbers = input('Enter numbers: ').split()
        numbers = [int(n) for n in numbers]
        word = input('Enter a word: ')
        print(f"Mixed entries: {shuffle(numbers, word)}")


if __name__ == "__main__":
    main()

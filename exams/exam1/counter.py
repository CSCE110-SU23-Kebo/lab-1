while True:
    count = 0
    entry = input('Enter sentence: ')
    sentence = entry.lower().split()
    if entry == 'quit':
        break
    for word in sentence:
        if word == word[::-1]:
            count += 1
    print(f'Found {count} palindromes and {len(sentence)-count} non-palindromes.\n')
print(f'end')
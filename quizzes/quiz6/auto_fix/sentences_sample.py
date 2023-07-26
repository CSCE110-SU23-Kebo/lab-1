import re


def main():
    with open("sentences.txt", "w") as data:
        sentence = input("Enter a sentence: ")
        while sentence != "quit":
            sentence = re.sub(r'[^\w\s]', '', sentence)
            words = sentence.split()
            reversed_sentence = " ".join(reversed(words))
            data.write(f"{reversed_sentence.upper()}\n")
            sentence = input("Enter a sentence: ")


main()

# accumulator.py

def main():
    """Driver function"""
    numbers = input("Enter numbers: ").split()
    numbers = [int(i) for i in numbers]
    res = accumulate(numbers)
    print('Accumulated sum:', *res, sep=' ')
    # print(accumulate(numbers))


def accumulate(entries):
    """Returns a list of the accumulating sum"""
    if len(entries) == 0:
        return []
    else:
        accumulator = []
        temp_sum = 0
        for item in entries:
            temp_sum += item
            accumulator.append(temp_sum)
    return accumulator

if __name__ == "__main__":
    main()

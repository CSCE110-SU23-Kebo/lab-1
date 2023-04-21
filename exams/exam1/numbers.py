numbers = input('Enter numbers: ').split()
numbers = [int(num) for num in numbers]  # [expression for iterator in sequence]
even = 0
for num in numbers:
    if num % 2 == 0:  # if the number is even
        even += 1
print(f'Count of numbers: {len(numbers)}')
print(f'Even numbers: {even}')
print(f'Odd numbers: {len(numbers) - even}')
print(f'Sum of numbers: {sum(numbers)}')
print(f'Highest number: {max(numbers)}')
print(f'Lowest number: {min(numbers)}')

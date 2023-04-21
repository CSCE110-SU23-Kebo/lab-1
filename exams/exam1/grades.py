# Grades calculator
first_name = input("First name: ")
last_name = input("Last name: ")
grades_count = int(input("Number of grades: "))
grades_sum = 0  # Initialize

for item in range(grades_count):
    grade = float(input(f"Enter grade {item + 1}: "))
    grades_sum += grade

grade_average = grades_sum / grades_count

if 90 <= grade_average <= 100:
    letter = 'A'
elif 80 <= grade_average < 90:
    letter = 'B'
elif 70 <= grade_average < 80:
    letter = 'C'
elif 60 <= grade_average < 70:
    letter = 'D'
elif 0 <= grade_average < 60:
    letter = 'F'
else:
    letter = ''

print(f"\nStudent name: {first_name.capitalize()} {last_name.capitalize()}")
print(f"Average grade: {round(grade_average, 2)}")

if letter:  # if the variable letter is not empty
    print(f"Letter grade: {letter}")
else:
    print(f'Invalid grade')

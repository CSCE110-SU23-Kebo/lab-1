students = {2022: {'name': 'lizzy', 'grades': [100, 91, 96, 98]}, 2023: {'name': 'michael', 'grades': [89, 95, 83, 90]}}
print(students.get(2022).get('grades')[2])
print(students[2022]['grades'][2])

student = {'name': 'Cindy', 'class': 110, 'grade': 98}
student.clear()
print(student)

student = {'name': 'Iris', 'class': 121, 'grade': 96}
score = student.get(2)
score = student.get('grade')
score = student[2]
score = student['grade']

print(student.get(2))
print(student.get('grade'))
#print(student[2])
print(student['grade'])

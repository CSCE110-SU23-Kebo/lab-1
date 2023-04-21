# File: filename.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

# Ask for the number of rows and the number of columns of matrix A, space-separated on one line.
matrix_A_rows, matrix_A_columns = input("Matrix A number of rows and columns: ").split()
# No matrix row or column number should exceed 10.
while not (0 < int(matrix_A_rows) <= 10 and 0 < int(matrix_A_columns) <= 10):
    matrix_A_rows, matrix_A_columns = input("Matrix A number of rows and columns: ").split()
matrix_A_rows = int(matrix_A_rows)
matrix_A_columns = int(matrix_A_columns)

# Ask for the number of rows and the number of columns of matrix B, space-separated on one line.
matrix_B_rows, matrix_B_columns = input("Matrix B number of rows and columns: ").split()
# No matrix row or column number should exceed 10.
while not (0 < int(matrix_B_rows) <= 10 and 0 < int(matrix_B_columns) <= 10):
    matrix_B_rows, matrix_B_columns = input("Matrix B number of rows and columns: ").split()
matrix_B_rows = int(matrix_B_rows)
matrix_B_columns = int(matrix_B_columns)

if matrix_A_columns != matrix_B_rows:
    print(
        f"Matrix A: ({matrix_A_rows}x{matrix_A_columns}) Matrix B: ({matrix_B_rows}x{matrix_B_columns}) cannot be multiplied.")
    exit()

# Ask for the integers in matrix A one row at a time.
matrix_A = []
print()
for row in range(matrix_A_rows):
    line = input(f"Matrix A row {row + 1}: ").split()
    while len(line) != matrix_A_columns:
        line = input(f"Matrix A row {row + 1}: ").split()
    line = [int(number) for number in line]
    matrix_A.append(line)

# Ask for the integers in matrix B one row at a time.
matrix_B = []
print()
for row in range(matrix_B_rows):
    line = input(f"Matrix B row {row + 1}: ").split()
    while len(line) != matrix_B_columns:
        line = input(f"Matrix B row {row + 1}: ").split()
    line = [int(number) for number in line]
    matrix_B.append(line)

# Initialize matrix C
matrix_C = []
for rows in range(matrix_A_rows):
    line = [0] * matrix_B_columns;
    matrix_C.append(line)

# Print matrix A
print("\nMatrix A:")
for row in range(matrix_A_rows):
    for column in range(matrix_A_columns):
        print(f"{matrix_A[row][column]:<6}", end="")
    print()

# Print matrix B
print("\nMatrix B:")
for row in range(matrix_B_rows):
    for column in range(matrix_B_columns):
        print(f"{matrix_B[row][column]:<6}", end="")
    print()

# Multiply matrix A by matrix B, and store the result in a matrix C.
for i in range(matrix_A_rows):
    for j in range(matrix_B_columns):
        for k in range(matrix_A_columns):
            matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]

# Print matrix C
print("\nMatrix C:")
for row in range(matrix_A_rows):
    for column in range(matrix_B_columns):
        print(f"{matrix_C[row][column]:<6}", end="")
    print()

# Print matrix T
print("\nMatrix T:")
for column in range(matrix_B_columns):
    for row in range(matrix_A_rows):
        print(f"{matrix_C[row][column]:<6}", end="")
    print()

# Generate a barcode made out of all the numbers that are the sum of the column numbers of C
barcode = [0] * matrix_B_columns
for column in range(matrix_B_columns):
    for row in range(matrix_A_rows):
        barcode[column] += matrix_C[row][column]

print(f"\nBarcode: ")
for code in barcode:
    print(f"|{code}", end="")
print(f"|")

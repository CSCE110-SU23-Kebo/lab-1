# File: students.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

def add_name(first_name):
    """
    Adds the first name to the file of students
    @param first_name:
    @return:
    """
    students = open('students.txt', 'a')
    name = first_name + '\n'
    students.write(name)
    students.close()
    print("The name has been successfully added.")


def find_name(first_name):
    """
    Finds the name from the file student.txt and returns the index number of the first instance of the first_name found or 'No such student'
    @param first_name:
    @return:
    """
    students = open('students.txt', 'r')
    count = 0

    while True:
        count += 1

        # Get next line from file
        line = students.readline()

        # if line is empty
        # end of file is reached
        if not line:
            print('No such student')
            break
        else:
            if first_name in line:
                print(f'The name is found on line: {count}')
                students.close()
                return count


def update_name(first_name, new_name):
    """
    Finds the name from the file student.txt and replaces the first_name with new_name
    @param first_name:
    @param new_name:
    @return:
    """
    count = find_name(first_name)
    if count:
        students = open("students.txt", "r")
        list_of_lines = students.readlines()
        list_of_lines[count - 1] = new_name + '\n'

        students = open("students.txt", "w")
        students.writelines(list_of_lines)
        students.close()
        print('The name has been updated successfully')


def main():
    """
    Driver function
    @return:
    """
    run = True
    while run:
        print('Choose from the menu? \n',
              '\t1. Add a student \n',
              '\t2. Find a student \n',
              '\t3. Update an existing student \n',
              '\t4. quit \n'),
        user_input = input('Your choice: ')
        if user_input == '1':
            name = input('Please enter the first name: ')
            add_name(name)
        if user_input == '2':
            name = input('Please enter the first name: ')
            find_name(name)
        if user_input == '3':
            name = input('Please enter the first name: ')
            new_name = input('Please enter the target name: ')
            update_name(name, new_name)
        if user_input == '4':
            print('The program has quit.')
            run = False
        print()
        print(f'{"*"*56}')
        print()

if __name__ == '__main__':
    main()

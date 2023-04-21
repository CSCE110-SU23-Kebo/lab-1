import matplotlib.pyplot as drawing
import statistics


def get_grades(filename):
    """
    This function takes a file name as input and populates a dictionary containing the assignment types and grades.
    @param filename:
    @return: dictionary of grades
    """
    gradebook = dict()
    # todo

    return gradebook


def main():
    """
    This function prompts for the grades file name.
    Next, it calls the functions get_grades().
    Next, it draws the bar chart of the average grade for each assignment.
    @return:
    """
    filename = input("Enter the grade file name: ")
    gradebook = get_grades(filename)
    print(f'The dictionary of grades is: {gradebook}')
    # todo


main()

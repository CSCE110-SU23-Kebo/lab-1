import matplotlib.pyplot as drawing
import statistics


def get_grades(filename):
    """
    This function takes a file name as input and populates a dictionary containing the assignment types and grades.
    @param filename:
    @return: dictionary of grades
    """
    gradebook = dict()
    try:
        with open(filename, "r") as data:
            lines = data.readlines()
            lines = [line.strip() for line in lines]
            lines = [line.split() for line in lines]
            for line in lines:
                assignment = line[0]
                grade = float(line[1])
                if assignment in gradebook:
                    gradebook[assignment].append(grade)
                else:
                    gradebook[assignment] = [grade]
    except Exception as e:
        print(e)
        exit()

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
    assignments = list(gradebook.keys())
    grades = [statistics.mean(grades) for grades in gradebook.values()]

    drawing.xlabel('Assignment')
    drawing.ylabel('Average grade')
    drawing.title('CSCE 110 assignment grades')

    drawing.bar(assignments, grades, align='center', label="grades")
    drawing.legend()

    drawing.savefig('grades.png')
    drawing.show()


main()

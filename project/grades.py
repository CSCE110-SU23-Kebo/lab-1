import csv
import matplotlib.pyplot as plt
import numpy as np

grades = {}
keys = {}

def isNumeric(s):
    for letter in s:
        if not letter.isnumeric():
            return False
    return True

def menu():
    message = '''
*******************Main Menu*****************
1. Read CSV file of grades
2. Generate student report file
3. Generate student report charts
4. Generate class report file
5. Generate class report charts
6. Quit
************************************************
'''
    return input(message)

def readFile(fid):
    """A function just for me.

    ::param fid: The first of my arguments.

    """
    flag = True
    with open(fid) as file:
        d = csv.reader(file, delimiter=',')
        for row in d:
            if flag:
                for i in range(len(row)):
                    keys[i] = row[i]
                flag = False
            else:
                uin = row[0]
                grades[uin] = {"exams": 0, "labs": 0, "quizzes": 0, "readings": 0, "project": 0, "all_labs": [],
                "all_exams": [], "all_quizzes": [], "all_readings": []}
                for i in range(1,len(row)):
                    if i <= 6:
                        grades[uin]["labs"] += float(row[i])/6
                        grades[uin]["all_labs"].append(float(row[i]))
                    elif i <= 12:
                        grades[uin]["quizzes"] += float(row[i])/6
                        grades[uin]["all_quizzes"].append(float(row[i]))
                    elif i <= 18:
                        grades[uin]["readings"] += float(row[i])/6
                        grades[uin]["all_readings"].append(float(row[i]))
                    elif i <= 21:
                        grades[uin]["exams"] += float(row[i])/3
                        grades[uin]["all_exams"].append(float(row[i]))
                    else:
                        grades[uin]["project"] = float(row[i])

def studentFile(uin):

    fid = input("Enter output filename: ")
    examAvg = grades[uin]["exams"]
    labAvg = grades[uin]["labs"]
    quizAvg = grades[uin]["quizzes"]
    readingAvg = grades[uin]["readings"]
    with open(fid,"w+") as file:
        file.write(f"Exam average: {examAvg:.1f}\n")
        file.write(f"Lab average: {labAvg:.1f}\n")
        file.write(f"Quiz average: {quizAvg:.1f}\n")
        file.write(f"Reading/Activities average: {readingAvg:.1f}\n")

        score = 0.45*examAvg + 0.25*labAvg + 0.1*quizAvg + 0.1*readingAvg + 0.1*grades[uin]["project"]
        file.write(f"Score: {score:.1f}\n")
        file.write("Final Grade: ")
        if score < 60:
            file.write("F")
        elif score < 70:
            file.write("D")
        elif score < 80:
            file.write("C")
        elif score < 90:
            file.write("B")
        else:
            file.write("A")

def classFile(fid):
    """Read file 3"""
    finals = []
    for uin in grades.keys():
        score = 0.45*grades[uin]["exams"] + 0.25*grades[uin]["labs"] + 0.1*grades[uin]["quizzes"] + 0.1*grades[uin]["readings"] + 0.1*grades[uin]["project"]
        finals.append(score)

    with open(fid, "w+") as file:
        file.write(f"Total number of students: {len(finals)}\n")
        file.write(f"Minimum score: {min(finals):.1f}\n")
        file.write(f"Maximum score: {max(finals):.1f}\n")
        file.write(f"Median score: {np.median(finals):.1f}\n")
        file.write(f"Mean score: {np.mean(finals):.1f}\n")
        file.write(f"Standard deviation: {np.std(finals):.1f}\n")

def studentChart(uin):
    """Read file 4"""
    plt.figure(1)
    plt.title(f"Exam grades for {uin}", fontsize=16)
    plt.bar(range(1,4), grades[uin]["all_exams"])
    plt.xticks
    plt.xlabel('Exam #', fontsize=16)
    plt.ylabel('Score (%)', fontsize=16)

    plt.figure(2)
    plt.title(f"Lab grades for {uin}", fontsize=16)
    plt.bar(range(1,7), grades[uin]["all_labs"])
    plt.xlabel('Lab #', fontsize=16)
    plt.ylabel('Score (%)', fontsize=16)

    plt.figure(3)
    plt.title(f"Quiz grades for {uin}", fontsize=16)
    plt.bar(range(1,7), grades[uin]["all_quizzes"])
    plt.xlabel('Quiz #', fontsize=16)
    plt.ylabel('Score (%)', fontsize=16)

    plt.figure(4)
    plt.title(f"Reading activity grades for {uin}", fontsize=16)
    plt.bar(range(1,7), grades[uin]["all_readings"])
    plt.xlabel('Reading Activity #', fontsize=16)
    plt.ylabel('Score (%)', fontsize=16)

    plt.show()

def classChart():
    finals = [0,0,0,0,0]
    for uin in grades.keys():
        score = 0.45*grades[uin]["exams"] + 0.25*grades[uin]["labs"] + 0.1*grades[uin]["quizzes"] + 0.1*grades[uin]["readings"] + 0.1*grades[uin]["project"]
        if score < 60:
            finals[4] += 1
        elif score < 70:
            finals[3] += 1
        elif score < 80:
            finals[2] += 1
        elif score < 90:
            finals[1] += 1
        else:
            finals[0] += 1

    pie_finals = []
    for grade in finals:
        pie_finals.append(grade/sum(finals))

    plt.figure(5)
    plt.title(f"Class letter grades", fontsize=16)
    plt.pie(x=finals, labels=["A","B","C","D","E"])

    plt.figure(6)
    plt.title(f"Class letter grades", fontsize=16)
    plt.bar(["A","B","C","D","E"], finals)
    plt.xlabel('Grade', fontsize=16)
    plt.ylabel('Count', fontsize=16)

    plt.show()

def main():
    option = -1
    while option != 6:
        option = menu()
        if option == 'q' or option == "quit":
            break
        else:
            try:
                option = int(option)
            except:
                print("Unknown input please try again.")
                continue

        if option == 1:
            readFile(input("Enter filename: "))
        elif option == 2:
            uin = input("Enter student UIN: ")
            while True:
                if len(uin) != 10 or not isNumeric(uin):
                    print("UIN should be 10 digits long.")
                elif uin not in grades.keys():
                    print(f"UIN: {uin} is not in the database")
                else:
                    break
                uin = input("Enter student UIN: ")

            studentFile(uin)
        elif option == 3:
            uin = input("Enter student UIN: ")
            while True:
                if len(uin) != 10 or not isNumeric(uin):
                    print("UIN should be 10 digits long.")
                elif uin not in grades.keys():
                    print(f"UIN: {uin} is not in the database")
                else:
                    break
                uin = input("Enter student UIN: ")
            studentChart(uin)
        elif option == 4:
            classFile(input("Enter output filename: "))
        elif option == 5:
            classChart()
        else:
            print("Unknown input please try again.")


if __name__=="__main__":
    main()

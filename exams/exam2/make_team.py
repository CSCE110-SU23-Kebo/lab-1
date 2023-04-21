# make_team.py
import random


def main():
    """This function collects the students names and call the make_team function"""
    names = input('Enter the students name: ').split(',')
    team_size = int(input("Enter the team size: "))
    team = make_team(names, team_size)
    if team:
        print("The team is:", end=" ")
        print(*team, sep=",")
    else: # if team = 0
        print(f"The team size is too large")


def make_team(names, team_size):
    """ This function makes a list of random team members and prints it """
    names = list(set(names))
    if team_size <= len(names):
        return random.sample(names, team_size)
    else:
        return 0


if __name__ == "__main__":
    main()

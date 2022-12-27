#!/usr/bin/env python3

# Created by: Tamer Zreg
# Created on: Dec 20, 2022
# This program calculates the average of a list of grades entered by the user. The user can enter grades
# one at a time until they enter -1 to signal the end of the list. If the user enters a grade outside of
# the range 0-100, the program will display an error message and clear the list of grades.


def calculate_average(list_of_grade):
    """Calculate the average of a list of grades"""
    # Initialize sum to 0 and get the length of the list
    sum = 0
    length = len(list_of_grade)

    # If the list is empty, return -1
    if length == 0:
        return -1
    # Otherwise, loop through the list and add up the grades
    else:
        for counter in list_of_grade:
            sum = sum + counter
        # Calculate the average and return it
        average = sum / length
        return average


def main():
    # Initialize the list of grades and the grade variable
    list_of_grade = []
    grade = None

    # Keep prompting the user for grades until they enter -1
    while grade != -1:
        try:
            grade = int(input("Please enter a Grade (-1 to Stop): "))
            # If the grade is valid (between 0 and 100, inclusive), add it to the list
            if grade != -1 and grade >= 0 and grade <= 100:
                list_of_grade.append(grade)
            # If the user entered -1, calculate the average
            elif grade == -1:
                average = calculate_average(list_of_grade)
                # If the average is -1, it means the list was empty, so display an error message
                if average == -1:
                    print("Please enter at least one grade")
                # Otherwise, display the average
                else:
                    print(f"Your average among {list_of_grade} is {average}")
            # If the user entered a grade outside of the range 0-100, display an error message and clear the list
            elif grade != -1:
                print("Please enter a grade between 0 and 100 (inclusive)")
                list_of_grade = []
        # If the user didn't enter a number, display an error message
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    main()

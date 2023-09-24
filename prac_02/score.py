"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    random_result = get_result(get_random())
    print(f"User's result: {result}")
    print(f"Random result: {random_result}")


def get_result(score):
    if 90 <= score <= 100:
        return "Excellent!"
    elif 50 <= score < 90:
        return "Pass"
    elif 0 <= score < 50:
        return "Bad"
    else:
        return "Invalid Input!"


def get_random():
    return random.randint(0, 100)


main()

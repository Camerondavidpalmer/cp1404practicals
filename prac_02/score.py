"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    if 90 <= score <= 100:
        print("Excellent!")
    elif 50 <= score <= 100:
        print("Pass")
    elif 0 <= score <= 100:
        print("Bad")
    else:
        print("Invalid Input!")


main()

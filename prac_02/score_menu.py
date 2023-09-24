"""
Got the code to work, but cant figure out why the show stars wont work
"""


def main():
    display_menu()
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            get_result(get_valid_score())
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid Choice")
        display_menu()
        choice = input("Choice: ").upper()


def display_menu():
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def print_asterisks(score):
    score = int(score)
    number_of_asterisks = len(score)
    print("*" * number_of_asterisks)


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def get_result(score):
    if 90 <= score <= 100:
        result = "Excellent!"
    elif 50 <= score < 90:
        result = "Pass"
    elif 0 <= score < 50:
        result = "Bad"
    else:
        result = "Invalid Input!"
    print(result)


main()

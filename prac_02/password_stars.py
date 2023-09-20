def main():
    length = int(input("Length: "))
    password = get_password(length)
    print_asterisks(password)


def print_asterisks(password):
    number_of_asterisks = len(password)
    print("*" * number_of_asterisks)


def get_password(length):
    password = input("Enter a password:")
    while len(password) < length:
        print("Invalid length")
        password = input("Enter a password:")
    return password


main()

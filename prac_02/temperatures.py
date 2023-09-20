"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
celsius = 0
fahrenheit = 0


def convert_celsius_to_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9


while choice != "Q":
    if choice == "C":
        convert_celsius_to_fahrenheit()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        convert_fahrenheit_to_celsius()
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
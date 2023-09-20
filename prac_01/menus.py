# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>>").lower()
while choice != "q":
    if choice == "h":
        print("Hello", name)
    elif choice == "g":
        print("Goodbye", name)
    else:
        print("Invalid input!")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>>")
print("Finished")

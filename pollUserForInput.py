"""Module for pollUserForInput."""


def pollUserForInput(message, list):
    """Display a list with a header message, and get input from a user."""
    print("\n" + message)
    for i in range(0, len(list)):
        print(str(i + 1) + ". " + str(list[i]))
    return list[int(input("Choose an option: "))-1]

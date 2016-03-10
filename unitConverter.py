"""Has many different functions that convert units.

Includes f_to_c(f), c_to_f(c), f_to_k(f), k_to_f(k), c_to_k(c),
k_to_c(k).
"""


class Solver:
    """docstring for Solver."""

    def __init__(self, find, equation):
        """Define values."""
        self.find = find
        self.equation = equation
        out = eval(equation)
        self.out = out


solverDict = {
    "Farenheit to Celsius:": "(in - 32) * (5/9)",
    "Celsius to Farenheit": "(in * (9/5)) + 32",
    "f_to_k": "(in + 459.67) * (5/9)",
    "k_to_f": "(in * (9/5)) - 459.67",
    "c_to_k": "in + 273.15",
    "k_to_c": "in - 273.15"
}
convertOptions = ["Temperature"]
Temperature1 = ["Farenheit", "Celsius", "Kelvin"]


def poll_user_for_input(message, list):
    """Display a list with a header message, and get input from a user."""
    print(message)
    for i in range(0, len(list)):
        print(str(i + 1) + ". " + str(list[i]))
    return list[int(input("Choose an option: "))-1]


input0 = poll_user_for_input("Options:", convertOptions)
print(input0)
input1 = poll_user_for_input("H24?", input0+"1")
print(input1)

"""Has many different functions that convert units.

Includes .
"""


class Solve:
    """docstring for Solve."""

    def __init__(self, input, equation):
        """Define values."""
        input = int(input)
        self.equation = equation
        out = eval(equation)
        self.out = out


solverDict = {
    "Farenheit to Celsius": "(input - 32) * (5/9)",
    "Celsius to Farenheit": "(input * (9/5)) + 32",
    "Farenheit to Kelvin": "(input + 459.67) * (5/9)",
    "Kelvin to Farenheit": "(input * (9/5)) - 459.67",
    "Celsius to Kelvin": "input + 273.15",
    "Kelvin to Celsius": "input - 273.15"
}

listDict = {
    "convertOptions": ["Temperature"],
    "Temperature": ["Farenheit", "Celsius", "Kelvin"]
}


def poll_user_for_input(message, list):
    """Display a list with a header message, and get input from a user."""
    print("\n" + message)
    for i in range(0, len(list)):
        print(str(i + 1) + ". " + str(list[i]))
    return list[int(input("Choose an option: "))-1]

convertTypeChoice = \
    poll_user_for_input("Category:", listDict["convertOptions"])

convertFrom = \
    poll_user_for_input("Type to Convert From:", listDict[convertTypeChoice])

amount = input("How many? ")

convertTo = \
    poll_user_for_input("Type to Convert To:", listDict[convertTypeChoice])

equation = solverDict[convertFrom + " to " + convertTo]
answer = Solve(amount, equation).out
print(str(answer))

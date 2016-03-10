"""Includes next_prime(list) and check_for_user_Y_N(message)."""


import sys


foundPrimes = [2]
message_text = "Do you want to see another prime? [y/n] "


def next_prime(list):
    """Find the next prime in a sequence."""
    prime_candidate = list[-1]+1
    while True:
        result = True
        for i in range(0, len(list)):
            if prime_candidate % list[i] == 0:
                result = False
                break
        if result:
            break
        if result is False:
            prime_candidate += 1
            i = 0
    print(prime_candidate)
    list.append(prime_candidate)


def check_for_user_Y_N(message):
    """Check for a yes or no answer from a message."""
    while True:
        input_message = input(message)
        if input_message.upper() == "Y":
            return True
            break
        if input_message.upper() == "N":
            return False
            break
        else:
            print("Answer must be \"y\" or \"n\".")


# This is the actual code that is called when the program is run.
print(foundPrimes[-1])
while True:
    should_exit = check_for_user_Y_N(message_text)
    if should_exit is True:
        next_prime(foundPrimes)
    if should_exit is False:
        sys.exit()

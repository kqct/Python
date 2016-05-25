"""North Korea Game."""
import datetime
import os
import cPickle
from pollUserForInput import pollUserForInput

# Variable definitions
# From StackOverflow
SCORES_FILE = "scores.pickle"

# List definitions
listOfVictims = ["Barack Obama", "Dennis Rodman", "David Cameron",
                 "Julian Poyner"]
mainMenuOptions = ["Play", "Tutorial", "High Scores", "Exit"]


# Function definitions
# From StackOverflow
def read_high_scores():
    """Initialize an empty score file if it does not exist already.

    Return an empty list.
    """
    if not os.path.isfile(SCORES_FILE):
        write_high_scores([])
        return []

    with open(SCORES_FILE, 'r') as f:
        scores = cPickle.load(f)
    return scores


def write_high_scores(scores):
    """Write high scores."""
    with open(SCORES_FILE, 'w') as f:
        cPickle.dump(scores, f)


def main():
    """Main function of the program."""
    print("The NORTH KOREA (governmentally-sponsored) MAFIA GAME!")
    pollUserForInput("MAIN MENU:", mainMenuOptions)
    currentDate = datetime.datetime.now()
    print(currentDate)
main()

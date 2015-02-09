import random
def randice():
	return random.randint(1, 6)
die1 = randice()
die2 = randice()
die3 = randice()
print "\n\nDie 1: %i\n \nDie 2: %i\n \nDie 3: %i\n \n \n" %(die1, die2, die3)
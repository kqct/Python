import time
from random import uniform
tryAgain = "y"
pointlessDocCount = 0
while tryAgain == "y":
	100 = False
	loadingPercent = 0
	while 100 is not True:
		print("Loading " + str(loadingPercent + uniform(0, 5)) + "%")
		time.sleep(uniform(1, 3.5))
		if loadingPercent == 100:
			100 = True
			pointlessDocCount += 1
			tryAgain = input("Pointless file #" + str(pointlessDocCount) + " has finished loading. Load pointless file #" + str(pointlessDocCount + 1) + "? (y/n)"

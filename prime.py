while True:
	query = input("Enter a number between 2 and 1,000: ")
	if query > 1:
		if query < 1001:
			break
result = True
for i in range(2, query):
	if query % i == 0:
		print(i)
		result = False
		break
print(result)
if result is True:
	print("The number " + str(query) + " is prime.")
factors = []
factorLength = len(factors)
j = 0
if result is False:
	# Find factors
	for i in range(2, query):
		if query % i == 0:
			print(i)
# Filters out composite numbers from "factors" list
	for factorListPlacement in range(0, factorLength-1):
		for incurringVariable in range(2, factors[factorListPlacement]):
			try:
				if factors[factorListPlacement] % incurringVariable == 0:
					factors.pop(factorListPlacement)
					factorLength -= 1
				else:
					pass
			except:
				print("The number " + str(query) + " is not prime. Its factors are ")
				print(factors)
				break

#CAUTION: Only works if first number is positive.
input = open("input.txt", "r")
calc = input.read()
input.close()
split = calc.split()
chickens = 0
chickens += int(split[0])
for x in range(len(split)):	
	if split[x] == '+':
		chickens += int(split[x+1])
	elif split[x] == '-':
		chickens -= int(split[x+1])
	elif split[x] == '*':
		chickens *= int(split[x+1])
	elif split[x] == '/':
		chickens /= int(split[x+1])
f = open("output.txt", "w")
f.write(str(chickens))
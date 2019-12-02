import math

def calculate(n):
	k = int(n)
	if 9>k:
		return 0
	val = math.floor(int(k)/3)-2
	return val + calculate(val)

f = open("dayOne.txt", "r")
i = 10
counter = 0
for x in f:
	counter += calculate(x)
print("counter: ", counter)

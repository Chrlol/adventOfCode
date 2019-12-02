import math

def posOne(arr, n):
	val1 = arr[n+1]
	val2 = arr[n+2]
	val3 = arr[n+3]
	res = arr[val1] + arr[val2]
	arr[val3] = res

def posTwo(arr, n):
	val1 = arr[n+1]
	val2 = arr[n+2]
	val3 = arr[n+3]
	res = arr[val1] * arr[val2]
	arr[val3] = res


f = open("dayTwo.txt", "r")

str = f.read()
input = [int(x.strip()) for x in str.split(',')]
pos = 0

while pos < len(input):
	cur = input[pos]
	if cur == 1: # Add
		posOne(input, pos)
		pos += 4
	elif cur == 2: # multiplicate
		posTwo(input, pos)
		pos += 4
	elif cur == 99:
		break

print(input[0])
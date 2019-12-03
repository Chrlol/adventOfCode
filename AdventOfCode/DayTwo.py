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

def loadInput():
    f = open("dayTwo.txt", "r")
    str = f.read()
    return [int(x.strip()) for x in str.split(',')]



for x in range(100):
    for y in range(100):
        pos = 0
        input = loadInput()
        input[1] = x
        input[2] = y
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
        if(input[0] == 19690720):
            print("done: ",100 * x + y)
            break
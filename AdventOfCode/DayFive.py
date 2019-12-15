import math

class OpCode:
    def __init__(self, code, m1, m2, m3):
        self.code = code
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

def posOne(arr, n, oc):
    if oc.m1 == 0:
        val1 = arr[n+1]
    else:
        val1 = n+1

    if oc.m2 == 0:
        val2 = arr[n+2]
    else:
        val2 = n+2

    if oc.m3 == 0:
        val3 = arr[n+3]
    else:
        val3 = n+3
    res = arr[val1] + arr[val2]
    arr[val3] = res

def posTwo(arr, n, oc):
    if oc.m1 == 0:
        val1 = arr[n+1]
    else:
        val1 = n+1

    if oc.m2 == 0:
        val2 = arr[n+2]
    else:
        val2 = n+2

    if oc.m3 == 0:
        val3 = arr[n+3]
    else:
        val3 = n+3

    res = arr[val1] * arr[val2]
    arr[val3] = res

def posThree(arr, n, oc):
    inp = input("Enter integer:")
    i = int(inp)
    if oc.m1 == 0:
        arr[arr[n+1]] = i
    else:
        arr[n+1] = i

def posFour(arr, n, oc):
    if oc.m1 == 0:
        print(arr[arr[n+1]])
    else:
        print(arr[n+1])

def loadInput():
    f = open("dayFive.txt", "r")
    str = f.read()
    return [int(x.strip()) for x in str.split(',')]


def InterpretOpCode(n):
    n += 1000000
    #    0123456
    s = str(n)
    return OpCode(int(s[5:]), int(s[4:5]), int(s[3:4]), int(s[2:3]))


pos = 0
data = loadInput()
while pos < len(data):
    oc = InterpretOpCode(data[pos])
    
    if oc.code == 1: # Add
        posOne(data, pos, oc)
        pos += 4
    elif oc.code == 2: # multiplicate
        posTwo(data, pos, oc)
        pos += 4
    elif oc.code == 3:
        posThree(data, pos, oc)
        pos += 2
    elif oc.code == 4:
        posFour(data, pos, oc)
        pos += 2
    elif oc.code == 99:
        break
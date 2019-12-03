import math

def LoadInput():
    f = open("dayThree.txt", "r")
    line1 = f.readline()
    parsedLine1 = [x.strip() for x in line1.split(',')]
    r1 = [[x[0],int(x[1:])] for x in parsedLine1]

    line2 = f.readline()
    parsedLine2 = [x.strip() for x in line2.split(',')]
    r2 = [[x[0],int(x[1:])] for x in parsedLine2]
    return [r1, r2]

def Left(n, points):
    k = int(n)
    if k == 0:
        return
    curr = points[-1]
    for x in range(n):
        points.append([curr[0]-1-x, curr[1]])
    

def Right(n, points):
    k = int(n)
    if k == 0:
        return
    curr = points[-1]
    for x in range(n):
        points.append([curr[0]+1+x, curr[1]])

def Up(n, points):
    k = int(n)
    if k == 0:
        return
    curr = points[-1]
    for x in range(n):
        points.append([curr[0], curr[1]+1+x])

def Down(n, points):
    k = int(n)
    if k == 0:
        return
    curr = points[-1]
    for x in range(n):
        points.append([curr[0]-1, curr[1]-1-x])

def GetLinePoints(line):
    linePoints = [[0,0]]
    for x in line:
        if x[0] == 'L':
            Left(x[1], linePoints)
        elif x[0] == 'R':
            Right(x[1], linePoints)
        elif x[0] == 'U':
            Up(x[1], linePoints)
        elif x[0] == 'D':
            Down(x[1], linePoints)
        else:
            print("Computer says no")
    return linePoints

def FindIntersectPoints(points1, points2):
    points = []
    for n in points1:
        for m in points2:
            if (n[0] == 0 and n[1] == 0) or (m[0] == 0 and m[1] == 0):
                continue
            if n[0] == m[0] and n[1] == m[1]:
                points.append(n)
    return points

input = LoadInput()

line1 = input[0]
line2 = input[1]


linePoints1 = GetLinePoints(line1)
linePoints2 = GetLinePoints(line2)

intersectPoints = FindIntersectPoints(linePoints1, linePoints2)

print("computer says done")

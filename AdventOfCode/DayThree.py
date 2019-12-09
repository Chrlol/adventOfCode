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

def GetLines(dirs):
    print("length:", len(dirs))
    coords = [[0,0]]
    for dir in dirs:
        last = coords[-1]
        if dir[0] == 'R':
            coords.append([last[0]+dir[1], last[1]])
        elif dir[0] == 'L':
            coords.append([last[0]-dir[1], last[1]])
        elif dir[0] == 'U':
            coords.append([last[0], last[1]+dir[1]])
        elif dir[0] == 'D':
            coords.append([last[0], last[1]-dir[1]])
    return coords

def Union(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def CommonRange(n1,n2,n3,n4):
    nr1 = range(1,2)
    nr2 = range(1,2)
    if n1 < n2:
        nr1 = range(n1,n2+1)
    else:
        nr1 = range(n2,n1+1)
    if n3 < n4:
        nr2 = range(n3,n4+1)
    else:
        nr2 = range(n4,n3+1)
    return Union(nr1,nr2)

def FindIntersections(one, two):
    intersections = []
    for i1 in range(1,len(one)):
        for i2 in range(1,len(two)):
            x1 = one[i1-1][0]
            y1 = one[i1-1][1]
            x2 = one[i1][0]
            y2 = one[i1][1]
            
            x3 = two[i2-1][0]
            y3 = two[i2-1][1]
            x4 = two[i2][0]
            y4 = two[i2][1]

            if x1 == x2 and x3 == x4: # both vertical
                if x1 == x3:
                    for y in CommonRange(y1,y2,y3,y4):
                        intersections.append([x1, y])
                continue

            elif y1 == y2 and y3 == y4: # both horizontal
                if y1 == y3:
                    for x in CommonRange(x1,x2,x3,x4):
                        intersections.append([x, y1])
                continue

            if x1 == x2:
                ys = [y1,y2]
                ys.sort()
                xs = [x3,x4]
                xs.sort()
                if y3 >= ys[0] and y3 <= ys[1] and x1 >= xs[0] and x1 <= xs[1]:
                    intersections.append([x1, y3])
            else:
                ys = [y3,y4]
                ys.sort()
                xs = [x1,x2]
                if y1 >= ys[0] and y1 <= ys[1] and x3 >= xs[0] and x3 <= xs[1]:
                    intersections.append([x3, y1])
    return intersections

def Shortest(points):

    lengths = []
    for x in points:
        lengths.append(abs(x[0]) + abs(x[1]))
    lengths.sort()
    return lengths[1]


input = LoadInput()

dirs1 = input[0]
dirs2 = input[1]

path1 = GetLines(dirs1)
path2 = GetLines(dirs2)

intersections = FindIntersections(path1, path2)
shortest = Shortest(intersections)

print(shortest)
print("computer says done")

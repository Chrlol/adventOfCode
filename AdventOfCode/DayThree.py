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

def FindIntersections(one, two):
    for i1 in range(1,len(one)):
        for i2 in range(1,len(two)):
            l1p1 = one[i1-1]
            l1p2 = one[i1]
            
            l2p1 = one[i2-1]
            l2p2 = one[i2]

            if l1p1[0] == l1p2[0] and l2p1[0] == l2p2[0]: # both vertical
                print("both vertical: ", l1p1,l1p2," | ",l2p1,l2p2)
                if l1p1[0] == l2p1[0]:
                    print("On top of one another")

            if l1p1[1] == l1p2[1] and l2p1[1] == l2p2[1]: # both horizontal
                print("both horizontal: ", l1p1,l1p2," | ",l2p1,l2p2)
                if l1p1[1] == l2p1[1]:
                    print("On top of one another")
input = LoadInput()

dirs1 = input[0]
dirs2 = input[1]

path1 = GetLines(dirs1)
path2 = GetLines(dirs2)


intersections = FindIntersections(path1, path2)


print("computer says done")

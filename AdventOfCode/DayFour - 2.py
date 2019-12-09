
def HasAdjecent(x):
    s = str(x)
    list = [[s[0], 0]]
    for c in s:
        if c == list[-1][0]:
            list[-1][1] = list[-1][1] + 1
        else:
            list.append([c,1])
    list2 = []
    for x in list:
        list2.append(x[1])

    if 2 in list2:
        return True
    return False


def NeverDecrease(x):
    s = str(x)
    for i in range(0, len(s)-1):
        a = int(s[i])
        b = int(s[i+1])
        if a > b:
            return False
    return True

p = range(206938, 679128)
counter = 0
for x in p:
    if HasAdjecent(x) and NeverDecrease(x):
        counter = counter + 1
print(counter)
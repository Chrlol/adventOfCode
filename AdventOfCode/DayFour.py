
def HasAdjecent(x):
    s = str(x)
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
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
import sys
m = int(sys.stdin.readline())
s = {}
for i in range(1,21):
    s[str(i)] = 0

for i in range(m):
    try:
        commend, num = map(str,sys.stdin.readline().split())
    except:
        if commend == "all":
            for i in range(1,21):
                s[str(i)] = 1
        if commend == "empty":
            for i in range(1,21):
                s[str(i)] = 0
    if commend == "add":
        if s[num] == 0:
            s[num] = 1
    if commend == "remove":
        if s[num] == 1:
            s[num] = 0
    if commend == "check":
        if s[num] == 1:
            print(1)
        else:
            print(0)
    if commend == "toggle":
        if s[num] == 1:
            s[num] = 0
        else:
            s[num] = 1
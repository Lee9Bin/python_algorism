import sys
m = int(sys.stdin.readline())
s = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}

for i in range(m):
    commend= list(map(str,sys.stdin.readline().split()))
    if commend[0] == "all":
        s = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1}
    if commend[0] == "empty":
        s = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}
    if commend[0] == "add":
        if s[commend[1]] == 0:
            s[commend[1]] = 1
    if commend[0] == "remove":
        if s[commend[1]] == 1:
            s[commend[1]] = 0
    if commend[0] == "check":
        if s[commend[1]] == 1:
            print(1)
        else:
            print(0)
    if commend[0] == "toggle":
        if s[commend[1]] == 1:
            s[commend[1]] = 0
        else:
            s[commend[1]] = 1
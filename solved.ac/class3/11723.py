import sys
m = int(sys.stdin.readline())
s = []
All = []
for i in range(1,21):
    All.append(i)
emty = []

for i in range(m):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == "add":
        if int(command[1]) not in s:
            s.append(int(command[1]))
    if command[0] == "remove":
        if int(command[1]) in s:
            s.remove(int(command[1]))
    if command[0] == "check":
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    if command[0] == "toggle":
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.append(int(command[1]))
    if command[0] == "all":
        s = All
    if command[0] == "empty":
        s = emty

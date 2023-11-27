import sys
n = int(sys.stdin.readline())
result = []
for i in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        result.append(command[1])
    
    if command[0] == 2:
        if result:
            print(result.pop())
        else:
            print(-1)

    if command[0] == 3:
        print(len(result))

    if command[0] == 4:
        if result:
            print(0)
        else:
            print(1)
    
    if command[0] == 5:
        if result:
            print(result[-1])
        else:
            print(-1)
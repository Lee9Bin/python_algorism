import sys
n = int(sys.stdin.readline())

first = list(sys.stdin.readline().rstrip())

for i in range(n-1):
    nextW = list(sys.stdin.readline().rstrip())
    for j in range(len(first)):
        if first[j] != nextW[j]:
            first[j] = "?"
print(''.join(first))
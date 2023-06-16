import sys

n = int(sys.stdin.readline())
numlist = [0] * 10001
for i in range(n):
    x = int(sys.stdin.readline())
    numlist[x] += 1

for i in range(1, 10001):
    if numlist[i] != 0:
        for j in range(numlist[i]):
            print(i)

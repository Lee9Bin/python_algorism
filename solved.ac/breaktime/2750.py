import sys
n = int(sys.stdin.readline())
numlist = []

for i in range(n):
    numlist.append(int(sys.stdin.readline()))

numlist.sort()

for i in numlist:
    print(i)
import sys

n = int(sys.stdin.readline())

numlist = []

for i in range(n):
    numlist.append(int(sys.stdin.readline()))
    
numlist.sort()

for i in range(n-1,-1,-1):
    print(numlist[i])

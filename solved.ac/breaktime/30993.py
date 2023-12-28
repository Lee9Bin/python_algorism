import sys
numlist = list(map(int, sys.stdin.readline().split()))

up = 1
for i in range(1,numlist[0]+1):
    up *= i

down = 1
for i in range(1,len(numlist)):
    for j in range(1,numlist[i]+1):
        down *= j
        
print(up//down)
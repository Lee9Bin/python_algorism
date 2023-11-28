import sys
numlist = list(map(int, sys.stdin.readline().split(":")))

minNum = min(numlist)
ans = 1
for i in range(minNum,0,-1):
    if numlist[0] % i == 0 and numlist[1] % i == 0:
        ans = i
        break

print(f"{numlist[0]//ans}:{numlist[1]//ans}")

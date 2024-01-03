import sys
n, m = map(int, sys.stdin.readline().split())

plist = []

for i in range(m):
    plist.append(int(sys.stdin.readline()))

plist.sort()

ansA = 0
ansCost = 0

for i in range(m):
    nowCost = 0
    if n >= m:
        nowCost = plist[i] * m
        m -=1
    
    else:
        nowCost = plist[i] * n
        m -=1
    if ansCost < nowCost:
        ansCost = nowCost
        ansA = plist[i]

print(ansA, ansCost)
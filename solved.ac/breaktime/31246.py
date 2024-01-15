import sys
n, k = map(int, sys.stdin.readline().split())

# items = []
xList = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if b-a < 0:
        xList.append(0)
    else:
        xList.append(b-a)

xList.sort()

cnt = 0
ans = 0
for x in range(len(xList)):
    cnt +=1
    if cnt == k:
        ans = x
print(xList[ans])
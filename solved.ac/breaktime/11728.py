import sys
n, m = map(int, sys.stdin.readline().split())
result = []

# alist = list(map(int, sys.stdin.readline().split()))
# blist = list(map(int, sys.stdin.readline().split()))

# result = alist + blist

# result.sort()

# print(*result)

alist = list(map(int, sys.stdin.readline().split()))
blist = list(map(int, sys.stdin.readline().split()))

alist.sort()
blist.sort()
aStart = 0
bStart = 0

while aStart<n and bStart <m:
    if alist[aStart] <= blist[bStart]:
        result.append(alist[aStart])
        aStart +=1
    else:
        result.append(blist[bStart])
        bStart +=1
for i in range(aStart,n):
    result.append(alist[i])
for i in range(bStart,m):
    result.append(blist[i])

print(*result)
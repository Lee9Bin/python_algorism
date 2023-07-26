import sys
n,m = map(int,sys.stdin.readline().split())
numlist = set(map(int,sys.stdin.readline().split()))
numlist = list(numlist)

numlist.sort()
result = []
visited = [0] * n;
def back(start):
    if len(result) == m:
        print(*result)
        return
    for i in range(start,len(numlist)):
        if visited[i] == 0:
            result.append(numlist[i])
            back(i)
            result.pop()

back(0)
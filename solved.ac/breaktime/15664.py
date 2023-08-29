import sys
n,m = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
numlist.sort()

result = []
visited = [False] * 10000

def back(start):
    if len(result) == m:
        print(*result)
        return
    benum = 0
    for i in range(start,n):
        if visited[i] == False and benum != numlist[i]:
            visited[i] = True
            benum = numlist[i]
            result.append(numlist[i])
            back(i)
            result.pop()
            visited[i] = False

back(0)
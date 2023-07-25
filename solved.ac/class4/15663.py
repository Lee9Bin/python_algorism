import sys
n,m = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
numlist.sort()

result = []
visited = [False] * 10000

def back():
    if len(result) == m:
        print(*result)
        return
    benum = 0
    print(benum)
    for i in range(n):
        if visited[i] == False and benum != numlist[i]:
            print(benum)
            visited[i] = True
            benum = numlist[i]
            result.append(numlist[i])
            back()
            result.pop()
            visited[i] = False

back()
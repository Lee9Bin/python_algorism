import sys

n, m= map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
numlist.sort()

result = []

def back(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start,n):
        if numlist[i] not in result:
            result.append(numlist[i])
            back(i)
            result.pop()
back(0)
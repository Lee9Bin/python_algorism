import sys

n, m= map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
numlist.sort()

result = []

def back():
    if len(result) == m:
        print(*result)
        return
    
    for i in range(n):
        result.append(numlist[i])
        back()
        result.pop()
back()
import sys
n, m  = map(int,sys.stdin.readline().split())
def back(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start,n+1):
        result.append(i)
        back(i)
        result.pop()
result = []
back(1)
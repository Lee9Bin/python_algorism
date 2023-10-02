import sys

def back():
    if len(result) == m:
        print(*result)
        return
    
    
    for i in range(len(numlist)):
        result.append(numlist[i])
        back()
        result.pop()


n, m = map(int,sys.stdin.readline().split())
numlist = set(map(int,sys.stdin.readline().split()))
numlist = sorted(list(numlist))

result = []
back()

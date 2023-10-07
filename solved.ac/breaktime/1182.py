import sys
def back(start):
    global ans
    if sum(result) == s and len(result) > 0:
        ans += 1
    
    for i in range(start,n):
        result.append(numlist[i])
        back(i+1)
        result.pop()
        
n, s = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
ans = 0
result = []
back(0)
print(ans)
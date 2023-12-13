import sys
n = int(sys.stdin.readline())

numlist = list(map(int,sys.stdin.readline().split()))

ans = 0
maxPrice = 0

for i in range(n-1,-1,-1):
    maxPrice = max(maxPrice, numlist[i])
    ans = max(ans, maxPrice-numlist[i]) 
print(ans)
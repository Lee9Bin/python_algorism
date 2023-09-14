import sys
n, m = map(int,sys.stdin.readline().split())
nlist = list(map(int,sys.stdin.readline().split()))

dp = [0] *(n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1] + nlist[i-1]

start = 0
end = 0
result = 1e9
while start <= end:
    if end == n+1:
        break

    if dp[end] - dp[start] < m:
        end +=1
        
    elif dp[end] - dp[start] >= m:
        if result > end - start:
            result = end-start
        start +=1
        
if (result == 1e9):
    result = 0

print(result)
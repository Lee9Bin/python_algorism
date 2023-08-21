import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())

dp = [1e9] * 100001
dp[n] = 0
que = deque()
que.append(n)
result= 1
while que:
    nown = que.popleft()
    
    for i in (nown+1,nown-1,2*nown):
        if i >= 0 and i <=100000:
            if dp[i] > dp[nown] + 1:
                if i ==k:
                    result = 1
                dp[i] = dp[nown]+1
                que.append(i)
            elif dp[i] == dp[nown]+1:
                if i == k:
                    result +=1
                dp[i] = dp[nown]+1
                que.append(i)
                
print(dp[k])
print(result)
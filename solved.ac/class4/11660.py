import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
graph = []
mlist = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(m):
    mlist.append(list(map(int,sys.stdin.readline().split())))
    
dp = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(n+1):
        if j != 0 and j != 1:
            dp[i][j] = dp[i][j-1] + graph[i-1][j-1]
        elif j == 0:
            dp[i][j] = dp[i-1][n]
        elif j == 1 :
            dp[i][j] = dp[i-1][n] + graph[i-1][j-1]
            
for x1,y1,x2,y2 in mlist:
    result = 0
    for i in range(x1,x2+1):
        result += dp[i][y2] - dp[i][y1-1]
    print(result)
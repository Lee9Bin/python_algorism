import sys
n = int(sys.stdin.readline())
graph = []
dp = [[0 for i in range(n)] for i in range(n+1)]
result = 0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
dp[1][0] = graph[0][0]
for i in range(2,n+1):
    for j in range(n+1):
        try:
            dp[i][j] = max(dp[i-1][j-1]+graph[i-1][j],dp[i-1][j]+graph[i-1][j])
        except:
            continue
print(min(dp[n]))
import sys
n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for i in range(m+1)] for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + graph[i-1][j-1]
print(dp[n][m])
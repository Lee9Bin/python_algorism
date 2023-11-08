import sys
n, m = map(int,sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
dp = [[0 for i in range(m+1)] for i in range(n)] 

for i in range(n):
    for j in range(1,m+1):
        dp[i][j] = dp[i][j-1] + graph[i][j-1]

k = int(sys.stdin.readline())

for _ in range(k):
    i,j,x,y = map(int,sys.stdin.readline().split())
    ans = 0
    for start in range(i-1,x):
        ans += dp[start][y] - dp[start][j-1]
    print(ans)
    
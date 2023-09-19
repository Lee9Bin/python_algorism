import sys
n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))
dp = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if nlist[i] == nlist[i+1]:
        dp[i][i+1] = 1

for lens in range(2, n): # len >= 3
    for start in range(n - lens):
        end = start + lens
        if nlist[start] == nlist[end]:
            if dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

m = int(sys.stdin.readline())

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(dp[a-1][b-1])
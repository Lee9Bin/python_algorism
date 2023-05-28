import sys

n, m = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))
result = []
ans = 0


def dfs(start):
    global ans
    if len(result) == 3:
        if sum(result) <= m:
            if m - ans > m - sum(result):
                ans = sum(result)
        return
    for i in range(start, n):
        result.append(numlist[i])
        dfs(i + 1)
        result.pop()


dfs(0)
print(ans)

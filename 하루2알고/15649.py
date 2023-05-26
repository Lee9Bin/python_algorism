import sys

n, m = map(int,sys.stdin.readline().split())
ans = []
visit = [0]*(n+1)
def back():
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,n+1):
        if visit[i] == 0:
            visit[i] = 1
            ans.append(i)
            back()
            visit[i] = 0
            ans.pop()
back()

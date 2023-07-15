import sys

n, m = map(int,sys.stdin.readline().split())
ans = []
visitied = []
def back():
    if len(ans) == m:
        b = sorted(ans)
        visitied.append("".join(map(str,ans)))
        return
    for i in range(1,n+1):
        ans.append(i)
        back()
        ans.pop()
back()
for i in visitied:
    for j in i:
        print(j,end=' ')
    print()
import sys

n, m = map(int,sys.stdin.readline().split())
ans = []
def back():
    if len(ans) == m:
        for i in ans:
            print(i,end=' ')
        print()
        return
    
    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()
back()
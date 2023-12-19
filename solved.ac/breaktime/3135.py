import sys
a, b = map(int,sys.stdin.readline().split())

n = int(sys.stdin.readline())

ans = abs(a-b)
for i in range(n):
    nowx = int(sys.stdin.readline())

    if ans > abs(nowx-b) + 1:
        ans = abs(nowx-b) + 1
print(ans)
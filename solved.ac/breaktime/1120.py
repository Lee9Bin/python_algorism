import sys

a, b = map(str,sys.stdin.readline().split())
ans = 1e9
for i in range(len(b)-len(a) + 1):
    diff = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            diff += 1
    ans = min(ans, diff)
print(ans)
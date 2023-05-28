import sys

n = int(sys.stdin.readline())
ans = 0
for i in range(1, n):
    result = 0
    result += i
    for j in str(i):
        result += int(j)
    if result == n:
        ans = i
        break
print(ans)

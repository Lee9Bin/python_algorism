import sys

n, m = map(int, sys.stdin.readline().split())
up = 1
down = 1
for i in range(m):
    up *= n - i
for i in range(m, 0, -1):
    down *= i
print(up // down)

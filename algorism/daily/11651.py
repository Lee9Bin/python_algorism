import sys

n = int(sys.stdin.readline())
xy = []

for i in range(n):
    xy.append(list(map(int, sys.stdin.readline().split())))

xy.sort(key=lambda x: (x[1], x[0]))

for i in xy:
    print(*i)

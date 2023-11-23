import sys
n, m = map(int, sys.stdin.readline().split())
result = []

alist = list(map(int, sys.stdin.readline().split()))
blist = list(map(int, sys.stdin.readline().split()))

result = alist + blist

result.sort()

print(*result)
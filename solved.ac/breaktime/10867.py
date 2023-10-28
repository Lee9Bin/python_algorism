import sys
n = int(sys.stdin.readline())
numlist = set(map(int,sys.stdin.readline().split()))

result = sorted(list(numlist))
print(*result)
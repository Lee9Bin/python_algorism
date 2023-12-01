import sys
n = int(sys.stdin.readline())

cnt = 0

for i in range(1, n+1):
    total = 0
    start = i
    while total < n:
        total += start
        start += 1
    if total == n:
        cnt += 1

print(cnt)
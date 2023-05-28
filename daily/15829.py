import sys

n = int(sys.stdin.readline())
senten = sys.stdin.readline().rstrip()
numlust = []

for i in senten:
    numlust.append(ord(i) - 96)

ans = 0

for i in range(n):
    ans += numlust[i] * 31**i
print(ans % 1234567891)

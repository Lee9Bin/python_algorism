import sys
target = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

ans = 0

senList = []

for i in range(n):
    sens = sys.stdin.readline().rstrip()
    senList.append(sens+sens)


for sens in senList:
    if target in sens:
        ans += 1
print(ans)
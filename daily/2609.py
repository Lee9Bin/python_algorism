import sys

n, m = map(int, sys.stdin.readline().split())
ans1 = 0
ans2 = 0
for i in range(min(n, m), 0, -1):
    if max(n, m) % i == 0 and min(n, m) % i == 0:
        ans1 = i
        break
combi = 1
ans3 = ans1
while True:
    if ans3 == 1:
        ans2 = n * m
        break
    ans1 = ans3 * combi
    if ans1 % n == 0 and ans1 % m == 0:
        ans2 = ans1
        break
    combi += 1

print(ans3)
print(ans2)

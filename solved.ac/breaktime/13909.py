import sys
n = int(sys.stdin.readline())

ans = 1
now = 2

while True:
    if now ** 2 > n:
        break
    now +=1
    ans +=1
print(ans)
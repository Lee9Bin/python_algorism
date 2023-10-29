import sys
n = int(sys.stdin.readline())

ans = 0
now = 9
for i in range(1,len(str(n))+1):
    if n < now:
        ans += i * n
        break
    else:
        n -= now
        ans += i * now
        now *= 10
print(ans)
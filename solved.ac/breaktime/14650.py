import sys
n = int(sys.stdin.readline())

s = []
ans = 0
def back(cnt):
    global ans
    if cnt == n:
        now = int(''.join(s))
        if now % 3 == 0 and len(str(now)) == n and now != 0:
            ans += 1
        return

    for i in ("0","1","2"):
        s.append(i)
        back(cnt + 1)
        s.pop()

back(0)
print(ans)
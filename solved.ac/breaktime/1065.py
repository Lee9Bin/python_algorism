import sys
n = int(sys.stdin.readline())
ans = 0
for nown in range(1,n+1):
    if nown < 10:
        ans +=1
        continue
    d = int(str(nown)[0]) - int(str(nown)[1])
    for nown_len in range(len(str(nown))-1):
        nowd = int(str(nown)[nown_len]) - int(str(nown)[nown_len+1])
        if nowd != d:
            break
        if nown_len == len(str(nown))-2:
            ans += 1
print(ans)
import sys

t = int(sys.stdin.readline())
for i in range(t):
    wear = {}
    n = int(sys.stdin.readline())
    for j in range(n):
        a, b = map(str,sys.stdin.readline().split())
        if b not in wear:
            wear[b] = 1
        else:
            wear[b] +=1
    cnt = []
    for k in wear:
        cnt.append(wear.get(k))
    result = 0
    
    for l in range(len(cnt)):
        now = cnt[l]
        for m in range(l+1,len(cnt)):
            now *= 2**cnt[m]
        result += now
        
    print(result)
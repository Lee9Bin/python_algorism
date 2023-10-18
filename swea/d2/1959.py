t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())
    alist = list(map(int,input().split()))
    blist = list(map(int,input().split()))
    ans = 0
    if n < m:
        for i in range(m-n+1):
            total = 0
            for j in range(n):
                total += alist[j] * blist[i+j]
            if ans < total:
                ans = total
    else:
        for i in range(n-m+1):
            total = 0
            for j in range(m):
                total += blist[j] * alist[i+j]
            if ans < total:
                ans = total
    print(f"#{tc} {ans}")
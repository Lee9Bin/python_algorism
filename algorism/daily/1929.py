import sys
m,n = map(int, sys.stdin.readline().split())
prim = [2]
for i in range(m,n+1):
    for j in range(len(prim)+1):
        if j == len(prim):
            prim.append(i)
            break
        if i % prim[j] == 0:
            break
for i in prim:
    if m<= i <=n:
        print(i)
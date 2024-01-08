import sys
prim = []
visited = [False] * (10001)
for i in range(2,int(10001**0.5)):
    if visited[i] == False:
        
        for j in range(i+i,10001,i):
            visited[j] = True

for i in range(2,10001):
    if visited[i] == False:
        prim.append(i)

n = int(sys.stdin.readline())

for t in range(n):
    num = int(sys.stdin.readline())
    diff = 1e9
    
    a,b = 0, 0
    
    for i in range(len(prim)):
        if i >= num:
            continue
        for j in range(i,len(prim)):
            if prim[i] + prim[j] == num:
                if diff > abs(prim[i]-prim[j]):
                    diff = abs(prim[i]-prim[j])
                    a,b = prim[i], prim[j]
                    break
            elif prim[i] + prim[j] > num:
                break
    
    print(a, b)
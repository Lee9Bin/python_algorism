import sys

prim = []
visited = [False] *(123456*2+1)

for i in range(2,int((123456*2)**0.5)):
    if visited[i] == False:
        for j in range(i*2,123456*2+1,i):
            visited[j] = True
for i in range(2,123456*2+1):
    if visited[i] == False:
        prim.append(i)

while True:
    n = int(sys.stdin.readline())
    ans = 0
    if n == 0:
        break
    else:
        for i in prim:
            if n < i <= 2*n:
                ans +=1
            elif i > 2*n:
                break
    print(ans)
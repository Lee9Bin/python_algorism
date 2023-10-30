import sys 
n, m = map(int,sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))
    
ans = 1e9
for i in range(n-7):
    for j in range(m-7):
        # 하얀색 버젼
        nowColor = 'W'
        difColor = 'B'
        wCnt = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if nowColor != graph[k][l]:
                    wCnt += 1
                if l == j+7:
                    continue
                nowColor,difColor = difColor,nowColor   
        if ans > wCnt:
            ans = wCnt
        nowColor = 'B'
        difColor = 'W'
        bCnt = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if nowColor != graph[k][l]:
                    bCnt += 1
                if l == j + 7:
                    continue
                nowColor,difColor = difColor,nowColor
        if ans > bCnt:
            ans = bCnt
print(ans)
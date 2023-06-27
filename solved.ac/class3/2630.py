import sys

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    graph.append(arr)

def dfs(x,y,n):
    global white
    global blue
    nowcolor = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != nowcolor:
                dfs(x,y,n//2)
                dfs(x+n//2,y,n//2)
                dfs(x+n//2,y+n//2,n//2)
                dfs(x,y+n//2,n//2)
                return
    print(nowcolor)
    if nowcolor == 1:
        blue += 1
    else:
        white += 1
white = 0
blue = 0
dfs(0,0,n)
print(white)
print(blue)
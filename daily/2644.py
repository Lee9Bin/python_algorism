import sys
sys.setrecursionlimit(10**6)
def DFS(v):
    for i in range(n+1):
        if graph[v][i] == 1 and visited[i] == False:
            visited[i] = True
            path.append(i)
            DFS(i)
        if i == n and saram1 not in path:
            path.pop()
        elif saram1 in path:
            break

n = int(sys.stdin.readline())
saram1 , saram2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

path = [saram2] 
visited = [False] * (n+1)    
visited[saram2] = True

DFS(saram2)
if not path:
    print(-1)
else:
    print(len(path)-1)

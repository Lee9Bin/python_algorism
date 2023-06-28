import sys
n,m = map(int,sys.stdin.readline().split())
# 노드 갯수 n개 이니깐
graph = [[0 for i in range(n+1)] for i in range(n+1)]
visited = [False]*(n+1)


for i in range(m):
    # 방향이 없는 그래프(무방향 그래프)라는 것은 연결만 된다면 다 갈 수 있다는 뜻
    # 그러면 둘다 1 체크
    x, y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(start):
    visited[start] = True
    
    for i in range(n+1):
        if graph[start][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(i)
                
cnt = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        cnt +=1
print(cnt)
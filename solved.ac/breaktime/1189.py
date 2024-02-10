import sys
r, c, k = map(int, sys.stdin.readline().split())
graph = []

for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

visited = [[False for i in range(c)] for i in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def home(x, y, cnt):
    global ans
    if x == 0 and y == c-1 and cnt == k:
        ans += 1
        return
    
    for i in range(4):
        nextx = x + dx[i]
        nexty = y + dy[i]
        
        if 0 <= nextx < r and 0 <= nexty < c:
            if visited[nextx][nexty] == False and graph[nextx][nexty] != "T":
                visited[nextx][nexty] = True
                home(nextx,nexty,cnt+1)
                visited[nextx][nexty] = False

ans = 0
visited[r-1][0] = True
home(r-1, 0, 1)
print(ans)
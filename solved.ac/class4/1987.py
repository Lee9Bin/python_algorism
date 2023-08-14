import sys
r,c = map(int,sys.stdin.readline().split())
graph = []

for i in range(r):
    graph.append(list(map(str,sys.stdin.readline().strip())))

def dfs(x,y,cnt):
    global result
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx <r and ny<c:
            if nowlist[ord(graph[nx][ny])] == 1:
                if result < cnt:
                    result = cnt
                continue
            elif nowlist[ord(graph[nx][ny])] == 0:
                nowlist[ord(graph[nx][ny])] = 1
                dfs(nx,ny,cnt+1)
                nowlist[ord(graph[nx][ny])] = 0
nowlist = [0] * 123
result = 0
nowlist[ord(graph[0][0])] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
dfs(0,0,1)
print(result)
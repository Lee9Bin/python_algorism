import sys
n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
cnt = 0
def dfs(x,y,state):
    global cnt
    if (x == n-1 and y == n-1):
        cnt +=1
        return
    
    if state == "가로" or state == "대각":
        if y+1 < n and graph[x][y+1] == 0:
            dfs(x,y+1,"가로")
    if state == "세로" or state == "대각":
        if x+1 < n and graph[x+1][y] == 0:
            dfs(x+1,y,"세로")
    if state == "가로" or state == "세로" or state == "대각":
        if x+1< n and y+1<n and graph[x][y+1] == 0 and graph[x+1][y+1] ==0 and graph[x+1][y] == 0:
            dfs(x+1,y+1,"대각")

dfs(0,1,"가로")
print(cnt)
import sys

def dfs(x,y):
    if len(result) == 6:
        if ''.join(result) not in ans:
            ans.append(''.join(result))
        return
    if x+1 >= 0 and y >= 0 and x+1 < 5 and y <5:
        result.append(graph[x][y])
        dfs(x+1,y)
        result.pop()
    if x >= 0 and y+1 >= 0 and x < 5 and y+1 <5:
        result.append(graph[x][y])        
        dfs(x,y+1)
        result.pop()
    if x-1 >= 0 and y >= 0 and x-1 < 5 and y <5:
        result.append(graph[x][y])   
        dfs(x-1,y)
        result.pop()
    if x >= 0 and y-1 >= 0 and x < 5 and y-1 <5:
        result.append(graph[x][y])   
        dfs(x,y-1)
        result.pop()
graph = []
ans = []
for i in range(5):
    graph.append(list(map(str,sys.stdin.readline().split())))

for i in range(5):
    for j in range(5):
        result = []
        dfs(i,j)
print(len(ans))
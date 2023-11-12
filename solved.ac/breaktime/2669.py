import sys
graph = [[0 for i in range(101)] for i in range(101)]

for i in range(4):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    
    
    for x in range(y1,y2):
        for y in range(x1,x2):
            graph[x][y] = 1
            
ans = 0
for i in graph:
    ans += i.count(1)
print(ans)
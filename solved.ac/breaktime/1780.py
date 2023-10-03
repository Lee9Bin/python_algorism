import sys

def divide(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[x][y] != graph[i][j]:
                divide(x,y,n//3)
                divide(x,y+n//3,n//3)
                divide(x,y+n//3*2,n//3)
                
                divide(x+n//3,y,n//3)
                divide(x+n//3,y+n//3,n//3)
                divide(x+n//3,y+n//3*2,n//3)
                
                divide(x+n//3*2,y,n//3)
                divide(x+n//3*2,y+n//3,n//3)
                divide(x+n//3*2,y+n//3*2,n//3)
                return
            
    result.append(graph[x][y])
    
n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))    
result = []

divide(0,0,n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
import sys
n = int(sys.stdin.readline())
graph = [[" "for i in range(n*2)]for i in range(n)]

def draw(x,y,n):
    if n == 3:
        graph[x][y] = "*"
        graph[x + 1][y - 1] = "*"
        graph[x + 1][y + 1] = "*"
        for i in range(5):
            graph[x + 2][y - 2 + i] = "*"
        return
    draw(x,y,n//2)
    draw(x + n//2, y - n//2, n//2)
    draw(x + n//2, y + n//2, n//2)

draw(0,n-1,n)
for m in (graph):
    print("".join(m))
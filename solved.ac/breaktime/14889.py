import sys
def back(star):
    global ans
    if len(start) == n//2:
        link = []
        for i in range(n):
            if i not in start:
                link.append(i)
        ans = min(ans,abs(checkPoint(start)-checkPoint(link)))
        return
    
    for i in range(star,n):
        if visited[i] == False:
            start.append(i)
            visited[i] = True
            back(i)
            start.pop()
            visited[i] = False

def checkPoint(team):
    point = 0
    for i in range(n//2):
        for j in range(n//2):
            point += graph[team[i]][team[j]]
    
    return point    


n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

visited = [False] * n
start = []
ans = 1e9

back(0)

print(ans)
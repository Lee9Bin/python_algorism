import sys
import heapq
n = int(sys.stdin.readline())
graph = [[]for i in range(n+1)]
dis = [1e9]*(n+1)
visited = [False] * (n+1)

xy = []
for i in range(n):
    xy.append(list(map(float,sys.stdin.readline().split())))

# print(xy)
for i in range(n):
    for j in range(1,n):
        dist = ((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5
        graph[i+1].append((j+1,dist))

def prim(start):
    result = 0
    hq = []
    heapq.heappush(hq,(0,start))

    dis[start] = 0

    while hq:
        nowdist, nown = heapq.heappop(hq)
        if visited[nown] == False:
            visited[nown] = True
            result += nowdist

            for i in graph[nown]:
                newdist = i[1]
                if visited[i[0]] == False and dis[i[0]] > newdist:
                    heapq.heappush(hq,(newdist,i[0]))
    print(result)
prim(1)
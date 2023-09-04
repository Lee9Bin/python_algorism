import sys
from collections import deque

v = int(sys.stdin.readline())
graph = [[] for i in range(v+1)]

for i in range(v):
    wlist = deque(map(int,sys.stdin.readline().split()))
    a = wlist.popleft()
    for j in range(0,len(wlist),2):
        if wlist[j] != -1:
            graph[a].append((wlist[j],wlist[j+1]))
            
def dfs(nowv,dis):
    global ans
    global max1
    if ans < dis:
        ans = dis
        max1 = nowv
        
    #현재 노드의 연결된 정보를 가져와서 거리와 다음 노드로 가기
    for i in graph[nowv]:
        if visited[i[0]] == False:
            visited[i[0]] = True
            dfs(i[0],dis + i[1])
    #더이상 탐색할 노드가 없다면 함수 종료
    return


ans = 0
max1 = 0
#먼저 임의의 점을 잡아서 가장 멀리있는 노드 구하기
visited = [False] *(v+1)
visited[1] = True 
dfs(1,0)

#가장 멀리 있던 노드를 기준으로 다시 한번 가장 멀리있는 노드 찾아서 거리 구하기
ans = 0
visited = [False] *(v+1)
visited[max1] = True
dfs(max1,0)
print(ans)
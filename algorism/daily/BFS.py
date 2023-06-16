""" 
BFS는 너비우선탐색으로 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
BFS는 큐 자료구조를 이용한다.
1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
모두 큐에 삽입하고 방문 처리를 한다.
"""

from collections import deque

def BFS(graph,start,visited):
    queue = deque([start])
    visited[start] =True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
        
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
a = int(input())

BFS(graph,a,visited)
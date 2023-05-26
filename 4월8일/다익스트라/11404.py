# 문제가 원하는 것, 문제설명
# 정점 n개가 있고 간선의 갯수가 m개가 있을때 각 노드 기준으로 다른 노드들 까지의
# 최단 경로를 출력하는 문제

# 어떻게 풀려고 하였는지 => 플로우차트
# 플로이드 워셜 이론을 보고 문제에 적용

""" 문제에서 모든 경우의 최단거리 인지
    한지점에서의 최단거리인지 파악 중요
"""

import sys
INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF for i in range(n+1)] for i in range(n+1)]

# 문제에서 도시끼리 연결하는 간선이 여러개 있다고 해서 같은 노선일때
# 작은 노선으로 바꾸어줌
for i in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    if graph[a][b] >= c:
        graph[a][b] = c

#문제에서 시작점과 도착지점이 같을수 없다 했으므로 같은 지점을 0으로 저장 
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

# 1번부터 v번 까지 각각이 중간지점이 되는 경우에서 반복문을 돌려 
# 모든 노드에서의 최단경로 찾기
for v in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][v]+graph[v][j])
    print(graph)

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()
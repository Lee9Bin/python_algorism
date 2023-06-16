# 문제가 원하는 것, 문제설명
# N개의 컴퓨터가 있고 M개의 연결된 컴퓨터 쌍이 존재할때 (컴퓨터 번호는 차례로 1~N)
# 1번 컴퓨터가 바이러스에 걸린 상태 1번에 연결된 컴퓨터 모두가 바이러스에 걸리는데
# 이때 바이러스가 걸리는 컴퓨터의 갯수 세기

# 어떻게 풀려고 하였는지 => 플로우차트
# visted 리스트를 만들어서 함수내에 for문을 이용해서 1 이면 방문처리하고
# DFS경우 재귀함수로 인자 넘겨주고 BFS경우 큐에 추가
# 1번 컴퓨터 기준으로 탐색을 진행
import sys
from collections import deque

def DFS(start):
    # 1번은 방문 처리한다.
    visted[1] = True
    # x좌표가 v를 기준으로 반복문을 실행하면서 그래프상에 1이면서 visited[i] 값이 False 라면 
    # 방문 처리하고 함수로 넘겨준다. 그러면 1행에서 1인 부분이 처음에 걸리면 걸린 값을 함수로
    # 재귀가 실행이 되고 이 함수가 다 할 일을 마치면 다시 돌아오는 선입 후출 구조
    for i in range(v+1):
        if graph[start][i] == 1 and visted[i] == False:
            graph[start][i] = -1
            visted[i] = True
            DFS(i)

def BFS(start):
    # 큐에 현재 노드 위치 값을 담기 위해 큐 선언
    que = deque()
    que.append(start)
    visted[start] = True
    
    while que:
        # 현재 노드 위치를 큐에서 꺼낸다
        nowv = que.popleft()
        # 현재 노드 위치를 기준으로 반복문을 통해 그래프에서 1 이면서 방문하지 않은 노드를 찾아
        # 큐에 추가
        for i in range(v+1):
            if graph[nowv][i] == 1 and visted[i] == False:
                graph[nowv][i] = -1
                visted[i] = True
                que.append(i)
    

v = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph = [[0 for i in range(v+1)] for i in range(v+1)]
visted = [False] * (v+1)

for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    # (x,y), (y,x) 둘다 1 처리한 이유는 간선이 양방향이므로
    graph[x][y] = 1
    graph[y][x] = 1
    
# DFS(1)
BFS(1)
print(visted.count(True)-1)
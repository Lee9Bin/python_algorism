# 문제가 원하는 것, 문제설명
# N,M의 크기의 2차원 배열을 선언하고 '-'와 '|'로만 입력을 시킨다
# 이때 '-'는 같은 행에서 인접해 있을때 1개로 치고 
# '|'는 같은 열에 인접해 있을때 1개로 친다.

# 어떻게 풀려고 하였는지 => 플로우차트
# 탐색을 할때 for문을 사용할거기 때문에 '-'는 오른쪽으로만 
# 이동하게 해서 인접해있는지 체크
# '|'는 아래쪽으로만 이동하게 해서 인접해있는지 체크한뒤 
# ---->인접해 있으면 재귀함수 돌게
# 각각의 경우를 더해준다.

import sys
def dfs1(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return 
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == '-':
        # 해당 노드 방문 처리
        graph[x][y] = 'check'
        dfs1(x , y+1)

def dfs2(x, y,target):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return
    # 현재 노드를 아직 방문하지 않았다면   
    if graph[x][y] == target:
    # if graph[x][y] == '|':
        graph[x][y] = 'check'
        dfs2(x+1 , y)
# 한개의 함수로 처리하고 싶었지만 재귀 함수를 통해 한번에 '-' '|'가 같이 처리
# 되는 경우가 있어 먼저 '-' 탐색후 '|'탐색을 진행했다

N,M = map(int,sys.stdin.readline().split())
result = 0
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))

for i in range(N):
    for j in range(M):
        dfs2(i,j,graph[i][j])
        result += 1
        # if graph[i][j] == '-':
        #     dfs1(i,j)
        #     result +=1
        # elif graph[i][j] == '|':
        #     dfs2(i,j)
        #     result +=1
print(result)
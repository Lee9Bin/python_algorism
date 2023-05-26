# 문제가 원하는 것, 문제설명
# N,M의 행렬의 크기를 입력하고 K개 만큼 배추가 있는 좌표를 입력해서
# 배추가 있는곳은 1로 표시

# 어떻게 풀려고 하였는지 => 플로우차트
# 상하좌우 네 방향으로 1끼리 이어져 있으면 한개로 보기때문에 DFS BFS를 통해
# 탐색을 하여 체크하기
# 앞서 푼 문제들과 동일한 방법

import sys
from collections import deque
sys.setrecursionlimit(10**6)
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return
    # 현재 노드를 아직 방문하지 않았다면
    if baecho[x][y] == 1:
        # 해당 노드 방문 처리
        baecho[x][y] = -1
        dfs(x-1 , y) # 상
        dfs(x+1 , y) # 하
        dfs(x , y-1) # 좌
        dfs(x , y+1) # 우
    # 재귀 함수는 스택형식으로 쌓인다 예를 들어 '상'에 해당하는 함수가
    # 실행이되면 스택 구조에 쌓이면서 선입 후출 형식으로 함수가 실행
def BFS(x,y):
    # BFS는 큐로 구현 가능하다 따라서 좌표를 담을 큐선언 후 함수 인자값 추가
    que = deque()
    que.append((x,y))
    # 그래프의 상하좌우 탐색을 위해 다음 좌표를 확인하기 위한 리스트 생성
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # 본인 자리는 탐색 완료
    baecho[x][y] = -1
    # 큐가 빌때까지 반복
    while que:
        # 현재 좌표를 꺼낸다
        nowx, nowy = que.popleft()
        
        # 다음 좌표를 dx,dy를 이용해 만든다
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            
            # 좌표가 벗어나지 않게 조건을 걸어준다
            if nextx >= 0 and nexty>=0 and nextx < M and nexty < N:
                # 탐색할 자리가 1이면 아직 탐색을 안한 상태이므로 탐색
                if baecho[nextx][nexty] == 1:
                    baecho[nextx][nexty] = -1
                    que.append((nextx,nexty))
                    
        
# 테스트케이스 수 입력
T = int(sys.stdin.readline())
for i in range(T):
    # 가로길이 M 세로길이 N 배추개수 K
    M,N,K = map(int,sys.stdin.readline().split())
    # 탐색을 하면서 갯수를 체킹하기 위해 cnt 선언
    cnt = 0
    # M*N 행렬 선언
    baecho = [[0 for i in range(N)] for i in range(M)]

    # K개 만큼 1이 있는 그래프 좌표 입력
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        baecho[x][y] = 1
    
    # 그래프를 돌면서 1이면 탐색을 마치고 빠져나와 cnt +=1 한후 반복
    for i in range(M):
        for j in range(N):
            if baecho[i][j] == 1:
                # dfs(i,j)
                BFS(i,j)
                cnt += 1
    print(cnt)
    
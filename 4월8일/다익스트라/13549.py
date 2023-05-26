# 문제가 원하는 것, 문제설명
# 문제에서 제시한 시작지점에서 다른지점으로 까지 갈때에 최소 시간

# 어떻게 풀려고 하였는지 => 플로우차트
# 시작지점을 기준으로 -1 1 *2 를 보고 부모 노드를 기준으로
# 아래로 자식들이 펼쳐나간다 생각해서 우선 BFS가 떠올랐다

import sys
from collections import deque
INF = int(1e9)
n,m = map(int,sys.stdin.readline().split())

# 아직 방문하지 않았음과 시작지점은 0으로 초기화 하는 visited 함수 선언
visited = [INF] * 100001
visited[n] = 0

# BFS 아이디어를 사용하기 위해 큐를 사용
que = deque()
que.append(n)

while que:
    nown = que.popleft()
    
    # 뻗어나가는 경우가 문제에서 제시한 3가지 경우를 반복문을 통해 확인
    for nextn in (nown*2,nown+1,nown-1):
        if 0 <= nextn < 100001:
            # 처음 방문 했을 경우에만 실행
            if visited[nextn] == INF:
                # *2인 경우는 걸리는 시간이 0초 이므로 큐에 맨앞에 추가
                if nextn == nown*2 and nextn != 0:
                    visited[nextn] = visited[nown]
                    que.appendleft(nextn)    
                else:
                # 나머지 경우들은 순차적으로 큐에 추가
                    visited[nextn] = visited[nown] + 1
                    que.append(nextn)
                    
print(visited[m])
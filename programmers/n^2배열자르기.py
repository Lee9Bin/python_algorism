from collections import deque
# 문제설명: 문제에서 주어진 규칙대로 n*n 배열을 만들어 요소 뽑아 오기
# 첫번째 해결 전략
# 그래프를 bfs를 통해 채운다.
# left와 right가 의미하는 바를 파악한다. -> 몫이 행이 되고 나머지가 열이된다.
# 결과: 시간초과 why? n의 범위가 크므로 탐색을 하면서 진행하기에는 무리가 있다.

# 두번째
# 이런 경우 문제에서 주어진 규칙이 있을것이다. -> 규칙을 찾아 수식으로 해결
# 만든 그래프를 굳이 행 단위로 짤라서 이어 붙였을까 ? 
# 찾은 규칙 행 단위로 짤라서 이어 붙인 배열에서 보면 결국 인덱스 번호를 n으로 나눴을때 나머지와 몫 둘중 큰 값에 +1 을 해주는 규칙성이 보임
def solution(n, left, right):
    answer = []
    # graph = [[0 for i in range(n)] for i in range(n)]
    # graph[0][0] = 1
    # visited = [[False for i in range(n)] for i in range(n)]
    
    # que = deque()
    # que.append((0,0))
    # visited[0][0] = True
    # dx = [0,1,1]
    # dy = [1,1,0]
    
    # while que :
    #     nowx, nowy = que.popleft()
        
    #     for i in range(3):
    #         nextx = nowx + dx[i]
    #         nexty = nowy + dy[i]
            
    #         if nextx >=0 and nexty>=0 and nextx < n and nexty <n:
    #             if visited[nextx][nexty] == False:
    #                 visited[nextx][nexty] = True
                    # graph[nextx][nexty] = graph[nowx][nowy] + 1
                    # que.append((nextx,nexty))
    
    # for i in range(left//n,right//n+1):
    #     if i == left//n:
    #         for j in range(left%n,n):
    #             answer.append(j+1)
    #     elif i == right//n:
    #         for j in range(right%n+1):
    #             answer.append(j+1)
    #     else:
    #         for j in range(n):
    #             answer.append(j+1)
    
    for i in range(left, right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

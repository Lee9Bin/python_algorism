# 문제설명: 연결된 노드들을 한 묶음이라고 생각하고 몇 묶음인지 구하기
#        -> 0번 노드부터 n-1번 노드를 확인하는데 이때 방문을 안했던 노드라면 dfs탐색을 해준다.
#           노드들끼리 연결돼 있다면 한 노드를 기준으로 탐색했을때 방문처리가 될것이기 때문에
#           dfs탐색이 들어간 횟수를 구한다면 묶음의 갯수와 같다
def dfs(n, computers, start, visited):
    for i in range(n):
        if computers[start][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(n, computers, i, visited)
            
def solution(n, computers):
    answer = 0
    visited = [False] * (n)
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(n, computers, i, visited)
            answer +=1 
    return answer
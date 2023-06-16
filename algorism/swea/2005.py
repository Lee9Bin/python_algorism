# 2시 14분시작
# 파스칼 삼각형
# 첫번째 줄은 항상 숫자 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    graph = [[0 for i in range(n)]for i in range(n)]
    graph[0][0] = 1
    for i in range(1,n):
        for j in range(n):
            if j == 0:
                graph[i][j] = 1
            else:
                graph[i][j]= graph[i-1][j-1] + graph[i-1][j]
    print(graph)
# 24 + 6 33

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    cnt = 0
    #그래프 위로는 n극 s극
    for i in range(n):
        nown = 0
        for j in range(n):
            if graph[j][i] == 1:
                nown = 1
            elif graph[j][i] == 2:
                if nown == 1:
                    cnt +=1
                nown = 0
    print(f"#{test_case} {cnt}")
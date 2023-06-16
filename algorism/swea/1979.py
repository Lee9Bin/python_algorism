# 4시 4
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))

    result = 0
    for i in range(n):
        start = 0
        end = 0
        for j in range(n+1):
            if j == n:
                if k == end -start:
                    result +=1
                    continue
            elif graph[i][j] == 1:
                end +=1
            else:
                if k == end-start:
                    result+=1
                end +=1
                start = end
    for i in range(n):
        start = 0
        end = 0
        for j in range(n+1):
            if j == n:
                if k == end -start:
                    result +=1
                    continue
            elif graph[j][i] == 1:
                end +=1
            else:
                if k == end-start:
                    result+=1
                end +=1
                start = end
    print(f"#{test_case} {result}")
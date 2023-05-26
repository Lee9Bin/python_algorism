# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    graph = []
    for i in range(5):
        graph.append(list(map(str,input())))
    maxlen = 0
    for i in graph:
        if maxlen < len(i):
            maxlen = len(i)
    print(f"#{test_case}",end=' ')
    for i in range(maxlen):
        for j in range(5):
            if len(graph[j]) > i:
                print(graph[j][i],end='')
    print()
    # 0 1 2 3 4 5
    # a v c d
    # a v c 
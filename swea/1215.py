
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    graph = []
    for i in range(8):
        graph.append(list(map(str, input())))
    # 입력받을거 끝 ------
    ans = 0
    # result = []
    # 그래프를 가로로 하나씩 확인?
    for i in range(8):
        for j in range(8-n+1):
            result  = graph[i][j:j+n]
            sub = list(reversed(result))
            if result == sub :
                ans +=1
    for i in range(8):
        for j in range(8-n+1):
            result = []
            while True:
                result.append(graph[j][i])
                if len(result) == n:
                    sub = list(reversed(result))
                    if result == sub:
                        ans +=1
                    break
                j += 1
    print(f"#{test_case} {ans}")
    
# 8 8 a b c로만 이루어진 판에서 회문을 찾아라 
# 가로 세로 직선으로만 가능
# 첫째줄에는 회문의 길이가 주어짐
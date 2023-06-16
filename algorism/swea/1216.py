
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 4 41
for test_case in range(1, 11):
    T = int(input())
    graph = []
    for i in range(100):
        graph.append(list(map(str, input())))
    maxlength = 1
    ans = 0
    result = []
    # 행을 가져와서 각 인덱스 번호를 기준으로 끝에서 부터 담아서 확인
    for i in range(100):
        for j in range(100):
            end = 100
            while j < end:
                result = graph[i][j:end]
                sub = list(reversed(result))
                # 같으면 end값 저장 하고 스톱
                if result == sub:
                    if ans < end-j:
                        ans = end-j
                    break
                else:
                    end -= 1
    
    for i in range(100):
        for j in range(100):
            end = 100
            
            while j < end:
                for k in range(j,end):
                    result.append(graph[k][i])
                sub = list(reversed(result))
                if result == sub:
                    if ans < end-j:
                        ans = end-j
                    break
                else:
                    result = []
                    end -= 1
    print(f"#{test_case} {ans}")
# 시나리오
# 각 행을 가져와서 길이 인덱스 기준 100을 한칸씩 줄여나가자
# 알고리즘은 글쓰기 내가 얼마나 내머릿속에 있는 논리적인 생각을 잘 표현 할수 있는지

# 1
# CBCABBAC
# BBABCABA
# ABCBCCCA
# BACCAABB
# BCBCACBC
# CABACACB
# CAAACCAB
# CBABACAC
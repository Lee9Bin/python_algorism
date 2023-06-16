T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = list(map(int, input()))
    arr = [0] * len(n)
    cnt = 0
    sub = []
    # 필요한 입력과 변수 정리 끝
    for i in range(len(n)):
        if arr[i] == n[i]:
            continue
        else:
            cnt +=1
            nownum = n[i]
            sub = [nownum] * (len(n)-i)
            arr[i:] = sub
    
    print(f"#{test_case} {cnt}")
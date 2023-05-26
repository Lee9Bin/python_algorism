# 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    n = int(input())
    secret = list(map(int, input().split()))
    m = int(input())
    comand = list(map(str, input().split()))
    for i in range(len(comand)):
        if comand[i] == 'I':
            where = int(comand[i+1])
            cnt = int(comand[i+2])
            sub = comand[i+3:i+3+cnt]
            for j in range(cnt):
                secret.insert(where+j,sub[j])
        elif comand[i] == 'D':
            where = int(comand[i+1])
            cnt = int(comand[i+2])
            for i in range(cnt):
                secret.pop(where)

    print(f"#{test_case}", end=' ')
    print(*secret[:10])
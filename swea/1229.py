# 6 14
for test_case in range(1,11):
    n = int(input())
    secret = list(map(int,input().split()))
    m = int(input())
    comand = list(map(str,input().split()))
    
    for i in range(len(comand)):
        if comand[i] == 'I':
            where = int(comand[i+1])
            cnt = int(comand[i+2])
            pluslist = comand[i+3:i+3+cnt]
            for j in range(cnt):
                secret.insert(where+j,pluslist[j])
        elif comand[i] == 'D':
            where = int(comand[i+1])
            cnt = int(comand[i+2])
            for j in range(cnt):
                secret.pop(where)
    print(f"#{test_case}",end=' ')
    print(*secret[:10])
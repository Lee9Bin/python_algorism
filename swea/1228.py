# 3 56
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    n = int(input())    #원본 암호문 갯수
    nlist = list(map(int,input().split())) # 숫자를 담을 리스트
    
    m = int(input()) #명령어 갯수
    mlist = list(map(str, input().split()))
    
    for i in range(len(mlist)):
        if mlist[i] == 'I':
            x = int(mlist[i+1])
            cnt = int(mlist[i+2])
            newlist = mlist[i+3:i+3+cnt]
            for j in range(cnt):
                nlist.insert(x+j,int(newlist[j]))
    
    print(f"#{test_case}",end=' ')
    for i in nlist[:10]:
        print(i,end=' ')
    print()
    
    
    
    

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # T = int(input())
    # target = input()
    # slist = input()
    # cnt =0
    # for i in range(len(slist)):
    #     if slist[i:i+len(target)] == target:
    #         cnt +=1
    # print(f"#{test_case} {cnt}")
    
    T = int(input())
    target = input()
    slist = input()
    newlist = slist.replace(target,'ㄱ')
    cnt = 0
    for i in newlist:
        if i =='ㄱ':
            cnt +=1
    print(f"#{test_case} {cnt}")